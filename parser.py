
import lexer
import tokens
import exceptions
import bin_node

def parenthesized_list (tokens_list, index):
    """
    gets: tokens list and starting index
    returns: a syntax tree of the expression inside the parentheses
    """
    end_index = index + 1
    count = 1
    found = False
    while (end_index < len(tokens_list) and not found):
        if (type(tokens_list[end_index]) == tokens.Parentheses):
            if (tokens_list[end_index].get_parentheses_type == "open"):
                count +=1
            else:
                count -= 1
        end_index += 1
        found = (count == 0)
    if not found:
        raise exceptions.ExpectedTokenException("Syntax Error: ')' Expected.")
    sub_list = tokens_list[index+1: end_index-1]
    return build_syntax_tree(sub_list), end_index - 1

def append_node (node, operands_list, operators_list):
    """
    adds node to operands_list, checks if there is a prefix unary operator and applies it accordingly
    """
    while (len(operators_list) > 0 and operators_list[-1].get_side == "left"):
        node = bin_node.BinNode(operators_list[-1], node)
        operators_list.pop()

    operands_list.append(node)


def apply_operator(operator, operand_list, operator_list):
    """
    gets: operator object and the operand list
    checks for syntax errors and builds a mini-tree that represents that singular operation
    returns: the mini syntax tree
    """
    if (isinstance(operator, tokens.BinaryOperator)):
        try:
            right_operand = operand_list.pop()
            left_operand = operand_list.pop()
        except IndexError:
            raise exceptions.ExpectedTokenException(f"expected 2 operands for binary operator: {operator} at index {operator.get_index}.")
        else:
            operand_list.append(bin_node.BinNode(operator, left_operand, right_operand))
    elif (operator.get_side == "left"):
        operator_list.append(operator)
    else:
        try:
            operand = operand_list.pop()
        except IndexError:
            raise exceptions.ExpectedTokenException(f"expected operand for operator: {operator} at index {operator.get_index}.")
        else:
            operand_list.append(bin_node.BinNode(operator, operand))


def append_operator(operator, operator_list, operand_list):
    """
    while lower in precedence, applies the operators in operator_list on the nodes of operand_list
    when precedence is greater, appends operator to operator_list
    """
    if (operator.get_side == "right"):
        apply_operator(operator, operand_list, operator_list)
    elif not operator_list or operator.get_side == "left":
        operator_list.append(operator)
    else:
        while (len(operator_list) > 0 and operator_list[-1] >= operator):
            apply_operator(operator_list.pop(), operand_list, operator_list)
        operator_list.append(operator)

def apply_all_operators(operators_list, operands_list):

    while(len(operators_list) > 0):
        operator = operators_list.pop()
        apply_operator(operator, operands_list, operators_list)

    if(len(operands_list) > 1):
        raise exceptions.ExpectedTokenException("Syntax error: missing operator.")


def build_syntax_tree(tokens_list: list):
    """
    builds an Abstract Syntax Tree that represents the arithmetic expression
    gets: list of tokens
    returns: binary tree that represents an arithmetic expression with standardized precedence
    """
    operators_list = []
    operands_list = []

    token_index = 0
    while (token_index < len(tokens_list)):
        token = tokens_list[token_index]
        if (type(token) == tokens.Parentheses):
            if(token.get_parentheses_type() == "open"):
                node, token_index = parenthesized_list(tokens_list, token_index)
                append_node(node, operands_list, operators_list)
            else:
                raise exceptions.UnexpectedTokenException(f"Unexpected Token ')' at index: {token.get_index}.")

        elif (isinstance(token, tokens.Operand)):
            node = bin_node.BinNode(value= token)
            append_node(node, operands_list, operators_list)

        elif (isinstance(token, tokens.Operator)):
            append_operator(token, operators_list, operands_list)
        else:
            raise exceptions.UnexpectedTokenException(f"unexpected token {repr(token)} at index {token.get_index}.")
        token_index += 1

    apply_all_operators(operators_list, operands_list)

    if(len(operands_list) > 1):
        raise exceptions.ExpectedTokenException("Expected operator.")
    else:
        return operands_list.pop()


if (__name__ == "__main__"):
    lst = lexer.tokenize("5+40&(5^2)---~(4+8)*3")
    ast = build_syntax_tree(lst)
    print(ast)

