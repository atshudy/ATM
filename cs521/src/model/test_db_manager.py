import unittest

from cs521.src.model.bank import Bank
from cs521.src.model.checking_account import CheckingAccount
from cs521.src.model.savings_account import SavingsAccount
from cs521.src.model.db_manager import BankDB
from cs521.src.model.account import Account

__author__ = 'ATshudy'

class TestAccounts(unittest.TestCase):
    bank = Bank()
    acct1 = CheckingAccount(200.0)
    acct2 = SavingsAccount(550.00)
    test_database = "TestBank.db"

    def setUp(self):
        print("*** Starting setUp ***\n")
        self.bank.set(1234, self.acct1)
        self.bank.set(1111, self.acct2)
        print(self.bank)
        print("*** Finished setUp ***\n")

    def tearDown(self):
        print("*** Starting tearDown ***\n")
        bankDB = BankDB(self.test_database)
        bankDB.delete_account(1234)
        bankDB.delete_account(1111)
        bankDB.close_db()
        self.bank.clear()
        print("*** Finished tearDown ***\n")

    def test_add_accounts_db(self):
        print("*** Starting test_add_accounts_db ***\n")
        bankDB = BankDB(self.test_database)
        acct = self.bank.get(1234)
        acct1 = self.bank.get(1111)
        # add the account from the dict to the database
        bankDB.add_account(1234, acct)
        bankDB.add_account(1111, acct1)
        print(bankDB.get_all_accounts())
        self.assertEqual(bankDB.get_all_accounts(), [(1111, 'Savings Account', 550.0, None), (1234, 'Checking Account', 200.0, None)])
        bankDB.close_db()
        print("*** Finished test_add_accounts_db ***\n")

    def test_update_accounts_db(self):
        print("*** Starting test_update_accounts_db ***\n")
        bankDB = BankDB(self.test_database)
        acct = self.bank.get(1234)
        acct1 = self.bank.get(1111)
        bankDB.add_account(1234, acct)
        bankDB.add_account(1111, acct1)
        self.assertEqual(bankDB.get_all_accounts(), [(1111, 'Savings Account', 550.0, None), (1234, 'Checking Account', 200.0, None)])
        # get the account from the database
        listItem = bankDB.get_account(1234)
        acct = Account(listItem)
        acct.deposit(150.0)
        # add the updated acct to the database
        bankDB.update_account(1234,acct)
        print(bankDB.get_account(1234))
        self.assertEqual(bankDB.get_all_accounts(), [(1111, 'Savings Account', 550.0, None), (1234, 'Checking Account', 350.0, None)])
        bankDB.close_db()
        print("*** Finished test_update_accounts_db ***\n")

    def test_add_transactionsdb(self):
        print("*** Starting test_add_transactionsdb ***\n")
        bankDB = BankDB(self.test_database)
        acct = self.bank.get(1234)
        acct1 = self.bank.get(1111)
        bankDB.add_account(1234, acct)
        bankDB.add_account(1111, acct1)
        bankDB.add_transactions(1234, "deposited an initial off $200")
        bankDB.add_transactions(1111, "deposited an initial off $550")
        print("*** Finished test_add_transactionsdb ***\n")

    def test_delete_transactions_db(self):
        print("*** Starting test_delete_transactions_db ***\n")
        bankDB = BankDB(self.test_database)
        bankDB.delete_transaction_for_account(1234)
        bankDB.delete_transaction_for_account(1111)
        print("*** Finished test_delete_transactions_db ***\n")