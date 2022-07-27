import matplotlib.pyplot as plt
import numpy as np
'''
x = np.arange(-10, 10, 0.1)
# print(x)
y = np.sin(x)

plt.plot(x, y)
plt.show()
'''

# Bar Plot/ Chart

# plt.bar(x, y, width, color)

'''
x = np.arange(-10, 10, 0.1)
y = x*x + 2*x +5

plt.plot(x, y)
plt.show()
'''

# For single line graph
'''
x = [i for i in range(10)]
y = [1, 2, 5, 6, 3, 8, 3, 7]
plt.bar(x, y, color = "blue", width = 0.2, lable = "2017")

plt.show()
'''

# For multi line graph
'''
x = [i for i in range(10)]
y = [1, 2, 5, 6, 3, 8, 3, 7]
x2 = [i + 0.2 for i in range(10)]
z = [3, 5, 2, 8, 3, 8, 9, 0]
plt.bar(x, y, color = "blue", width = 0.2, lable = "2017")
plt.bar(x2, z, color = "red", width = 0.2, lable = "2018")
plt.legend()
plt.show()
'''

# Pie Plot / Chart---->>>

# plt.pie(sizes, colors, labels, shadow, explode)


hours = [1, 2, 5, 6, 3]
activities = ["ready", "study", "exercise", "rest", "sleep"]
explodes = [1, 0, 0, 0, 1]
plt.pie(hours, labels = activities, shadow = True, explode = explodes)
plt.show()