# obj = open("readhere.txt", 'w')

# obj.write("Hey bro...")

# adding list items into file

'''
fruits = ["mango\n", "banana\n", "apple\n"]
obj.writelines(fruits)

obj.close()
'''

# by using with function we don't need both open and close function

with open("readhere.txt", 'w') as obj:
    fruits = ["mango\n", "banana\n", "apple\n"]
    obj.writelines(fruits)

