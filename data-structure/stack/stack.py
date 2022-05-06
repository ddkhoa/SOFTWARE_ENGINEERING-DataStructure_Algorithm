"""
Methods:
 __init__: init an empty stack
 push(item): add new item on the top of the stack
 pop(item): get the item on the top of the stack and remove it from the stack
 peek(item): get the item on the top of the stack, but does not remove it from the stack
 is_empty: check if stack is empty or not

 Stack can be implemented using array or linked list
"""

from abc import ABCMeta, abstractmethod

class StackOverflowError(BaseException):
    pass

class StackUnderflowError(BaseException):
    pass

class AbstractStack(metaclass=ABCMeta):
    """Abstract Class for Stacks"""

    def __init__(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def push(self, value):
       pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass

class ArrayStack(AbstractStack):
    def __init__(self, limit=10):

        super().__init__()
        self._stack = []
        self._limit = limit

    def is_empty(self):
        return len(self._stack) == 0

    def size(self):
        return len(self._stack)

    def push(self, value):

        # check if we exceeed the stack limit
        if self.size() >= self._limit:
            raise StackOverflowError

        # happy case, add element on the top of stack -> at the end of the array
        self._stack.append(value)

    def pop(self):

        # we cannot get element from stack if it is empty
        if self.is_empty():
            raise StackUnderflowError

        # happy case, we get and remove the element on the top of stack -> at the end of the array
        return self._stack.pop()

    def peek(self):
        
        if self.is_empty():
            raise StackUnderflowError

        return self._stack[-1]

def test_stack():

    stack = ArrayStack(limit=10)

    assert stack.is_empty() is True
    
    try:
        _ = stack.pop()
        assert False # should not happen
    except StackUnderflowError:
        assert True # should happen
      
    try:
        _ = stack.peek()
        assert False # should not happen
    except StackUnderflowError:
        assert True # should happen

    for i in range(10):
        assert stack.size() == i
        stack.push(i)

    assert not stack.is_empty()
    assert stack.pop() == 9
    assert stack.peek() == 8
    assert stack.pop() == 8
    
    stack.push(8)
    stack.push(9)

    try : 
        stack.push(10)
        assert False # should not happen becase we exceeded stack limit
    except StackOverflowError:
        assert True

    assert stack.size() == 10

    print("Test stack OK")

if __name__ == "__main__":
    test_stack()

    