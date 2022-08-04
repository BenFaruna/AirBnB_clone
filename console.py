#!/usr/bin/python3
"""module that contains entry point to the command interpreter"""
import cmd
from hashlib import new

import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    @staticmethod
    def handle_arg(arg):
        """return key and other arguments"""
        new_arg = arg.split(" ")
        if len(new_arg) > 1:
            key = "{}.{}".format(new_arg[0], new_arg[1])
            return key, new_arg
        else:
            return new_arg[0], new_arg

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        return False

    def do_create(self, arg):
        """creates a new instance of BaseModel, saves it to
        json file and prints its id"""

        if arg:
            try:
                cls = models.classes[arg]
                new = cls()
                models.storage.save()
                print("{}".format(new.id))
            except (KeyError):
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """prints the string representation of an instance based on the
        class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
        else:
            key, new_arg = self.handle_arg(arg)
            try:
                models.classes[new_arg[0]]
            except (KeyError):
                print("** class doesn't exist **")
                return

            if len(new_arg) == 1:
                print("** instance id missing **")
            else:
                try:
                    model = models.storage.all()[key]
                    print(model)
                except (KeyError):
                    print("** no instance found **")

    def do_destroy(self, arg):
        """deletes an instance based on the class name and id and save
        changes to file"""
        if len(arg) == 0:
            print("** class name missing **")
        else:
            key, new_arg = self.handle_arg(arg)
            if not models.classes.get(new_arg[0], False):
                print("** class doesn't exist **")
            else:
                if len(new_arg) == 1:
                    print("** instance id missing **")
                    return

                try:
                    models.storage.all().pop(key)
                    models.storage.save()
                except (KeyError):
                    print("** no instance found **")

    def do_all(self, arg):
        """prints all string representation of all instances based
        or not on the class name"""
        if len(arg) == 0:
            for model in models.storage.all():
                print(models.storage.all()[model])
        else:
            key, new_arg = self.handle_arg(arg)
            if not models.classes.get(new_arg[0], False):
                print("** class doesn't exist **")
            else:
                for model in models.storage.all():
                    if model.split(".")[0] == new_arg[0]:
                        print(models.storage.all()[model])

    def do_update(self, arg):
        """updates an instance based on the class name and id by adding
        or updating attribute"""
        if len(arg) == 0:
            print("** class name is missing **")
        else:
            key, new_arg = self.handle_arg(arg)
            if not models.classes.get(new_arg[0], False):
                print("** class doesn't exist **")
                return
            else:
                if len(new_arg) >= 2:
                    if len(new_arg) == 2:
                        print("** attribute name missing **")
                        return

                    elif len(new_arg) % 2 == 1:
                        print("** value missing **")
                        return
                    else:
                        attr = new_arg[2::2]
                        value = new_arg[3::2]
                        try:
                            model_dict = models.storage.all().get(key)
                            model = models.classes.get(new_arg[0])
                            model = (model_dict)
                            for i in range(len(attr)):
                                setattr(model, attr[i], value[i])
                            model.save()
                        except (KeyError):
                            print("** no instance found **")
                            return


            if len(new_arg) == 1:
                print("** instance id missing **")
                return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
