def is_palindrome(s):
    s = s.lower().replace(" ","")
    return s == s[::-1]
print(is_palindrome("radar"))
print(is_palindrome("apple"))