#!/usr/bin/python3
""" Command interpreter for the HBNB project """


import cmd


class HBNBCommand(cmd.Cmd):
    """ Console class """
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program """
        return True

    def emptyline(self):
        """ Empty line """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
