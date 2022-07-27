# Python namespace & LEGB Rule --->

'''
varible lookup
L = Local 
E = Enclosed
G = Global 
B = Built in 
'''

# Local variable
# Here pi is acting as a local variabe
'''
def myfun():
    pi = "hii"
    print(pi)
myfun()
'''

# Global variable --->

'''
pi = "hello"

def myfun():
    pi = "hii"
    print(pi)

print(pi)
myfun()
'''

# Enclosed and built in variable

from math import pi

#pi = "hello"

def my_outer_fun():
    #pi = "outer"
    def myfun():
        #pi = "hii"
        print(pi)
    myfun()

#print(pi)
my_outer_fun()