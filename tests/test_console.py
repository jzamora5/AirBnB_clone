#!/usr/bin/python3
""" Unittests for AirBnB Console
"""

from datetime import datetime
import io
from console import HBNBCommand
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from os import path, remove
import unittest
from unittest.mock import patch


class Test_non_existing_command(unittest.TestCase):

    """ Tests a command that does not exist """

    def test_unknown(self):
        """ Command that does not exist """
        msg = "*** Unknown syntax: asd\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("asd")
            st = f.getvalue()
            self.assertEqual(msg, st)


class Test_help(unittest.TestCase):

    """ Tests the help commands """

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_help_help(self):
        """  Test for help of quit command """
        msg = "List available commands with \"help\" or " \
              "detailed help with \"help cmd\".\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help help")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_help_quit(self):
        """  Test for help of quit command """
        msg = "Quit command to exit the program\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_help_EOF(self):
        """  Test for help of EOF command """
        msg = "EOF command to exit the program\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_help_create(self):
        """  Test for help of create command """
        msg = "Create an instance if the Model exists\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help create")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_help_show(self):
        """  Test for help of show command """
        msg = "Print dict of a instance in base of it's ID\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help show")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_help_destroy(self):
        """  Test for help of destroy command """
        msg = "Deletes an instance based on it's ID and save the changes\n \
        Usage: destroy <class name> <id>\n"

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_help_all(self):
        """  Test for help of all command """
        msg = "Print all the instances saved in file.json\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help all")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_help_update(self):
        """  Test for help of update command """
        msg = "Usage: update <class name> <id> <attribute name> " \
              "<attribute value>\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help update")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_help_count(self):
        """  Test for help of count command """
        msg = "Usage: count <class name> or <class name>.count()\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help count")
            st = f.getvalue()
            self.assertEqual(msg, st)


class Test_create(unittest.TestCase):

    """ Tests the create commands """
    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_create_no_class(self):
        """  Test for create with class missing """
        msg = "** class name missing **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_create_invalid_class(self):
        """  Test for create with invalid class """
        msg = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_create_valid_class(self):
        """  Test for create with existing id  """
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("create " + i)
                id_st = f.getvalue()
                alldic = storage.all()
                self.assertTrue((i + '.' + id_st[:-1]) in alldic.keys())
        self.assertEqual(len(alldic), len(classes))


class Test_destroy(unittest.TestCase):

    """ Tests the destroy commands """
    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_destroy_no_class(self):
        """  Test for destroy with class missing """
        msg = "** class name missing **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_new_destroy_no_class(self):
        """  Test for destroy with class missing by second method """
        msg = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            pre_cmd = HBNBCommand().precmd("MyModel.destroy()")
            HBNBCommand().onecmd(pre_cmd)
            st = f.getvalue()
            if st[0] == "\n":
                msg = "\n" + msg
            self.assertEqual(msg, st)

    def test_destroy_invalid_class(self):
        """  Test for destroy with invalid class """
        msg = "** class doesn't exist **\n"

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_destroy_no_id(self):
        """  Test for destroy with id missing """
        msg = "** instance id missing **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("destroy " + i)
                st = f.getvalue()
                self.assertEqual(msg, st)

    def test_new_destroy_no_id(self):
        """  Test for destroy with id missing """
        msg = "** instance id missing **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                pre_cmd = HBNBCommand().precmd(i + ".destroy()")
                HBNBCommand().onecmd(pre_cmd)
                st = f.getvalue()
                if st[0] == "\n":
                    msg = "\n" + msg
                self.assertEqual(msg, st)

    def test_destroy_no_existent_id(self):
        """  Test for destroy with non-existent id """
        msg = "** no instance found **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("destroy " + i + " 123")
                st = f.getvalue()
                self.assertEqual(msg, st)

    def test_new_destroy_no_existent_id(self):
        """  Test for destroy with non-existent id """
        msg = "** no instance found **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                pre_cmd = HBNBCommand().precmd(i + ".destroy(123)")
                HBNBCommand().onecmd(pre_cmd)
                st = f.getvalue()
                if st[0] == "\n":
                    msg = "\n" + msg
                self.assertEqual(msg, st)

    def test_destroy_valid_class(self):
        """  Test for destroy with existing id  """
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        lencl = len(classes)
        id_cl = []
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("create " + i)
                id_st = f.getvalue()
                id_cl.append(id_st)
                alldic = storage.all()
                self.assertTrue((i + '.' + id_st[:-1]) in alldic.keys())
        self.assertEqual(len(alldic), lencl)
        for i, j in zip(classes, id_cl):
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("destroy " + i + " " + j)
                alldic = storage.all()
                self.assertFalse((i + '.' + id_st[:-1]) in alldic.keys())
                lencl -= 1
                self.assertEqual(len(alldic), lencl)


class Test_show(unittest.TestCase):

    """ Tests the show commands """
    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_show_no_arg(self):
        """  Test for show with no command """
        msg = "** class name missing **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_show_no_exist_class(self):
        """  Test for show non-existent class """
        msg = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_new_show_no_exist_class(self):
        """  Test for show non-existent class """
        msg = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            pre_cmd = HBNBCommand().precmd("MyModel.show()")
            HBNBCommand().onecmd(pre_cmd)
            st = f.getvalue()
            if st[0] == "\n":
                msg = "\n" + msg
            self.assertEqual(msg, st)

    def test_show_no_id(self):
        """  Test for show with id missing """
        msg = "** instance id missing **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("show " + i)
                st = f.getvalue()
                self.assertEqual(msg, st)

    def test_new_show_no_id(self):
        """  Test for show with id missing """
        msg = "** instance id missing **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                pre_cmd = HBNBCommand().precmd(i + ".show()")
                HBNBCommand().onecmd(pre_cmd)
                st = f.getvalue()
                if st[0] == "\n":
                    msg = "\n" + msg
                self.assertEqual(msg, st)

    def test_show_no_existent_id(self):
        """  Test for show with non-existent id """
        msg = "** no instance found **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("show " + i + " 123")
                st = f.getvalue()
                self.assertEqual(msg, st)

    def test_new_show_no_existent_id(self):
        """  Test for show with non-existent id """
        msg = "** no instance found **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                pre_cmd = HBNBCommand().precmd(i + ".show(123)")
                HBNBCommand().onecmd(pre_cmd)
                st = f.getvalue()
                if st[0] == "\n":
                    msg = "\n" + msg
                self.assertEqual(msg, st)

    def test_show_existing_id(self):
        """  Test for show with existing id  """
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("create " + i)
                id_st = f.getvalue()
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("show " + i + " " + id_st)
                st = f.getvalue()
                alldic = storage.all()
                objst = str(alldic[i + '.' + id_st[:-1]])
                self.assertEqual(st[:-1], objst)

    def test_show_show_existing_id(self):
        """  Test for show with existing id  """
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("create " + i)
                id_st = f.getvalue()
            with patch('sys.stdout', new=io.StringIO()) as f:
                pre_cmd = HBNBCommand().precmd(i + ".show(\"" + id_st + "\")")
                HBNBCommand().onecmd(pre_cmd)
                st = f.getvalue()
                alldic = storage.all()
                objst = str(alldic[i + '.' + id_st[:-1]])
                self.assertEqual(st[:-1], objst)


class Test_all(unittest.TestCase):

    """ Tests the all command """

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_update_no_existent_class(self):
        """  Test for all with no existent class """
        msg = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_new_update_no_existent_class(self):
        """  Test for all with no existent class """
        msg = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            pre_cmd = HBNBCommand().precmd("MyModel.all()")
            HBNBCommand().onecmd(pre_cmd)
            st = f.getvalue()
            if st[0] == "\n":
                msg = "\n" + msg
            self.assertEqual(msg, st)

    def test_empty(self):
        """ Tests for empty storage """
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        msg = "[]\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("all")
                st = f.getvalue()
                self.assertEqual(msg, st)
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("all " + i)
                st = f.getvalue()
                self.assertEqual(msg, st)

    def test_new_empty(self):
        """ Tests for empty storage """
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        msg = "[]\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("all()")
                st = f.getvalue()
                self.assertEqual(msg, st)
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                pre_cmd = HBNBCommand().precmd(i + ".all()")
                HBNBCommand().onecmd(pre_cmd)
                st = f.getvalue()
                if st[0] == "\n":
                    msg = "\n" + msg
                self.assertEqual(msg, st)

    def test_all_classes(self):
        """ Tests All command for classes_double """
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        classes += classes
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("create " + i)
                st = f.getvalue()
            alldic = storage.all()
            all_cl = []
            all_full = []
            for j in alldic.keys():
                    all_full.append(str(alldic[j]))
                    if i in j:
                        all_cl.append(str(alldic[j]))
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("all " + i)
                st = f.getvalue()
                self.assertEqual(str(all_cl) + "\n", st)
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("all")
                st = f.getvalue()
                self.assertEqual(str(all_full) + "\n", st)


class Test_update(unittest.TestCase):

    """ Tests the update commands """
    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_update_no_class(self):
        """  Test for update with no class """
        msg = "** class name missing **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("update")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_update_no_existent_class(self):
        """  Test for update with no existent class """
        msg = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("update MyModel")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_new_update_no_existent_class(self):
        """  Test for update with no existent class """
        msg = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            pre_cmd = HBNBCommand().precmd("MyModel.update()")
            HBNBCommand().onecmd(pre_cmd)
            st = f.getvalue()
            if st[0] == "\n":
                msg = "\n" + msg
            self.assertEqual(msg, st)

    def test_update_no_id(self):
        """  Test for update with id missing """
        msg = "** instance id missing **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("update " + i)
                st = f.getvalue()
                self.assertEqual(msg, st)

    def test_new_update_no_id(self):
        """  Test for update with id missing """
        msg = "** instance id missing **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                pre_cmd = HBNBCommand().precmd(i + ".update()")
                HBNBCommand().onecmd(pre_cmd)
                st = f.getvalue()
                if st[0] == "\n":
                    msg = "\n" + msg
                self.assertEqual(msg, st)

    def test_update_no_existent_id(self):
        """  Test for update with non-existent id """
        msg = "** no instance found **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("update " + i + " 123")
                st = f.getvalue()
                self.assertEqual(msg, st)

    def test_update_existing_id_no_attr(self):
        """  Test for update with existing id no attr """
        msg = "** attribute name missing **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("create " + i)
                id_st = f.getvalue()
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("update " + i + " " + id_st)
                st = f.getvalue()
                self.assertEqual(msg, st)

    def test_update_no_value(self):
        """  Test for update with no value """
        msg = "** value missing **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("create " + i)
                id_st = f.getvalue()
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("update " + i + " " + id_st + " name")
                st = f.getvalue()
                self.assertEqual(msg, st)

    def test_update_extra_args(self):
        """  Test for update with BaseModel """
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        attr = ["name", "code"]
        value = ["Holberton", "123"]
        typeval = [str, str]

        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("create " + i)
                id_st = f.getvalue()
                alldic = storage.all()
                self.assertTrue((i + '.' + id_st[:-1]) in alldic.keys())
                for j, k in zip(attr, value):
                    with patch('sys.stdout', new=io.StringIO()) as f:
                        HBNBCommand().onecmd("update " + i + " " + id_st +
                                             " " + j + " " + "\"" + k + "\"" +
                                             "Hey_name \"Betty\"")
                alldic = storage.all()
                ins = alldic[i + '.' + id_st[:-1]]
                for j, k, m in zip(attr, value, typeval):
                    gattr = getattr(ins, j, False)
                    self.assertEqual(gattr, k)
                    self.assertEqual(m, type(gattr))
                self.assertFalse(getattr(ins, "Hey_name", False))

    def test_update_BaseModel(self):
        """  Test for update with BaseModel """
        i = "BaseModel"
        attr = ["name", "code"]
        value = ["Holberton", "123"]
        typeval = [str, str]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create " + i)
            id_st = f.getvalue()
            alldic = storage.all()
            self.assertTrue((i + '.' + id_st[:-1]) in alldic.keys())
        for j, k in zip(attr, value):
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd("update " + i + " " + id_st +
                                         " " + j + " " + k)
        alldic = storage.all()
        ins = alldic[i + '.' + id_st[:-1]]
        for j, k, m in zip(attr, value, typeval):
            gattr = getattr(ins, j, False)
            self.assertEqual(gattr, k)
            self.assertEqual(m, type(gattr))

    def test_update_User(self):
        """  Test for update with User """
        i = "User"
        attr = ["name", "code", "email", "password", "first_name", "last_name"]
        value = ["Holberton", "123", "ga@gmail.com", "pswd", "Larry", "Page"]
        typeval = [str, str, str, str, str, str]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create " + i)
            id_st = f.getvalue()
            alldic = storage.all()
            self.assertTrue((i + '.' + id_st[:-1]) in alldic.keys())
        for j, k in zip(attr, value):
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd("update " + i + " " + id_st +
                                         " " + j + " " + k)
        alldic = storage.all()
        ins = alldic[i + '.' + id_st[:-1]]
        for j, k, m in zip(attr, value, typeval):
            gattr = getattr(ins, j, False)
            self.assertEqual(gattr, k)
            self.assertEqual(m, type(gattr))

    def test_update_State(self):
        """  Test for update with State """
        i = "State"
        attr = ["name", "code"]
        value = ["Holberton", "123"]
        typeval = [str, str]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create " + i)
            id_st = f.getvalue()
            alldic = storage.all()
            self.assertTrue((i + '.' + id_st[:-1]) in alldic.keys())
        for j, k in zip(attr, value):
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd("update " + i + " " + id_st +
                                         " " + j + " " + k)
        alldic = storage.all()
        ins = alldic[i + '.' + id_st[:-1]]
        for j, k, m in zip(attr, value, typeval):
            gattr = getattr(ins, j, False)
            self.assertEqual(gattr, k)
            self.assertEqual(m, type(gattr))

    def test_update_City(self):
        """  Test for update with City """
        i = "City"
        attr = ["state_id", "name", "code"]
        value = ["568", "Holberton", "123"]
        typeval = [str, str, str]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create " + i)
            id_st = f.getvalue()
            alldic = storage.all()
            self.assertTrue((i + '.' + id_st[:-1]) in alldic.keys())
        for j, k in zip(attr, value):
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd("update " + i + " " + id_st +
                                         " " + j + " " + k)
        alldic = storage.all()
        ins = alldic[i + '.' + id_st[:-1]]
        for j, k, m in zip(attr, value, typeval):
            gattr = getattr(ins, j, False)
            self.assertEqual(gattr, k)
            self.assertEqual(m, type(gattr))

    def test_update_Amenity(self):
        """  Test for update with Amenity """
        i = "Amenity"
        attr = ["name", "code"]
        value = ["Holberton", "123"]
        typeval = [str, str]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create " + i)
            id_st = f.getvalue()
            alldic = storage.all()
            self.assertTrue((i + '.' + id_st[:-1]) in alldic.keys())
        for j, k in zip(attr, value):
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd("update " + i + " " + id_st +
                                         " " + j + " " + k)
        alldic = storage.all()
        ins = alldic[i + '.' + id_st[:-1]]
        for j, k, m in zip(attr, value, typeval):
            gattr = getattr(ins, j, False)
            self.assertEqual(gattr, k)
            self.assertEqual(m, type(gattr))

    def test_update_Place(self):
        """  Test for update with Place """
        i = "Place"
        attr = ["city_id", "user_id", "name", "description", "number_rooms",
                "number_bathrooms", "max_guest", "price_by_night", "latitude",
                "longitude", "code"]
        value = ["686", "123", "Larry", "Nice", 5, 2, 15, 136,
                 8.7, 9.4, "988"]
        typeval = [str, str, str, str, int, int, int, int, float, float, str]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create " + i)
            id_st = f.getvalue()
            alldic = storage.all()
            self.assertTrue((i + '.' + id_st[:-1]) in alldic.keys())
        for j, k in zip(attr, value):
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd("update " + i + " " + id_st +
                                         " " + j + " " + str(k))
        alldic = storage.all()
        ins = alldic[i + '.' + id_st[:-1]]
        for j, k, m in zip(attr, value, typeval):
            gattr = getattr(ins, j, False)
            self.assertEqual(gattr, k)
            self.assertEqual(m, type(gattr))

    def test_update_Review(self):
        """  Test for update with Review """
        i = "Review"
        attr = ["place_id", "user_id", "text", "name", "code"]
        value = ["985", "7621", "Random Text", "Holberton", "123"]
        typeval = [str, str]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create " + i)
            id_st = f.getvalue()
            alldic = storage.all()
            self.assertTrue((i + '.' + id_st[:-1]) in alldic.keys())
        for j, k in zip(attr, value):
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd("update " + i + " " + id_st +
                                         " " + j + " " + k)
        alldic = storage.all()
        ins = alldic[i + '.' + id_st[:-1]]
        for j, k, m in zip(attr, value, typeval):
            gattr = getattr(ins, j, False)
            self.assertEqual(gattr, k)
            self.assertEqual(m, type(gattr))


class Test_count(unittest.TestCase):

    """ Tests the update commands """
    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass
