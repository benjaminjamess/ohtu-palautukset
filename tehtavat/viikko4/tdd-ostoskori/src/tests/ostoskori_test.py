"""Tests for Ostoskori."""

import unittest
from ostoskori import Ostoskori
from tuote import Tuote


class TestOstoskori(unittest.TestCase):
    """Test shopping-cart behavior."""

    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        """An empty cart has no items and no price."""
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_tavaroiden_maara(self):
        """Count each added unit of a product."""
        tuote = Tuote("test", 5)
        self.kori.lisaa_tuote(tuote)
        self.kori.lisaa_tuote(tuote)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
