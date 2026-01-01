import exceptions
from math import pow

class Token:
    def __init__(self, index):
        self._index = index

    @property
    def get_index(self):
        return self._index

    def calculate(self, value):
        return value


class Operand(Token):
    def __init__(self, value, index):
        super().__init__(index)
        self._value = value

    def __repr__(self):
        return str(self._value)

    def calculate(self, comment=None):
        return super().calculate(self._value)

    @property
    def get_value(self):
        return self._value

class IntegerOperand(Operand):
    def __init__(self, value, index):
        super().__init__(int(value), index)

class RealOperand(Operand):
    def __init__(self, value, index):
        super().__init__(float(value), index)


class Operator(Token):
    def __init__(self, operator, precedence, side, index):
        super().__init__(index)
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

prefix_operators = {'~', '-', }
postfix_operators = {'!', }

def factorial_wrapper(fact):
    cache = {}
    def wrapper(num):
        if num not in cache:
            cache[num] = fact(num)
        return cache[num]
    return wrapper

class UnaryOperator(Operator):
    def __init__(self, operator, precedence, side, index):
        super().__init__(operator, precedence, side, index)

class Factorial(UnaryOperator):
    def __init__(self, index):
        super().__init__('!',6,'right', index)
    @factorial_wrapper
    def calculate(self, opnd):
        if (opnd == 0):
            return 1
        super().calculate(opnd * self.calculate(opnd-1))
        return None

class Tilde(UnaryOperator):
    def __init__(self, index):
        super().__init__('~',6,'left', index)
    def calculate(self, opnd):
        if not (isinstance(opnd, Operand)):
            raise exceptions.ExpectedTokenException(f"expected type 'operand' for operator '~' at index {self.get_index}. got '{opnd} instead.")
        super().calculate(-1 * opnd.calculate())

class Negation(UnaryOperator):
    def __init__(self, index):
        super().__init__('-', 2.5, 'left', index)
    def calculate(self, opnd):
        super().calculate(-1 * opnd)

class DigSum(UnaryOperator):
    def __init__(self, index):
        super().__init__('#', 6, 'right', index)
    def calculate(self, opnd):
        result = 0
        while (int(opnd) != opnd):
            opnd *= 10
        while (opnd > 0):
            result += opnd % 10
            opnd = int(opnd/10)
        super().calculate(result)

class BinaryOperator(Operator):
    def __init__(self, operator, precedence, index):
        super().__init__(operator, precedence, 'middle', index)
    def calculate(self, left, right):
        return left if not left is None else right

class Addition(BinaryOperator):
    def __init__(self, index):
        super().__init__('+', 1, index)

    def calculate(self, left, right):
        return super().calculate(left + right, None)

class Subtraction(BinaryOperator):
    def __init__(self, index):
        super().__init__('-', 1, index)

    def calculate(self, left, right):
        return super().calculate(left - right, None)

class Multiply(BinaryOperator):
    def __init__(self, index):
        super().__init__('*', 2, index)
    def calculate(self, left, right):
        super().calculate(left * right, None)

class Divide(BinaryOperator):
    def __init__(self, index):
        super().__init__('/', 2, index)
    def calculate(self,left, right):
        if (right == 0):
            raise exceptions.DivisionByZeroException(f'Division by zero is not allowed at index: {self._index}')
        super().calculate(left / right, None)

class Power(BinaryOperator):
    def __init__(self, index):
        super().__init__('^', 3, index)
    def calculate(self, left, right):
        super().calculate(pow(left,right), None)

class Mod(BinaryOperator):
    def __init__(self, index):
        super().__init__('%', 4, index)
    def calculate(self, left, right):
        super().calculate(left % right, None)

class Max(BinaryOperator):
    def __init__(self, index):
        super().__init__('$', 5, index)
    def calculate(self, left, right):
        super().calculate(left if left > right else right, None)

class Min(BinaryOperator):
    def __init__(self, index):
        super().__init__('&', 5, index)
    def calculate(self, left, right):
        super().calculate(left if left < right else right, None)

class Average(BinaryOperator):
    def __init__(self, index):
        super().__init__('@', 5, index)
    def calculate(self, left, right):
        super().calculate(float(left+right)/2, None)

class Parentheses(Token):
    def __init__(self, value, index):
        if (value == '('):
            parentheses_type = 'open'
        else:
            parentheses_type = 'closed'
        super().__init__(index)
        self._value = value
        self._type = parentheses_type

    def get_parentheses_type(self):
        return self._type

    def __repr__(self):
        return self._value

