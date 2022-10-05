# Array Pair Sum, AKA Two Sum: https://leetcode.com/problems/two-sum/description/
# Given an integer array, output all the number of pairs that sum up to a specific value k.

# So the input:

# pair_sum([1,3,2,2],4)

# would return the output of 2:

#  (1,3)  1
#  (2,2)  2

"""Function for determining how many pairs of numbers in a given array sum to a specific value"""

# clarifying question: are all values positive? If so, we can exclude any values greater than k.
# I will assume that negative values are tested.
# Should all pairs be unique?

def pair_sum(arr,k):
    """Find the number of integer pairs sum to a given value

    :param arr: list - a list of integers
    :param k: int - value that pairs should sum to
    """

    #loop through the array
    # keep track of the "root number"
    # create a second variable that keeps track of the subsequent numbers in the array
    # if at any point the root number and secondary number are equal to the target, return the pair
    # of the root and secondary
    # use enumerate to keep track of both the number (and index to set the range for the second pointer)

    if len(arr) < 2:
        return IndexError("Array must have a minimum of 2 integers")

    answer = set()

    for idx, num in enumerate(arr):
        for i in range(idx+1, len(arr)):
            if num+arr[i] == k:

                # we need to use min, max here because the set will not distinguish
                # pairs like [1,2], [2,1]
                answer.add((min(num, arr[i]), max(num, arr[i])))

    return len(answer)

#bonus: what is the runtime of this solution? O(n^2) due to nested iteration.