"""Shopping-cart implementation."""

from ostos import Ostos
from tuote import Tuote


class Ostoskori:
    """Store purchases and calculate cart contents."""

    def __init__(self):
        self._ostokset = []

    def _hae_ostos(self, tuote: Tuote) -> Ostos | None:
        for ostos in self._ostokset:
            if ostos.tuote == tuote:
                return ostos
        return None

    def tavaroita_korissa(self):
        """Return the number of individual items in the cart."""
        return sum(ostos.lukumaara() for ostos in self._ostokset)

    def hinta(self):
        """Return the total price of the cart."""
        return sum(ostos.hinta() for ostos in self._ostokset)

    def lisaa_tuote(self, lisattava: Tuote):
        """Add one unit of a product to the cart."""
        ostos = self._hae_ostos(lisattava)
        if ostos is None:
            self._ostokset.append(Ostos(lisattava))
            return
        ostos.muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        """Remove one unit of a product from the cart."""
        ostos = self._hae_ostos(poistettava)
        if ostos is None:
            return

        ostos.muuta_lukumaaraa(-1)
        if ostos.lukumaara() == 0:
            self._ostokset.remove(ostos)

    def tyhjenna(self):
        """Remove all purchases from the cart."""
        self._ostokset.clear()

    def ostokset(self):
        """Return the purchases in the cart."""
        return self._ostokset
