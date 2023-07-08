#!/usr/bin/python3
""" Command interpreter for the HBNB project """


import cmd
import sys


from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Console class """
    if sys.stdin and sys.stdin.isatty():
        prompt = '(hbnb) '
    else:
        prompt = '(hbnb) \n'

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
