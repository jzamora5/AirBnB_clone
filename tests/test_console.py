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
              "\"<attribute value>\"\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help update")
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

    def test_update_BaseModel(self):
        """  Test for update with BaseModel  """
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
