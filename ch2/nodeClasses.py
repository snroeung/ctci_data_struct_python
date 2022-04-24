class SinglyNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return str(self.value)


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        values = []
        current = self.head
        while current != None:
            values.append(str(current.value))
            current = current.next
        return '->'.join(values)

    def addToEnd(self, value):
        current = self.head
        while current != None:
            if current.next == None:
                current.next = SinglyNode(value)
                break
            else:
                current = current.next

    def addToFront(self, value):
        oldHead = self.head
        self.head = SinglyNode(value)
        self.head.next = oldHead

    def delete(self, value):
        current = self.head
        while current != None:
            if current.next.value == value:
                nextNode = current.next
                current.next = nextNode.next
                break
            else:
                current = current.next


if __name__ == "__main__":
    singlyLinkedList = SinglyLinkedList()
    n1 = SinglyNode(1)
    n2 = SinglyNode(2)
    n3 = SinglyNode(3)

    singlyLinkedList.head = n1
    n1.next = n2
    n2.next = n3

    # singlyLinkedList.addToEnd(4)
    # singlyLinkedList.addToFront(0)
    # singlyLinkedList.delete(2)
    # print(singlyLinkedList)
