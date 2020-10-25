#Name: Aarya Vira
#Roll No: 374

class Stack():
    def __init__(self):
        self.items = [1,2,3,4,5]

    
    
    def enque(self,item):
        self.items.append(item)
        print(item)

        
    def deque(self):
        b= self.items
        b.pop()
        print(b)

    def traverse(self):
        a = []
        l = self.items
        for i in l:
            a.append(i)
        print(a)

s=Stack()

print("Adding the element in the queue : ")
s.enque(6)
print("initial queue : ")
s.traverse()

print("After removing an element from the queue : ")
s.deque()
