import tokens
import exceptions

class UnknownTokenException(Exception):
    def __init__(self, message):
        super().__init__()
        self._message = message
    def __str__(self):
        return self._message

binary_operators = {'+': 1, '*': 2, '/': 2, '^': 3, '%': 4, '$': 5, '&': 5, '@': 5}
unary_operators = {'!': 6, '~': 6, '#': 6}
white_spaces = {' ', '\t', '-'} #minus is counted as a white space so the tokenize_operand func will know to stop scanning the operand,
                                # but the - operator need special tokenization so isn't included in any other set

def token_type(char, index):
    if char == '(' or char == ')' : return 3
    if char in binary_operators   : return 2
    if char in unary_operators    : return 1
    if char >= '0' and char <= '9'\
                   or char == '.' : return 0
    if char in white_spaces       : return -1
    else:
        raise UnknownTokenException(f"Unknown token: {char} at index {index}.")

def tokenize_minus(token_list, expression, index):
    """
    receives: the current token list, the given expression and the index of the -
    determines the role of the - operator according to the context
    returns: a tokenized - according to the role of the token
    """
    token = None
    if (not index <= len(expression)):
        raise exceptions.ExpectedTokenException(f"Expected operand after operator '-' at index: {index}")
    if (isinstance(token_list[-1], tokens.Operator)): # if last inserted token is an operator, then it is an operand bound minus
        token = tokens.OperandBoundMinus(index)
    elif (isinstance(token_list[-1], tokens.Operand)):
        token = tokens.Subtraction(index)
    else:
        token = tokens.Negation(index)
    return token


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
    while (index < len(expression) and token_type(char, index) == 0):
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

def tokenize_unary_operator(token_list, char, index):
    if (char == '~' and type(token_list[-1]) == tokens.Tilde):
        raise exceptions.ExpectedTokenException(f"expected operand after operator '~' at index {index}")
    if (char == '~'):
        return tokens.Tilde(index)
    elif (char == '!'):
        return tokens.Factorial(index)
    elif (char == '#'):
        return tokens.DigSum(index)
    else:
        return "please add the new operator to the tokenization functions"

def tokenize_binary_operator(char, index):
    if (char == '+'):
        return tokens.Addition(index)
    elif (char == '*'):
        return tokens.Multiply(index)
    elif (char == '/'):
        return tokens.Divide(index)
    elif (char == '^'):
        return tokens.Power(index)
    elif (char == '%'):
        return tokens.Mod(index)
    elif (char == '$'):
        return tokens.Max(index)
    elif (char == '&'):
        return tokens.Min(index)
    elif (char == '@'):
        return tokens.Average(index)
    else:
        return "please add the new operator to the tokenization functions"

def tokenize(expression):
    token_list = []
    char_index = 0
    while (char_index in range(len(expression))):
        character = expression[char_index]
        if (character == '-'):
            token_list.append(tokenize_minus(token_list, expression, char_index))
        tok_type = token_type(expression[char_index], char_index)
        if (tok_type == 0):
            operand, char_index = tokenize_operand(expression = expression, index = char_index)
            token_list.append(operand)
        elif (tok_type == 1):
            operator = tokenize_unary_operator(token_list, character, char_index)
            token_list.append(operator)
        elif (tok_type == 2):
            operator = tokenize_binary_operator(character, char_index)
            token_list.append(operator)
        elif (tok_type == 3):
            parentheses = tokens.Parentheses(character, char_index)
            token_list.append(parentheses)
        else:
            pass
        char_index += 1
    return token_list


if (__name__ == "__main__"):
    exp = "5+ 4-32+ .57/(6 9) +4"
    tokens = tokenize(exp)
    print(tokens)