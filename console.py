#!/usr/bin/python3
""" Holberton AirBnB Console """
import cmd
import sys
import json
import re
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City


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
        """
        Print the string representation of all instances or a specific class.
        """
        if arg != "":
            argss = arg.split(' ')
            if argss[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == argss[0]]
                print(nl)
        else:
            new_obj = [str(obj) for key, obj in storage.all().items()]
            print(new_obj)

    def do_update(self, arg):
        """Updates an instance by adding or updating attribute.
        """
        if arg == "" or arg is None:
            print("** class name missing **")
            return

        regex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(regex, arg)
        classname, uid, attribute, value = match.groups()
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
                attr = storage.attributes()[classname]
                if attribute in attr:
                    value = attr[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_count(self, line):
        """Print the count all class instances"""
        kclass = globals().get(line, None)
        if kclass is None:
            print("** class doesn't exist **")
            return
        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == line:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
