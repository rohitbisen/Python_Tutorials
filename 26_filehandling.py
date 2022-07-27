obj = open("read.txt", 'r')

'''
lines = obj.read()
print(lines)
'''

# another way of printing lines

'''
for line in obj:
    print(line)
'''

# read.txt will print with new line character

'''
for line in obj:
    print(line, end="")
'''

# line will print one by one

'''
line = obj.readline()
print(line)
line = obj.readline()
print(line)
'''

# printing lines by using while loop

line = obj.readline()
while line != '':
    print(line, end="")
    line = obj.readline()

obj.close()