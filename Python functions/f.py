def fibonacci(n):
    a, b = 0, 1
    count = 0
    if n <= 0:
        print("Enter a positve number")
    elif n == 1:
        return 1
    else:
        while count < n:
            print(a)
            c = a+b
            a = b
            b = c
            count += 1
            # return c
fibonacci = fibonacci(5)
print(fibonacci)