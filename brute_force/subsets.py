from typing import List


def get_all_subsets(s: List[int]) -> List[List[int]]:
    if len(s) == 0:
        return [[]]
    subsets = get_all_subsets(s[1:])
    return subsets + [[s[0]] + subset for subset in subsets]


def get_all_subsets_bitwise(s: List[int]) -> List[List[int]]:
    n = len(s)
    subsets = []
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(s[j])
        subsets.append(subset)
    return subsets
