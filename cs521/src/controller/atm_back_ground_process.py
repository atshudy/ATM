import os
import time
from threading import Thread
__author__ = 'ATshudy'

class ATMThread(Thread):
    '''
    Class that load the transactionLog.txt file in notepad
    '''
    def run(self):
        os.system('notepad.exe TransactionLog.txt')
