dict = {"name":"vaishanvi", "age":21, "city":"agra"}
key = (input("Enter a key: "))
try:
    value = dict[key]
    print(value)
except KeyError:
    print("Key not found")
