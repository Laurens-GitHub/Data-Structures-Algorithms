"""Function for reversing the order of words in a sentence"""
# Given a string of words, reverse all the words. For example:

# Given:

# 'This is the best'

# Return:

# 'best the is This'

# As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:

# '  space here'  and 'space here      '

# both become:

# 'here space'

def reverser(words):
    """Reverses the order of words in a sentence

    :param words: str - a string of characters
    """

    split_words = words.split()
    new_sentence = ""

    while len(split_words) > 0:
        new_sentence += (f'{split_words[-1]} ')
        split_words.pop()

    return new_sentence.strip()

# print(reverser('best the is This'))