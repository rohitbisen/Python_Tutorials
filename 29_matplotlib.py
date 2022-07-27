'''
from math import radians
import numpy as np     # installed with matplotlib
import matplotlib.pyplot as plt

def main():
    x = np.arange(0, radians(1800), radians(12))
    plt.plot(x, np.cos(x), 'b')
    plt.show()

main()
'''

# Matplotlib pyplot functions
'''
plt.plot(x, y, color, ohers)
plt.xlable("")
plt.ylable("")
plt.set_title("title")
plt.show()
'''
# Basic code 
'''
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
''''''
plt.plot(x, y)
plt.show()
'''
'''
plt.plot(x, y)
plt.xlable("time")
plt.ylable("date")
plt.title("time and date graph")
plt.show()
'''

# Mathematical equation graph---->>>>
'''
x = np.arange(-2, 2, 0.01)
y = np.sin(x)
y = x*x + 5*x + 2

plt.plot(x, y)
'''

# Multipe view---->>>

## plt.subplot(numrows, numcols, fignum)

import matplotlib.pyplot as plt

x = [i for i in range(10)]
y = [i*i*i for i in range(10, 20)]
z = [i*2 for i in range(10, 20)]

plt.subplot(2, 1, 2)
plt.plot(x, y)

plt.subplot(2, 1, 2)
plt.plot(x, z)

plt.show()