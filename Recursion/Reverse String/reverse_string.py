# Reverse a String
# This interview question requires you to reverse a string using recursion.
# Make sure to think of the base case here.


def reverse(our_string):
    #edge cases
    if isinstance(our_string, str) is False:
        return TypeError("you must enter a string")

    #define the base case
    if len(our_string) <= 1:
        return our_string

    # recursive call
    else:
        return reverse(our_string[1:]) + our_string[0]

print(reverse("hello world"))
