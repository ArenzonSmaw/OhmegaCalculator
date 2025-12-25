class Token:
    def __init__(self):
        pass


class Operand(Token):
    def __init__(self, value, real_flag = False):
        super().__init__()
        self._value = value
        self._is_real = real_flag or type(value) == float

    def __repr__(self):
        return str(self._value)


class Operator(Token):
    def __init__(self, operator):
        super().__init__()
        self._operator = operator

    def __repr__(self):
        return self._operator

class UnaryOperator(Operator):
    def __init__(self, operator):
        super().__init__(operator)

class BinaryOperator(Operator):
    def __init__(self, operator):
        super().__init__(operator)