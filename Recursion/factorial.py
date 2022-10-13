"""A factorial function"""

def factorial(n):
    if n == 0:
        print(f'BASE CASE HAS BEEN MET! n={n}')
        return 1

    else:
        print(f'Recursive case triggered. n={n}')
        # print(n * factorial(n-1))
        return n * factorial(n-1)

print(factorial(5))

