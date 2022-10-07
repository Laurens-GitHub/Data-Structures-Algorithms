from re import L
from largest_sum import largest_sum

def test_largest_sum():

    assert largest_sum([1,2,-1,3,4,-1]) == 9
    assert largest_sum([1,2,-1,3,4,10,10,-10,-1]) == 29
    assert largest_sum([-1,1]) == 1

    return "ALL TEST CASES PASSED"

print(test_largest_sum())