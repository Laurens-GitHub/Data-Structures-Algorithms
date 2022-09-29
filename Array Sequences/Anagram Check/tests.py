"""Tests for Anagram_Check.py"""
from Anagram_Check import anagram

def test_is_anagram():
    assert anagram('go go go','gggooo') is True
    assert anagram('abc','cba') is True
    assert anagram('hi man','hi     man') is True
    assert anagram('aabbcc','aabbc') is False
    assert anagram('123','1 2') is False
    print("ALL TEST CASES PASSED")

test = test_is_anagram()
print(test)