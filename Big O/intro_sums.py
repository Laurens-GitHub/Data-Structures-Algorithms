# Import time module
import time

# record start time
start = time.time()

def sum1(n):
    """
    Take an input of n and return the sum of the numbers from 0 to n
    """
    final_sum = 0
    for i in range(n+1):
        final_sum += i

    return final_sum

sum1(10)
# record end time
end = time.time()
print("The time of execution of sum1 program is :",
      (end-start) * 10**3, "ms")

start = time.time()
def sum2(n):
    """
    Take an input of n and return the sum of the numbers from 0 to n
    """
    return (n*(n+1))/2

sum2(10)
end = time.time()
print("The time of execution of sum2 program is :",
      (end-start) * 10**3, "ms")
