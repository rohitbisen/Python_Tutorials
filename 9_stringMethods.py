# Python string methods --->
'''
All of this is used with .   ex. = variable.isalpha()

isalpha
isdigit
islower
lower
upper
isupper
lstrip
rstrip
ord() ----> This is used for finding ascii value of an alphabate
char
'''

x = "abcd"
print(x.isalpha())

x = "abcd1"
print(x.isalpha())

x = "123"
print(x.isdigit())

x = "abc123"
print(x.isdigit())

y = "abc$"
print(y.islower())

y = "abc"
print(y.upper())

z = y.upper()
print(z)

y = "ABC"
print(y.lower())

y = "    abc"
print(y.lstrip())

y = "abc   "
print(y.rstrip())

y = "abc"
print(ord('a'))
print(ord('h'))