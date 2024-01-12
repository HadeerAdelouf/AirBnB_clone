#!/usr/bin/python3
"""
Module for the entry point of the command interpreter
Defines the HBnB console
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter."""

    def do_EOF(self, line):
        """Ctrl+D signal to exit the program"""
        print()
        return True

    def do_quit(self, line):
        """Exits the program"""
        return True

    def emptyline(self):
        """
        Do nothing
        """
        pass
    
    def do_create(self, arg):
        """
        Creates an instance &  saves it in JSON file and prints the id
        """
        if not arg: 
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            new_inst = storage.classes()[arg]()
            new_inst.save()
            print(new_inst.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
