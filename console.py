#!/usr/bin/python3
""" Command interpreter for the HBNB project """
import cmd
import sys

from models import storage

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


classes = { 'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Place': Place,
            'Amenity': Amenity,
            'Review': Review }


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

    def do_create(self, arg):
        """Create command to create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in classes:
            print("** class doesn't exist **")
            return
        class_obj = classes[arg]
        new_instance = class_obj()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """ Show command to print the string representation of an instance
            based on the class name and id """
        if not arg:
            print("** class name missing **")
            return
        """ Divides the string (arguments) into a list of strings """
        arg_list = arg.split()
        if arg_list[0] not in classes:
            """ Check if the class name is valid  """
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            """ Check if the id is valid """
            print("** instance id missing **")
            return
        """ Key to access the dictionary """
        key = arg_list[0] + "." + arg_list[1]
        if key not in storage.all():
            """ Check if the key exists """
            print("** no instance found **")
            return
        print(storage.all()[key])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
