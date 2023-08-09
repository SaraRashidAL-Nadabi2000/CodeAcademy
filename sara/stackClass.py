#add comments LIFO
#Think how to add/apply is_FULL??
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):#to check if stack has empty
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty, cannot pop an item.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1] #exit last element
        else:
            raise IndexError("Stack is empty, cannot peek an item.")

    def size(self): ##length of the list
        return len(self.items)