#!/usr/bin/python3
"""test suite for the console/command_interpreter"""
import os
import unittest
from unittest.mock import patch
from io import StringIO
import console
from models.engine.file_storage import FileStorage
from models import storage
from console import HBNBCommand


class test_HBNBCommand(unittest.TestCase):
    """Test for console"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.consol = HBNBCommand()

    def tearDown(self):
        """Remove temporary file (file.json) created as a result"""
        FileStorage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_prompt(self):
        """test the prompt is correct"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_emptyline(self):
        """test empyt line input does not close interpreter"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual("", f.getvalue())

    def test_docstrings_in_console(self):
        """checking for docstrings"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)

    def test_help_help(self):
        """tests if the f of help command is correct"""
        line1 = "Documented commands (type help <topic>):"
        line2 = "========================================"
        line3 = "Amenity    City  Place   State  all    create   help  show"
        line4 = "BaseModel  EOF   Review  User   count  destroy  quit  update"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        line = f.getvalue()
        self.assertIn(line1, line)
        self.assertIn(line2, line)
        self.assertIn(line3, line)
        self.assertIn(line4, line)

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_create(self):
        """Test create with space notation"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            test_value = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            test_value = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            test_value = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            test_value = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            test_value = f.getvalue().strip()
        msg = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")

    def test_create_dot_notation(self):
        """Test create with dot notation"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create()")
            test_value = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.create()")
            test_value = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.create()")
            test_value = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.create()")
            test_value = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.create()")
            test_value = f.getvalue().strip()

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
        expected_output_1 = [
            "User", "123-4567-890", "name", "John Doe", "age", "100"
            ]

        expected_output_2 = [
            "Place", "321-7654-098", "lat", "22.0", "lon", "10.3"
            ]
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
        expected_output_1 = (
            "BaseModel.123-4567-890", [
                "BaseModel", "123-4567-890"
                ])
        expected_output_2 = (
            "User.456-7890-123", [
                "User", "456-7890-123"
                ])
        output_1 = HBNBCommand().handle_arg(str_1)
        output_2 = HBNBCommand().handle_arg(str_2)
        self.assertEqual(expected_output_1, output_1)
        self.assertEqual(expected_output_2, output_2)

    def test_handle_arg_using_three_or_more_word_input(self):
        """test to show what handle_arg returns with multiple words as
        input"""
        str_1 = 'User 123-4567-890 name "John Doe" age 100'
        str_2 = "Place 321-7654-098 lat 22.0 lon 10.3"
        expected_output_1 = (
            "User.123-4567-890", [
                "User", "123-4567-890", "name", "John Doe", "age", "100"
                ])
        expected_output_2 = (
            "Place.321-7654-098", [
                "Place", "321-7654-098", "lat", "22.0", "lon", "10.3"
                ])
        output_1 = HBNBCommand().handle_arg(str_1)
        output_2 = HBNBCommand().handle_arg(str_2)
        self.assertEqual(expected_output_1, output_1)
        self.assertEqual(expected_output_2, output_2)

    def test_show(self):
        """Test show with space notation"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            test_value = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            obj_test = storage.all()["BaseModel.{}".format(test_value)]
            command = "show BaseModel {}".format(test_value)
            HBNBCommand().onecmd(command)
            self.assertEqual(obj_test.__str__(), f.getvalue().strip())
        msg = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
        self.assertEqual(msg, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
        self.assertEqual(msg, f.getvalue().strip())

    def test_show_dot_notation(self):
        """Test show with dot notation"""
        msg = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show()")
        self.assertEqual(msg, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show()")
        self.assertEqual(msg, f.getvalue().strip())
        msg = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show(6767)")
        self.assertEqual(msg, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 35353")
        self.assertEqual(msg, f.getvalue().strip())
        msg = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show(4544)")
        self.assertEqual(msg, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show(5667)")
        self.assertEqual(msg, f.getvalue().strip())
        msg = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        self.assertEqual(msg, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        self.assertEqual(msg, f.getvalue().strip())

    def test_destroy(self):
        """Test destroy with space notation"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["BaseModel.{}".format(obj_id)]
            command = "destroy BaseModel {}".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["User.{}".format(obj_id)]
            command = "destroy User {}".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        msg = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(msg, f.getvalue().strip())
        msg = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual(msg, f.getvalue().strip())
        msg = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertEqual(msg, f.getvalue().strip())
        msg = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 1"))
            self.assertEqual(msg, f.getvalue().strip())

    def test_destroy_dot_notation(self):
        """Test destroy with dot notation"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["Review.{}".format(obj_id)]
            command = "Review.destroy({})".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        msg = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy(1)"))
            self.assertEqual(msg, f.getvalue().strip())

    def test_all(self):
        """Test all with space notation"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertIn("BaseModel", f.getvalue().strip())
            self.assertIn("User", f.getvalue().strip())
            self.assertIn("State", f.getvalue().strip())
            self.assertIn("Place", f.getvalue().strip())
            self.assertIn("City", f.getvalue().strip())
            self.assertIn("Amenity", f.getvalue().strip())
            self.assertIn("Review", f.getvalue().strip())
        msg = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all latitude"))
            self.assertEqual(msg, f.getvalue().strip())

    def all_dot_notation(self):
        """Test all with dot notation"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", f.getvalue().strip())
            self.assertNotIn("User", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertIn("User", f.getvalue().strip())
            self.assertNotIn("BaseModel", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
            self.assertIn("State", f.getvalue().strip())
            self.assertNotIn("BaseModel", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
            self.assertIn("City", f.getvalue().strip())
            self.assertNotIn("BaseModel", f.getvalue().strip())

    def test_update(self):
        """Test update with space notation"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            obj_id = f.getvalue().strip()
            testCmd = "update City {} attr_name 'attr_value'".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            test_dict = storage.all()["City.{}".format(obj_id)].__dict__
            self.assertEqual("attr_value", test_dict["attr_name"])
        msg = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(msg, f.getvalue().strip())
        msg = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            testCmd = "update BaseModel {} attr_name".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(msg, f.getvalue().strip())
        msg = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            obj_id = f.getvalue().strip()
            testCmd = "update Amenity {}".format(obj_id)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(msg, f.getvalue().strip())

    def test_update_dotnotation(self):
        """Test for the method updated with dot notation"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        testCmd = "BaseModel.update({}, attr_name, 'attr_value')".format(
            obj_id)
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        test_dict = storage.all()["BaseModel.{}".format(obj_id)].__dict__
        self.assertEqual("attr_value", test_dict["attr_name"])
        msg = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            obj_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            testCmd = "City.update({}, attr_name)".format(obj_id)
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(msg, f.getvalue().strip())
        msg = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            obj_id = f.getvalue().strip()
            testCmd = "BaseModel.update({})".format(obj_id)
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(testCmd))
            self.assertEqual(msg, f.getvalue().strip())

    def test_count(self):
        """Test for the method count"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertEqual("1", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertEqual("1", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertEqual("1", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertEqual("1", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertEqual("1", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertEqual("1", f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertEqual("1", f.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
