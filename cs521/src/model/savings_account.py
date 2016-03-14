from cs521.src.model.account import Account
__author__ = 'ATshudy'


class SavingsAccount(Account):
    '''
    This class inherits for the account class.  The savings account sets the type of the account.
    '''
    __SAVINGS = 2

    def __init__(self, balance=0.0):
        """
        Initilizes a savings account object
        :param balance: the starting balance for the new account [default: 0.0]
        :return: A Savings account object
        """
        super().__init__( None, self.__SAVINGS, balance)
