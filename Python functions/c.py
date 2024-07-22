def is_prime(n):
    if n < 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False
    else:
        if (n % 2 != 0):
            print("It is prime")
        else:
            print("Not Prime")


is_prime(77)
