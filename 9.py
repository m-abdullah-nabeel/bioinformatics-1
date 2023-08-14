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

# Pattern = 'ATTCTGGA'
# DNA = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
# allowedHammingDistance = 3


# Pattern = 'GGGGTTCTCCA'
# DNA = DNA9
# allowedHammingDistance = 4

Pattern = 'AAAAA'
DNA = 'AACAAGCTGATAAACATTTAAAGAG'
allowedHammingDistance = 2

res = ApproximatePatternMatching(Pattern, DNA, allowedHammingDistance)
print(res)


df=open('out9.txt','w')
for i in res: 
    df.write(str(i))
    df.write('\n')
    print(i)
df.close()


# print(len(DNA9))