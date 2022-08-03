#!/usr/bin/python3
"""test suite for the console/command_interpreter"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand



class test_HBNBCommand(unittest.TestCase):
    """Test for console"""

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
