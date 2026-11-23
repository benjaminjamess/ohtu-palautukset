"""Mock-based tests for Kassapaate."""

import unittest
from unittest.mock import Mock
from kassapaate import Kassapaate, HINTA


class TestKassapaate(unittest.TestCase):
    """Test card charging and top-up behavior."""

    def setUp(self):
        self.kassa = Kassapaate()

    def test_kortilta_velotetaan_hinta_jos_rahaa_on(self):
        """Charge the lunch price when the card has enough balance."""
        maksukortti_mock = Mock()
        maksukortti_mock.saldo.return_value = 10

        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_called_with(HINTA)

    def test_kortilta_ei_veloteta_jos_raha_ei_riita(self):
        """Do not charge when the card balance is insufficient."""
        maksukortti_mock = Mock()
        maksukortti_mock.saldo.return_value = 4

        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_not_called()

    def test_kortille_ladataan_positiivinen_summa(self):
        """Load a positive amount onto the card."""
        maksukortti_mock = Mock()

        self.kassa.lataa(maksukortti_mock, 10)

        maksukortti_mock.lataa.assert_called_once_with(10)

    def test_kortille_ei_ladata_negatiivista_summaa(self):
        """Do not load a negative amount onto the card."""
        maksukortti_mock = Mock()

        self.kassa.lataa(maksukortti_mock, -10)

        maksukortti_mock.lataa.assert_not_called()
