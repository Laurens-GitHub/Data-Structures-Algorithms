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

array1 = [1,2,3,4,5]
print(array1[1:])
# print(largest_sum([1,2,-1,3,4,10,10,-10,-1]))

# def largest_sum2(arr):

#     result = sum(arr)
#     biggest_arr = [0, -1]

#     for idx, num in enumerate(arr):
