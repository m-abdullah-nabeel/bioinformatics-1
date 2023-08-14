def FrequencyTable(Text, k):
    freqMap  = {}
    n  = len(Text)
    print(f"n = {n}")
    for i in range(n-k):
        Pattern = Text[i:i+k] #← Text(i, k)
        print(f"Pattern: {Pattern}")
        if Pattern not in freqMap: #freqMap[Pattern] doesn't exist
            freqMap[Pattern] = 1
        else:
           freqMap[Pattern] = freqMap[Pattern]+1 
    return freqMap


def BetterFrequentWords(Text, k):
    FrequentPatterns = [] 
    freqMap = FrequencyTable(Text, k)
    # max ← MaxMap(freqMap)
    maxVal = max(freqMap.values())
    for Pattern in freqMap:
        if freqMap[Pattern] == maxVal:
            FrequentPatterns.append(Pattern)
    return FrequentPatterns

# textSample = "TAGGTGCAGCCGAAGCTGAACTTCGTCGCGATTGCGTCTCAACTTTCACTAGGTGCAGCCGAAGCTGATAGGTGCAGGATTGCGTCTGATTGCGTCTCAACTTTCACGATTGCGTCTTAGGTGCAGCAACTTTCACTAGGTGCAGCCGAAGCTGAACTTCGTCGCACTTCGTCGCTAGGTGCAGCCGAAGCTGAGATTGCGTCTCCGAAGCTGACAACTTTCACGATTGCGTCTCCGAAGCTGACCGAAGCTGAACTTCGTCGCGATTGCGTCTACTTCGTCGCCAACTTTCACACTTCGTCGCCAACTTTCACGATTGCGTCTCCGAAGCTGACAACTTTCACCAACTTTCACCCGAAGCTGACCGAAGCTGACCGAAGCTGACAACTTTCACCAACTTTCACTAGGTGCAGGATTGCGTCTGATTGCGTCTCCGAAGCTGACCGAAGCTGAACTTCGTCGCGATTGCGTCTTAGGTGCAGACTTCGTCGCACTTCGTCGCGATTGCGTCTGATTGCGTCTACTTCGTCGCACTTCGTCGCTAGGTGCAGCCGAAGCTGACAACTTTCACTAGGTGCAGTAGGTGCAGGATTGCGTCTCCGAAGCTGAACTTCGTCGCTAGGTGCAGCCGAAGCTGATAGGTGCAGTAGGTGCAGACTTCGTCGCGATTGCGTCTACTTCGTCGCGATTGCGTCTGATTGCGTCTTAGGTGCAGGATTGCGTCTACTTCGTCGCGATTGCGTCTTAGGTGCAGCAACTTTCACCCGAAGCTGATAGGTGCAGACTTCGTCGCCAACTTTCACCAACTTTCACTAGGTGCAGTAGGTGCAGCAACTTTCACGATTGCGTCTACTTCGTCGCCCGAAGCTGACAACTTTCACCCGAAGCTGACAACTTTCACCAACTTTCACACTTCGTCGCTAGGTGCAGCAACTTTCACTAGGTGCAGTAGGTGCAGACTTCGTCGCACTTCGTCGCCCGAAGCTGA"
# tx = "atcaatgatcaacgtaagcttctaagcATGATCAAGgtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagATGATCAAGagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaATGATCAAGctgctgctcttgatcatcgtttc"
# o = BetterFrequentWords(tx, 9)
# print(o)
# for i in o: print(i)


print(BetterFrequentWords(Text='aactctatacctcctttttgtcgaatttgtgtgatttatagagaaaatcttattaactgaaactaaaatggtaggtttggtggtaggttttgtgtacattttgtagtatctgatttttaattacataccgtatattgtattaaattgacgaacaattgcatggaattgaatatatgcaaaacaaacctaccaccaaactctgtattgaccattttaggacaacttcagggtggtaggtttctgaagctctcatcaatagactattttagtctttacaaacaatattaccgttcagattcaagattctacaacgctgttttaatgggcgttgcagaaaacttaccacctaaaatccagtatccaagccgatttcagagaaacctaccacttacctaccacttacctaccacccgggtggtaagttgcagacattattaaaaacctcatcagaagcttgttcaaaaatttcaatactcgaaacctaccacctgcgtcccctattatttactactactaataatagcagtataattgatctga', k=9))


# if __name__ == "__main__":
#     main()