class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def is_empty(self):
        return len(self.items)==0
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            return self.items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            return self.items[-1]
    def __len__(self):
        return len(self.items)
p=Stack()
p.push(20)
p.push(67)
print(p.__len__())
print(p.is_empty())
print(p.pop())

        