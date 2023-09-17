class Queue:
    def __init__(self, length):
        self.data = [None] * length
        self.head = 0
        self.tail = 0

    def enqueue(self, element):
        self.data[self.tail] = element
        if self.tail == len(self.data)-1:
            self.tail = 1
        else:
            self.tail += 1

    def dequeue(self):
        retElement = self.data[self.head]
        self.data[self.head] = None
        if self.head == len(self.data)-1:
            self.head = 1
        else:
            self.head += 1
        return retElement


def main():
    q = Queue(3)
    print(q.data, q.head, q.tail)
    q.enqueue(1)
    print(q.data, q.head, q.tail)
    q.enqueue(2)
    print(q.data, q.head, q.tail)
    q.enqueue(3)
    print(q.data, q.head, q.tail)
    q.dequeue()
    print(q.data, q.head, q.tail)
    q.dequeue()
    print(q.data, q.head, q.tail)
    q.dequeue()
    print(q.data, q.head, q.tail)

    print(q.data, q.head, q.tail)
    q.enqueue(3)
    print(q.data, q.head, q.tail)
    q.dequeue()

    print(q.data, q.head, q.tail)
    q.enqueue(3)
    print(q.data, q.head, q.tail)
    q.dequeue()


main()
