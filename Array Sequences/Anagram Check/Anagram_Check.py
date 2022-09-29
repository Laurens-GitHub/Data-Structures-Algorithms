# Anagram Check

# Given two strings, check to see if they are anagrams. An anagram is when the two strings
# can be written using the exact same letters (so you can just rearrange the letters to
# get a different phrase or word).

# For example:

# "public relations" is an anagram of "crap built on lies."

# "clint eastwood" is an anagram of "old west action"

# Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".

"""Function for determining whether two strings are anagrams"""

def anagram(s1,s2):
    """Verify whether two strings are anagrams of each other

    :param s1: str - the first string
    :param s2: str - the second string
    """

    dic1 = {}
    dic2 = {}

    for char in s1.replace(" ", ""):
        if char not in dic1.keys():
            dic1[char] = 0
        dic1[char] += 1
    # print(dic1)

    for char in s2.replace(" ", ""):
        if char not in dic2.keys():
            dic2[char] = 0
        dic2[char] += 1
    # print(dic2)

    if dic1 == dic2:
        return True

    return False
