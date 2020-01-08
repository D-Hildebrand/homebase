import re


class dna:
    def __init__(self, seq):
        # self.__setDNA = "" #open("Felis_catus.Felis_catus_8.0.cdna.all.fa")       "AGTAAGTCGATTCAGATGAACGTAATTTGAC"
        self.setDNA(seq)

    def setDNA(self, seq):
        """Kijkt of de aangeleverde sequentie DNA is. Print of it zo is of niet"""
        if re.search("^[ATGCN]*$", seq):
            print("Dit is DNA, de sequentie is geaccepteerd.")
            self.__seq = seq
        else:
            print("Dit is geen DNA, de sequentie is niet geaccepteerd.")

    def getdna(self):
        """Returnt de DNA sequentie string"""
        print(self.__seq, "5>3 DNA")
        # return(self.__seq)

    def gettranscript(self):
        """"Pakt 5>3 DNA en returnt 5>3 RNA"""
        # Iets gaat mis met de replace functie, hij vervangt niks en zet gewoon de letter in temp
        seq = self.__seq
        temp = ""
        for letter in seq:
            if letter == "A":
                letter =letter.replace("A", "U")
                temp += letter
            elif letter == "T":
                letter =letter.replace("T", "A")
                temp += letter
            elif letter == "G":
                letter =letter.replace("G", "C")
                temp += letter
            elif letter == "C":
                letter =letter.replace("C", "G")
                temp += letter
            else:
                print("uh oh iets is mis")
        print(temp, "3<5 RNA")
        # return temp[::-1]

    def getlength(self):
        seq = self.__seq
        length = len(seq)
        print("De lengte van het DNA is", length)
        # return length

    def getgc(self):
        seq = self.__seq
        g = seq.count("G")
        c = seq.count("C")
        length = len(seq)
        gcperc = (g + c) / length
        gcperc = gcperc * 100
        print("Het GC Percentage is", str(gcperc)+"%")
        # return gcperc


klasse = dna("ACTGGAATCAGATGATAAACCCAGAGGATGACGAG")
klasse.getdna()
klasse.getlength()
klasse.gettranscript()
klasse.getgc()

def lees_inhoud():
    """Opent bestand,
    returnt headers en sequenties in een lijst"""

    try:
        bestand = open("Felis_catus.Felis_catus_8.0.cdna.all.fa")
        headers = []
        seqs = []
        seq = ""
        for line in bestand:
            line = line.strip()
            if ">" in line:
                if seq != "":
                    seqs.append(seq)
                    seq = ""
                headers.append(line)
            else:
                seq += line.strip()
        seqs.append(seq)
        if headers == "":
            print("Weet u zeker of u wel het goede bestand heeft? Er zijn namelijk geen headers.")
        return headers, seqs
    except FileNotFoundError:
        print("Het gegeven bestand bestaat niet, "
              "check of het bestand in het mapje met de code zit en of het wel FASTA is.")
        exit()


def dnachecks(seqs, headers):
    counter = 0
    dnalist = []
    highestgc = 0.0
    highestgcnum = ""
    for seq in seqs[:5]:
        counter += 1
        dnanum = counter
        dnanum = dna(seq)
        number = counter
        number = str(number)
        dnalist += number
        dnanum.getlength()
        dnanum.gettranscript()
        dnanum.getgc()
    #     if dnanum.getgc() > highestgc:
    #         highestgc = dnanum.getgc()
    #         highestgcnum = number
    # highestgcnum -= 1
    # print(highestgc, headers[highestgcnum])
    #Return werkt niet helemaal op de class dus ik kan niet hier de variabele krijgen.
def main():
    headers, seqs = lees_inhoud()
    dnachecks(seqs, headers)

main()