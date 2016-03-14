import unittest

from cs521.src.model.bank import Bank
from cs521.src.model.checking_account import CheckingAccount
from cs521.src.model.savings_account import SavingsAccount
from cs521.src.model.address import Address

__author__ = 'ATshudy'


class TestAccounts(unittest.TestCase):
    bank = Bank()
    acct1 = CheckingAccount(200.0)
    acct2 = SavingsAccount(550.00)

    def setUp(self):
        print("*** Starting setUp ***\n")
        self.bank.set(1234, self.acct1)
        self.bank.set(1111, self.acct2)
        print(self.bank)
        print("*** Finished setUp ***\n")

    def tearDown(self):
        print("*** Starting tearDown ***\n")
        self.bank.clear()
        print("*** Finished tearDown ***\n")

    def test_credit_account(self):
        print("*** Starting test_credit_account ***\n")
        self.acct1 = self.bank.get(1234)
        self.acct1.deposit(100.00)
        self.assertEqual(self.acct1.get_balance(), 300.00)
        self.acct1.deposit(15.00)
        self.assertEqual(self.acct1.get_balance(), 315.00)

        print ("Finished: crediting the account")
        print("current balance in Checking account is "+str(self.acct1.get_balance()))

        print ("String: withdrawing from account")
        self.acct1.withdraw(50.00)
        self.assertEqual(self.acct1.get_balance(), 265.00)
        self.acct1.withdraw(30.00)
        self.assertEqual(self.acct1.get_balance(), 235.00)

        print("current balance in Checking account is "+str(self.acct1.get_balance()))
        print ("Finished: withdrawing the account\n")

        print()
        print("The current accounts in the bank are\n")
        print(self.bank)
        print("*** Finished test_credit_account ***\n")

    def test_does_pin_number_exist(self):
        print("*** Starting test_does_pin_number_exist ***\n")
        self.assertEqual(self.bank.contains_key(1234), True)
        self.assertEqual(self.bank.contains_key(1222), False)
        print("*** Finished test_does_pin_number_exist ***\n")

    def test_new_account_with_addresses(self):
        print("*** Starting test_new_account_with_addresses ***\n")
        addr1 = Address("Allen Tshudy", "800 commonwealth Ave", "Boston", "MA", "02215")

        self.acctAddr1 = SavingsAccount(100.0)
        self.bank.set(1112, self.acctAddr1, addr1)
        addr2 = Address("Bob Marly", "880 commonwealth Ave", "Boston", "MA", "02215")
        self.acctAddr2 = CheckingAccount(50.00)
        self.bank.set(2222, self.acctAddr2, addr2)
        print(self.bank)
        print("*** Finished test_new_account_with_addresses ***\n")
