def parser(polynomial):
    """parse the polynom and convert it to a dictionary ready to solve

    Args:
        polynomial (str): the equation input string
    """
    try:
        poly_after_syntax_check = check_syntax(polynomial)
    except Exception as e:
        raise e("There is a Syntax Error")


def get_expression(polynom, index):
    expression = ""
    if polynom[i] == '-' or polynom[i] == '+':
        pass
    if polynom[i] in "0123456789":
        pass
    return expression, index


def check_syntax(polynom):
    polynom_to_list = []
    for i in range(len(polynom)):
        if polynom[i] != ' ':
            expression, i = get_expression(polynom, i)
            polynom_to_list.append(expression)
    return polynom_to_list

# in the parsing part i have to find sign (-+) followed by number
# and then followed by the astrisk and then the X operator and after then follwed by ^ and the degree
# like that (-|+)[0-9]*X^[0-9]
# i have the find only one = operator
# always the left and the right of the = operator must be not empty
# the first phase of parsing is set to check if there are any syntax error and store the
# the second phase of parsing is set to check if there are any
