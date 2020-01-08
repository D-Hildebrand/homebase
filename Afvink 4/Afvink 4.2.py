import time
import re

def lees_inhoud():
    """Opent bestand,
    returnt headers en sequenties apart in een lijst"""

    try:
        bestand = open("Mus_musculus.GRCm38.pep.all.fa")
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

def dna_finder(header, seq):
    """Zoekt DNA in sequentie dmv regex. Print tijd.
    input header, seq. Output 2d lijst met header en seq."""
    tijd = time.time()
    dna = "[^ATGCN]"
    lijst = []
    lijst2 = []
    lijst4 = []

    teller = 0

    for i in seq:
        i.upper()
        match = re.search(dna, i)
        if match == None:
            lijst.append(i)
            lijst2.append(header[teller])
            lijst3 = []
            lijst3.append(lijst2[-1])
            lijst3.append(lijst[-1])
            lijst4.append(lijst3)
        teller += 1

    lijst.append(lijst2)
    print(lijst4)
    tijd2 = time.time()
    tottime = tijd2 - tijd
    print(tottime)

def oude_finder(header, seq):
    """Zoekt of een sequentie DNA is door het tellen van ATCGN en dit te vergelijken met
    de lengte van de gehele sequentie en print hoe lang het runt.
    Input header, seq. Output lijst met header en seq."""
    tijd = time.time()
    teller = 0
    lijst = []
    for i in seq:
        i.upper()
        isdna = i.count("A") + i.count("T") + i.count("C") + i.count("G") + i.count("N")
        if len(i) == isdna:
            dna = header[teller] + " " + i
            lijst.append(dna)
            teller += 1
    print(lijst)
    tijd2 = time.time()
    tottijd = tijd2 - tijd
    print(tottijd)

def main():
    header, seq = lees_inhoud()
    dna_finder(header, seq)
    oude_finder(header, seq)

main()


consensuspatroon = "[(TATA)(A|T)(AA|T)]"