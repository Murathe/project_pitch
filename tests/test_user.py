import unittest
from app.models import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(password='1122334455')

    def testPassword(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def testNoAccessPd(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def testVerifyPd(self):
        self.assertTrue(self.new_user.verify_password('1122334455'))