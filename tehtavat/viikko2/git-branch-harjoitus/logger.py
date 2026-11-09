"""Aikaleimallisten viestien tulostaminen."""

from datetime import datetime


def logger(viesti):
    """Tulostaa viestin nykyisen aikaleiman kanssa."""
    print(f"{datetime.now()}: {viesti}")
