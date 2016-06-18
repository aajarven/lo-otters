#-*- coding:utf-8 -*-

class Laatta:
    """ Laatta joista kartta koostuu. Muun muassa jokeinen pelaaja, laatikko ja ansa on pelin aikana koko ajan yhden
    laatan päällä
    """

    def __init__(self, x, y):
        self.sijainti = (x, y)
        self.ansa = None
        self.hahmo = None
        self.monsteri = None
        self.laatikko = None

    def onKaveltavissa(self):
        """ Palauttaa True jos laatan päälle voi kävellä, False jos ei voi
        """
        if self.ansa == None and self.hahmo == None and self.monsteri == None:
            return True
        else:
            return False

    def poistaPelaaja(self):
        self.hahmo = None

    def asetaPelaaja(self, hahmo):
        if self.hahmo != None:
            raise LaattaVarattu("Laatta sijainnissa "+str(self.sijainti)+" sisälsi jo hahmon "+str(self.hahmo)+
                                " kun sinne yritettiin sijoittaa hahmo "+str(hahmo))
        else:
            self.hahmo = hahmo


class LaattaVarattu(Exception):
    pass