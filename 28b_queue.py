a = []

def push_queue(element):
    a.append(element)

def pop_queue():
    if len(a) <= 0:
        print("List is empty")
    else:
        return a.pop(0)

def display_queue():
    for i in range(len(a)-1, -1, -1):
        print(a[i], end=" ")
    print()

push_queue(21)
display_queue()
push_queue(22)
display_queue()
pop_queue()
display_queue()
push_queue(45)
display_queue()
push_queue(32)
display_queue()
pop_queue()
display_queue()