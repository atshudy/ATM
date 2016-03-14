__author__ = 'ATshudy'


class Address:
    '''
    This class is the accounts address that is used for the account.
    This is an option when creating an account
    '''
    __name = None
    __street = None
    __city = None
    __state = None
    __zip_code = None

    def __init__(self, name, street, city, state, zipCode):
        '''
        Initializes the address object
        :param name:
        :param street:
        :param city:
        :param state:
        :param zipCode:
        :return:
        '''
        self.__name = name
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zipCode = zipCode

    def get_name(self):
        '''
        getter method for the name of an address object
        :return: the name as a string
        '''
        return self.__name

    def set_name(self, name):
        '''
        setter method for setting the name of an address object
        :param name:
        :return: None
        '''
        self.__name = name

    def get_street(self):
        '''
        getter method for the street of the address object
        :return: the street as a string
        '''
        return self.__street

    def set_street(self, street):
        '''
        setter method for setting the street of an address object
        :param street:
        :return: None
        '''
        self.__street = street

    def get_city(self):
        '''
        getter method for the city of the address object
        return the city as a string
        '''
        return self.__city

    def set_city(self, city):
        '''
        setter method for the city of the address object
        :param city:
        :return:  None
        '''
        self.__city = city

    def get_state(self):
        '''
        getter method for the state of the address object
        :return: the state as a string
        '''
        return self.__state

    def set_state(self, state):
        '''
        setter method for the state of the address object
        :param state:
        :return: the state as a string
        '''
        self.__state = state

    def get_zip_code(self):
        '''
        getter method for the zip code in the address object
        :return: the zip code as a string
        '''
        return self.__zipCode

    def set_zip_code(self, zipCode):
        '''
        setter method for the zip code in the address object
        :param zipCode:
        :return: None
        '''
        self.__zipCode = zipCode

    def __str__(self):
        '''
        used to print the object
        :return: a string
        '''
        return self.get_name()