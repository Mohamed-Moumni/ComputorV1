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
