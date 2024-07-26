def string():
    try:
        str = input("Enter a string: ")
        print(int(str))
    except ValueError:
        print("Please enter a number")
string()