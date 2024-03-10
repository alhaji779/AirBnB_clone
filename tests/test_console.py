#!/usr/bin/python3
import unittest
import os
import tests
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test for the console file"""

    @classmethod
    def setUpClass(cls):
        """method to setup console class"""
        cls.console = HBNBCommand()

    @classmethod
    def teardown(cls):
        """method to tear down console class"""
        del cls.console

    def test_docstrings_in_console(self):
        """test for docstring exist in all funcs in console file"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)


if __name__ == '__main__':
    unittest.main()
