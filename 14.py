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

# MotifEnumeration(Dna, k, d)
#     Patterns ← an empty set
#     for each k-mer Pattern in Dna
#         for each k-mer Pattern’ differing from Pattern by at most d mismatches
#             if Pattern' appears in each string from Dna with at most d mismatches
#                 add Pattern' to Patterns
#     remove duplicates from Patterns
#     return Patterns

def MotifEnumeration(Dna, k, d):
    Patterns = []
    motifs_candidate_all = []
    found_in_Dna = []
    shortlist_cand = []

    for strand in Dna: 
        for w in range(len(strand)+1-k):
            pattern = strand[w:w+k]
            pattern_neighbors = Neighbors(pattern, d)
            for pn in pattern_neighbors:
                motifs_candidate_all.append(pn)

    # print(len(motifs_candidate_all))

    for strand in Dna:
        for mf in motifs_candidate_all:
            print(f"{mf} exists in {strand}: {mf in strand}")
            if mf in strand:
                found_in_Dna.append(mf)

    print("found_in_Dna")
    print(found_in_Dna)
    print(len(found_in_Dna))

    for i in range(len(found_in_Dna)-1):
        if found_in_Dna[i] in Neighbors(found_in_Dna[i+1], d):
           shortlist_cand.append(found_in_Dna[i])


    print('shortlist_cand')
    print(shortlist_cand)
    print(len(shortlist_cand))
    print(len(list(set(shortlist_cand))))
    print(list(set(shortlist_cand)))
            
    #         if Pattern' appears in each string from Dna with at most d mismatches
    #             add Pattern' to Patterns
    # remove duplicates from Patterns
    return Patterns


sample = ['ATTTGGC', 'TGCCTTA' ,'CGGTATC', 'GAAAATT']
res = MotifEnumeration(sample, 3, 1)

print(res)