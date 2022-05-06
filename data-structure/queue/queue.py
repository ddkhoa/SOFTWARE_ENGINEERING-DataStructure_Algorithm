"""
Queue: FIFO

Methods:
__init__: create an empty queue
enqueue(item): add a new item at the rear of the queue
dequeue(): remove the front item from the queue
peek(): return the front item of the queue
is_empty(): check if the queue is empty
size(): return the number of items in the queue
"""

from abc import ABCMeta, abstractmethod


class StackOverflowError(BaseException):
    pass


class StackUnderflowError(BaseException):
    pass


class AbstractQueue(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def enqueue(self, item):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class ArrayQueue(AbstractQueue):

    def __init__(self, limit=10):
        super().__init__()
        self._queue = []
        self._rear = 0
        self._limit = limit

    def size(self):
        return self._rear

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, item):
        if self.size() >= self._limit:
            raise StackOverflowError

        self._queue.append(item)
        self._rear += 1

    def dequeue(self):
        if self.is_empty():
            raise StackUnderflowError

        front_item = self._queue[0]
        self._queue = self._queue[1:]
        self._rear -= 1

        return front_item

    def peek(self):
        if self.is_empty():
            raise StackUnderflowError
        return self._queue[0]

    def __str__(self):
        return " > ".join(map(str,self._queue))


def test_queue():

    queue = ArrayQueue(limit=10)

    assert queue.is_empty() is True

    try:
        _ = queue.dequeue()
        assert False  # should not happen
    except StackUnderflowError:
        assert True  # should happen

    try:
        _ = queue.peek()
        assert False  # should not happen
    except StackUnderflowError:
        assert True  # should happen

    for i in range(10):
        assert queue.size() == i
        queue.enqueue(i)

    # 0 1 2 3 4 5 6 7 8 9

    assert not queue.is_empty()
    assert queue.dequeue() == 0     # 1 2 3 4 5 6 7 8 9
    assert queue.peek() == 1        # 1 2 3 4 5 6 7 8 9
    assert queue.dequeue() == 1     # 2 3 4 5 6 7 8 9

    queue.enqueue(0)  # 2 3 4 5 6 7 8 9 0
    queue.enqueue(1)  # 2 3 4 5 6 7 8 9 0 1

    try:
        queue.enqueue(10)
        assert False  # should not happen becase we exceeded stack limit
    except StackOverflowError:
        assert True

    assert queue.size() == 10

    print("Test queue OK")
    print(queue)


if __name__ == "__main__":
    test_queue()
