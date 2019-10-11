#D.Hildebrand 10-10-2019




def openfile():
    """Opent bestand met bestandsnaam, retourneert sequentie in string(seq) en header in string(header)"""

    bestand = open(input("geef bestandsnaam "))

    seq = ""
    header = ""
    for regel in bestand:
        if not regel.startswith(">") or regel.startswith(" "):
            seq += regel.rstrip()

    for regel in bestand:
        if regel.startswith(">"):
            header += regel.rstrip()

    print (seq)
    return seq, header


def isDNA(seq):
    """Checkt of input sequentie(seq) in string DNA is. Retourneert DNA = True of DNA = False"""

    lengte = len(seq)
    DNA = False
    n = seq.count ("N") #Asparagine Asn
    a = seq.count ("A") #Alanine Ala
    t = seq.count ("T") #Threonine Thr
    c = seq.count ("C") #Cysteine Cys
    g = seq.count ("G") #Glycine Gly

    if lengte == n + a + t + c + g:
        print ("\nDit is DNA.")
        print ("Complete seq lengte is ",lengte)
        DNA = True
    else:
        print ("Dit is een eiwit.")
        DNA = False
    return (DNA)


"""Input sequentie(seq) in string en input DNA = True/False, knip checkt of 5 enzymen knippen op (seq). Retourneert knipt = True/False."""


def knip(seq,DNA):
    knipt = False
    if DNA == False:
        print("Kan niet op een eiwit knippen")
    else:
        DdeI   = "CTGAG"    #knipt op C^TGAG      Desulfovibrio desulfuricans    	
        BspMII = "TCCGGA"   #knipt op T^CCGGA     Klebsiella pneumoniae 
        EcoRI  = "GAATTC"   #knipt op G^AATTC     Escherichia coli
        HindIII= "AAGCTT"   #knipt op A^AGCTT     Haemophilus influenzae
        TaqI   = "TCGA"     #knipt op T^CGA    	  Thermus aquaticus

        DdeI = seq.count (DdeI)
        BspMII = seq.count (BspMII)
        EcoRI = seq.count (EcoRI)
        HindIII = seq.count (HindIII)
        TaqI = seq.count (TaqI)
        if (DdeI) > 0:
            print("DdeI knipt op de sequentie op",DdeI,"plaatsen.")
        if (BspMII) > 0:
            print("BspMII knipt op de sequentie op",BspMII,"plaatsen.")
        if (EcoRI) > 0:
            print("EcoRI knipt op de sequentie op",EcoRI,"plaatsen.")
        if (HindIII) > 0:
            print("HindIII knipt op de sequentie op",HindIII,"plaatsen.")
        if (TaqI) > 0:
            print("TaqI knipt op de sequentie op",TaqI,"plaatsen.")
        if (DdeI) > 0 or (BspMII) > 0 or (EcoRI) > 0 or (HindIII) > 0 or (TaqI) > 0:
            knipt = True

        return (knipt)




def main():
    seq, header =openfile()
    print(header,"\nDit is het ingevoerde bestand")
    DNA =isDNA(seq)
    knipt =knip(seq,DNA)
    
    
main()
    
    
