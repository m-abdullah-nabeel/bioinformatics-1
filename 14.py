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
    strand_kmers = {}


    for strand in Dna: 
        for w in range(len(strand)+1-k):
            pattern = strand[w:w+k]
            pattern_neighbors = Neighbors(pattern, d)
            for pn in pattern_neighbors:
                motifs_candidate_all.append(pn)


    for strand in Dna:
        strand_data = []
        for n in motifs_candidate_all:
            for i in range(len(strand)+1-k):
                c = strand[i:i+k]
                nbs = Neighbors(c, d)
                if n in nbs:
                    strand_data.append(n)
        strand_kmers[strand] = set(strand_data)
        

    print("strand_kmers")
    print(strand_kmers)

    strand_sets = list(strand_kmers.values())
    print("strand_sets")
    print(strand_sets)

    res = set.intersection(*strand_sets)

    print("res")
    print(res)
    print(len(res))
    # print(res)

    #         if Pattern' appears in each string from Dna with at most d mismatches         = if neighbor is found in each strand of dna
    #             add Pattern' to Patterns
    # remove duplicates from Patterns
    return Patterns


sample = ['ATTTGGC', 'TGCCTTA' ,'CGGTATC', 'GAAAATT']
res = MotifEnumeration(sample, 3, 1)

print(res)