import stack
import bin_node
import lexer
import tokens
import exceptions

def build_syntax_tree(tokens_list: list):
    """
    builds an Abstract Syntax Tree that represents the arithmetic expression
    gets: list of tokens
    returns: binary tree that represents an arithmetic expression with standardized precedence
    """
    operator_stack = stack.Stack()
    operand_stack = stack.Stack()

    for token_index in range(len(tokens_list)):
        token = tokens_list[token_index]
        if (type(token) == type(tokens.Parentheses)):
            parentheses = token
            if(parentheses.get_parentheses_type() == "open"):
                operand_stack.push(token)
                operator_stack.push(token)
            
        elif (isinstance(token,tokens.Operand)):
            operand_stack.push(bin_node.BinNode(token))
            #if(not operator_stack.is_empty())
            if (not operator_stack.is_empty() and operator_stack.peek().get_side == "left"):
                node = bin_node.BinNode(operator_stack.pop(), left= operand_stack.pop())
                operand_stack.push(node)
        else:
            operator = token
            if (operator.get_side == "right"):
                try:
                    operand = operand_stack.pop()
                except stack.StackEmptyException:
                    raise exceptions.MissingOperandException(f"Missing operand for operator: {operator}.")
                else:
                    if (type(operand) == type(tokens.Parentheses)):
                        raise exceptions.MissingOperandException(f"Missing operand for operator: {operator}.")
            while (not operator_stack.is_empty() and operator_stack.peek() >= operator):
                try:
                    node = bin_node.BinNode(operator_stack.peek(),left = operand_stack.pop(), right = operand_stack.pop())
                except stack.StackEmptyException:
                    raise exceptions.MissingOperandException(f"One or more operands are missing for operator: {operator_stack.pop()}.")
                else:
                    operator_stack.pop()
                    operand_stack.push(node)
            operator_stack.push(operator)

    return operand_stack.pop()


if (__name__ == "__main__"):
    lst = lexer.tokenize("54+(!6)")
    ast = build_syntax_tree(lst)

