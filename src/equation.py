from typing import List, Dict, Any


class Equation:
    """
        Equation Solution class contains the methods and the logic for solving the 1,2,3 degree equation
    """

    def __init__(self, _degree: int, _terms: List[Dict[str, float]]):
        self.degree = _degree
        self.terms = _terms

    def solve_one_degree_equation(self) -> Any:
        sorted_terms = sorted(self.terms, key=lambda x: x['degree'])
        if len(sorted_terms) == 1:
            return dict(sentence="All real numbers in are solution of this equation", solution=())
        else:
            _solution = round(
                (-self.terms[1]['coeff']) / self.terms[0]['coeff'], 2)
            return dict(sentence="The solution is", solution=(_solution))

    def solve_two_degree_equation(self):
        pass

    def solve_three_degree_equation(self):
        pass

    def solve_less_than_zero_degree_equation(self):
        pass
