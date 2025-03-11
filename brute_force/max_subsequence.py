from typing import List


def max_subsequence_bf(number_list: List[int], index_list: List[int]) -> int:
    max_sum = float("-inf")
    cur_sum = 0
    index_list[0] = 0
    index_list[1] = 0
    for i in range(len(number_list)):
        for j in range(i + 1):
            cur_sum = 0
            for k in range(j, i + 1):
                cur_sum += number_list[k]
            if cur_sum > max_sum:
                max_sum = cur_sum
                index_list[0] = j
                index_list[1] = i

        for k in range(i, len(number_list)):
            cur_sum = 0
            for l in range(i, k + 1):
                cur_sum += number_list[l]
            if cur_sum > max_sum:
                max_sum = cur_sum
                index_list[0] = i
                index_list[1] = k

    return max_sum


def max_subsequence(number_list: List[int], index_list: List[int]) -> int:
    max_sum = float("-inf")
    cur_sum = 0
    start_index = 0
    index_list[0] = 0
    index_list[1] = 0

    for i in range(len(number_list)):
        cur_sum += number_list[i]

        if cur_sum > max_sum:
            max_sum = cur_sum
            index_list[0] = start_index
            index_list[1] = i

        elif cur_sum < 0:
            cur_sum = 0
            start_index = i + 1

    return max_sum


# Code Testing
if __name__ == "__main__":
    # BF
    print("Brute Force Algorithm")

    # Expected Maximum Subsequence Sum: 99
    index_list = [0, 0]
    number_list = [53, -72, -90, -55, -37, 99, -78, 24, 7, 5]
    print(max_subsequence_bf(number_list, index_list))
    print(index_list)

    # Expected Maximum Subsequence Sum: 134
    index_list = [0, 0]
    number_list = [-48, -20, -40, -60, -82, 97, 37, 0, -99, -1]
    print(max_subsequence_bf(number_list, index_list))
    print(index_list)

    # Expected Maximum Subsequence Sum: 210
    index_list = [0, 0]
    number_list = [53, -69, 3, 51, 62, 13, 81, -74, 33, -93]
    print(max_subsequence_bf(number_list, index_list))
    print(index_list)

    # Clever Algorithm
    print("Clever Algorithm")

    # Expected Maximum Subsequence Sum: 99
    index_list = [0, 0]
    number_list = [53, -72, -90, -55, -37, 99, -78, 24, 7, 5]
    print(max_subsequence(number_list, index_list))
    print(index_list)

    # Expected Maximum Subsequence Sum: 134
    index_list = [0, 0]
    number_list = [-48, -20, -40, -60, -82, 97, 37, 0, -99, -1]
    print(max_subsequence(number_list, index_list))
    print(index_list)

    # Expected Maximum Subsequence Sum: 210
    index_list = [0, 0]
    number_list = [53, -69, 3, 51, 62, 13, 81, -74, 33, -93]
    print(max_subsequence(number_list, index_list))
    print(index_list)
