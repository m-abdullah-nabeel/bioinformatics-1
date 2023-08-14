# def Neighbors(Pattern, d):
#     if d == 0:
#         return {Pattern}
#     if len(Pattern) == 1:
#         return {'A', 'C', 'G', 'T'}
#     Neighborhood = ()
#     SuffixNeighbors ← Neighbors(Suffix(Pattern), d)
#     for each string Text from SuffixNeighbors
#         if HammingDistance(Suffix(Pattern), Text) < d
#             for each nucleotide x
#                 add x • Text to Neighborhood
#         else
#             add FirstSymbol(Pattern) • Text to Neighborhood
#     return Neighborhood
