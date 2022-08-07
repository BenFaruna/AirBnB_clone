#!/usr/bin/python3
"""test suite for the console/command_interpreter"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class test_HBNBCommand(unittest.TestCase):
    """Test for console"""

    def setUp(self):
        """set up before starting every test case"""
        pass

    def tearDown(self):
        """tear down procedures after every test case"""
        pass

    def test_prompt(self):
        """test the prompt is correct"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_emptyline(self):
        """test empyt line input does not close interpreter"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual("", f.getvalue())

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_pattern_handling_using_one_word_input(self):
        """test to determine how the function handles patterns using one
        word"""
        str_1 = "BaseModel"
        str_2 = "User"
        expected_output_1 = ["BaseModel"]
        expected_output_2 = ["User"]
        output_1 = HBNBCommand().pattern_handling(str_1)
        output_2 = HBNBCommand().pattern_handling(str_2)
        self.assertEqual(expected_output_1, output_1)
        self.assertEqual(expected_output_2, output_2)

    def test_pattern_handling_using_two_word_input(self):
        """test to show what pattern_handling method returns with two word
        argument"""
        str_1 = "BaseModel 123-4567-890"
        str_2 = "User 456-7890-123"
        expected_output_1 = ["BaseModel", "123-4567-890"]
        expected_output_2 = ["User", "456-7890-123"]
        output_1 = HBNBCommand().pattern_handling(str_1)
        output_2 = HBNBCommand().pattern_handling(str_2)
        self.assertEqual(expected_output_1, output_1)
        self.assertEqual(expected_output_2, output_2)

    def test_pattern_handling_using_three_or_more_word_input(self):
        """test to show what pattern_handling returns with multiple words as
        input"""
        str_1 = 'User 123-4567-890 name "John Doe" age 100'
        str_2 = "Place 321-7654-098 lat 22.0 lon 10.3"
        expected_output_1 = ["User", "123-4567-890", "name", "John Doe", "age", "100"]
        expected_output_2 = ["Place", "321-7654-098", "lat", "22.0", "lon", "10.3"]
        output_1 = HBNBCommand().pattern_handling(str_1)
        output_2 = HBNBCommand().pattern_handling(str_2)
        self.assertEqual(expected_output_1, output_1)
        self.assertEqual(expected_output_2, output_2)

    def test_handle_arg_using_one_word_input(self):
        """test to determine how the function handles arguments using one
        word"""
        str_1 = "BaseModel"
        str_2 = "User"
        expected_output_1 = ("BaseModel", ["BaseModel"])
        expected_output_2 = ("User", ["User"])
        output_1 = HBNBCommand().handle_arg(str_1)
        output_2 = HBNBCommand().handle_arg(str_2)
        self.assertEqual(expected_output_1, output_1)
        self.assertEqual(expected_output_2, output_2)

    def test_handle_arg_using_two_word_input(self):
        """test to show what handle arg method returns"""
        str_1 = "BaseModel 123-4567-890"
        str_2 = "User 456-7890-123"
        expected_output_1 = ("BaseModel.123-4567-890",
        ["BaseModel", "123-4567-890"])
        expected_output_2 = ("User.456-7890-123",
        ["User", "456-7890-123"])
        output_1 = HBNBCommand().handle_arg(str_1)
        output_2 = HBNBCommand().handle_arg(str_2)
        self.assertEqual(expected_output_1, output_1)
        self.assertEqual(expected_output_2, output_2)

    def test_handle_arg_using_three_or_more_word_input(self):
        """test to show what handle_arg returns with multiple words as
        input"""
        str_1 = 'User 123-4567-890 name "John Doe" age 100'
        str_2 = "Place 321-7654-098 lat 22.0 lon 10.3"
        expected_output_1 = ("User.123-4567-890",
        ["User", "123-4567-890", "name", "John Doe", "age", "100"])
        expected_output_2 = ("Place.321-7654-098",
        ["Place", "321-7654-098", "lat", "22.0", "lon", "10.3"])
        output_1 = HBNBCommand().handle_arg(str_1)
        output_2 = HBNBCommand().handle_arg(str_2)
        self.assertEqual(expected_output_1, output_1)
        self.assertEqual(expected_output_2, output_2)


if __name__ == "__main__":
    unittest.main()
