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
            except:
                print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
