from itertools import permutations
import math
import ast

def count_permutations_with_inversion_set(n, inversion_set_1_based):
    # all permutations of length n
    all_permutations = permutations(range(1, n+1))

    def count_inversions(perm):
        # +2 family Hessenberg function
        h = []
        
        # Adding entries to h
        for i in range(n):
            if i<3:
                h.append(i+3)
            else: 
                h.append(n)
                
        # Inversions list
        inversions = []
        for i in range(n):
            for j in range(i + 1, n):
                # Strict inequality because inversion set is 0-based and additional check with h
                if perm[i] > perm[j] and j < h[i]:
                    inversions.append((i, j))
        return inversions
    
    # Check how many permutations match the desired inversion set
    valid_perms = []
    for perm in all_permutations:
        perm_inversions = count_inversions(perm)
        if sorted(perm_inversions) == sorted(inversion_set_1_based):
            valid_perms.append(perm)

    return valid_perms

# this is a h-inversion polynomial developed in my research project
def polynomial(n, hinversions):
    # Getting m (maximum index for adjacent pair)
    m = 0
    adjacent_pair_i = []

    for i in range(len(hinversions)):
        if hinversions[i][1] == hinversions[i][0] + 1:
            index = hinversions[i][0]+1 #convert to 1-based
            adjacent_pair_i.append(index)
    if adjacent_pair_i:
        m = max(adjacent_pair_i)
    else:
        m = 0  # or handle differently if needed

    bh = []
    # Get B_h(S;2m+1)
    perms = count_permutations_with_inversion_set(2 * m + 1, hinversions)
    pi = []
    # For each k = 0 to m
    for k in range(m+1):
        for perm in perms:
            for i in perm:
                if m + 2 <= i and i <= m + k + 1:
                    pi.append(perm) # size of pi is a_k(S)
        chunk = len(pi) * math.comb(n - m - 1, k) # this is k-th term of the series
        bh.append(chunk)
    
    total = sum(bh) # total summation of the series
    return total    

# Input from user
n = int(input("Enter the value of n (length of permutation): "))
inversion_set_str = input("Enter the inversion set, e.g. [(1, 2), (1, 3)]: ")
inversion_set = ast.literal_eval(inversion_set_str)

# Convert inversion set from 1-based to 0-based indexing
inversion_set_0_based = [(i - 1, j - 1) for (i, j) in inversion_set]

# Getting permutations and the count of valid permutations
result = count_permutations_with_inversion_set(n, inversion_set_0_based)
poly_result = polynomial(n, inversion_set_0_based)

# Print
for perm in result:
    print(perm)
print(f"Number of permutations with the given inversion set: {len(result)}")
print(f"With Polynomial: {poly_result}")