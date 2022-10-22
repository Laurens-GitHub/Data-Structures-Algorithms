"""Function for finding the sequential array with the largest sum"""
# Given an array of integers (positive and negative) find the largest continuous sum.

def largest_sum(arr):
    """Finds the largest sum of sequential numbers within a given array

    :param arr: list - a list of integers"""

    sums = []

    for i in range (0,len(arr)):
        for j in range(len(arr),i,-1):
            sums.append(sum(arr[i:j]))

    return max(sums)


# print(largest_sum([1,2,-1,3,4,10,10,-10,-1]))

# def largest_sum2(arr):
#     """Finds the largest sum and index

#     :param arr: list - a list of integers"""

#     current_sum = max_sum = arr[0]
#     start_idx = 0
#     end_idx = -1

#     for idx, num in enumerate(arr[1:]):
#         current_sum=max(current_sum + num, num)
#         if max_sum < current_sum:
#             max_sum = current_sum
#             end_idx = idx

#     return max_sum, start_idx, end_idx

# print(largest_sum2([-1,1]))

# def test_largest_sum2():

#     assert largest_sum2([1,2,-1,3,4,-1]) == (9, 0, 4)
#     # assert largest_sum2([1,2,-1,3,4,10,10,-10,-1]) == (29, 0, 6)
#     assert largest_sum2([-1,1]) == (1, 1, -1)

#     return "ALL TEST CASES PASSED"

# # print(test_largest_sum2())