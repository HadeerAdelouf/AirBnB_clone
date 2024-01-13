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
from shlex import split


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter."""

    prompt = "(hbnb) "

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
        elif arg not in storage.__classes():
            print("** class doesn't exist **")
        else:
            new_inst = storage.__classes()[arg]()
            new_inst.save()
            print(new_inst.id)

    def do_show(self, arg):
        """
        Display the string repr of a class instance of a given id.
        """
        argss = arg.split(' ')
        if arg == "" or arg is None:
            print("** class name missing **")
            if argss[0] not in storage.__classes():
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
            if argss[0] not in storage._classes():
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
            if argument[0] not in storage.__classes():
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
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False
            
    def do_update(self, line):
        """Updates an instance by adding or updating attribute.
        """
        if line == "" or line is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass  # fine, stay a string then
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
