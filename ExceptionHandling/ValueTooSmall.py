def Value():
    try:
        number = int(input("Enter a number: "))
        if number < 10:
            raise Exception("ValueTooSmall")
    except Exception as e:
        print(e)
Value()