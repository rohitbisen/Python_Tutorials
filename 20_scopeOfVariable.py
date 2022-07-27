def simple_interest(p, r, t):
    si = (p * r * t)/100
    print("before return")
    return si

'''
def main():
    print(simple_interest(10000, 2.5, 1))

if __name__ == '__main__':
    main()
'''

# recursion --->

def main():
    infinite(10)

def infinite(count):
    if count == 0:
        return
    print("hi", count)
    count -= 1
    infinite(count)

if __name__ == '__main__':
    main()
    