from Array_pair_sum import pair_sum

def test_pair_sum():
    assert pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10) == 6
    assert pair_sum([1,2,3,1],3) == 1
    assert pair_sum([1,3,2,2],4) == 2
    return('ALL TEST CASES PASSED')

#Run tests
test = test_pair_sum()
print(test)