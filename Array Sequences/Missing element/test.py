"""Test for missing_element.py"""


from missing_element import find_missing_int, find_missing_int2

def find_missing_int_test():

    # assert find_missing_int([5,5,7,7],[5,7,7]) == 5
    assert find_missing_int([1,2,3,4,5,6,7],[3,7,2,1,4,6]) == 5
    assert find_missing_int([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]) == 6

    return "ALL TESTS PASSED"

test1 = find_missing_int_test()
print(test1)

def find_missing_int_test2():

    assert find_missing_int2([5,5,7,7],[5,7,7]) == 5
    assert find_missing_int2([1,2,3,4,5,6,7],[3,7,2,1,4,6]) == 5
    assert find_missing_int2([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]) == 6

    return "ALL TESTS PASSED FUNCTION 2"

test2 = find_missing_int_test2()
print(test2)
