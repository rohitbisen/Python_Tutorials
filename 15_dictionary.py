'''
marks = {'rohit': 99, 'rishabh': 98, 'yuvan': 97}
print(marks)

# Changing the value of key inside the dictionary

marks['rohit'] = 100
print(marks['rohit'])

# Deleting the value of key

del marks['rohit']
print(marks)
'''

'''
x = {1: "hii", "rb": 45, 9: 89}
for key in x:
    print(x[key])
x.clear()
print(x)

x = {1: "hii", "rb": 45, 9: 89}
y = x.copy()
print(y)

items = y.items()
print(items)

keys = y.keys()
print(keys)

values = y.values()
print(values)
'''
a = {1 : 2, 3 : 4}
b = {3 : 5, 4 : 7}
c = a.update(b)
print(a)