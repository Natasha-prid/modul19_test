import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 3, 3) == 9

    def test_division_correctly(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction_correctly(self):
        assert self.calc.subtraction(self, 100, 10) == 90

    def test_adding_correctly(self):
        assert self.calc.adding(self, 10, 10) == 20
