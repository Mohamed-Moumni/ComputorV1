import pytest
from src.utils import sqrt
from src.equation import Equation

"""
    This file contains test for equation class
    
    Test one Degree equation examples:
    - x^1 + 1 = 0 -> -1
    - -1/2x^1 + 4  = 0 -> 8
    - 5x^1 = 0 -> every element in |R
    - -5x^1 - 5 = 0 -> -1
    - 2x^1 - 55 = 0 -> 55 / 2
    Test two Degree equation examples:
    - 2x^2 + 3x^1 + 2 = 0
    - x^2 + 2x^1 + 1 = 0
    - x^2 - x^1 + 2 = 0
    - x^2 - 2 = 0
    - 4x^2 - 4 = 0
    - 4x^2 + 16x^1 = 0
    - 2x^2 + x^1 = 0
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

    # - 2x^2 + 3x^1 + 2 = 0
    # - x^2 + 2x^1 + 1 = 0
    # - x^2 - x^1 + 2 = 0
    # - x^2 - 2 = 0
    # - 4x^2 - 4 = 0
    # - 4x^2 + 16x^1 = 0
    # - x^2 −4x^1 + 4=0

    def test_solve_two_degree_equation_equation1(self):
        _degree = 2
        _terms = [{"coeff": 2.0, "degree": 2}, {
            "coeff": 3.0, "degree": 1}, {"coeff": 2.0, "degree": 0}]
        _equation = Equation(_degree, _terms)
        _solution = _equation.solve_two_degree_equation()
        _correct_solution = [{'real': -0.75, 'imaginary': round(sqrt(7.0)/4, 2)}, {
            'real': -0.75, 'imaginary': -round(sqrt(7.0)/4, 2)}]
        assert _solution['type'] == "complex"
        assert sorted(_correct_solution, key=lambda x:x['real']) == sorted(_solution['solution'], key=lambda x:x['real'])

    def test_solve_two_degree_equation_equation2(self):
        _degree = 2
        _terms = [{"coeff": 1.0, "degree": 2}, {
            "coeff": 2.0, "degree": 1}, {"coeff": 1.0, "degree": 0}]
        _equation = Equation(_degree, _terms)
        _solution = _equation.solve_two_degree_equation()
        assert _solution['type'] == "real"
        assert _solution['solution'] == -1.0

    def test_solve_two_degree_equation_equation3(self):
        _degree = 2
        _terms = [{"coeff": 1.0, "degree": 2}, {
            "coeff": -1.0, "degree": 1}, {"coeff": 2.0, "degree": 0}]
        _equation = Equation(_degree, _terms)
        _solution = _equation.solve_two_degree_equation()
        _correct_solution = [{'real': 0.5, 'imaginary': round(sqrt(7)/2, 2)}, {
            'real': 0.5, 'imaginary': -round(sqrt(7)/2, 2)}]
        assert _solution['type'] == "complex"
        assert sorted(_correct_solution, key=lambda x: x['real']) == sorted(
            _solution['solution'], key=lambda x: x['real'])

    def test_solve_two_degree_equation_equation4(self):
        _degree = 2
        _terms = [{"coeff": 1.0, "degree": 2}, {
            "coeff": 0.0, "degree": 1}, {"coeff": -2.0, "degree": 0}]
        _equation = Equation(_degree, _terms)
        _solution = _equation.solve_two_degree_equation()
        assert _solution['type'] == "real"
        assert sorted(_solution['solution']) == [-round(sqrt(2.0),2), round(sqrt(2.0),2)]

    def test_solve_two_degree_equation_equation5(self):
        _degree = 2
        _terms = [{"coeff": 4.0, "degree": 2}, {
            "coeff": 0.0, "degree": 1}, {"coeff": -4.0, "degree": 0}]
        _equation = Equation(_degree, _terms)
        _solution = _equation.solve_two_degree_equation()
        assert _solution['type'] == "real"
        assert sorted(_solution['solution']) == [-1.0, 1.0]

    def test_solve_two_degree_equation_equation6(self):
        _degree = 2
        _terms = [{"coeff": 4.0, "degree": 2}, {
            "coeff": 16.0, "degree": 1}, {"coeff": 0.0, "degree": 0}]
        _equation = Equation(_degree, _terms)
        _solution = _equation.solve_two_degree_equation()
        assert _solution['type'] == "real"
        assert sorted(_solution['solution']) == [-4.0, 0.0]

    def test_solve_two_degree_equation_equation7(self):
        _degree = 2
        _terms = [{"coeff": 1.0, "degree": 2}, {
            "coeff": -4.0, "degree": 1}, {"coeff": 4.0, "degree": 0}]
        _equation = Equation(_degree, _terms)
        _solution = _equation.solve_two_degree_equation()
        assert _solution['type'] == "real"
        assert _solution['solution'] == 2.0
