# O(1) Constant

def func_constant(values):
    return(values[0])

lst = [1,2,3,4,5,6]

print("constant:")
print(func_constant(lst))
# This function has constant runtime because it prints one value, regardless of the length of the list.

# O(n) Linear

def func_lin(values):
    for value in values:
        return(value)

print("linear:")
print(func_lin(lst))
#This function is linear because for a list of n values, it will print n times

# O(n^2) Quadratic

def func_quad(values):
    for i in values:
        for j in values:
            print(i, j)

items = [1,2,3]
print("quadratic:")
print(func_quad(items))

def comp(lst):
    '''
    This function prints the first item O(1)
    Then is prints the first half of the list O(n/2)
    Then prints a string 10 times O(10)
    '''
    print(lst[0]) # O(1)

    midpoint = len(lst) // 2

    for val in lst[:midpoint]: # O(n/2)
        print(val)

    for i in range(10): # O(10)
        print('number')

# we can combine each operation to get the total Big-O of the function:
# O(1 + n/2 + 10)
# but we only care about the worst case as n approaches infinity
# so this function has an linear runtime O(n)