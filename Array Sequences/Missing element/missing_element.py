"""Function for determining the missing integer between two arrays"""

# Consider an array of non-negative integers. A second array is formed
# by shuffling the elements of the first array and deleting a random element.
# Given these two arrays, find which element is missing in the second array.

# Here is an example input, the first array is shuffled and the number 5
# is removed to construct the second array.

# Input:

# finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

# Output:

# 5 is the missing number

#clarifying question: do we need to account for repeating values?

#This solution works if there are no repeating values
def find_missing_int(arr1, arr2):
    """Given a first array, finds the number that has been removed from the second

    :param arr1: list - a list of positive integers
    :param arr2: list - a list made by shuffling and removing 1 element from arr1
    """

    if sorted(arr1) == sorted(arr2):
        return IndexError("arrays must be of different lengths")

    for i in arr1:
        if i not in arr2:
            return i


# print(find_missing_int([1,2,3,4,5,6,7],[3,7,2,1,4,6]))

#runtime beakdown

#if sorted(arr1) == sorted(arr2): <~ sorting twice O(2nlogn)
#nlog(n) is Log linear. worse than Linear, but better than quadratic

#for i in arr1: <~ iteration O(n)
    #if i not in arr2 <~ contains/in O(n)

#runtime is O(n^2), I think.

#Alternatively, this solution works if there are repeating values:

def find_missing_int2(arr1, arr2):
    """Given a first array, finds the number that has been removed from the second"""

    list1 = sorted(arr1)
    list2 = sorted(arr2)

    if list1 == list2:
        return IndexError("arrays must be of different lengths")

    for idx, num in enumerate(list1):
        for idx2, num2 in enumerate(list2):
            if idx == idx2 and not num == num2:
                return num

print(find_missing_int2([5,5,7,7],[5,7,7]))

#runtime beakdown

# for idx, num in enumerate(list1): <~ enumerate is O(1) + loop O(n) = O(n) x2 = O(n^2)

