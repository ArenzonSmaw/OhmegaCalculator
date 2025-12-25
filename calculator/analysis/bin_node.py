class BinNode():
    def __init__(self, value = None, right = None, left = None):
        super().__init__()
        self._value = value
        self._right: BinNode = right
        self._left: BinNode = left

    def __str__(self):
        return str(self._value)

    @property
    def get_value(self):
        return self._value

    @property
    def get_right(self):
        return self._right

    @property
    def get_left(self):
        return self._left

    def set_value(self, value):
        self._value = value

    def set_right(self, node):
        if (type(node) == type(BinNode)):
            self._right = node
        else:
            self._right = BinNode(node)
    def set_left(self, node):
        if (type(node) == type(BinNode)):
            self._left = node
        else:
            self._left = BinNode(node)
    """value = property(get_value,set_value)
    right = property(get_right, set_right)
    left = property(get_left, set_left)"""

if (__name__ == "__main__"):
    node = BinNode(5)
    node.set_left(4)
    node2 = node.get_left
    node2.set_left(2)

    print(node)
    print(node2)
    print(f"{node2.get_right} {node2.get_left}")