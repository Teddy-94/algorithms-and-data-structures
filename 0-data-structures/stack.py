class Stack:
    def __init__(self, length):
        self.data = [None] * length
        self.top = -1

    def push(self, element):
        self.top += 1
        self.data[self.top] = element

    def pop(self):
        if self.top == -1:
            return "underflow"
        else:
            returnData = self.data[self.top]
            self.data[self.top] = None
            self.top -= 1
            return returnData


def main():
    q = Stack(3)
    print(q.data, q.top)
    q.push(1)
    print(q.data, q.top)
    q.push(2)
    print(q.data, q.top)
    q.push(3)
    print(q.data, q.top)
    q.pop()
    print(q.data, q.top)
    q.pop()
    print(q.data, q.top)
    q.pop()
    print(q.data, q.top)

    print(q.data, q.top)
    q.push(3)
    print(q.data, q.top)
    q.pop()

    print(q.data, q.top)
    q.push(3)
    print(q.data, q.top)
    q.pop()


main()
