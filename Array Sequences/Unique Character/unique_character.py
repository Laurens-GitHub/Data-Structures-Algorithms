"""Function for determining if all characters within a string are unique"""

# Given a string, determine if it is compreised of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return false.

def unique_char(our_string):
    """Determines if all characters in a string are unique

    :param our_string: - a string
    """

    if len(our_string) == 0:
        return True

    if len(our_string) == 1:
        return True

    dic = {}

    for char in our_string:
        if char in dic:
            return False
        else:
            dic[char] = 1

    return True

# print(unique_char('aabcde')) #False

def test_unique_char():
    assert unique_char('') == True
    assert unique_char('AABBCC') == False
    assert unique_char('abcdefg') == True
    return('ALL TEST CASES PASSED')

print(test_unique_char())
