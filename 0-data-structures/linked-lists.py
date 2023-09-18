class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    # Inserting before an element is all about taking the pointer
    # element.prev and pointing it to the newElement.
    # And pointing newElement.next to element.
    # (element is the element in the list that we
    # want to insert our newElement before)
    def insertBeforeElement(self, element, newElement):
        if element == self.head:
            newElement.next = self.head
            self.head = newElement
        else:
            newElement.prev = element.prev
            element.prev.next = newElement
            newElement.next = element

    # Deleting an element requires removing the element from the list, and then
    # connecting the element to the left and right of the element removed.
    # This is done by pointing element.prev.next at element.next
    # and pointing element.next.prev to elemement.prev
    def deleteElement(self, element):
        if element.prev is None:
            self.head = element.next
        else:
            element.prev.next = element.next
        if element.next is not None:
            element.next.prev = element.prev

    def findElement(self, key):
        x = self.head
        while x is not None and x.data is not key:
            x = x.next
        return x

    def print(self):
        x = self.head
        while x is not None:
            print(x)
            x = x.next


class LinkedListElement:
    def __init__(self, key) -> None:
        self.data = key
        self.prev = None
        self.next = None

    def __str__(self) -> str:
        return f"{self.data}"


# this has some bug
# TODO fix the bug
print("hiya")
ll = LinkedList()
a = LinkedListElement(1)
b = LinkedListElement(2)
c = LinkedListElement(3)
d = LinkedListElement(4)

ll.insertBeforeElement(ll.head, a)
ll.insertBeforeElement(a, b)
ll.insertBeforeElement(b, c)
ll.insertBeforeElement(c, d)
ll.print()
print()
ll.deleteElement(c)
ll.print()
