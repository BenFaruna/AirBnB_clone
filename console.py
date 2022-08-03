#!/usr/bin/python3
"""module that contains entry point to the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        return False

if __name__ == "__main__":
    HBNBCommand().cmdloop()