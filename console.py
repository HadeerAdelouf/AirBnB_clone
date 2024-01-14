#!/usr/bin/python3
"""
Module for the entry point of the command interpreter
Defines the HBnB console
"""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json
import sys
from shlex import split


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter."""

    prompt = "(hbnb) "
    classes = {'BaseModel': BaseModel}

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

    def do_show(self, arg):
        """
        Display the string repr of a class instance of a given id.
        """
        argss = arg.split(' ')
        if arg == "" or arg is None:
            print("** class name missing **")
            if argss[0] not in storage.classes():
                print("** class doesn't exist **")

            elif len(argss) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(argss[0], argss[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Delete instance based on the class name and id
        """
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            argss = arg.split(' ')
            if argss[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(argss) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(argss[0], argss[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, arg):
        """
        Display string representations of all instances of
        a given class
        """
        if arg != "":
            argument = arg.split(' ')
            if argument[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                form = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == argument[0]]
                print(form)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_update(self, arg):
        """
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary
        """
        arg = arg.split()
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print('** instance id missing **')
            return
        else:
            key = arg[0] + '.' + arg[1]
            if key in storage.all():
                if len(arg) > 2:
                    if len(arg) == 3:
                        print('** value missing **')
                    else:
                        setattr(
                            storage.all()[key],
                            arg[2],
                            arg[3][1:-1])
                        storage.all()[key].save()
                else:
                    print('** attribute name missing **')
            else:
                print('** no instance found **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
