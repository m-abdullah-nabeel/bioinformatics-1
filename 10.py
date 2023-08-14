with open('data9.txt', 'r') as file:
    DNA9 = file.read().rstrip()

def HammingDistance(a, b):
    a = a.lower()
    b = b.lower()
    hd = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            hd += 1
    return(hd)

def ApproximatePatternMatching(Pattern, DNA, allowedHammingDistance):
    pos = []
    for i in range((len(DNA)+1)-len(Pattern)):
        kmer = DNA[i:i+len(Pattern)]
        # print(kmer)
        hammingDistance = HammingDistance(Pattern, kmer)
        if hammingDistance <= allowedHammingDistance:
            print(f"K-mer: {kmer} => Hamming Distance = {hammingDistance}")
            pos.append(i)
    return pos

def ApproximatePatternCount(Pattern, DNA, allowedHammingDistance):
    res = ApproximatePatternMatching(Pattern, DNA, allowedHammingDistance)
    print(res)
    print(len(res))
    return len(res)
    
# Pattern = 'GAGG'
# DNA = 'TTTAGAGCCTTCAGAGG'
# allowedHammingDistance = 2

Pattern = 'GCCGA'
DNA = 'CTTAAAAGTAAAAACTTTTATAACGCTCTGTCAACCATACAAGTCAGAAACCTTCGTCGCCTTACTTCCGGCGTTTTAGAGCAAGGTTTGTCGTAAAGTCTGCACAGTCCGGGGGGTGTCGCAAACCAACGGAGCTCCTGCTAAAGTTTAAGCGTGCCGACCCTAGCCGGCACGAGGGTATGTGATAAGCGTGTCATAGATCTGAATCGGGTGGCAAAGTTGTAATCTGTAAGCGCGAACAATAGCAAGTCCGTTCATCTACTGTGAAACTTAACACGCAACTCCTTCGTCAAGGCGATTCCGGCACTTGACACCCCGCCATGG'
allowedHammingDistance = 3

res = ApproximatePatternCount(Pattern, DNA, allowedHammingDistance)
print(res)

