from sentence_reversal import reverser

def test_reverser():

    assert reverser('    space before') == 'before space'
    assert reverser('space after     ') == 'after space'
    assert reverser('   Hello Lauren    how are you   ') == 'you are how Lauren Hello'
    assert reverser('1') == '1'
    return "ALL TEST CASES PASSED"

print(test_reverser())