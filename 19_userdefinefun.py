'''

def greet(name):
    print("hello", name)

print(greet("rohit"))
'''
'''
# Default function

def greet(name = "rb"):
    print("hello", name, "Good Morning")

greet()
print(greet("rohit"))
'''

'''
def greet(name, salary):
    print("Hello",  name)
    print("Your Salary is: ", salary, "per month")
# greet("Rohit", 100000 )
greet(salary = 100000, name = "Rohit" )
'''

# another way of defining a function
'''
def greet(*name):
    for my_name in name:
        print("Hello", my_name, "Gm")

greet("rb", "rishi", "u1", "soham")
'''

# Calculating interest through function

def simple_interest(p, r, t):
    si = (p * r * t)/100
    return si

print("my simple interest is ", simple_interest(25000, 3, 1))
    