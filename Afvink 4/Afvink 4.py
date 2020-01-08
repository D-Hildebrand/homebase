import re

def lees_inhoud():
    """Opent bestand,
    returnt headers en sequenties in een lijst"""

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


def zoekpatroon(header, seq):
    lijst = []
    lijst2 = []
    regular_expression = "MCNSSC[MV]GGMNRR"
    for i in seq:
        match = re.search(regular_expression, i)
        if match:
            print(match.group())
            lijst2.append(header[seq.index(i)])
            lijst2.append(i)
            lijst.append(lijst2)

    print(lijst, lijst2)


#zoekpatroon is MCNSSC[MV]GGMNRR

def main():
    header, seq = lees_inhoud()
    zoekpatroon(header, seq)


main()