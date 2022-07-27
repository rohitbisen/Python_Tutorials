a = []

def push_stack(element):
    a.append(element)

def pop_stack():
    if len(a) <= 0:
        print("List is empty")
    else:
        return a.pop()

def display_stack():
    for i in range(len(a)-1, -1, -1):
        print(a[i], end=" ")
    print()

push_stack(25)
display_stack()
push_stack(2)
display_stack()
pop_stack()
display_stack()
push_stack(45)
display_stack()
push_stack(1)
display_stack()
pop_stack()
display_stack()
