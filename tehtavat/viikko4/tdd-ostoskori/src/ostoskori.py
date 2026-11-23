"""Shopping-cart implementation."""

from ostos import Ostos
from tuote import Tuote


class Ostoskori:
    """Store purchases and calculate cart contents."""

    def __init__(self):
        self._ostokset = []

    def tavaroita_korissa(self):
        """Return the number of individual items in the cart."""
        return sum(ostos.lukumaara() for ostos in self._ostokset)

    def hinta(self):
        """Return the total price of the cart."""
        return sum(ostos.hinta() for ostos in self._ostokset)

    def lisaa_tuote(self, lisattava: Tuote):
        """Add one unit of a product to the cart."""
        for ostos in self._ostokset:
            if ostos.tuote == lisattava:
                ostos.muuta_lukumaaraa(1)
                return

        self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        """Remove one unit of a product from the cart."""

    def tyhjenna(self):
        """Remove all purchases from the cart."""

    def ostokset(self):
        """Return the purchases in the cart."""
        return self._ostokset
