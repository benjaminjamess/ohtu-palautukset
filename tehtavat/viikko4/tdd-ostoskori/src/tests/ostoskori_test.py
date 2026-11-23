"""Tests for Ostoskori."""

import unittest
from ostoskori import Ostoskori
from tuote import Tuote


class TestOstoskori(unittest.TestCase):
    """Test shopping-cart behavior."""

    def setUp(self):
        self.kori = Ostoskori()

    def test_tyhjassa_korissa_ei_ole_tuotteita_eika_hintaa(self):
        """An empty cart has no products or price."""
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(len(self.kori.ostokset()), 0)

    def test_yhden_tuotteen_lisaaminen(self):
        """A single product becomes one purchase at its listed price."""
        tuote = Tuote("test", 5)
        self.kori.lisaa_tuote(tuote)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.assertEqual(self.kori.hinta(), tuote.hinta())
        self.assertEqual(len(self.kori.ostokset()), 1)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), tuote.nimi())
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaaminen(self):
        """Different products have separate purchases and summed prices."""
        tuote1 = Tuote("test1", 5)
        tuote2 = Tuote("test2", 7)
        self.kori.lisaa_tuote(tuote1)
        self.kori.lisaa_tuote(tuote2)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        self.assertEqual(self.kori.hinta(), tuote1.hinta() + tuote2.hinta())
        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_saman_tuotteen_lisaaminen_kahdesti(self):
        """Identical additions share one purchase with quantity two."""
        tuote = Tuote("test", 5)
        self.kori.lisaa_tuote(tuote)
        self.kori.lisaa_tuote(tuote)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        self.assertEqual(self.kori.hinta(), tuote.hinta() * 2)
        self.assertEqual(len(self.kori.ostokset()), 1)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), tuote.nimi())
        self.assertEqual(ostos.lukumaara(), 2)

    def test_yhden_kahdesta_samasta_tuotteesta_poistaminen(self):
        """Removing one of two units leaves one unit in one purchase."""
        tuote = Tuote("test", 5)
        self.kori.lisaa_tuote(tuote)
        self.kori.lisaa_tuote(tuote)

        self.kori.poista_tuote(tuote)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.assertEqual(len(self.kori.ostokset()), 1)
        self.assertEqual(self.kori.ostokset()[0].lukumaara(), 1)

    def test_ainoan_tuotteen_poistaminen(self):
        """Removing the only product leaves the cart empty."""
        tuote = Tuote("test", 5)
        self.kori.lisaa_tuote(tuote)

        self.kori.poista_tuote(tuote)

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(self.kori.ostokset()), 0)

    def test_tyhjentaminen(self):
        """Clearing the cart removes all purchases."""
        self.kori.lisaa_tuote(Tuote("test1", 5))
        self.kori.lisaa_tuote(Tuote("test2", 6))

        self.kori.tyhjenna()

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(self.kori.ostokset()), 0)
