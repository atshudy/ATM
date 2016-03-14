from cs521.src.model.bank import Bank
from cs521.src.model.address import Address
from cs521.src.model.checking_account import CheckingAccount
from cs521.src.model.savings_account import SavingsAccount
from cs521.src.model.account import Account
from cs521.src.model.db_manager import BankDB
from cs521.src.controller.atm_exception import AtmException
from cs521.src.controller.atm_back_ground_process import ATMThread

__author__ = 'ATshudy'


class TransactionController:

    bank = None
    def __init__(self):
        """
        initilizes a singleton bank object to be used
        """
        if self.bank is None:
            self.bank = Bank()

    def withdraw_from_account(self, pin, amount):
        """
        :param pin: pin number to access the account from the bank
        :param amount: the amount to withdraw from the account
        :return: None

        precondition: - user must enter an amount before processing the withdraw.

        """
        bankDB = BankDB()
        try:
            acct = self.bank.get(pin)
            # get the account from the database
            listItem = bankDB.get_account(int(pin))
            acct = Account(listItem)
            acct.withdraw(amount)
            # update the dict
            self.bank.set(pin, acct)
            # updated the database
            bankDB.update_account(pin,acct)
            acct = self.bank.get(pin)
            bankDB.add_transactions(pin, "User "+str(pin)+" withdrew "+str(amount)+" from "+acct.get_account_type_str()+ "current balance is : "+str(acct.get_balance()))
        finally:
            bankDB.close_db()

    def credit_account(self, pin, amount):
        """
        :param pin: pin number to access the account from the bank
        :param amount: the amount to credit from the account
        :return:

        precondition: - user must enter an amount before processing the credit(deposit).
        """
        bankDB = BankDB()
        try:
            acct = self.bank.get(pin)
            # get the account from the database
            listItem = bankDB.get_account(int(pin))
            acct = Account(listItem)
            acct.deposit(amount)
            # update the dict
            self.bank.set(pin, acct)
            # updated the database
            bankDB.update_account(pin,acct)
            acct = self.bank.get(pin)
            bankDB.add_transactions(pin, "User "+str(pin)+" deposited "+str(amount)+" into "+acct.get_account_type_str()+ "current balance is : "+str(acct.get_balance()))
        finally:
            bankDB.close_db()

    def get_account_balance(self, pin):
        """
        :param pin: pin number to access the account from the bank
        :return: the current balance in the account
        """
        acct = Account(self.bank.get(pin))
        return acct.get_balance()

    def create_new_savings_account(self, name, street, city, state, zipCode, pin):
        """
        Creates a new saving account
        :param name: the name associated with the new account
        :param street: street used for the address
        :param city: city used for the address
        :param state: state used for the address
        :param zipCode: zip code used for the address
        :param pin: the pin number associated with the account
        :return: None
        """
        address = Address(name, street, city, state, zipCode)
        acct = SavingsAccount(0.0)
        self.bank.set(pin, acct, address)
        bankDB = BankDB()
        try:
            bankDB.add_account(pin, acct)
            bankDB.add_transactions(pin, "Created a new "+acct.get_account_type_str()+" for user "+str(pin))
        finally:
            bankDB.close_db()

    def create_new_checking_account(self, name, street, city, state, zipCode, pin):
        """
        Creates a new checking account
        :param name: the name associated with the new account
        :param street: street used for the address
        :param city: city used for the address
        :param state: state used for the address
        :param zipCode: zip code used for the address
        :param pin: the pin number associated with the account
        :return: None
        """
        address = Address(name, street, city, state, zipCode)
        acct = CheckingAccount(0.0)
        self.bank.set(pin, acct, address)
        bankDB = BankDB()
        try:
            bankDB.add_account(pin, acct)
            bankDB.add_transactions(pin, "Created a new "+acct.get_account_type_str()+" for user "+str(pin))
        finally:
            bankDB.close_db()

    @staticmethod
    def print_all_user_transactions(pin):
        '''
        selects all the audits made by an account and saves the information to a file.
        then spawns a thread to load the file into nodepad to display to the user.
        :param pin: pin number to access the account from the bank
        :return: None

        Precondidtion: Only the current logged in users account will be viewed.
        '''
        bankDB = BankDB()
        try:
            auditData = bankDB.get_all_transactions(int(pin))
        finally:
            bankDB.close_db()
        # using a context manger to automatically close the file
        with open("TransactionLog.txt", "w") as text_file:
            for irow in range(len(auditData)):
                line = '{} : {} : {}'.format(auditData[irow][1], auditData[irow][2], auditData[irow][3])
                text_file.write(line+"\n")
        # create a thread to launch notepad and load the transaction log file
        thread = ATMThread()
        # this will kill the thread when the main app exits.
        thread.setDaemon(True)
        thread.start()

    def account_exists(self, pin):
        '''
        checks to see if the accounts exists.
        :param pin: pin number to access the account from the bank
        :return: True or False
        '''
        bankDB = BankDB()
        try:
            acct = bankDB.get_account(int(pin))
        finally:
            bankDB.close_db()

        # if it's not in the database check memory
        if acct.__len__() == 0:
            return self.bank.contains_key(pin)
        else: # found it in the database so load account into memory
            self.bank.set(pin, acct)
            return True

    def delete_account(self, pin):
        '''
        deletes an account from the database
        :param pin: pin number to access the account from the bank
        :return: None

        precondition:  only the current logged in user will be deleted.
        '''
        bankDB = BankDB()
        try:
            bankDB.delete_account(int(pin))
            self.bank.pop(pin)
        except Exception:
            raise AtmException("User account does not exist or you are not logged in!")
        finally:
            bankDB.close_db()