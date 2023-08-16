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
    print("Starting Brute-Force Search for Candidate Motif / Motif Enumeration...\n\n\n")
    motifs_candidate_all = []
    strand_kmers = {}

    for strand in Dna: 
        print("Starting Search with Dna String: ", strand)
        for w in range(len(strand)+1-k):
            pattern = strand[w:w+k]
            # print(f"Along the window in {strand}, the k-mer is {pattern}.")
            pattern_neighbors = Neighbors(pattern, d)
            for pn in pattern_neighbors:
                motifs_candidate_all.append(pn)
            # print(f"Generated and processed Neighbors of {pattern}: {pattern_neighbors}")
    
    print("Completed the generation of k-mers library\n\n\n")

    print("Started the finding of each kmer from kmer library, in Dna strands")
    for strand in Dna:
        strand_data = []
        for n in motifs_candidate_all:
            # print("Current Motif: ", n)
            for i in range(len(strand)+1-k):
                # print("Starting a window")
                c = strand[i:i+k]
                nbs = Neighbors(c, d)
                # print(f"Comparing {n} with neighbors of {c}, the neighbors are: {nbs}")
                if n in nbs:
                    strand_data.append(n)
                    # print(f"Found {n} in {nbs}...")
        strand_kmers[strand] = set(strand_data)
        # print(f"Storing Data of strand {strand} in dictionary. The data is an array converted to set: {strand_data} ")
        
    print("Data of Strands and KMers. This shows all the kmers with a hamming distance of d found in a Dna Strand")
    # print(strand_kmers)

    strand_sets = list(strand_kmers.values())
    print("Getting values from Dictionary")
    print("The Values are: ")
    print(strand_sets)

    for i in range(10):
        print("Finalizing Results", "."*i)
    res = set.intersection(*strand_sets)
    print("Intersecting the sets contaning data from each strand.")

    print("Result: ")
    print(res)
    print(len(res))

    print("Script written by Muhammad Abdullah Nabeel")
    return res


# sample = ['ATTTGGC', 'TGCCTTA' ,'CGGTATC', 'GAAAATT']
# res = MotifEnumeration(sample, 3, 1)

sample = ['CTGATGTACACCATCCGCGCGTATG', 'GGGGGTATGGTTTCTGGAGACCCTC', 'CCCTCAGTTCCATCACTGGCGTGGT', 'CCTTCTTATACAGTGCAACACGGAT', 'CATAACCGTCTCGGTACTAGTCTGA', 'TAGATCCGTCACAATAGCTAGCTTG']
res = MotifEnumeration(sample, 5, 1)

print(res)
for i in res:
    print(i)