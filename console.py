#!/usr/bin/python3
""" Holberton AirBnB Console """
import cmd
import sys
import json
import os
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ Class for the command interpreter HBNBCommand """
    prompt = '(hbnb) '

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.classes = storage.classes()

    def do_quit(self, arg):
        """ Exit method """
        exit()

    def emptyline(self):
        """ Method to pass when emptyline entered """
        pass

    def do_EOF(self, arg):
        """ Exit method for EOF """
        print('')
        exit()

    def do_create(self, arg):
        """ Create a new instance """
        if len(arg) == 0:
            print('** class name missing **')
            return
        new_model = None
        if arg:
            arg_list = arg.split()
            if len(arg_list) == 1:
                if arg in self.classes.keys():
                    new_model = self.classes[arg]()
                    new_model.save()
                    print(new_model.id)
                else:
                    print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance.
        """
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg.split()[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg.split()) > 1:
            key = arg.split()[0] + '.' + arg.split()[1]
            if key in storage.all():
                i = storage.all()
                print(i[key])
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        line = arg.split()
        try:
            obj = eval(line[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(line) == 1:
            print('** instance id missing **')
            return
        if len(line) > 1:
            key = line[0] + '.' + line[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print('** no instance found **')
                return

    def do_all(self, arg):
        """ Method to print all instances """
        if len(arg) == 0:
            print([str(obj) for obj in storage.all().values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for b, obj in storage.all().items() if arg in b])

    def do_update(self, arg):
        """ Updates an instance by adding or updating attribute"""
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
