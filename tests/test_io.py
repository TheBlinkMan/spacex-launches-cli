import unittest
from unittest.mock import MagicMock, patch, call
from output_interface import PythonSimpleIO

class PythonSimpleIOTest(unittest.TestCase):

    def test_input_with_valid_input(self):
        expected = "1"
        io = PythonSimpleIO()
        with patch("builtins.input", return_value="1"):
            result = io.input("digite o valor")
            self.assertEqual(expected, result)

    def test_should_exit_when_ctrl_d_is_pressed(self):
        io = PythonSimpleIO()
        with patch("builtins.input", side_effect=EOFError()):
            with self.assertRaises(SystemExit):
                io.input("digite o valor")

    def test_should_exit_when_ctrl_c_is_pressed(self):
        io = PythonSimpleIO()
        with patch("builtins.input", side_effect=KeyboardInterrupt()):
            with self.assertRaises(SystemExit):
                io.input("digite o valor")