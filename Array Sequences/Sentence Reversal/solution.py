# We could take advantage of Python's abilities and solve the problem
# with the use of split() and some slicing or use of reversed:

def rev_word1(s):
    return " ".join(reversed(s.split()))

#Or

def rev_word2(s):
    return " ".join(s.split()[::-1])


# While these are valid solutions, in an interview setting you'll have to work out the basic algorithm that is used.
# In this case what we want to do is loop over the text and extract words form the string ourselves.
# Then we can push the words to a "stack" and in the end opo them all to reverse.
# Let's see what this actually looks like:

def rev_word3(s):
    """
    Manually doing the splits on the spaces.
    """

    words = []
    length = len(s)
    spaces = [' ']

    # Index Tracker
    i = 0

    # While index is less than length of string
    while i < length:

        # If element isn't a space
        if s[i] not in spaces:

            # The word starts at this index
            word_start = i

            while i < length and s[i] not in spaces:

                # Get index where word ends
                i += 1
            # Append that word to the list
            words.append(s[word_start:i])
        # Add to index
        i += 1

    # Join the reversed words
    return " ".join(reversed(words))