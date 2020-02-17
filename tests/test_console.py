#!/usr/bin/python3
""" Unittests for AirBnB Console
"""

from datetime import datetime
import io
from console import HBNBCommand
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
