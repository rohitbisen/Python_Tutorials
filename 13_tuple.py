# In list we use [] & In tuple we use ()
# In list we can change the value of an eliment but In tuple we can not.
# e(1) is not tuple, e(1, ) is tuple

'''
b = (1, 3, 4)
print(b)
print(b[1])

a = (1, )
print(a)
print(type(a))
a[0] = 1
print(a)
'''
a = (1, 2, 3, 4, 5, 6)
for i in range(len(a)):
    print(a[i]**2)

print(a[3:5])
