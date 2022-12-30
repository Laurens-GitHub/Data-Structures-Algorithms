# Recursive Binary search
def rec_binary_search(arr, low, high, target):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == target:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > target:
            return rec_binary_search(arr, low, mid - 1, target)

        # Else the element can only be present in right subarray
        else:
            return rec_binary_search(arr, mid + 1, high, target)

    else:
        # Element is not present in the array
        return -1

# list must already be sorted!
arr = [1,2,3,4,5,6,7,8,9,10]
print(rec_binary_search(arr, 0, len(arr)-1, 4)) # => 3

#Iterative Binary Search
def binary_search(list, target):
    """Returns the index of the target element if in the array"""
    start_idx = 0
    end_idx = len(list) - 1

    while start_idx <= end_idx:
        guess = (start_idx + end_idx) // 2

        if list[guess] == target:
            return guess

        else:
            if target < list[guess]:
                end_idx = guess - 1
            else:
                start_idx = guess + 1

    return -1


# print(binary_search(arr,4)) # => 3