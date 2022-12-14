# Since Python strings are immutable, we'll need to work off of a list of characters,
# and at the end convert that list back into a string with a join statement.

# The solution below should yield us with a Time and Space complexity of O(n).
# Let's take a look with careful attention to the explanatory comments:

def compress(s):
    """
    This solution compresses without checking. Known as the RunLength Compression algorithm.
    """

    # Begin Run as empty string
    r = ""
    l = len(s)

    # Check for length 0
    if l == 0:
        return ""

    # Check for length 1
    if l == 1:
        return s + "1"

    #Intialize Values
    cnt = 1
    i = 1

    while i < l:

        # Check to see if it is the same letter
        if s[i] == s[i - 1]:
            # Add a count if same as previous
            cnt += 1
        else:
            # Otherwise store the previous data
            r = r + s[i - 1] + str(cnt)
            cnt = 1

        # Add to index count to terminate while loop
        i += 1

    # Put everything back into run
    r = r + s[i - 1] + str(cnt)

    return r

print(compress('AAAAABBBBCCCC'))
