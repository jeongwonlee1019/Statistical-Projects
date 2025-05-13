from itertools import permutations

def count_permutations_with_inversion_set(n, inversion_set_1_based):
    # Convert inversion set from 1-based to 0-based indexing
    inversion_set = [(i - 1, j - 1) for (i, j) in inversion_set_1_based]

    # Generate all permutations of length n
    all_permutations = permutations(range(1, n + 1))

    def count_inversions(perm):
        # Count (0-based) inversion pairs in a permutation
        inversions = []
        for i in range(len(perm)):
            for j in range(i + 1, len(perm)):
                if perm[i] > perm[j]:
                    inversions.append((i, j))
        return inversions

    # Check how many permutations match the desired inversion set
    valid_perms = [
        perm for perm in all_permutations if sorted(count_inversions(perm)) == sorted(inversion_set)
    ]

    return valid_perms

# Input from user
n = int(input("Enter the value of n (length of permutation): "))
inversion_set_input = input("Enter the inversion set, e.g. [(1, 2), (1, 3)]: ")

# Parse and run
inversion_set_1_based = eval(inversion_set_input)
result = count_permutations_with_inversion_set(n, inversion_set_1_based)
print(result)
print(f"Number of permutations with the given inversion set: {len(result)}")