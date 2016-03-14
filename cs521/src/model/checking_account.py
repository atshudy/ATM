from cs521.src.model.account import Account
__author__ = 'ATshudy'


class CheckingAccount(Account):
    '''
    This class inherits for the account class.  The checking account sets the type of the account.
    '''
    __CHECKING = 1

    def __init__(self, balance=0.0):
        """
        Initilizes a checking account
        :param balance: the starting balance for the new account [default: 0.0]
        :return: A Checking account object
        """
        super().__init__(None, self.__CHECKING, balance)
