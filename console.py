#!/usr/bin/env python3
from models.base_model import BaseModel
from models.__init__ import storage
import cmd

"File to manage by commands the HolbBNB apps"

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def do_create(self, arg):
        if (arg == ""):
            print("** class name missing **")
        else:
            try:
                my_model = eval(arg + "()")
                my_model.save()
                print(my_model.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, arg):
        argv = arg.split()
        if (len(argv) == 0):
            print("** class name missing **")
        else:
            try:
                eval(argv[0])
                try:
                    all_objs = storage.all()
                    flag = 0
                    for obj_id in all_objs:
                        split_key = obj_id.split('.')
                        if (split_key[1] == argv[1]):
                            print(all_objs[obj_id])
                            flag = 1
                    if (flag == 0):
                        print("** no instance found **")
                except:
                    print("** instance id missing **")
            except:
                print("** class doesn't exist **")

    def do_all(self, arg):
        try:
            eval(arg)
            all_objs = storage.all()
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                print(obj)
        except:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        argv = arg.split()
        if (len(argv) == 0):
            print("** class name missing **")
        else:
            try:
                eval(argv[0])
                try:
                    all_objs = storage.all()
                    flag = 0
                    for obj_id in all_objs:
                        split_key = obj_id.split('.')
                        if (split_key[1] == argv[1]):
                            print(all_objs[obj_id])
                            flag = 1
                    if (flag == 0):
                        print("** no instance found **")
                except Exception as e:
                    print(str(e))
                    print("** instance id missing **")
            except:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
