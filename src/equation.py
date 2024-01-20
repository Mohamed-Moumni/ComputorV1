from typing import List, Dict, Any
from .utils import sqrt, power_two


class Equation:
    """
        Equation Solution class contains the methods and the logic for solving the 1,2,3 degree equation
    """

    def __init__(self, _degree: int, _terms: List[Dict[str, float]]):
        self.degree = _degree
        self.terms = sorted(_terms, key=lambda x: x['degree'])

    def solve_one_degree_equation(self) -> Any:
        if len(self.terms) == 1:
            return dict(sentence="All real numbers are solution for this equation", solution=())
        else:
            _solution = round(
                (-self.terms[0]['coeff']) / self.terms[1]['coeff'], 2)
            return dict(sentence="The solution is", solution=(_solution))

    def solve_two_degree_equation(self):
        discriminant: float = power_two(
            self.terms[1]['coeff']) - (4.0 * self.terms[0]['coeff'] * self.terms[2]['coeff'])
        print("Discriminant:", discriminant)
        if discriminant == 0:
            return self.neutral_discriminant()
        elif discriminant > 0:
            return self.positive_discriminant(discriminant)
        else:
            return self.negative_discriminant(discriminant)

    def solve_three_degree_equation(self):
        pass

    def neutral_discriminant(self):
        _solution = round(-self.terms[1]['coeff'] /
                          (2 * self.terms[2]['coeff']), 2)
        return dict(sentence="Discriminant is zero, the only solution is:", type="real", solution=(_solution))

    def positive_discriminant(self, _discriminant):
        _solution1 = round(
            (-self.terms[1]['coeff'] + sqrt(_discriminant)) / (2 * self.terms[2]['coeff']), 2)
        _solution2 = round(
            (-self.terms[1]['coeff'] - sqrt(_discriminant)) / (2 * self.terms[2]['coeff']), 2)
        return dict(sentence="Discriminant is strictly positive, the two solutions are: ",
                    type="real", solution=(_solution1, _solution2))

    def negative_discriminant(self, _discriminant):
        _solution1 = {"real": round(
            (-self.terms[1]['coeff']) / (2 * self.terms[2]['coeff']), 2),
            "imaginary": round((sqrt(-_discriminant)) / (2 * self.terms[2]['coeff']), 2)}
        _solution2 = {"real": round(
            (-self.terms[1]['coeff']) / (2 * self.terms[2]['coeff']), 2),
            "imaginary": -round((sqrt(-_discriminant)) / (2 * self.terms[2]['coeff']), 2)}
        return dict(sentence="Discriminant is strictly negative, the two solutions are: ",
                    type="complex", solution=(_solution1, _solution2))
