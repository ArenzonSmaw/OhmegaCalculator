import tokens

class UnknownTokenException(Exception):
    def __init__(self, message):
        super().__init__()
        self._message = message

binary_operators = {'+': 1, '*': 2, '/': 2, '^': 3, '%': 4, '$': 5, '&': 5, '@': 5}
unary_operators = {'!': 6, '~': 6, '-': 1}
white_spaces = {' ', '\t', ''}

def token_type(char):
    if char == '(' or char == ')' : return 3
    if char in binary_operators   : return 2
    if char in unary_operators    : return 1
    if char >= '0' and char <= '9'\
                   or char == '.' : return 0
    if char in white_spaces       : return -1
    else:
        raise UnknownTokenException(f"Unknown token: {char}.")


def tokenize_operand(expression, index):
    """
    extracts operand from input
    Args:
        expression - input string
        index - first index of the operand
    Returns:
        object of operand type (Integer/Real - depends on real_flag)
        index - first index after the operand
    """
    value = 0
    count = 0
    char = expression[index]
    real_flag = char == '.' #flags whether a decimal point has been encountered
    while (index < len(expression) and token_type(char) == 0):
        if (char == '.'):
            real_flag = True
        else:
            value *= 10
            value += int(char)
            if (real_flag):
                count += 1
        index += 1
        if (index < len(expression)):
            char = expression[index]
    value /= 10**count
    token = tokens.Operand(value, real_flag)
    return token, index-1



def tokenize(expression):
    token_list = []
    char_index = 0
    while (char_index in range(len(expression))):
        tok_type = token_type(expression[char_index])
        if (tok_type == 0):
            operand, char_index = tokenize_operand(expression = expression, index = char_index)
            token_list.append(operand)
        elif (tok_type == 1):
            operator = tokens.UnaryOperator(expression[char_index], unary_operators[expression[char_index]])
            if(operator.get_precedence == 1 and token_list and not isinstance(token_list[-1],tokens.Operator)):
                token_list.append(tokens.BinaryOperator('+',1))
            token_list.append(operator)

        elif (tok_type == 2):
            operator = tokens.BinaryOperator(expression[char_index], binary_operators[expression[char_index]])
            token_list.append(operator)
        elif (tok_type == 3):
            parentheses = expression[char_index]
            token_list.append(tokens.Parentheses(parentheses))
        else:
            pass
        char_index += 1
    return token_list


if (__name__ == "__main__"):
    exp = "5+ 4-32+ .57/(6 9) +4"
    tokens = tokenize(exp)
    print(tokens)