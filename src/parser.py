from typing import List, Dict, Tuple
import re


class Parser:
    def __init__(self, _equation: str) -> None:
        self.equation = _equation
        self.remove_spaces()

    @staticmethod
    def parser_error(index: int, side: int, equation_side: str) -> None:
        sides: List[str] = ["Left", "right"]
        print(f"Encounter an error at the {sides[side]}, At index {index}")
        print(equation_side)
        location_error: str = (
            "_" * (index - 1) + "^" + (len(equation_side) - index + 1) * "_"
        )
        print(location_error)

    def start(self) -> List[Dict[str, float]]:
        terms: List[Dict[str, float]] = []
        equal_found: int = self.equation.count("=")

        if equal_found == 0:
            raise SyntaxError("No Equal (=) sign found in The Equation")
        if equal_found > 1:
            raise SyntaxError("There are more than one equal Sign (=)")

        parsed_equation: List[str] = self.equation.split("=")
        left_side: str = parsed_equation[0]
        right_side: str = parsed_equation[1]
        if left_side != "0":
            for term in Parser.parse_equation_side(left_side, 0):
                terms.append(term)
        if right_side != "0":
            for term in Parser.parse_equation_side(right_side, 1):
                terms.append(term)
        return terms

    def remove_spaces(self):
        self.equation = re.sub(r"\s+", "", self.equation)

    @staticmethod
    def get_term(index: int, equation_side: str, side: int) -> Dict[str, float]:
        print(f"Index: {index} -- Equation Side: {equation_side[index:]}")
        equation_side_len: int = len(equation_side)
        term: Dict[str, float] = {}
        coeff, index = Parser.get_coeff(index, equation_side, side)
        print(f"Coefficient: {coeff}")
        term["coeff"] = coeff
        term["degree"] = 0
        if index < equation_side_len and equation_side[index] == "*":
            index = Parser.get_X_term(index + 1, equation_side, side)
            degree, index = Parser.get_degree(index, equation_side, side)
            print(f"Degree: {degree}")
            term["degree"] = degree
        return term, index

    @staticmethod
    def get_coeff(index: int, equation_side: str, side: int) -> float:
        print(f"Index: {index} -- Coeff Side: {equation_side[index:]}")
        start: int = index
        end: int = index
        float_point: bool = False
        equation_side_len: int = len(equation_side)
        while end < equation_side_len:
            if equation_side[end] == ".":
                if not float_point:
                    float_point = True
                else:
                    Parser.parser_error(end, side, equation_side)
                    raise SyntaxError("Invalid Coefficient format")
            elif not equation_side[end].isdigit():
                break
            end += 1
        if start == end:
            raise SyntaxError("Invalid Coeff Error")
        return float(equation_side[start:end]), end

    @staticmethod
    def get_X_term(index: int, equation_side: str, side: int) -> None:
        print(f"Index: {index} -- X Term Side: {equation_side[index:]}")
        equation_side_len: int = len(equation_side)
        if index < equation_side_len and equation_side[index] != "X":
            Parser.parser_error(index, side, equation_side)
            raise SyntaxError("Term Syntax Error (X)")
        index += 1
        if index < equation_side_len and equation_side[index] != "^":
            Parser.parser_error(index, side, equation_side)
            raise SyntaxError("Term Syntax Error (^)")
        index += 1
        return index

    @staticmethod
    def get_degree(index: int, equation_side: str, side: int) -> int:
        print(f"Index: {index} -- Degree Side: {equation_side[index:]}")
        equation_side_len: int = len(equation_side)
        start: int = index
        end: int = index
        degree = 0
        while end < equation_side_len and equation_side[end].isdigit():
            end += 1
        if start == end:
            raise SyntaxError("Invalid Degree")
        degree = int(equation_side[start:end])
        if degree > 3:
            raise SyntaxError("You have to enter Degree between 0 <= degree <= 3")
        return degree, end

    @staticmethod
    def parse_equation_side(equation_side: str, side: int) -> List[Dict[str, float]]:
        terms: List[Dict[str, float]] = []
        first_term: bool = True
        index: int = 0
        equation_side_len: int = len(equation_side)
        while index < equation_side_len:
            print(f"Iteration: {equation_side[index:]}")
            if first_term and equation_side[index] not in ["+", "-"]:
                equation_side = "+" + equation_side
                first_term = False
            if equation_side[index] not in ["+", "-"]:
                Parser.parser_error(index, side, equation_side)
                raise SyntaxError("Error in your Equation Syntax")
            term, current_index = Parser.get_term(index + 1, equation_side, side)
            print(f"TERM: {term}")
            terms.append(term)
            index = current_index
        if len(terms) == 0:
            raise SyntaxError("Empty Side of The Equation")
        return terms
