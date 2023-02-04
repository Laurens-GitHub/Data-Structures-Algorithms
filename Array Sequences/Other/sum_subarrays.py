# def sum_subsets(arr,n):
#     result = []
#     subset = []
#     add_subset(arr,n,result,subset)
#     return print(result)

# def add_subset(arr, count, result, new_set):
#     result.append(new_set)
#     for i in range(count):
#         add_subset(arr[i+1], count, result, new_set.append(arr[i]))
#         # new_set.pop(len(new_set)-1)

def sum_subsets(arr,n):
    result = [[]]
    sums = []
    for num in arr:
        result += [i+[num] for i in result]

    for i in result:
        sums.append(sum(i))
    return sum(sums)

# print(sum_subsets([5,4,3],3))
assert sum_subsets([5,4,3],3) == 48
assert sum_subsets([0],1) == 0
assert sum_subsets([1,2],2) == 6
assert sum_subsets([1,2,3],3) == 24


