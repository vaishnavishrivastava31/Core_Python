


# file = open("C:/Users/SHRIVASTAVA/Desktop/Newfolder/file.txt",'w')
# file.write("Hello World")
# print("Done")
# file.close()
#
# fo = open("C:/Users/SHRIVASTAVA/Desktop/Newfolder/file.txt",'r')
# text = fo.read()
# print(text)
# fo.close()

# fo = open("C:/Users/SHRIVASTAVA/Desktop/Newfolder/file.txt",'r')
# for line in fo:
#     print(line)
# fo.close()

# fo = open("C:/Users/SHRIVASTAVA/Desktop/Newfolder/file.txt",'r')
# print("File Name: ", fo.name)
# print("Mode of Opening: ", fo.mode)
# print("Is Closed: ", fo.closed)
# fo.close()

# file = open("C:/Users/SHRIVASTAVA/Desktop/Newfolder/Newfile.txt",'w')
# file.write("Hello World \n")
# file.write("This is a Python file")
# file.close()

# with open("C:/Users/SHRIVASTAVA/Desktop/Newfolder/Newfile.txt",'w') as file:
#     file.write("Hi\n")
#     file.write("How are you\n")

import pickle

class Employee:
    def __init__(self, fname, lname, id):
        self.fname = fname
        self.lname = lname
        self.id = id
e = Employee('John', 'Smith', 123)
f = open("C:/Users/SHRIVASTAVA/Desktop/Newfolder/Serialization.txt",'wb')
pickle.dump(e, f)
print("Done")
f.close()
print(e.fname)
print(e.lname)

f = open("C:/Users/SHRIVASTAVA/Desktop/Newfolder/Serialization.txt",'rb')
e = pickle.load(f)
f.close()
print(e.fname)
print(e.lname)
