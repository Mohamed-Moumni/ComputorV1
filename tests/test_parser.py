import pytest
from src.parser import Parser

"""
    This file contains test for Parser class
"""


class TestParser:
    def test_start_parse(self):
        parser = Parser("X^2 + 4")
        with pytest.raises(SyntaxError):
            parser.start()

    def test_start_parse(self):
        parser = Parser("2.0 * X^2 = 2 * X ^1 = 0")
        with pytest.raises(SyntaxError):
            parser.start()

    def test_remove_spaces(self):
        parser = Parser("2 * X^2 + 33 - 4 * X  = 0")
        parser.remove_spaces()
        assert parser.equation == "2*X^2+33-4*X=0"

        parser = Parser("2*X^2+33-4*X=0")
        parser.remove_spaces()
        assert parser.equation == "2*X^2+33-4*X=0"

        parser = Parser("2 * X ^ 2  + 3 * X ^ 1 + 20 = 0")
        parser.remove_spaces()
        assert parser.equation == "2*X^2+3*X^1+20=0"

    def test_get_X_term(self):
        parser = Parser("")
        assert parser.get_X_term(2, "2*X^4") == 4
        assert parser.get_X_term(0, "X^") == 2
        assert parser.get_X_term(2, "3*X^3") == 4

    def test_get_degree(self):
        parser = Parser("")
        assert parser.get_degree(0, "2hhhh") == (2, 1)
        assert parser.get_degree(4, "2*X^3") == (3, 5)
        with pytest.raises(SyntaxError):
            parser.get_degree(4, "2*X^4") == (3, 5)
        with pytest.raises(SyntaxError):
            parser.get_degree(4, "2*X^-3") == (3, 5)

    def test_start_1(self):
        parser = Parser("2 * X ^ 2 + 3 * X ^ 1 - 2 = 0")
        expected_terms = [
            {"coeff": 2.0, "degree": 2},
            {"coeff": 3.0, "degree": 1},
            {"coeff": 2.0, "degree": 0},
        ]
        terms = parser.start()
        assert terms == expected_terms
    
    # def test_start_2(self):
    #     parser = Parser("2 * X ^ 2 + 3 * X ^ 1 - 2 = 2 * X ^ 2 + 3.5 + 1 * X ^ 0")
    #     expected_terms = [
    #         {"coeff": 2.0, "degree": 2},
    #         {"coeff": 3.0, "degree": 1},
    #         {"coeff": 2.0, "degree": 0},
    #         {"coeff": 2.0, "degree": 2},
    #         {"coeff": 3.5, "degree": 0},
    #         {"coeff": 1.0, "degree": 0},
    #     ]
    #     terms = parser.start()
    #     print(f"Terms: {terms}")
    #     print(f"Expected Terms: {expected_terms}")
    #     assert terms == expected_terms
        
        
