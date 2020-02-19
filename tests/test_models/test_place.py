#!/usr/bin/python3
""" Unittest for Place class
"""

from datetime import datetime
import io
from models.base_model import BaseModel
from models.place import Place
from os import path, remove
import unittest
from unittest.mock import patch
from time import sleep


class Test_instancePlace(unittest.TestCase):

    """ Class for unittest of instance check """

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_instance(self):
        """ Checks if user is instance of base_model """
        b = Place()
        self.assertTrue(isinstance(b, BaseModel))

    def test_instance_args(self):
        """ Checks if user with args is instance of base_model """
        b = Place(123, "Hello", ["World"])
        self.assertTrue(isinstance(b, BaseModel))

    def test_instance_kwargs(self):
        """ Checks if user with args is instance of base_model """
        d = {"name": "Holberton"}
        b = Place(**d)
        self.assertTrue(isinstance(b, BaseModel))


class Test_class_attrsPlace(unittest.TestCase):

    """ Class for checking if classa attr were set correctly """

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_correct_classattr(self):
        """ Checks if class attr are present """
        b = Place()
        attr = ["city_id", "user_id", "name", "description", "number_rooms",
                "number_bathrooms", "max_guest", "price_by_night", "latitude",
                "longitude", "amenity_ids"]
        value = ["12", "34", "Larry", "Nice", 5, 2, 10, 25, 4.3,
                 6.8, ['Ha', 'Am']]
        d = b.__dict__
        for i, j in zip(attr, value):
            self.assertFalse(i in d)
            self.assertTrue(hasattr(b, i))
            if (type(j) is int):
                self.assertEqual(getattr(b.__class__, i, False), 0)
            elif (type(j) is float):
                self.assertEqual(getattr(b.__class__, i, False), 0.0)
            elif (type(j) is list):
                self.assertEqual(getattr(b.__class__, i, False), [])
            else:
                self.assertEqual(getattr(b.__class__, i, False), "")

    def test_set_attr(self):
        """ Check settings instance attr and accessing class attr """
        b = Place()
        attr = ["city_id", "user_id", "name", "description", "number_rooms",
                "number_bathrooms", "max_guest", "price_by_night", "latitude",
                "longitude", "amenity_ids"]
        value = ["12", "34", "Larry", "Nice", 5, 2, 10, 25, 4.3,
                 6.8, ['Ha', 'Am']]
        for i, j in zip(attr, value):
            setattr(b, i, j)
        d = b.__dict__
        for i, j, in zip(attr, value):
            self.assertEqual(getattr(b, i, False), j)
        for i, j in zip(attr, value):
            if (type(j) is int):
                self.assertEqual(getattr(b.__class__, i, False), 0)
            elif (type(j) is float):
                self.assertEqual(getattr(b.__class__, i, False), 0.0)
            elif (type(j) is list):
                self.assertEqual(getattr(b.__class__, i, False), [])
            else:
                self.assertEqual(getattr(b.__class__, i, False), "")


class Test_initPlace(unittest.TestCase):
    """ Class for unittest of __init__ """

    def setUp(self):
        """ Set up for all methods """
        pass

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_instance_creation_no_arg(self):
        """ No arguments """
        b1 = Place()
        self.assertTrue(hasattr(b1, "id"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))

    def test_attr_types(self):
        """ No arguments """
        b1 = Place()
        self.assertEqual(type(b1.id), str)
        self.assertEqual(type(b1.created_at), datetime)
        self.assertEqual(type(b1.updated_at), datetime)

    def test_id_diff_for_each_instance(self):
        """ Checks If every id generated is different """
        b1 = Place()
        b2 = Place()
        b3 = Place()
        b4 = Place()
        self.assertFalse(b1.id == b2.id)
        self.assertFalse(b1.id == b3.id)
        self.assertFalse(b1.id == b4.id)
        self.assertFalse(b2.id == b3.id)
        self.assertFalse(b2.id == b4.id)
        self.assertFalse(b3.id == b4.id)

    " ===========================  ARGS  ================================"

    def test_args(self):
        """ Tests that args works """
        b1 = Place(1)
        b2 = Place(1, "hola")
        b3 = Place(1, "hola", (1, 2))
        b4 = Place(1, "hola", (1, 2), [1, 2])

    def test_args_def_(self):
        """ Tests that default attr are set even with args """
        b1 = Place(1, "hola", (1, 2), [1, 2])
        self.assertTrue(hasattr(b1, "id"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))

    " =========================== KWARGS  =============================== "

    def test_instance_creation_kwarg(self):
        """ Arguments in Kwarg """
        d = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
             'created_at': '2017-09-28T21:03:54.053212',
             '__class__': 'Place',
             'updated_at': '2017-09-28T21:03:54.056732'}
        b1 = Place(**d)
        self.assertTrue(hasattr(b1, "id"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "__class__"))
        self.assertTrue(b1.__class__ not in b1.__dict__)

        self.assertEqual(b1.id, '56d43177-cc5f-4d6c-a0c1-e167f8c27337')
        self.assertEqual(b1.created_at.isoformat(),
                         '2017-09-28T21:03:54.053212')
        self.assertEqual(b1.updated_at.isoformat(),
                         '2017-09-28T21:03:54.056732')

    def test_no_default_args(self):
        """ Checks if id and dates are created even if not in kwargs """
        d = {"name": "Holberton"}
        b1 = Place(**d)
        self.assertTrue(hasattr(b1, "id"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertEqual(b1.name, "Holberton")

    def test_dates_str_to_datetime(self):
        """ Checks that the proper conversion is made for datetimes """

        d = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
             'created_at': '2017-09-28T21:03:54.053212',
             '__class__': 'Place',
             'updated_at': '2017-09-28T21:03:54.056732'}
        b1 = Place(**d)
        self.assertEqual(b1.created_at.isoformat(),
                         '2017-09-28T21:03:54.053212')
        self.assertEqual(b1.updated_at.isoformat(),
                         '2017-09-28T21:03:54.056732')
        self.assertEqual(type(b1.created_at), datetime)
        self.assertEqual(type(b1.updated_at), datetime)

    def test_args_kwargs(self):
        """ Tests that kwargs works even if there is args """

        d = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
             'created_at': '2017-09-28T21:03:54.053212',
             '__class__': 'Place',
             'updated_at': '2017-09-28T21:03:54.056732'}
        b1 = Place(1, "Hello", ["World"], **d)
        self.assertTrue(hasattr(b1, "id"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "__class__"))
        self.assertTrue(b1.__class__ not in b1.__dict__)

        self.assertEqual(b1.id, '56d43177-cc5f-4d6c-a0c1-e167f8c27337')
        self.assertEqual(b1.created_at.isoformat(),
                         '2017-09-28T21:03:54.053212')
        self.assertEqual(b1.updated_at.isoformat(),
                         '2017-09-28T21:03:54.056732')


class Test_str__Place(unittest.TestCase):

    """ Class for testing __str__ method """

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_print(self):
        """ Tests the __str__ method """
        b1 = Place()
        s = "[{:s}] ({:s}) {:s}\n"
        s = s.format(b1.__class__.__name__, b1.id, str(b1.__dict__))
        with patch('sys.stdout', new=io.StringIO()) as p:
            print(b1)
            st = p.getvalue()
            self.assertEqual(st, s)

    def test_print2(self):
        """ Tests the __str__ method 2"""
        b1 = Place()
        b1.name = "Holberton"
        b1.code = 123
        s = "[{:s}] ({:s}) {:s}\n"
        s = s.format(b1.__class__.__name__, b1.id, str(b1.__dict__))
        with patch('sys.stdout', new=io.StringIO()) as p:
            print(b1)
            st = p.getvalue()
            self.assertEqual(st, s)

    def test_print_args(self):
        """ Test __str__ with args """
        b1 = Place(None, 1, ["A"])
        b1.name = "Holberton"
        b1.code = 123
        s = "[{:s}] ({:s}) {:s}\n"
        s = s.format(b1.__class__.__name__, b1.id, str(b1.__dict__))
        with patch('sys.stdout', new=io.StringIO()) as p:
            print(b1)
            st = p.getvalue()
            self.assertEqual(st, s)

    def test_print_kwargs(self):

        """ Test __str__ with prev set kwargs """
        d = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
             'created_at': '2017-09-28T21:03:54.053212',
             '__class__': 'Place',
             'updated_at': '2017-09-28T21:03:54.056732'}
        b1 = Place(**d)
        s = "[{:s}] ({:s}) {:s}\n"
        s = s.format(b1.__class__.__name__, b1.id, str(b1.__dict__))
        with patch('sys.stdout', new=io.StringIO()) as p:
            print(b1)
            st = p.getvalue()
            self.assertEqual(st, s)


class Test_savePlace(unittest.TestCase):

    """ Class to test save method """

    def test_save(self):
        """ Tests that update_at time is updated """

        b1 = Place()
        crtime = b1.created_at
        uptime = b1.updated_at
        sleep(0.05)
        b1.save()
        self.assertFalse(uptime == b1.updated_at)
        self.assertTrue(crtime == b1.created_at)

    def test_type(self):
        """ Checks that after save updated_at type is datetime """

        b1 = Place()
        b1.save()
        self.assertEqual(type(b1.updated_at), datetime)
        self.assertEqual(type(b1.created_at), datetime)


class Test_to_dictPlace(unittest.TestCase):

    """ Class to test to_dict method """

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_to_dict(self):
        """ Checks for correct dictionary conversion """
        b1 = Place()
        b1.name = "Holberton"
        b1.code = 123
        d = {}
        d["id"] = b1.id
        d["created_at"] = b1.created_at.isoformat()
        d["updated_at"] = b1.updated_at.isoformat()
        d["name"] = b1.name
        d["code"] = b1.code

        dic = b1.to_dict()

        self.assertEqual(d["id"], dic["id"])
        self.assertEqual(d["created_at"], dic["created_at"])
        self.assertEqual(d["updated_at"], dic["updated_at"])
        self.assertEqual(d["name"], dic["name"])
        self.assertEqual(d["code"], dic["code"])

    def test_to_dict_class_dates(self):
        """ Checks for correct dictionary conversion """
        b1 = Place()
        dic = b1.to_dict()
        self.assertEqual(dic["__class__"], "Place")
        self.assertEqual(type(dic["created_at"]), str)
        self.assertEqual(type(dic["updated_at"]), str)

    def test_isoformat(self):
        """ Checks if date is converted to string in isoformat """
        b1 = Place()
        ctime = datetime.now()
        uptime = datetime.now()
        b1.created_at = ctime
        b1.updated_at = uptime

        dic = b1.to_dict()
        self.assertEqual(dic["created_at"], ctime.isoformat())
        self.assertEqual(dic["updated_at"], uptime.isoformat())
