class Queue:
    def __init__(self):
        self.items = []

    def printQueue(self):
        print(self.items)

    def add(self, item):
        self.items.append(item)

    def remove(self):
        self.items.remove(self.items[0])

    def peek(self):
        return self.items[0]

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    q = Queue()
    print(q.isEmpty())
    q.add(1)
    q.add(2)
    q.add(3)
    q.add(1)
    q.printQueue()

    print(q.peek())
    q.remove()
    q.printQueue()
