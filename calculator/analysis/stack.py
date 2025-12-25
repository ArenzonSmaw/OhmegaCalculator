class StackEmptyException(Exception):
    """
    Exception for when user tries to get a value from an empty stack
    """
    def __init__(self, message):
        super().__init__()
        self._message = message
    def __str__(self):
        return str(self._message)

class Stack:
    """
    Stack data structure
    push(value) -> push a value down the stack
    pop() -> pop the last pushed value
    peek() -> get the last pushed value without popping
    """
    def __init__(self, size = -1):
        self._max_size = size
        self._data = []
        self._head = -1

    def is_empty(self):
        return self._head == -1

    def push(self, element):
        self._head += 1
        self._data.append(element)

    def pop(self):
        if not (self.is_empty()):
            value = self._data.pop()
            self._head -= 1
            return value
        else:
            raise StackEmptyException("can't pop from an empty stack.")

    def peek(self):
        if not (self.is_empty()):
            return self._data[self._head]
        else:
            raise StackEmptyException("can't peek into an empty stack.")

    def __str__(self):
        """
        for stack [1,2,3,4]
        return: bottom -> | 1 | 2 | 3 | 4 <- head
        """
        string_representation = "bottom -> "
        for i in range(0, self._head + 1):
            string_representation += f"| {str(self._data[i])} "
        string_representation += "<- head"
        return string_representation


if (__name__ == "__main__"):
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.push(7)

    print(s.pop())
    print(s.peek())
    print(s)