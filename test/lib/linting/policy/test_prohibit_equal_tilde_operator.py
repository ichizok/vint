import unittest
from test.asserting.policy import PolicyAssertion
from test.asserting.policy import get_fixture_path

from lib.linting.level import Levels
from lib.linting.policy.prohibit_equal_tilde_operator import ProhibitEqualTildeOperator

PATH_VALID_VIM_SCRIPT = get_fixture_path('prohibit_equal_tilde_operator_valid.vim')
PATH_INVALID_VIM_SCRIPT = get_fixture_path('prohibit_equal_tilde_operator_invalid.vim')


class TestProhibitEqualTildeOperator(PolicyAssertion, unittest.TestCase):
    def test_get_violation_if_found(self):
        # Expect no violations found
        self.assertFoundViolationsEqual(PATH_VALID_VIM_SCRIPT, ProhibitEqualTildeOperator, [])

        expected_violations = [
            {
                'name': 'ProhibitEqualTildeOperator',
                'level': Levels['WARNING'],
                'position': {
                    'line': 2,
                    'column': 12,
                    'path': PATH_INVALID_VIM_SCRIPT
                },
            },
            {
                'name': 'ProhibitEqualTildeOperator',
                'level': Levels['WARNING'],
                'position': {
                    'line': 3,
                    'column': 12,
                    'path': PATH_INVALID_VIM_SCRIPT
                },
            },
            {
                'name': 'ProhibitEqualTildeOperator',
                'level': Levels['WARNING'],
                'position': {
                    'line': 4,
                    'column': 12,
                    'path': PATH_INVALID_VIM_SCRIPT
                },
            },
            {
                'name': 'ProhibitEqualTildeOperator',
                'level': Levels['WARNING'],
                'position': {
                    'line': 5,
                    'column': 12,
                    'path': PATH_INVALID_VIM_SCRIPT
                },
            },
            {
                'name': 'ProhibitEqualTildeOperator',
                'level': Levels['WARNING'],
                'position': {
                    'line': 6,
                    'column': 12,
                    'path': PATH_INVALID_VIM_SCRIPT
                },
            },
            {
                'name': 'ProhibitEqualTildeOperator',
                'level': Levels['WARNING'],
                'position': {
                    'line': 7,
                    'column': 12,
                    'path': PATH_INVALID_VIM_SCRIPT
                },
            },
            {
                'name': 'ProhibitEqualTildeOperator',
                'level': Levels['WARNING'],
                'position': {
                    'line': 8,
                    'column': 12,
                    'path': PATH_INVALID_VIM_SCRIPT
                },
            },
            {
                'name': 'ProhibitEqualTildeOperator',
                'level': Levels['WARNING'],
                'position': {
                    'line': 9,
                    'column': 12,
                    'path': PATH_INVALID_VIM_SCRIPT
                },
            },
            {
                'name': 'ProhibitEqualTildeOperator',
                'level': Levels['WARNING'],
                'position': {
                    'line': 10,
                    'column': 12,
                    'path': PATH_INVALID_VIM_SCRIPT
                },
            },
            {
                'name': 'ProhibitEqualTildeOperator',
                'level': Levels['WARNING'],
                'position': {
                    'line': 11,
                    'column': 12,
                    'path': PATH_INVALID_VIM_SCRIPT
                },
            },
            {
                'name': 'ProhibitEqualTildeOperator',
                'level': Levels['WARNING'],
                'position': {
                    'line': 15,
                    'column': 8,
                    'path': PATH_INVALID_VIM_SCRIPT
                },
            },
            {
                'name': 'ProhibitEqualTildeOperator',
                'level': Levels['WARNING'],
                'position': {
                    'line': 16,
                    'column': 8,
                    'path': PATH_INVALID_VIM_SCRIPT
                },
            },
            {
                'name': 'ProhibitEqualTildeOperator',
                'level': Levels['WARNING'],
                'position': {
                    'line': 17,
                    'column': 8,
                    'path': PATH_INVALID_VIM_SCRIPT
                },
            },
            {
                'name': 'ProhibitEqualTildeOperator',
                'level': Levels['WARNING'],
                'position': {
                    'line': 18,
                    'column': 8,
                    'path': PATH_INVALID_VIM_SCRIPT
                },
            },
            {
                'name': 'ProhibitEqualTildeOperator',
                'level': Levels['WARNING'],
                'position': {
                    'line': 19,
                    'column': 8,
                    'path': PATH_INVALID_VIM_SCRIPT
                },
            },
            {
                'name': 'ProhibitEqualTildeOperator',
                'level': Levels['WARNING'],
                'position': {
                    'line': 20,
                    'column': 8,
                    'path': PATH_INVALID_VIM_SCRIPT
                },
            },
            {
                'name': 'ProhibitEqualTildeOperator',
                'level': Levels['WARNING'],
                'position': {
                    'line': 21,
                    'column': 8,
                    'path': PATH_INVALID_VIM_SCRIPT
                },
            },
            {
                'name': 'ProhibitEqualTildeOperator',
                'level': Levels['WARNING'],
                'position': {
                    'line': 22,
                    'column': 8,
                    'path': PATH_INVALID_VIM_SCRIPT
                },
            },
            {
                'name': 'ProhibitEqualTildeOperator',
                'level': Levels['WARNING'],
                'position': {
                    'line': 23,
                    'column': 8,
                    'path': PATH_INVALID_VIM_SCRIPT
                },
            },
            {
                'name': 'ProhibitEqualTildeOperator',
                'level': Levels['WARNING'],
                'position': {
                    'line': 24,
                    'column': 8,
                    'path': PATH_INVALID_VIM_SCRIPT
                },
            },
        ]

        self.assertFoundViolationsEqual(PATH_INVALID_VIM_SCRIPT, ProhibitEqualTildeOperator, expected_violations)

if __name__ == '__main__':
    unittest.main()
