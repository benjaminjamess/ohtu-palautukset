"""Mock-based tests for the store."""

import unittest
from types import SimpleNamespace
from unittest.mock import Mock
from kauppa import Kauppa

class TestKauppa(unittest.TestCase):
    """Test store purchase flows."""

    def setUp(self):
        self.saldot = {}
        self.pankki_mock = Mock()
        viitegeneraattori_mock = Mock()
        viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock = Mock()
        self.tuotteet = {
            1: SimpleNamespace(id=1, nimi="maito", hinta=5),
            2: SimpleNamespace(id=2, nimi="leipa", hinta=3)
        }

        def varasto_saldo(tuote_id):
            return self.saldot.get(tuote_id, 0)

        def varasto_hae_tuote(tuote_id):
            return self.tuotteet[tuote_id]

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        self.kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, viitegeneraattori_mock
        )

    def test_maksettaessa_yksi_ostos_tilisiirto_kutsutaan_oikeilla_tiedoilla(self):
        """Send the correct transfer details for one in-stock product."""
        self.saldot = {1: 1}
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

    def test_maksettaessa_kaksi_eri_tuotetta_summataan_hinnat(self):
        """Sum the prices of two different products."""
        self.saldot = {1: 1, 2: 1}
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 8
        )

    def test_maksettaessa_kaksi_samaa_tuotetta_hinta_lasketaan_kahdesti(self):
        """Count the price twice when buying the same product twice."""
        self.saldot = {1: 2}
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 10
        )

    def test_varastossa_oleva_tuote_veloitetaan_mutta_loppunutta_ei(self):
        """Charge only for products that are in stock."""
        self.saldot = {1: 1, 2: 0}
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

    def test_poista_korista_palauttaa_tuotteen_varastoon(self):
        """Return a removed product to inventory and remove its price."""
        self.saldot = {1: 1}
        tuote = self.tuotteet[1]

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)

        self.varasto_mock.palauta_varastoon.assert_called_once_with(tuote)

        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 0
        )
