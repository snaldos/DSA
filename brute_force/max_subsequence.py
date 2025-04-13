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
