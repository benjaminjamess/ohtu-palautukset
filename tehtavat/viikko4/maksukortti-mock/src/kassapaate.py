"""Handle lunch purchases and payment-card top-ups."""

HINTA = 5


class Kassapaate:
    """Cash register that charges and tops up payment cards."""

    def __init__(self):
        self.__myytyja_lounaita = 0

    def lataa(self, kortti, summa):
        """Load a positive amount onto a payment card."""
        if summa > 0:
            kortti.lataa(summa)

    def osta_lounas(self, kortti):
        """Charge for lunch when the card has enough balance."""
        if kortti.saldo() >= HINTA:
            kortti.osta(HINTA)
            self.__myytyja_lounaita = self.__myytyja_lounaita + 1
