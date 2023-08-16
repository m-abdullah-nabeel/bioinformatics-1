def HammingDistance(str1, str2):
  count = 0
  for i in range(len(str1)):
    if str1[i] != str2[i]:
      count += 1
  return count
  
def neighbors(kmer, distance):
  k = len(kmer)
  if k == 0:
      return {}
  if distance == 0:
      return {kmer}
  if k == 1:
      return {'A', 'T', 'C', 'G'}
  suffix = kmer[1:]
  suffix_neighbors = neighbors(suffix, distance)
  result = set()
  for suffix_neighbor in suffix_neighbors:
    if HammingDistance(suffix_neighbor, suffix) == distance:
        result.add(kmer[0] + suffix_neighbor)
    else:
        result.add('A' + suffix_neighbor)
        result.add('T' + suffix_neighbor)
        result.add('C' + suffix_neighbor)
        result.add('G' + suffix_neighbor)
  return result

    # MotifEnumeration(Dna, k, d)
    #     Patterns ← an empty set
    #     for each k-mer Pattern in the first string in Dna
    #         for each k-mer Pattern’ differing from Pattern by at most d mismatches
    #             if Pattern' appears in each string from Dna with at most d mismatches
    #                 add Pattern' to Patterns
    #     remove duplicates from Patterns
    #     return Patterns
        
def MotifEnumeration(dna, k, d):
  patterns = []
  motifs = []  
  motifs2 = []  
  fstr = []
  
  for strand in dna:
    sstr = []
    nsstr = []
    for i in range(len(strand)-k+1):
      sstr.append(list(neighbors(strand[i:i+k], d)))
      print(sstr)
      
      print("sstr---------------------------------------------------------------------------------------------------------")
      motifs.append(list(neighbors(strand[i:i+k], d))) 
      for ij in list(neighbors(strand[i:i+k], d)):
        print(ij)
        nsstr.append(ij)
      print(nsstr)
      print(len(nsstr))
    motifs2.append(nsstr)

    print("Next strand====================================================================================================")
      
  print(motifs) # 20 in number for sample dna
  print("motifs2")
  print(motifs2) 
  print(len(motifs2)) 
  
  result = set(motifs[0])
  for s in motifs[1:]:
    result.intersection(*s)

  result2 = set(motifs2[0])
  for s in motifs[1:]:
    result2.intersection(*s)

  print(result)
  print("result????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")
  print(result2)
  
  o = []
  for res in result:
    for strand in dna:
      for i in range(len(strand)-k+1):
        if(res in neighbors(strand[i:i+k], d)):
          o.append(res)
  print("Told to be accurate $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
  print(list(set(o)))
  print(len(list(set(o))))

#   return list(patterns)

  o2 = []
  for res in result2:
    for strand in dna:
      for i in range(len(strand)-k+1):
        if(res in neighbors(strand[i:i+k], d)):
          o2.append(res)
  
  print("Should be accurate $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
  print(list(set(o2)))


#   return list(set(o))
  return list(set(o2))
      


k = 3
d = 1
t = [
"ATTTGGC",
"TGCCTTA",
"CGGTATC",
"GAAAATT"]

res=MotifEnumeration(t,k,d)
# # print(neighbors(t[0], 1))    

# t = ['CTAGGATGGCTCCGCTTATTTCTGT', 'TAGGGCCTTAAAGTCCTAGACTGGC', 'ACATGGATGCATGTATTGGACTTGC', 'CTTGAACAAATCTGATTTCTCCGTA', 'GAGACCTCGCCTGCCCTGTTGACCA', 'AGCAGAATAACTAGGGGCTATCCCA']
# res = MotifEnumeration(t,5,2)

# print(res)

for i in res:
   print(i)
