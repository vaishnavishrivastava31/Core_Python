# a = 4
# b = 0
# try:
#     c = a / b
#     print(c)
# except ZeroDivisionError:
#     print("Division by zero")
# finally:
#     print("Always executed")
# # else:
# #     print("Division was greater than zero")
#
# print("hello world")

# list = [1,2,3]
# i = 5
# if i > len(list):
#     raise IndexError
# else:
#     print(list[i])

# while True:
#     try:
#         x = int(input("Enter a number: "))
#         break
#     except ValueError:
#         print("Please enter a number")

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    num3 = num1/num2
    print(num3)
except ZeroDivisionError:
    print("Division by zero")
else:
    print("I am else block")