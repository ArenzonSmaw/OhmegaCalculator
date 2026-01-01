import lexer
import parser
import tokens
import exceptions


def calculate_node(node):
    """
    calculates the result of a single node via postorder tree scan
    if node_value is an operand, returns its value
    returns: result in float type
    """
    node_value = node.get_value

    if (isinstance(node_value, tokens.Operand)): # bug in comparing types.
        return node_value.calculate()

    elif (isinstance(node_value, tokens.UnaryOperator)):
        return node_value.calculate(node.get_left.get_value.calculate())

    elif (isinstance(node_value, tokens.BinaryOperator)):
        left = calculate_tree(node.get_left.get_value.calculate())
        right = calculate_tree(node.get_right.get_value.calculate())
        return node_value.calculate(left,right)

    else:
        raise exceptions.ExpectedTokenException(f"node value should be an operator / operand. received value type: {type(node_value)}")


def calculate_tree(bin_tree):
    if (bin_tree is None):
        return
    value = bin_tree.get_value
    if (isinstance(value, tokens.Operand)):
        return value.calculate()
    else:
        left = right = None
        if (bin_tree.has_left()):
            left = calculate_tree(bin_tree.get_left)

        if (bin_tree.has_right()):
            right = calculate_tree(bin_tree.get_right)

        if (isinstance(value, tokens.UnaryOperator)):
            return value.calculate(left)
        return value.calculate(left, right)



def calculate(expression):
    token_list = lexer.tokenize(expression)
    syntax_tree = parser.build_syntax_tree(token_list)

    return calculate_tree(syntax_tree)


if (__name__ == "__main__"):
    example = "136/2+6^2#-7"
    result = calculate(example)
    print(result)