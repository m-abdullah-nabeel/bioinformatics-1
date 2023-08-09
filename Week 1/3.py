def revers_compliment(DNA):
    reverse = DNA[::-1]
    print(f"{reverse} = Reverse")
    compliment = ''
    for b in reverse:
        if b == 'A': compliment = compliment + 'T'
        if b == 'T': compliment = compliment + 'A'
        if b == 'C': compliment = compliment + 'G'
        if b == 'G': compliment = compliment + 'C'
    print(f"{compliment} = Reverse Compliment")
    return compliment

x = revers_compliment('AAAACCCGGT')
# print(x)
