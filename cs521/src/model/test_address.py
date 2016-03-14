import unittest

from cs521.src.model.address import Address

__author__ = 'ATshudy'


class TestAccount(unittest.TestCase):
    address = None

    def setUp(self):
        self.address = Address("Allen Tshudy", "800 commonwealth Ave", "Boston", "MA", "02215")

    def test_get_name(self):
        self.assertEqual(self.address.get_name(), "Allen Tshudy", "FALIED to get the name in the address")

    def test_set_name(self):
        self.address.set_name("Alan Tshudy")
        self.assertEqual(self.address.get_name(), "Alan Tshudy", "FALIED to change the name in the address")

    def test_get_street(self):
        self.assertEqual(self.address.get_street(), "800 commonwealth Ave", "FALIED to get the street in the address")

    def test_set_street(self):
        self.address.set_street("80 commonwealth Ave")
        self.assertEqual(self.address.get_street(), "80 commonwealth Ave", "FALIED to change the street in the address")

    def test_get_city(self):
        self.assertEqual(self.address.get_city(), "Boston", "FALIED to get the city in the address")

    def test_set_city(self):
        self.address.set_city("Providence")
        self.assertEqual(self.address.get_city(), "Providence", "FALIED to change the city in the address")

    def test_get_state(self):
        self.assertEqual(self.address.get_state(), "MA", "FALIED to get the state in the address")

    def test_set_state(self):
        self.address.set_city("RI")
        self.assertEqual(self.address.get_city(), "RI", "FALIED to change the state in the address")

    def test_get_zip_code(self):
        self.assertEqual(self.address.get_zip_code(), "02215", "FALIED to get the zip code in the address")

    def test_set_zip_code(self):
        self.address.set_zip_code("01122")
        self.assertEqual(self.address.get_zip_code(), "01122", "FALIED to change the zip code in the address")
