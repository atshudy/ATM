from cs521.src.model.account import Account
__author__ = 'ATshudy'


class Bank(dict):
    """
    The Bank class extents the built-in class dict.
    The methods override some of dict methods and it uses the super method to call super class methods

    This class creates a bank object and it holds bank accounts.  Each account is associated with a pin number.
    the pin number is the key and account is the value.  Therefore, you can only have one account for each pin number.
    """
    def __init__(self, *args):
        """
        :param args: means a variable number of parameters. No parameters are accepted
        :param kw: means a variable number of key value pairs as parameters. No parameters are accepted
        :return: a dict object
        """
        super().__init__(*args)
        self.itemlist = super(Bank,self).keys()

    def set(self, key, *values):
#        if self.contains_key(key):
#            raise Exception("Account exists for pin number "+str(key)+", close the account or create a new one")
#        else:
            self[key] = values

    def get( self, key ):
        return self[key][0]

    def __iter__(self):
        return iter(self.itemlist)

    def keys(self):
        return self.itemlist

    def values(self):
        return [self[key] for key in self]

    def itervalues(self):
        return (self[key] for key in self)

    def __str__(self):
        ret_str = ""
        for d in self.keys():
            ret_str += ""+str(d)
            for v in self[d]:
                ret_str += ","+str(v)
            ret_str += "\n"
        return ret_str

    def contains_key(self, key):
        for k in self.keys():
            if k == key:
                return True
        return False

    def contains_value(self, item):
        return super(Bank, self).__contains__(self, item)