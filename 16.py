def HammingDistance(a, b):
    a = a.lower()
    b = b.lower()
    hd = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            hd += 1
    return(hd)

def Suffix(Pattern): 
    return Pattern[1:]

def Neighbors(Pattern, d): 
    if d == 0: 
        return {Pattern}
    if len(Pattern) == 1: 
        return {'A', 'C', 'G', 'T'}
    Neighborhood = set()
    SuffixNeighbors = Neighbors(Suffix(Pattern), d)
    # for each string Text from SuffixNeighbors:
    for Text in SuffixNeighbors:
        if HammingDistance(Suffix(Pattern), Text) < d:
            # for each nucleotide x:
            for x in 'ATCG':
                # add x • Text to Neighborhood
                Neighborhood.add(x+Text)
        else:
            # add FirstSymbol(Pattern) • Text to Neighborhood
            Neighborhood.add(Pattern[0]+Text)

    return Neighborhood


def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k = len(Pattern)
    distance = 0
    for Text in Dna:
        HammingDis = float('inf')
        for i in range(len(Text)+1-k):
            kmer = Text[i:i+k]
            # print(Pattern, kmer)
            hdn = HammingDistance(Pattern, kmer)
            if HammingDis > hdn:
                HammingDis = hdn
        distance = distance + HammingDis
    return distance


def MedianString(Dna, k):
    distance = float('inf')
    Median = ''
    # Patterns ← AllStrings(k)
    Patterns = []
    for strand in Dna:
        for i in range(len(strand)+1-k):
            kmer = strand[i:i+k]
            nbs = Neighbors(kmer, 2)
            for n in nbs: Patterns.append(n)

    for i in range(len(Patterns)):
        Pattern =  Patterns[i]
        if distance > DistanceBetweenPatternAndStrings(Pattern, Dna):
            distance = DistanceBetweenPatternAndStrings(Pattern, Dna)
            Median = Pattern
    print("Median: ")
    print(Median)
    return Median

# sam = ['AAATTGACGCAT', 'GACGACCACGTT', 'CGTCAGCGCCTG', 'GCTGAGCACCGG', 'AGTTCGGGACAG']
# res = MedianString(sam, 3)

sam = [
'TGAAATGGAAACTGGACTGAGTCACGAAGATGTCCTTATGTT',
'CGCGACCCTCCATATGTTCGCCATGACGGATTGAGCGCGTGA',
'GAATGATATAAGTAAGTTAGCACCCATGTCGATAGTTTCAGA',
'TATGTTCTGAGACTAATTTAGCACTACTCTTATTGCGTCTGT',
'TAGGTTTAGCCAACGTGTCACCGCGATGAAGTCGGCCGCCGT',
'TCCTGTCGTTCGCTATCTTGGCGTTAAGTTCCAATACGGCAC',
'TTTCGGATTACAAATCATTCTGTCTGTTGCTACGTTTGCTCC',
'GGCTGCTCAAAGCACGTGACCACACAGGTGAAGTGATAGGTT',
'ATGTAATGATTTTTCATAAGAACCTACGTTCGAACCCGCCCC',
'CCCGCATACACGGGCCGTAATAACTGACTATACGTTGAATTA']

res = MedianString(sam, 6)

# print(res)