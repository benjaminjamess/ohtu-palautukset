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

    def test_priceofone(self):
        """One product costs the same as that product"""
        tuote=Tuote("test",5)
        self.kori.lisaa_tuote(tuote)
        self.assertEqual(self.kori.hinta(), tuote.hinta())

    def test_amounttwo(self):
        """Adding two products creates two products"""
        tuote1=Tuote("test1",5)
        tuote2=Tuote("test2", 6)
        self.kori.lisaa_tuote(tuote1)
        self.kori.lisaa_tuote(tuote2)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_sumofproduct(self):
        """Adding two different products equals sum of product prices"""
        tuote1=Tuote("test1",5)
        tuote2=Tuote("test2",7)
        self.kori.lisaa_tuote(tuote1)
        self.kori.lisaa_tuote(tuote2)
        self.assertEqual(self.kori.hinta(), tuote1.hinta()+tuote2.hinta())
    def test_priceequal2timesproductprice(self):
        """Adding two of the same products, the cart price is equal to 2 times the product price"""
        tuote=Tuote("test",5)
        self.kori.lisaa_tuote(tuote)
        self.kori.lisaa_tuote(tuote)
        self.assertEqual(self.kori.hinta(), tuote.hinta()*2)

    def test_ostoskoriin_lisatty_tuote_nakyy_ostoksissa(self):
        """Adding one product creates one purchase in the cart."""
        tuote = Tuote("test", 5)
        self.kori.lisaa_tuote(tuote)

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_kaksi_eri_tuotetta_luo_kaksi_ostosta(self):
        """Adding two different products creates two purchases."""
        tuote1 = Tuote("test1", 5)
        tuote2 = Tuote("test2", 6)
        self.kori.lisaa_tuote(tuote1)
        self.kori.lisaa_tuote(tuote2)

        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_kaksi_samaa_tuotetta_luo_yhden_ostoksen(self):
        """Adding the same product twice creates one purchase."""
        tuote = Tuote("test", 5)
        self.kori.lisaa_tuote(tuote)
        self.kori.lisaa_tuote(tuote)

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_kaksi_samaa_tuotetta_nimena_ja_maarana_yhdessa_ostoksessa(self):
        """One purchase stores the shared product name and quantity two."""
        tuote = Tuote("test", 5)
        self.kori.lisaa_tuote(tuote)
        self.kori.lisaa_tuote(tuote)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), tuote.nimi())
        self.assertEqual(ostos.lukumaara(), 2)

    def test_ostos_sisaltaa_tuotteen_nimen_ja_maaran(self):
        """The purchase stores the product name and quantity."""
        tuote = Tuote("test", 5)
        self.kori.lisaa_tuote(tuote)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), tuote.nimi())
        self.assertEqual(ostos.lukumaara(), 1)
