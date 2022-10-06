# If we don’t want to deal with the special case of duplicate numbers,
# we can sort both arrays and iterate over them simultaneously.
# Once two iterators have different values we can stop.
# The value of the first iterator is the missing element.
# This solution is also O(NlogN).
# Here is the solution for this approach:

from collections import defaultdict


def finder(arr1,arr2):

    # Sort the arrays
    arr1.sort()
    arr2.sort()

    # Compare elements in the sorted arrays
    for num1, num2 in zip(arr1,arr2): #zip will create an array of tuples until the elements are exhausted  zip([1,2,3],[4,5,6]) => [(1,4), (2,5) ,(3,6)]
        if num1!= num2:
            return num1

    # Otherwise return last element
    return arr1[-1]


# In most interviews, you would be expected to come up with a linear time solution.
# We can use a hashtable and store the number of times each element appears in the second array.
# Then for each element in the first array we decrement its counter.
# Once we hit an element with zero count that’s the missing element. Here is this solution:

# import collections

# def finder2(arr1, arr2):

#     # Using default dict to avoid key errors
#     dic=collections.defaultdict(int) # this is very useful because it automatically adds the key to the dictionary for us

#     # Add a count for every instance in Array 1
#     for num in arr2:
#         dic[num]+=1

#     # Check if num not in dictionary
#     for num in arr1:
#         if d[num]==0:
#             return num

#         # Otherwise, subtract a count
#         else: d[num]-=1


#refactored to tidier code, autoimport the collections module:

def finder2(arr1, arr2):
    our_dic = defaultdict(int)

    for num in arr2:
        our_dic[num]+=1

    for num in arr1:
        if our_dic[num]==0:
            return num
        our_dic[num]-=1

print(finder2([5,5,7,7],[5,7,7]))


# One possible solution is computing the sum of all the numbers in arr1 and arr2, and subtracting arr2’s sum from array1’s sum.
# The difference is the missing number in arr2.
# However, this approach could be problematic if the arrays are too long, or the numbers are very large.
# Then overflow will occur while summing up the numbers.
# You can mention a solution like this in the interview, but also talk about its shortcomings


# initialize a variable to 0, then use "Elxclusive or" (XOR) on every element in the first and
# second arrays with that variable. In the end, the value of the variable
# is the result, missing element in array2.
# By performing a very clever trick, we can achieve linear time and constant space complexity
# without any problems. Here it is:

def finder3(arr1, arr2):
    result=0

    for num in arr1+arr2: #concatenate the arrays and loop through them
        result^=num # Perform an exlusive or between the numbers in the arrays

        print(result)

    return result

# Here is a good explanation of how XOR works: https://youtu.be/8ng3R8eeGCA?t=485