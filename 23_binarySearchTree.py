a = [1, 2, 3, 4, 5, 6, 7, 8]

def binary_search(a, key, start, end):
    if start <= end:
        mid = int((start + end) / 2)
        if a[mid] > key:
            return binary_search(a, key, start, mid-1)
        elif a[mid] < key:
            return binary_search(a, key, mid+1, end)
        else:
            return mid
    
    print(key, "beta ijjat se search kro")
    return -1

print(binary_search(a, 8, 0, len(a)-1))