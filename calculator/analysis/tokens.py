class Token:
    def __init__(self):
        pass

prefix_operators = {'~','-',}
postfix_operators = {'!',}

class Operand(Token):
    def __init__(self, value, real_flag = False):
        super().__init__()
        self._value = value
        self._is_real = real_flag or type(value) == float

    def __repr__(self):
        return str(self._value)

    @property
    def get_value(self):
        return self._value


class Operator(Token):
    def __init__(self, operator, precedence, side= "middle"):
        super().__init__()
        self._operator = operator
        self._precedence = precedence
        self._side = side

    def __repr__(self):
        return self._operator
    def __ge__(self, other):
        return self._precedence >= other.get_precedence

    @property
    def get_precedence(self):
        return self._precedence

    @property
    def get_side(self):
        return self._side

class UnaryOperator(Operator):
    def __init__(self, operator, precedence):
        super().__init__(operator, precedence, side= "left" if (operator in prefix_operators) else "right")



class BinaryOperator(Operator):
    def __init__(self, operator, precedence):
        super().__init__(operator, precedence)

class Parentheses(Token):
    def __init__(self, value):
        super().__init__()
        self._value = value
    def get_parentheses_type(self):
        return "open" if self._value == '(' else "close"

    def __repr__(self):
        return self._value
