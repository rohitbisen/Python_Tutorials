a = [4, 6, 3, 1]

count = 0

for i in range(len(a)):
    for j in range(1, len(a)):
        if a[j-1] > a[j]:
            count +=1
            a[j-1], a[j] = a[j], a[j-1]

print(a, count)