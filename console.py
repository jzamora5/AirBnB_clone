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
import sys


class HBNBCommand(cmd.Cmd):
    """ Class HBNB to read command """
    prompt = '(hbnb) '
    __all_117 = 0

    def emptyline(self):
        """Pass if no command is given"""
        pass

    def precmd(self, line):
        """ Edit given command to allow second type of input"""
        if not sys.stdin.isatty():
            print()
        if '.' in line:
            HBNBCommand.__all_117 = 1
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
        print()
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

        cmd_argv[1] = cmd_argv[1].replace("\"", "")
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
        print_list = []
        len_objs = len(all_objs)
        for key, value in all_objs.items():
            if not cmd_argv:
                if HBNBCommand.__all_117 == 0:
                    print_list.append("\"" + str(value) + "\"")
                else:
                    print_list.append(str(value))
            else:
                check = key.split('.')
                if cmd_argv[0] == check[0]:
                    if HBNBCommand.__all_117 == 0:
                        print_list.append("\"" + str(value) + "\"")
                    else:
                        print_list.append(str(value))
        print("[", end="")
        print(", ".join(print_list), end="")
        print("]")

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

        cmd_argv[1] = cmd_argv[1].replace("\"", "")
        key = cmd_argv[0] + '.' + cmd_argv[1]

        if all_objs.get(key, False):
            all_objs.pop(key)
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, arg):
        "Usage: update <class name> <id> <attribute name> <attribute value>"
        cmd_argv = []
        part2_argv = []
        is_dict = 0
        if "\"" in arg:
            if "," in arg:
                if "{" in arg:
                    is_dict = 1
                    part1_argv = arg.split(",")[0].split()
                    for i in part1_argv:
                        cmd_argv.append(i.replace("\"", ""))
                    part2_argv = arg.replace("}", "").split("{")[1].split(", ")
                    for i in part2_argv:
                        for j in i.split(": "):
                            cmd_argv.append(j.replace("\"", "")
                                            .replace('\'', ""))
                else:
                    arg_key = arg.replace(",", "")
                    part1_argv = arg_key.split()
                    for i in part1_argv[:2]:
                        cmd_argv.append(i.replace("\"", ""))
                    part2_argv = arg.split(", ")[1:]
                    for i in part2_argv:
                        cmd_argv.append(i.replace("\"", ""))
            else:
                part1_argv = arg.split("\"")[0]
                for i in part1_argv.split():
                    cmd_argv.append(i)
                part2_argv = arg.split("\"")[1:]
                for i in part2_argv:
                    if i != " " and i != "":
                        cmd_argv.append(i.replace("\"", ""))

        else:
            part1_argv = arg.split()
            for i in range(len(part1_argv)):
                if i == 4:
                    break
                cmd_argv.append(part1_argv[i])

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

        all_objs = storage.all()

        key = cmd_argv[0] + '.' + cmd_argv[1]
        if all_objs.get(key, False):
            if (len(cmd_argv) >= 3):
                if (len(cmd_argv) % 2) == 0:
                    for i in range(2, len(cmd_argv), 2):
                        attr = cmd_argv[i]
                        type_att = getattr(all_objs[key], cmd_argv[i], "")
                        try:
                            cast_val = type(type_att)(cmd_argv[i + 1])
                        except:
                            cast_val = type_att
                        setattr(all_objs[key], cmd_argv[i], cast_val)
                        all_objs[key].save()
                        if is_dict == 0:
                            break
                else:
                    print("** value missing **")
            else:
                print("** attribute name missing **")
        else:
            print("** no instance found **")

    def do_count(self, arg):
        "Usage: count <class name> or <class name>.count()"
        cmd_argv = arg.split()

        if cmd_argv:
            try:
                eval(cmd_argv[0])
            except:
                print("** class doesn't exist **")
                return None

        all_objs = storage.all()
        count = 0

        for key, value in all_objs.items():
            if not cmd_argv:
                count += 1
            else:
                check = key.split('.')
                if cmd_argv[0] == check[0]:
                    count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
