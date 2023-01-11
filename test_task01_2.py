

import unittest
from unittest import TestCase
from random import randint
from task01_2 import *


class TestFunc(TestCase):
    def setUp(self):
        self.wage = randint(50, 150) * 10 ** 3
        self.bonus = randint(self.wage // 4, self.wage // 2)

    def test_fullname(self):
        self.assertEqual(Position('Kevin', 'Brown', 'Agent K', self.wage, self.bonus).get_full_name(), 'Kevin Brown')

    def test_total_income(self):
        self.assertEqual(Position('Kevin', 'Brown', 'Agent K', self.wage, self.bonus).get_total_income(),
                         self.wage + self.bonus)

    def test_name(self):
        with self.assertRaises(TypeError):
            Position(1, 'Brown', 'Agent K', self.wage, self.bonus)
            Position('Kevin', 1, 'Agent K', self.wage, self.bonus)

        with self.assertRaises(ValueError):
            Position('kevin', 'Brown', 'Agent K', self.wage, self.bonus)
            Position('Kevin', 'brown', 'Agent K', self.wage, self.bonus)

    def test_income(self):
        with self.assertRaises(TypeError):
            Position('Kevin', 'Brown', 'Agent K', str(self.wage), self.bonus)
            Position('Kevin', 'Brown', 'Agent K', self.wage, str(self.bonus))

        with self.assertRaises(ValueError):
            Position('Kevin', 'Brown', 'Agent K', -self.wage, self.bonus)
            Position('Kevin', 'Brown', 'Agent K', self.wage, -self.bonus)

    def test_instance(self):
        self.assertIsInstance(Position('Kevin', 'Brown', 'Agent K', self.wage, self.bonus), Worker)

    def test_is(self):
        self.assertIsNot(Position('Kevin', 'Brown', 'Agent K', self.wage, self.bonus),
                         Position('James Darrell', 'Edwards', 'Agent J', self.wage, 0))

if __name__ == '__main__':
    unittest.main()