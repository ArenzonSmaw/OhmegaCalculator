import lexer
import parser
import tokens
import exceptions


def recursive_operator_wrapper(func):
    #implements memoization for a recursive operate i.e: power, factorial
    cache = dict({})
    def wrapper(value):
        if (value in cache):
            return cache[value]
        else:
            result = func(value)
            cache[value] = result
            return result
    return wrapper

@recursive_operator_wrapper
def factorial(number):
    if (number < 0):
        raise exceptions.InvalidOperandException(f"operand: {number} is invalid for operator: '!'")
    if (number == 0 or number == 1):
        return 1
    else:
        return number * factorial(number -1)


def calculate_node(node):
    """
    calculates the result of a single node via postorder tree scan
    if node_value is an operand, returns its value
    returns: result in float type
    """
    node_value = node.get_value
    if (isinstance(node_value, tokens.Operand)): # bug in comparing types.
        return node_value.get_value

    elif (type(node_value) == tokens.UnaryOperator):
        operand = node.get_left.get_value.get_value
        if (repr(node_value) == '!'):
            return factorial(operand)
        elif (repr(node_value) == '~' or repr(node_value) == '-'):
            return -1 * operand
        else:
            raise exceptions.IllegalOperatorException(f"illegal operator {node_value}")

    elif (type(node_value) == tokens.BinaryOperator):
        left = calculate_tree(node.get_left)
        right = calculate_tree(node.get_right)
        if (repr(node_value) == '+'):
            return left + right
        elif (repr(node_value) == '*'):
            return left * right
        elif (repr(node_value) == '/'):
            if (left == 0):
                raise exceptions.DivisionByZeroException("Divide by zero is not allowed yet ;).")
            else:
                return left / right
        elif (repr(node_value) == '^'):
            return left ** right
        elif (repr(node_value) == '%'):
            return left % right
        elif (repr(node_value) == '$'):
            return left if left >= right else right
        elif (repr(node_value) == '&'):
            return left if left <= right else right
        elif (repr(node_value) == '@'):
            return float(right + left) / 2

        else:
            raise exceptions.IllegalOperatorException(f"illegal operator {str(node_value)}")
    else:
        raise exceptions.ExpectedTokenException(f"node value should be an operator / operand. received value type: {type(node_value)}")


def calculate_tree(bin_tree):
    if (bin_tree is None):
        return
    if (bin_tree.has_left()):
        bin_tree.set_left(tokens.Operand(calculate_tree(bin_tree.get_left)))
    if (bin_tree.has_right()):
        bin_tree.set_right(tokens.Operand(calculate_tree(bin_tree.get_right)))

    return calculate_node(bin_tree)


def calculate(expression):
    token_list = lexer.tokenize(expression)
    syntax_tree = parser.build_syntax_tree(token_list)

    return calculate_tree(syntax_tree)


if (__name__ == "__main__"):
    example = "3+6*7/9-1%4"
    print(calculate(example))