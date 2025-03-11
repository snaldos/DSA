def get_all_subsets(s):
    if len(s) == 0:
        return [[]]
    subsets = get_all_subsets(s[1:])
    return subsets + [[s[0]] + subset for subset in subsets]


def get_all_subsets_bitwise(s):
    n = len(s)
    subsets = []
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(s[j])
        subsets.append(subset)
    return subsets


"""
    Code Testing
"""

#get_all_subsets
print("Test get all subsets")

# Expected Output: [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]

print(get_all_subsets([1, 2, 3]))



#get_all_subsets_bitwise
print("Test get all subsets bitwise")

# Expected Output: [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]

print(get_all_subsets_bitwise([1, 2, 3]))
