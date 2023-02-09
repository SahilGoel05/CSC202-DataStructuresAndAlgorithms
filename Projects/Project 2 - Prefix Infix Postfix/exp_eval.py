from stack_array import Stack


# You should not change this Exception class!
class PostfixFormatException(Exception):
    pass


def postfix_eval(input_str: str) -> float:

    nums = Stack(30)
    amt_ops = 0
    amt_nums = 0

    if len(input_str) == 0:
        raise PostfixFormatException("Insufficient operands")

    while len(input_str) > 0:
        next_space_index = input_str.find(" ")
        if next_space_index == -1:
            next_space_index = len(input_str)
        temp = input_str[0: next_space_index]

        match temp:
            case "+":
                try:
                    nums.push(nums.pop() + nums.pop())
                    amt_ops += 1
                except IndexError:
                    raise PostfixFormatException("Insufficient operands")
            case "-":
                try:
                    num1 = nums.pop()
                    num2 = nums.pop()
                    nums.push(num2 - num1)
                    amt_ops += 1
                except IndexError:
                    raise PostfixFormatException("Insufficient operands")
            case "*":
                try:
                    nums.push(nums.pop() * nums.pop())
                    amt_ops += 1
                except IndexError:
                    raise PostfixFormatException("Insufficient operands")
            case "/":
                try:
                    num1 = nums.pop()
                    num2 = nums.pop()
                    if num1 == 0:
                        raise ValueError
                    nums.push(num2 / num1)
                    amt_ops += 1
                except IndexError:
                    raise PostfixFormatException("Insufficient operands")
            case "**":
                try:
                    num1 = nums.pop()
                    num2 = nums.pop()
                    nums.push(num2 ** num1)
                    amt_ops += 1
                except IndexError:
                    raise PostfixFormatException("Insufficient operands")
            case ">>":
                try:
                    num1 = nums.pop()
                    num2 = nums.pop()
                    if int(num1) != num1 or int(num2) != num2:
                        raise PostfixFormatException("Illegal bit shift operand")
                    t = int(num2) >> int(num1)
                    nums.push(t)
                    amt_ops += 1
                except IndexError:
                    raise PostfixFormatException("Insufficient operands")
            case "<<":
                try:
                    num1 = nums.pop()
                    num2 = nums.pop()
                    if int(num1) != num1 or int(num2) != num2:
                        raise PostfixFormatException("Illegal bit shift operand")
                    t = int(num2) << int(num1)
                    nums.push(t)
                    amt_ops += 1
                except IndexError:
                    raise PostfixFormatException("Insufficient operands")
            case _:
                try:
                    p_this = float(temp)
                    nums.push(p_this)
                except ValueError:
                    raise PostfixFormatException("Invalid token")
                amt_nums += 1
        input_str = input_str[next_space_index + 1: len(input_str)]

    if amt_nums - 1 == amt_ops:
        return nums.pop()
    raise PostfixFormatException("Too many operands")

    """Evaluates a postfix expression"""
    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""


def infix_to_postfix(input_str: str) -> str:
    ops = Stack(30)
    rpn = ""
    while len(input_str) > 0:
        next_space_index = input_str.find(" ")
        if next_space_index == -1:
            next_space_index = len(input_str)
        cur = input_str[0: next_space_index]
        cur_prec = get_prec(cur)

        if cur == "**" and cur_prec == 3:
            if not ops.is_empty():
                prev = ops.pop()
                prev_prec = get_prec(prev)
                while prev_prec > cur_prec:
                    rpn += prev + " "
                    if ops.is_empty():
                        prev_prec = -2
                    else:
                        prev = ops.pop()
                        prev_prec = get_prec(prev)
                if prev_prec <= cur_prec and prev_prec != -2:
                    ops.push(prev)
            ops.push(cur)
        elif cur == "(" and cur_prec == 0:
            ops.push(cur)
        elif cur == ")":
            prev = ops.pop()
            while prev != "(":
                rpn += prev + " "
                prev = ops.pop()
        elif cur_prec == -1:
            rpn += cur + " "
        else:
            if not ops.is_empty():
                prev = ops.pop()
                prev_prec = get_prec(prev)
                while prev_prec >= cur_prec:
                    rpn += prev + " "
                    if ops.is_empty():
                        prev_prec = -2
                    else:
                        prev = ops.pop()
                        prev_prec = get_prec(prev)
                if prev_prec < cur_prec and prev_prec != -2:
                    ops.push(prev)
            ops.push(cur)
        input_str = input_str[next_space_index + 1: len(input_str)]

    while not ops.is_empty():
        cur_op = ops.pop()
        rpn += cur_op + " "

    return rpn[0: len(rpn) - 1]

def get_prec(cur: str) -> int:
    match cur:
        case "(":
            return 0
        case "+":
            return 1
        case "-":
            return 1
        case "*":
            return 2
        case "/":
            return 2
        case "**":
            return 3
        case ">>":
            return 4
        case "<<":
            return 4
        case ")":
            return 5
        case _:
            return -1

    """Converts an infix expression to an equivalent postfix expression"""
    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression """
    pass


def prefix_to_postfix(input_str: str) -> str:
    rpn = Stack(30)

    while len(input_str) > 0:
        last_space_index = input_str.rfind(" ")
        temp = input_str[last_space_index + 1: len(input_str)]
        if is_op(temp):
            rpn.push(rpn.pop() + rpn.pop() + temp + " ")
        else:
            rpn.push(temp + " ")

        input_str = input_str[0: last_space_index]

    ret = rpn.pop()
    return ret[0: len(ret) - 1]


def is_op(temp: str) -> bool:
    if temp == "+" or temp == "-" or temp == "*" or temp == "/" or temp == "-" or temp == "**" or temp == ">>" or temp == "<<":
        return True
    return False

    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression(tokens are space separated)"""
    pass


