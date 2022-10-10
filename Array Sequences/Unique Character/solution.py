# We'll show two possible solutions, one using a built-in data structure and a built in function,
# and another using a built-in data structure but using a look-up method to
# check if the characters are unique.

def uni_char(s):
    return len(set(s)) == len(s)


def uni_char2(s):
    chars = set()
    for let in s:
        # Check if in set
        if let in chars:
            return False
        else:
            #Add it to the set
            chars.add(let)
    return True