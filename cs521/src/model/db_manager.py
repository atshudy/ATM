import sqlite3
import datetime

__author__ = 'ATshudy'


class BankDB:
    '''
    This is the database class.
    '''
    database_name = "bank.db"    # name of the sqlite database file
    table_accounts = "table_accounts"  # name of the table to hold account information
    table_transactions_audit = "table_transactions_audit"  # name of the table to log all transactions

    def __init__(self, dbName=None):
        """
        Initializes a SQL database.

        :param dbName: Is an optional parameter. This is the database name.
                        Default database name is the member variable database_name.
        :return: contructor
        """

        if dbName is not None:
            self.conn = sqlite3.connect(dbName)
        else:
            self.conn = sqlite3.connect(self.database_name)
        self.db_cursor = self.conn.cursor()
        self.create_tables()

    def create_tables (self):
        """
        creates the table_accounts and the transactions tables ONLY if they do not exist
            table_accounts example record :
                id                  primary key (automatically generated)
                pin_num             1112,
                account_type        Savings Account,
                account_balance     100.0,
                address             "Allen Tshudy", "800 commonwealth Ave", "Boston", "MA", "02215"

            table_transactions_audit example record :
                id                  primary key (automatically generated)
                pin_num             1112,
                DETAILS             "deposit - 20.00",
                TRX_DATE            "11/11/2015 at 8:54p",
        :return: None
        """
        # run SQL create table command only if the tables do not exists
        self.conn.execute('''CREATE TABLE IF NOT EXISTS '''+self.table_accounts+'''
               (pin_num         INTEGER  PRIMARY KEY NOT NULL,
               account_type     TEXT     NOT NULL,
               account_balance  REAL,
               address          CHAR(50));''')

        self.conn.execute('''CREATE TABLE IF NOT EXISTS '''+self.table_transactions_audit+'''
               (id          INTEGER   PRIMARY KEY AUTOINCREMENT   NOT NULL,
               pin_num      INTEGER   NOT NULL,
               details      CHAR(50)  NOT NULL,
               trx_date     TEXT);''')
        self.conn.commit()

    def add_account(self, pin, account, address=None):
        accountType = account.get_account_type_str()
        balance = account.get_balance()

        # Calls the execute method that will insert a record
        self.conn.execute("INSERT INTO "+self.table_accounts+"(pin_num, account_type, account_balance, address) "
                                                             "VALUES (?, ?, ?, ?)", (pin, accountType, balance, address))
        self.conn.commit()

    def delete_account(self, pin):
        """
        :param pin: the pin number to access the account to be deleted
        :return:
        """
        # Calls the execute method that will delete the record
        self.conn.execute("DELETE FROM "+self.table_accounts+" WHERE pin_num=%d" % pin,)
        self.conn.commit()

        # Calls the method to delete all the recorded transactions for the deleted account
        self.delete_transaction_for_account(pin)

    def get_account(self, pin):
        """
        :param pin: the pin number to access the account to be deleted
        :return:
        """
        # Calls the execute method that will delete the record
        self.db_cursor.execute("SELECT * FROM "+self.table_accounts+" WHERE pin_num=%d" % pin,)
        results = self.db_cursor.fetchall()
        return results

    def update_account(self, pin, account, address=None):
        """
        :param pin:
        :param account:
        :param address:
        :return:
        """
        accountType = account.get_account_type_str()
        balance = account.get_balance()

        # Calls the execute method that will insert a record
        self.conn.execute("UPDATE "+self.table_accounts+" SET account_type=?, account_balance=?, address=? WHERE pin_num=?", ( accountType, balance, address, pin))
        self.conn.commit()

    def get_all_accounts(self):
        """
        :return: all the account in the table_accounts
        """
        # Calls the execute method that will insert a record
        self.db_cursor.execute("SELECT * FROM "+self.table_accounts)
        results = self.db_cursor.fetchall()
        return results

    def add_transactions(self, pin, details):
        """
        :param pin: the pin number used in the where clause
        :return: all the records that are associated with pin number
        """
        # Calls the execute method that will insert a record
        now = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        self.conn.execute("INSERT INTO "+self.table_transactions_audit+"(pin_num, details, trx_date) "
                                                             "VALUES (?, ?, ?)", (pin, details, now))
        self.conn.commit()

    def get_all_transactions(self, pin):
        """
        :param pin: the pin number used in the where clause
        :return: all the records that are associated with pin number
        """
        # Calls the execute method that will return all records for account with pin number
        self.db_cursor.execute("SELECT * FROM "+self.table_transactions_audit+" WHERE pin_num=%d" % pin,)
        results = self.db_cursor.fetchall()
        return results

    def delete_transaction_for_account(self, pin):
        """
        :param pin: the pin number to access the account to be deleted
        :return:
        """
        # Calls the execute method that will delete the record
        self.conn.execute("DELETE FROM "+self.table_transactions_audit+" WHERE pin_num=%d" % pin,)
        self.conn.commit()

    def close_db(self):
        self.conn.close()