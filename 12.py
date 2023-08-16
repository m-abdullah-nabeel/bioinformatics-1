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


def FrequentWordsWithMismatches(Text, k, d): 
    Patterns = []
    freqMap ={}
    n = len(Text)
    for i in range(1+n - k): #check if any error
        Pattern = Text[i: i+k] 
        # RevComp = revers_compliment(Pattern)
        neighborhood = list(Neighbors(Pattern, d))
        for j in range(len(neighborhood)-1): #check if any error
            neighbor = neighborhood[j]
            if neighbor in freqMap:
                freqMap[neighbor] = freqMap[neighbor] + 1
            else:
                freqMap[neighbor] = 1

    m = max(freqMap.values())
    for key in freqMap:
        if freqMap[key] == m:
            Patterns.append(key)
            # append Pattern to Patterns
    return Patterns


# sample = "CTCCCGCTCGCTTTAATTAATTAAAAGACGCTAAGACTCCCGCTTTAAAAGACTCCCGCTCTCCCTCCTTAATCACGCTAAGACGCTAAGATTAATCACTCCTTAATTAACGCTAAGATTAACTCCTCACTCCTTAATTAACGCTCTCCTTAATCAAAGACTCCTCACGCTCTCCTTAACGCTTTAACGCTTCATCATCATCATCACGCTTTAACTCCAAGACGCTAAGACGCTTCAAAGATCATCACTCCAAGAAAGACGCTAAGATCATCATCACGCTCTCCCGCTTCATTAACTCCCTCCTCACGCTTTAACTCCCTCCCGCTCTCCTCAAAGATCACGCTTCAAAGAAAGACGCTTTAATCATTAACGCTTCATCAAAGACTCCAAGACTCC"
# res = FrequentWordsWithMismatches(sample, 7, 2)


sample = "ATTTGGC"
res = FrequentWordsWithMismatches(sample, 3, 1)

print(res)
