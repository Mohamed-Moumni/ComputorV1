from typing import List, Dict


class Parser:

    def __init__(self, _equation: str) -> None:
        self.equation = _equation

    def start(self) -> None:
        equal_found: int = self.equation.find("=")
        if equal_found == -1:
            raise SyntaxError("No Equal (=) sign found in The Equation")
        if equal_found > 1:
            raise SyntaxError("There are more than one equal Sign (=)")
        parsed_equation: List[str] = self.equation.split("=")
        left_side: str = parsed_equation[0]
        right_side: str = parsed_equation[1]
        # parse right side of the equation
        # parse left side of the equation
        # combine the sides
        # get the final equation that will be consumed by
        # the Equation Class

    @staticmethod
    def get_term(index: int, equation_side: str) -> Dict[str, float]:
        pass

    @staticmethod
    def skip_spaces(index: int, equation_side: str) -> int:
        equation_side_len = len(equation_side)
        while index < equation_side_len and equation_side[index].isspace():
            index += 1
        return index

    @staticmethod
    def parse_equation_side(equation_side: str) -> List[Dict[str, float]]:
        # there is a counter set to 0 at first
        # i check the sign at first if there is no
        # sign i accept it as positive
        # for the next terms if there is no sign
        # you have to raise an exception
        # check Coefficient
        #             |
        #           1  2
        # single degree Coeff
        # multiple degree coeff

        terms: List[Dict[str, float]] = []
        first_term: bool = True
        index: int = 0
        equation_side_len: int = 0
        while index < equation_side_len:
            index = Parser.skip_spaces(index, equation_side)
            if index == equation_side_len:
                break

            if first_term and equation_side[index] not in ["+", "-"]:
                equation_side = "+" + equation_side
                first_term = False

            if equation_side[index] not in ["+", "-"]:
                raise SyntaxError("Error in your Equation Syntax")
            term, current_index = Parser.get_term(index + 1, equation_side)
            terms.append(term)
            index = current_index
        if len(terms) == 0:
            raise SyntaxError("Empty Side of The Equation")
        return terms
