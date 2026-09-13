#!/usr/bin/env python3
"""Tests for the Sum Equation assignment."""

import re
import unittest

import numpy as np

from src.sum_equation import sum_equation


class TestSumEquation(unittest.TestCase):
    """sum_equation(L) -> a string "a + b + ... = total" for a list L."""

    def test_worked_example(self):
        L = [1, 5, 7]
        result = sum_equation(L)
        self.assertIsInstance(
            result,
            str,
            msg="sum_equation should return a string. Got %s."
            % (type(result),),
        )
        self.assertEqual(
            result,
            "1 + 5 + 7 = 13",
            msg="Incorrect result for input list %r! Expected "
            "'1 + 5 + 7 = 13'." % (L,),
        )

    def test_random_lists_match_their_own_sum(self):
        L = list(np.random.randint(1, 100, 50))
        result = sum_equation(L)
        self.assertIsInstance(
            result,
            str,
            msg="sum_equation should return a string. Got %s."
            % (type(result),),
        )
        m = re.match(r"(.*) = (\d+)", result)
        self.assertTrue(
            m,
            msg="Result %r did not match the expected 'a + b + ... = total' "
            "shape." % (result,),
        )
        s = int(m.group(2))
        self.assertEqual(
            s,
            sum(L),
            msg="The total on the right of '=' should equal sum(%r) = %d, "
            "got %d." % (L, sum(L), s),
        )
        a = m.group(1)
        L2 = list(map(int, a.split('+')))
        self.assertEqual(
            L,
            L2,
            msg="The numbers to the left of '=' should be exactly %r in "
            "order, got %r." % (L, L2),
        )

    def test_empty_list_gives_zero_equals_zero(self):
        result = sum_equation([])
        self.assertIsInstance(
            result,
            str,
            msg="sum_equation should return a string. Got %s."
            % (type(result),),
        )
        self.assertEqual(
            result,
            "0 = 0",
            msg="Incorrect result for an empty input list!",
        )

    def test_single_element_list(self):
        result = sum_equation([9])
        self.assertEqual(
            result,
            "9 = 9",
            msg="sum_equation([9]) should be '9 = 9': with only one number, "
            "there is nothing to add and the total equals it.",
        )


if __name__ == '__main__':
    unittest.main()
