import pytest
from src.equation import Equation

"""
    This file contains test for equation class
    
    Test one Degree equation examples:
    - x^1 + 1 = 0 -> -1
    - -1/2x^1 + 4  = 0 -> 8
    - 5x^1 = 0 -> every element in |R
    - -5x^1 - 5 = 0 -> -1
    - 2x^1 - 55 = 0 -> 55 / 2
"""


class TestEquation:
    def test_solve_one_degree_equation_equation1(self):
        _degree = 1
        _terms = [{"coeff": 1.0, "degree": 1}, {"coeff": 1.0, "degree": 0}]
        _equation = Equation(_degree, _terms)
        _solution = _equation.solve_one_degree_equation()
        assert _solution['solution'] == (-1.0)

    def test_solve_one_degree_equation_equation2(self):
        _degree = 1
        _terms = [{"coeff": 0.5, "degree": 1}, {"coeff": 4.0, "degree": 0}]
        _equation = Equation(_degree, _terms)
        _solution = _equation.solve_one_degree_equation()
        assert _solution['solution'] == (-8.0)


    def test_solve_one_degree_equation_equation3(self):
        _degree = 1
        _terms = [{"coeff": 5.0, "degree": 1}]
        _equation = Equation(_degree, _terms)
        _solution = _equation.solve_one_degree_equation()
        assert _solution['solution'] == ()

    def test_solve_one_degree_equation_equation4(self):
        _degree = 1
        _terms = [{"coeff": -5.0, "degree": 1}, {"coeff": -5.0, "degree": 0}]
        _equation = Equation(_degree, _terms)
        _solution = _equation.solve_one_degree_equation()
        assert _solution['solution'] == (-1.0)

    def test_solve_one_degree_equation_equation5(self):
        _degree = 1
        _terms = [{"coeff": 2.0, "degree": 1}, {"coeff": -55.0, "degree": 0}]
        _equation = Equation(_degree, _terms)
        _solution = _equation.solve_one_degree_equation()
        assert _solution['solution'] == (
            round(55.0/2.0, 2))
