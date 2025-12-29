print("Tokens module imported")
print(__name__)

class Token:
    def __init__(self):
        pass

prefix_operators = {'~','-',}
postfix_operators = {'!',}

class Operand(Token):
    def __init__(self, value, real_flag = False):
        super().__init__()
        if (real_flag or int(value) != value):
            self._real_flag = True
            self._value = float(value)
        else:
            self._real_flag = False
            self._value = int(value)

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

