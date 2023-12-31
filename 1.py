def PatternCount(Text, Pattern):
    count = 0
    for i in range((len(Text)+1)-len(Pattern)):
        print("Iteration "+str(i)+": Text: "+Text[i:i+len(Pattern)] + "=")
        if Text[i:i+len(Pattern)] == Pattern:
            count += 1

    print(f"Count: {count}")
    return count


# Text = 'TTGTGCCAGTTGTGCCATGTGCCATGTGCCAGGGTGTGCCATTGTGCCATTTGTGCCACCCTGTGCCACTGTGCCACTGTGCCATGTGCCAGTTGTGCCATTGTGCCATACGATATGTGCCAGAAGCTGTGCCAGTCCTGTGCCATGTGCCAACGTCTGTGTGCCAGAGACTGTGCCAATTGTGCCATTGTGCCAACTGTGCCATTTTGTGCCACAGCTGTGCCAATTGTGCCAGTTGTGCCAATTGTGCCAGGTCTGTGCCATGTGCCATTGTGCCACTCTGTGCCATATGTGCCATGTGCCAGATTGTGCCACATGTGCCACTGTGCCAGATGTAGCCTGTGCCACTTTCATGTGCCATAGTGTGCCACGCTGTGCCATGTGCCACACATGTGCCATTCTGTGCCAGACGATGTGCCATGGTGTGCCATTGTGTGCCAATGTGCCAAGGTGTGCCAACTTTGCATGTGTGCCATGTGCCAATGTGCCATGTGCCATTGTGCCAGTGTGCCATGTGCCATGTGCCACGTCATTACGTGTGCCAGTGTGCCACTGTGCCACTGTGCCAGCTCTGTGCCATGGGTTGTGCCACCGCTGTGCCAACGAATGTGCCACCGTCTGTGCCAGGACCGTGTGCCACCAGTGTGCCAGGCGGATGTGCCATTATTGTGCCATGATGTGCCACTGTGCCAACGTGTGCCATTGTGCCAATCTTGTGCCACTTGTGCCATGTGCCAGGGACATGTGCCATGTGCCAGGCCGTGTGCCATTGATGTGCCATGTGCCAAATGTGCCATTACTTCTGTGACATTTTGTGCCACTTTATGTGCCATGTGCCAAGGGTGTGCCATATGGGTTGTGCCATATGTGCCAACTGTGCCACTTGTGCCATGAAGTGTGCCAATGTGCTGTGCCATTGCCTGATGCCTGTGCCAATGTGCCAGTTTGCGTGTGCCACCAGCTGTGCCAACCCGTACTGTGCCAATAATGTGCCATGCGGTGTGCCACTTGGAAGCTTTCTTGTGCCATTGTGCCAGTTGTGCCATGTGCCAG' 
# Pattern = 'TGTGCCATG'
# print(PatternCount(Text, Pattern))

Text = 'aactctatacctcctttttgtcgaatttgtgtgatttatagagaaaatcttattaactgaaactaaaatggtaggtttggtggtaggttttgtgtacattttgtagtatctgatttttaattacataccgtatattgtattaaattgacgaacaattgcatggaattgaatatatgcaaaacaaacctaccaccaaactctgtattgaccattttaggacaacttcagggtggtaggtttctgaagctctcatcaatagactattttagtctttacaaacaatattaccgttcagattcaagattctacaacgctgttttaatgggcgttgcagaaaacttaccacctaaaatccagtatccaagccgatttcagagaaacctaccacttacctaccacttacctaccacccgggtggtaagttgcagacattattaaaaacctcatcagaagcttgttcaaaaatttcaatactcgaaacctaccacctgcgtcccctattatttactactactaataatagcagtataattgatctga' 
Pattern = 'aacctacca'
print(PatternCount(Text, Pattern))
print(len(Text))
