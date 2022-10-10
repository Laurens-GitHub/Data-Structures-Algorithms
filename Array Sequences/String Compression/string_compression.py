"""Function for condensing a string into character-number format"""

# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'.
# For this problem, you can falsely "compress" strings of single or double letters.
# For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.
# The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

from collections import defaultdict


def compress(our_str):
    """Compresses a given string into character-number format

    :param our_str: - a string
    """

    letter_dic = {}
    compressed = ""

    for char in our_str.strip():
        if char in letter_dic:
            letter_dic[char] += 1
        else:
            letter_dic[char] = 1


    for item in letter_dic:
        compressed += f'{item}{letter_dic[item]}'

    return compressed

# print(compress('AAAAABBBBCCCCaaaabc'))

def test_compress():
    assert compress(' ') == ''
    assert compress('AABBCC') == 'A2B2C2'
    assert compress('AAABCCDDDDD') == 'A3B1C2D5'
    return('ALL TEST CASES PASSED')

print(test_compress())