def Skew(Genome):
    skew = [0]
    skVal = 0
    for b in Genome:
        print(b)
        if b == 'G': 
            skVal += 1
            # skew.append(skVal)
        elif b == 'C': 
            skVal -= 1
            # skew.append(skVal)
        # else :
        skew.append(skVal)

    return skew

# print(Skew('CATGGGCATCGGCCATACGCC'))

# sample = 'GAGCCACCGCGATA'
sample = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'
x = Skew(sample)
print(x)
# for i in x: print(i)