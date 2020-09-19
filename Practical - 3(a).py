class Stack:
    def init(self):
        self.stack=[]

    def add(self,data):

        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False

    def top(self):
        return self.stack[-1]

    def remove(self):
        if len(self.stack)<=0:
            return ("No element in Stack")

        else:
            return self.stack.pop()

B=Stack()
B.add('E')
B.add('M')
B.top()
B.add('R')
B.add('A')
print(B.top())
print(B.remove())
print(B.remove())
