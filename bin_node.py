class BinNode():
    """
    Binary Node data structure: each node has 2 sub-nodes, right and left
    bn.value/right/left -> access the value / right son / left son of node
    bn.set_value/right/left() -> change the value / right son / left son of node
    """
    def __init__(self, value = None, left = None, right = None):
        super().__init__()
        if (not left is None and not isinstance(left, BinNode)):
            left = BinNode(left)
        if (not right is None and not isinstance(right, BinNode)):
            right = BinNode(right)
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
    def has_left(self):
        return not self._left is None
    def has_right(self):
        return not self._right is None


if (__name__ == "__main__"):
    node = BinNode(5,left= BinNode(4,left= BinNode(2,left= BinNode(1),right= BinNode(3))),right= BinNode(6,left= BinNode(7,9),right= BinNode(8)))

    print(node)
    print(node.get_left)
    print(f"{node.get_left.get_right} {node.get_left.get_left}")