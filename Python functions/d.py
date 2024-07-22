n = 5
def factorial(n):
    if n == 0 and n == 1:
        return 1
    elif n <= 0:
        print("take positive integer")
    else:
        return n * factorial(n-1)
# number = 5
factorial = factorial(n)
print(factorial)