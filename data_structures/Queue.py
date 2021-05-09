class Queue:

    DEFAULT_SIZE = 10
    def __init__(self, n=DEFAULT_SIZE):
        self.__head__ = -1 # Index of the first element; initially no elements
        self.__tail__ = 0 # Index of the element on enqueue
        self.__arr__ = [-1 for _ in range(n)]

    def is_empty(self):
        return self.__head__ == -1

    def is_full(self):
        return self.__head__ == self.__tail__
    
    def enqueue(self, val):
        if(self.is_full()):
            return Exception('Overflow!')
        if(self.is_empty()):
            self.__head__ = (self.__head__ + 1)%len(self.__arr__)
        self.__arr__[self.__tail__] = val
        self.__tail__ = (self.__tail__ + 1)%len(self.__arr__)

    def dequeue(self):
        self.__head__ = (self.__head__ + 1)%len(self.__arr__)
        return self.__arr__[self.__head__ - 1]


q = Queue(5)

print(q.is_empty())

q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
q.enqueue(5)

q.enqueue(1)
q.enqueue(2)

print(q.is_full())