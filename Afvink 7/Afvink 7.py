import re
import matplotlib


def bestandlezer():
    """Leest het bestand, in het bestand roept de functie regex aan, als het 'true' is, voeg het toe aan een 2d lijst.
    :return: 2d lijst met lijst[symbol][description][alias]
    """


def regex(regel):
    """Krijgt een variabele in string binnen, zoekt met een regular expression naar de woorden
    'Breast cancer', 'Breast carcinoma' of 'Ductal carcinoma'
    :return: boolean
    """


def print_(lijst2d):
    """Pakt een 2d lijst, telt hoeveel genen er zijn en print totaal aantal genen, gen naam en aliassen.
    :param lijst2d:
    :return: print aantal genen, gen naam en aliassen.
    """

def matplotlib_(lijst2d):
    """Gebruikt 2d lijst om aliassen per gene te tellen,
    maakt grafiek in matplotlib ter illustratie hoeveel aliassen genen hebben.
    :param lijst2d:
    :return: een grafiek
    """

def main():
    lijst2d = bestandlezer()
    print_(lijst2d)
    matplotlib_(lijst2d)