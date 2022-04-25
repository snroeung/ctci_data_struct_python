class Stack:
    def __init__(self):
        self.items = []

    def printStack(self):
        print(self.items)

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    stack = Stack()
    print(stack.isEmpty())

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack.isEmpty())
    stack.printStack()
    print(stack.peek())
    print(stack.pop())
