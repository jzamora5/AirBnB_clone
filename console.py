#!/usr/bin/env python3


""" AirBnB Console """

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def precmd(self, line):
        if '.' in line:
            line = line.replace('.', ' ').replace('(', ' ').replace(')', ' ')
            cmd_argv = line.split()
            cmd_argv[0], cmd_argv[1] = cmd_argv[1], cmd_argv[0]
            line = " ".join(cmd_argv)
        return cmd.Cmd.precmd(self, line)

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def do_create(self, arg):
        "Create an instance if the Model exists"
        if not arg:
            print("** class name missing **")
            return None
        try:
            my_model = eval(arg + "()")
            my_model.save()
            print(my_model.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, arg):
        "Print dict of a instance in base of it's ID"
        cmd_argv = arg.split()
        if not cmd_argv:
            print("** class name missing **")
            return None
        try:
            eval(cmd_argv[0])
        except:
            print("** class doesn't exist **")
            return None

        all_objs = storage.all()

        if len(cmd_argv) < 2:
                print("** instance id missing **")
                return None

        key = cmd_argv[0] + '.' + cmd_argv[1]

        if all_objs.get(key, False):
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_all(self, arg):
        "Print all the instances saved in file.json"
        cmd_argv = arg.split()

        if cmd_argv:
            try:
                eval(cmd_argv[0])
            except:
                print("** class doesn't exist **")
                return None

        all_objs = storage.all()

        for key, value in all_objs.items():
            if not cmd_argv:
                print(value)
            else:
                check = key.split('.')
                if cmd_argv[0] == check[0]:
                    print(value)

    def do_destroy(self, arg):
        "Deletes an instance based on it's ID and save the changes\n \
        Usage: destroy <class name> <id>"

        cmd_argv = arg.split()
        if not cmd_argv:
            print("** class name missing **")
            return None
        try:
            eval(cmd_argv[0])
        except:
            print("** class doesn't exist **")
            return None

        all_objs = storage.all()

        if len(cmd_argv) < 2:
                print("** instance id missing **")
                return None

        key = cmd_argv[0] + '.' + cmd_argv[1]

        if all_objs.get(key, False):
            all_objs.pop(key)
            storage.save()
        else:
            print("** no instance found **")


    def do_update(self, arg):
        "Usage: update <class name> <id> <attribute name> \"<attribute value>\""
        if "\"" in arg:
            quote_argv = arg.split("\"")
            cmd_argv = quote_argv[0].split()
            cmd_argv.append("")
            value = quote_argv[1]
        else:
            cmd_argv = arg.split()
            if len(cmd_argv) >= 4:
                value = cmd_argv[3]

        all_objs = storage.all()
        if (len(cmd_argv) == 0):
            print("** class name missing **")
            return None

        try:
            eval(cmd_argv[0])
        except:
            print("** class doesn't exist **")
            return None

        if len(cmd_argv) < 2:
            print("** instance id missing **")
            return None

        key = cmd_argv[0] + '.' + cmd_argv[1]

        all_objs = storage.all()

        key = cmd_argv[0] + '.' + cmd_argv[1]

        if all_objs.get(key, False):
            if (len(cmd_argv) >= 3):
                if len(cmd_argv) >= 4:
                    attr = cmd_argv[2]
                    type_att = getattr(all_objs[key], cmd_argv[2], "")
                    cast_val = type(type_att)(value)
                    setattr(all_objs[key], cmd_argv[2], cast_val);
                else:
                    print("** value missing **")
            else:
                print("** attribute name missing **")
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
