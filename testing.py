from calculator import calculate
import pytest
import exceptions



def test_valid_addition_precedent():
    assert(calculate("14+6-16"), 4)
def test_valid_addition_non_precedent():
    assert(calculate("5!+7!"), 5160)
def test_valid_addition_parenthesized():
    assert(calculate("(6+2)^3"), 512)
def test_invalid_addition_expected_operand():
    try:
        calculate("4*+3")
        assert(False)
    except exceptions.ExpectedTokenException:
        assert(True)
    except:
        assert(False)

def test_valid_subtraction_precedent():
    assert(calculate("8--5-3"), 10)
def test_valid_subtraction_not_precedent():
    assert(calculate("7-6*2"), -5)
def test_valid_subtraction_parenthesized():
    assert(calculate("40-(6^(3-1))"), 4)
def test_invalid_subtraction_operand_expected():
    try:
        calculate("8*4-")
        assert(False)
    except exceptions.ExpectedTokenException:
        assert(True)
    except:
        assert(False)

def test_valid_multiplication_precedent():
    assert(calculate("5 * 2 + 7"), 17)
def test_valid_multiplication_not_precedent():
    assert(calculate("5*4^2"), 80)
def test_invalid_operand_expected():
    try:
        calculate("*5 2+2")
        assert(False)
    except exceptions.ExpectedTokenException:
        assert(True)
    except:
        assert(False)

def test_valid_division_precedent():
    assert(calculate("5/6+13"), pytest.approx(13.8333,rel= 1e-3))
def test_valid_division_non_precedent():
    assert(calculate("(8.1-5)/3"), pytest.approx(1.0333,rel= 1e-3))
def test_invalid_expected_operand():
    try:
        calculate("7+/6")
        assert(False)
    except exceptions.ExpectedTokenException:
        assert(True)
    except:
        assert(False)
def test_invalid_zero_division():
    try:
        calculate("5*9/(92%4)#")
        assert(False)
    except exceptions.DivisionByZeroException:
        assert(True)
    except:
        assert(False)


def test_valid_power_precedent():
    assert(calculate("3*4^2"), 48)
def test_valid_power_non_precedent():
    assert(calculate("13638#^3"), 8)
def test_invalid_power_expected_operand():
    try:
        calculate("^50")
        assert(False)
    except exceptions.ExpectedTokenException:
        assert(True)
    except:
        assert(False)

def test_valid_modulus_precedent():
    assert(calculate("4+71%6"), 9)
def test_valid_modulus_non_precedent():
    assert(calculate("135117#%3"), 0)
def test_invalid_modulus_zero_division():
    try:
        calculate("61%0")
        assert(False)
    except exceptions.DivisionByZeroException:
        assert(True)
    except:
        assert(False)
def test_invalid_modulus_expected_operand():
    try:
        calculate("83%")
        assert(False)
    except exceptions.ExpectedTokenException:
        assert(True)
    except:
        assert(False)

def test_valid_max_precedent():
    assert(calculate("5$2-1"), 4)
def test_valid_max_non_precedent():
    assert(calculate("6!$(42*18)"), 756)
def test_invalid_max_expected_operand():
    try:
        calculate("$")
        assert(False)
    except exceptions.ExpectedTokenException:
        assert(True)
    except:
        assert(False)

def test_valid_min_precedent():
    assert(calculate("16-6&21"), 10)
def test_valid_min_non_precedent():
    assert(calculate("(86/9)&16/3"), pytest.approx(3.1851,rel= 1e-3))
def test_invalid_min_operand_expected():
    try:
        calculate("&")
        assert(False)
    except exceptions.ExpectedTokenException:
        assert(True)
    except:
        assert(False)

def test_valid_average_precedent():
    assert(calculate("6*4@8"), 36)
def test_valid_average_non_precedent():
    assert(calculate("(6*4)@8"), 16)
def test_invalid_average_expected_operand():
    try:
        calculate("@")
        assert(False)
    except exceptions.ExpectedTokenException:
        assert(True)
    except:
        assert(False)

def test_valid_tilde_simple():
    assert("~6", -6)
def test_valid_tilde_concatenated():
    assert(calculate("~(~(~(4&0-72)))"), 72)
def test_invalid_tilde_concatenated():
    try:
        calculate("~~3")
        assert(False)
    except exceptions.ExpectedTokenException:
        assert(True)
    except:
        assert(False)
def test_invalid_tilde_operand_expected_p1():
    try:
        calculate("~")
        assert(False)
    except exceptions.ExpectedTokenException:
        assert(True)
    except:
        assert(False)
def test_invalid_tilde_operand_expected_p2():
    try:
        calculate("-3~")
        assert(False)
    except exceptions.ExpectedTokenException:
        assert(True)
    except:
        assert(False)

def test_valid_factorial():
    assert(calculate("6!"), 720)
def test_valid_factorial_concatenated():
    assert(calculate("4!!"), pytest.approx(6.2044e23, rel= 1e19))
def test_invalid_factorial__too_large():
    try:
        calculate("99999!!")
        assert(False)
    except exceptions.InvalidOperandException:
        assert(True)
    except:
        assert(False)
def test_invalid_factorial_expected_operand():
    try:
        calculate("!")
        assert(False)
    except exceptions.ExpectedTokenException:
        assert(True)
    except:
        assert(False)
def test_invalid_factorial_negative():
    try:
        calculate("(-15)!")
        assert(False)
    except exceptions.InvalidOperandException:
        assert(True)
    except:
        assert(False)
def test_invalid_factorial_floating_point():
    try:
        calculate("5.3!")
        assert(False)
    except exceptions.InvalidOperandException:
        assert(True)
    except:
        assert(False)

def test_valid_digit_sum_precedent():
    assert(calculate("1234567#@5"), 3)
def test_valid_digit_sum_non_precedent():
    assert(calculate("6!#"), 9)
def test_valid_digit_sum_concatenated():
    assert(calculate("(((7777#)!#)!#^2)#"), 9)
def test_valid_digit_sum_floating_point():
    assert(calculate("123456789.987654321#"), 9)
def test_invalid_digit_sum_operand_expected():
    try:
        calculate("#5")
        assert(False)
    except exceptions.ExpectedTokenException:
        assert(True)
    except:
        assert(False)

def test_valid_minus_expression():
    assert(calculate("-8--4-2-------7--13-(-13)--100"), 113)
def test_invalid_minus_operand_expected():
    try:
        calculate("-4--(5-)--4")
        assert(False)
    except exceptions.ExpectedTokenException:
        assert(True)
    except:
        assert(False)

def test_valid_combined_operator_expression_1():
    assert(calculate("((123*(2/3)^2)%3*(853#^4)$(268^1.4))@(62!#--~153/1^-30)"), pytest.approx(764.11775, rel= 1e-3))

def test_valid_combined_operator_expression_2():
    assert(calculate("(6+8)/2+~(6@8)+(1368+613#+892)#-83%(4+2)"), 4)

def test_invalid_combined_operator_zero_division():
    try:
        calculate("~(6+5+~-7)/0$(62-80)*3+4+7")
        assert(False)
    except exceptions.DivisionByZeroException:
        assert(True)
    except:
        assert(False)
def test_invalid_combined_operator_invalid_operator():
    try:
        calculate("3+4+7*((5+6)/2)!")
        assert(False)
    except exceptions.InvalidOperandException:
        assert(True)
    except:
        assert(False)