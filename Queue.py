from queue import LifoQueue


class Queue:
    def __init__(self, max_size: int):
        self.max = max_size
        self.queue = [None for i in range(max_size)]
        self.rear = self.front = 0

    @property
    def size(self):
        if self.is_full():
            return self.max
        return (self.max - self.front + self.rear) % self.max

    def is_full(self):
        return self.rear == self.front and self.queue[self.rear] is not None

    def is_null(self):
        return self.rear == self.front and self.queue[self.rear] is None

    def enqueue(self, item):
        if not self.is_full():
            self.queue[self.rear] = item
            self.rear = (self.rear + 1) % self.max
        else:
            print("Queue is FULL!")

    def dequeue(self):
        if not self.is_null():
            value = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.max
            return value
        else:
            print("Queue is NULL!")

    def reverse(self):
        stack = LifoQueue(self.max)
        size = self.size
        for i in range(size):
            stack.put(self.dequeue())
        for i in range(size):
            self.enqueue(stack.get())

    def peek(self):
        return self.queue[self.front]

    def clear(self):
        for i in range(self.size):
            self.dequeue()

    def __str__(self):
        if self.is_null():
            return "Queue is NULL"
        return str([self.queue[(self.front + i) % self.max] for i in range(self.size)])

    def raw_format(self):
        return self.queue


if __name__ == '__main__':
    q = Queue(5)
    for i in range(1,5):
        q.enqueue(i)
        print(q.size)
        print(q)


