class Token:
    def __init__(self):
        pass


class Operand(Token):
    def __init__(self, value):
        super().__init__()
        self._value = value

class Integer(Operand):
    def __init__(self, value):
        super().__init__(value)

class Real(Operand):
    def __init__(self, value):
        super().__init__(value)


class Operator(Token):
    def __init__(self, operator):
        super().__init__()
        self._operator = operator

class UnaryOperator(Operator):
    def __init__(self, operator):
        super().__init__(operator)

class BinaryOperator(Operator):
    def __init__(self, operator):
        super().__init__(operator)