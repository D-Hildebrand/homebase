import random


class Pet:
    def __init__(self):
        self.__leeftijd = 0
        self.__naam = ""
        self.__soort = ""

    def setNaam(self, naam):
        self.__naam = naam

    def getNaam(self):
        return self.__naam

    def setDiersoort(self, soort):
        self.__soort = soort

    def getDiersoort(self):
        return self.__soort

    def setLeeftijd(self, leeftijd):
        self.__leeftijd = leeftijd

    def getLeeftijd(self):
        return self.__leeftijd


# Kreeg deze niet aan de praat: hij pakt het alleen maar als merk "Ford" tussen aanhalingstekens staan
# Ook krijg ik hem niet te pakken als ik de huidige snelheid wil returnen.
class auto:
    def __init__(self, merk, modeljaar):
        self.__snelheid = 0
        self.__merk = str(merk)
        self.__modeljaar = modeljaar

    def setSnelheid(self, inputspd):
        if isinstance(inputspd, str) == True:
            inputspd.lower()
            if inputspd == "optrekken" or inputspd == "accelerate":
                if self.__snelheid >= 0 and self.__snelheid <= 195:
                    self.__snelheid += 5
                elif self.__snelheid > 195 and self.__snelheid < 200:
                    self.__snelheid = 200
                    print("Topsnelheid van 200 km/u bereikt!")
                else:
                    print("Topsnelheid van 200 km/u bereikt! Je kan niet sneller.")
            if inputspd == "afremmen" or inputspd == "brake":
                if self.__snelheid >= 5 and self.__snelheid <= 200:
                    self.__snelheid -= 5
                elif self.__snelheid > 0 and self.__snelheid < 5:
                    self.__snelheid = 0
                    print("Je staat stil.")
                else:
                    print("Je staat stil. Je kan niet langzamer.")
        if isinstance(inputspd, int) == True:
            if inputspd >= 0 and inputspd <= 200:
                self.__snelheid == inputspd
            else:
                print("Deze snelheid kan je niet instellen: het kan tussen de van 0 tm 200 zijn.")
        print(self.getSnelheid())

    def getSnelheid(self):
        return self.__snelheid

    def getMerk(self):
        return self.__merk

    def getModeljaar(self):
        return self.getModeljaar


a = auto("Ford", 2006)
a.setSnelheid(80)
a.getSnelheid()
a.setSnelheid("optrekken")
a.setSnelheid("optrekken")
a.setSnelheid("optrekken")
a.setSnelheid("optrekken")
a.setSnelheid("optrekken")
a.setSnelheid("afremmen")
a.setSnelheid("afremmen")
a.setSnelheid("afremmen")
a.setSnelheid("afremmen")
a.setSnelheid("afremmen")


class trivia:
    score = 0

    def __init__(self):
        self.__question1 = "europa"
        self.__question2 = "nederland"
        self.__question3 = "willem"

    def question1(self):
        answer = input("Welk continent is het beste continent? ")
        answer.lower()
        print(self.question1)
        if answer == self.__question1:
            trivia.score += 1

    def question2(self):
        answer = input("Welk land is het mooiste in Europa? ")
        answer.lower()
        if answer == self.__question2:
            trivia.score += 1

    def question3(self):
        answer = input("Hoe heet de Koning van Nederland? ")
        answer.lower()
        if answer == self.__question3:
            trivia.score += 1


def main():
    trivia1 = trivia()
    trivia1.question1()
    trivia1.question2()
    trivia1.question3()
    speler1 = trivia.score
    trivia2 = trivia()
    trivia2.question3()
    trivia2.question2()
    trivia2.question1()
    speler2 = trivia.score

    if speler1 > speler2:
        print("Speler 1 wint!")
    elif speler2 > speler1:
        print("Speler 2 wint!")
    else:
        print("Gelijk spel.")


main()
