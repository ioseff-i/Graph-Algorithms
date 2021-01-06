class Stack:
    def __init__(self):
        self.MAXSIZE = 10000
        self.top = -1
        self.container = []
    def is_empty(self):
        return (self.top < 0)
    def push(self,item):
        if(self.top >= (self.MAXSIZE-1)):
            print('Stack Overflow')
        else:
            self.top+=1
            self.container.append(item)
            print('{} pushed to the Stack '.format(item))
    def pop(self):
        if(self.top < 0):
            print('Stack Underflow')
            return None
        else:
            self.top = self.top - 1
            return self.container[self.top]
    def print_stack(self):
        print(self.container)
        
    def peek(self):
        if(self.top < 0):
            print('Stack Underflow')
            return None
        else:
            return self.container[self.top]

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.print_stack()
print(str(stack.pop())+" popped from the stack")
stack.print_stack()
        
    