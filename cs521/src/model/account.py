from cs521.src.model.address import Address
__author__ = 'ATshudy'


class Account():
    __balance = None
    __accountType = None
    CHECKING_TYPE = 1
    SAVINGS_TYPE = 2

    def __init__(self, listItem=None, accountType=1 , balance=0.0):
        """
        :param list:  This is a tuple that is used when accessing the acct from the database
        :param accountType:  CHECKING=1 or SAVINGS=2 [default is CHECKING]
        :param balance: The initial balance when the accoun is open [default is 0.0]
        :return: an Account object
        """
        if not listItem:
            self.__balance = balance
            self.__accountType = accountType
        if isinstance(listItem, Account):
            self.__balance = listItem.__balance
            self.__accountType = listItem.__accountType
        elif isinstance(listItem, list):
            balance = float(listItem[0][2])
            self.set_balance(balance)
            if listItem[0][1] == 'Checking Account':
                self.__accountType = self.CHECKING_TYPE
            else:
                self.__accountType = self.SAVINGS_TYPE

    def get_balance(self):
        """
        getter method
        :return:  the __balance member variable
        """
        return self.__balance

    def set_balance(self, balance):
        """
        setter method
        :param balance:  A new balance is added to the existing balance
        :return: nothing is returned
        """
        self.__balance = balance

    def get_account_type(self):
        """
        :return: 1=CHECKING or 2=SAVINGS
        """
        return self.__accountType;

    def get_account_type_str(self):
        """
        :return: "Checking Account" or "Savings Account" as a string
        """
        if self.__accountType == self.CHECKING_TYPE:
            return "Checking Account"
        else:
            return "Savings Account"

    def withdraw(self, amount):
        """
        :param amount: the amount to withdraw from account
        :return:
        """
        self.set_balance(self.get_balance() - amount)

    def deposit(self, amount):
        """
        :param amount: the amount to deposit in the account
        :return:
        """
        self.set_balance(self.get_balance() + amount)

    def __str__(self):
        """
        :return: the account type and balance as a string
         """
        if self.__accountType == 1:
            return ("Checking Account:Balance "+str(self.get_balance()))
        else:
            return ("Savings Account:Balance "+str(self.get_balance()))