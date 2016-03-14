from tkinter import *
import tkinter.simpledialog as simpledialog

from cs521.src.controller.transactions_controller import TransactionController

__author__ = 'ATshudy'


class MainWnd(Frame):
    __CHECKING_ACCOUNT_TYPE = 1
    __SAVINGS_ACCOUNT_TYPE = 2

    # declared a dist to hold user session information
    __session = {'loggedIn' : False, 'pin' : None}

    __controller = TransactionController();

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parentWnd = parent
        self.menuBar = Menu(self.parentWnd)
        self.parentWnd.config(menu=self.menuBar)
        self.fileMenu = Menu(self.menuBar,tearoff=0)
        self.fileMenu.add_command(label="Create Account",command=self.create_account)
        self.fileMenu.add_command(label="Delete Account",command=self.on_delete_account)
        self.fileMenu.add_command(label="View Transaction Log",command=self.on_log_transactions)
        self.fileMenu.add_command(label="Log out",command=self.logout)
        self.menuBar.add_cascade(label="File",menu=self.fileMenu)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.on_exit)

        self.inputVar = StringVar()
        self.topFrame = Frame(self.parentWnd)
        self.centerFrame = Frame(self.parentWnd)
        self.bottomFrame = Frame(self.parentWnd)
        self.centerFrameLeft = Frame(self.centerFrame)
        self.centerFrameCenter = Frame(self.centerFrame, bd=1, relief=SUNKEN)
        self.centerFrameRight = Frame(self.centerFrame)

        self.bottomFrame.pack(side="bottom", fill="both", expand=True)
        self.topFrame.pack(side="top", fill="both", expand=False)
        self.centerFrame.pack(fill="both", expand=True, padx=5, pady=5)
        self.centerFrameLeft.pack(side="left", fill="both", expand=True)
        self.centerFrameCenter.pack(side="left", expand=False)
        self.centerFrameRight.pack(side="left", fill="both",expand=True)

        # add a vertical scroll bar to the text area
        self.inputVar = StringVar()
        self.displayText = StringVar()
        self.textAreaTxt = StringVar()
        self.input = Entry(self.topFrame, textvariable=self.inputVar).pack(side="bottom", padx=5, pady=5)
        self.textArea = Text(self.topFrame, height="7", width=40, wrap=WORD)
        self.textArea.insert(END, "Welcome, enter your pin number")
        self.textArea.pack(padx=15, pady=15)

        self.btn1Label = StringVar()
        self.btn2Label = StringVar()
        self.btn3Label = StringVar()
        self.btn4Label = StringVar()
        self.btn5Label = StringVar()
        self.btn6Label = StringVar()
        self.btn7Label = StringVar()
        self.btn8Label = StringVar()
        self.btn9Label = StringVar()
        self.btn0Label = StringVar()
        self.enterLabel = StringVar()
        self.cancelLabel = StringVar()
        self.withdrawLabel = StringVar()
        self.depositLabel = StringVar()
        self.decimalLabel = StringVar()
        self.statusTxt = StringVar()

        self.initialize_ui()

    def on_enter_click(self):
        if self.__session['loggedIn'] == False:
            self.textArea.delete(1.0, END)
            inputTxt = self.inputVar.get()
            if self.__controller.account_exists(int(inputTxt)):
                self.__session['loggedIn'] = True
                self.__session['pin'] = int(inputTxt)
                self.textArea.insert(END, "to continue enter an amount and Press\n withdraw or deposit\n")
            else:
                self.statusTxt.set("ERROR: pin does not match an checking account on file")
                self.textArea.insert(END, "Please, re-enter your pin number or create an account")
        self.inputVar.set("")
        self.statusTxt.set("You have successfully logged in to your account.  Your balance is :"+repr(self.__controller.get_account_balance(self.__session['pin'])))

    def on_cancel_click(self):
        self.inputVar.set("")
        self.statusTxt.set("Transaction Canceled")

    def on_withdraw_click(self):
        inputTxt = self.inputVar.get()
        if inputTxt == "":
            self.statusTxt.set("Input Text is empty, Please enter amount in the input field")
            return
        self.__controller.withdraw_from_account(self.__session['pin'], float(inputTxt))
        self.inputVar.set("")
        self.statusTxt.set("Current Balance : "+repr(self.__controller.get_account_balance(self.__session['pin'])))

    def on_deposit_click(self):
        inputTxt = self.inputVar.get()
        if inputTxt == "":
            self.statusTxt.set("Input Text is empty, Please enter amount in the input field")
            return
        self.__controller.credit_account(self.__session['pin'], float(inputTxt))
        self.inputVar.set("")
        self.statusTxt.set("Current Balance : "+repr(self.__controller.get_account_balance(self.__session['pin'])))

    def on_click_numpad(self, buttonLabel):
        value = str(buttonLabel.get())
        self.inputVar.set(self.inputVar.get()+value)

    def on_log_transactions(self):
        if self.__session['loggedIn'] == False:
            self.statusTxt.set("User not Logged In, Please login with a valid pin number")
            return
        pin = self.__session['pin']
        TransactionController.print_all_user_transactions(pin)

    def on_delete_account(self, pin=None):
        if pin is None:
            pin = self.__session['pin']
        self.__session['loggedIn'] = False
        self.__session['pin'] = None
        self.__controller.delete_account(pin)
        self.textArea.delete(1.0, END)
        self.textArea.insert(END, "Welcome, enter your pin number")
        self.statusTxt.set("Enter your pin number")

    def create_account(self):
        name = simpledialog.askstring("Name", "Enter the name on the account")
        if not name:
            return
        street = simpledialog.askstring("Street", "Enter your street address")
        if not street:
            return
        city = simpledialog.askstring("city", "Enter your city")
        if not city:
            return
        state = simpledialog.askstring("state", "Enter your state")
        if not state:
            return
        zipCode = simpledialog.askstring("zip", "Enter your zip code")
        if not zipCode:
            return
        pin = simpledialog.askstring("pin", "Enter your 4 digit pin number")
        if not pin:
            return
        accountType = simpledialog.askinteger("Account Type", "Enter 1 for checking and 2 for savings")
        if not accountType:
            return

        if accountType == self.__CHECKING_ACCOUNT_TYPE:
            self.__controller.create_new_checking_account(name, street, city, state, zipCode, pin)
        else:
            self.__controller.create_new_savings_account(name, street, city, state, zipCode, pin)

        if self.__controller.account_exists(pin):
            self.__session['loggedIn'] = True
            self.__session['pin'] = pin
            self.textArea.delete(1.0, END)
            self.textArea.insert(END, "Welcome\n\n, would like like to\n Deposit or Withdraw from your account")
            self.statusTxt.set("SUCCESSFUL new account created Current Balance : "+repr(self.__controller.get_account_balance(self.__session['pin'])))
        else:
            self.__session['loggedIn'] = False
            self.__session['pin'] = None
            self.statusTxt.set("ERROR: Could not create a new account with pin")

    def logout(self):
        self.__session['loggedIn'] = False
        self.__session['pin'] = None
        self.textArea.delete(1.0, END)
        self.textArea.insert(END, "Welcome, enter your pin number")
        self.statusTxt.set("Enter your pin number")

    def on_exit(self):
        self.logout()
        self.parentWnd.quit()

    def initialize_ui(self):
        self.btn1Label.set("1")
        self.btn2Label.set("2")
        self.btn3Label.set("3")
        self.btn4Label.set("4")
        self.btn5Label.set("5")
        self.btn6Label.set("6")
        self.btn7Label.set("7")
        self.btn8Label.set("8")
        self.btn9Label.set("9")
        self.btn0Label.set("0")
        self.enterLabel.set("Enter")
        self.cancelLabel.set("Cancel")
        self.withdrawLabel.set("Withdraw")
        self.depositLabel.set("Deposit")
        self.decimalLabel.set(".")

        self.button1 = Button(self.centerFrameCenter, width=12, height=2, textvariable=self.btn1Label, command=lambda: self.on_click_numpad(self.btn1Label)).grid(row=0, column=0)
        self.button2 = Button(self.centerFrameCenter, width=12, height=2, textvariable=self.btn2Label, command=lambda: self.on_click_numpad(self.btn2Label)).grid(row=0, column=1)
        self.button3 = Button(self.centerFrameCenter, width=12, height=2, textvariable=self.btn3Label, command=lambda: self.on_click_numpad(self.btn3Label)).grid(row=0, column=2)
        self.button4 = Button(self.centerFrameCenter, width=12, height=2, textvariable=self.btn4Label, command=lambda: self.on_click_numpad(self.btn4Label)).grid(row=1, column=0)
        self.button5 = Button(self.centerFrameCenter, width=12, height=2, textvariable=self.btn5Label, command=lambda: self.on_click_numpad(self.btn5Label)).grid(row=1, column=1)
        self.button6 = Button(self.centerFrameCenter, width=12, height=2, textvariable=self.btn6Label, command=lambda: self.on_click_numpad(self.btn6Label)).grid(row=1, column=2)
        self.button7 = Button(self.centerFrameCenter, width=12, height=2, textvariable=self.btn7Label, command=lambda: self.on_click_numpad(self.btn7Label)).grid(row=2, column=0)
        self.button8 = Button(self.centerFrameCenter, width=12, height=2, textvariable=self.btn8Label, command=lambda: self.on_click_numpad(self.btn8Label)).grid(row=2, column=1)
        self.button9 = Button(self.centerFrameCenter, width=12, height=2, textvariable=self.btn9Label, command=lambda: self.on_click_numpad(self.btn9Label)).grid(row=2, column=2)
        self.button0 = Button(self.centerFrameCenter, width=12, height=2, textvariable=self.btn0Label, command=lambda: self.on_click_numpad(self.btn0Label)).grid(row=3, column=1)
        self.enterBtn = Button(self.centerFrameCenter, textvariable=self.enterLabel, command=self.on_enter_click, width=12, height=2).grid(row=3, column=2)
        self.cancelBtn = Button(self.centerFrameCenter, textvariable=self.cancelLabel, command=self.on_cancel_click, width=12, height=2).grid(row=3, column=0)
        self.withdrawBtn = Button(self.centerFrameCenter, textvariable=self.withdrawLabel, command=self.on_withdraw_click, width=12, height=2).grid(row=5, column=1)
        self.depositBtn = Button(self.centerFrameCenter, textvariable=self.depositLabel, command=self.on_deposit_click, width=12, height=2).grid(row=5, column=2)
        self.decimal = Button(self.centerFrameCenter, textvariable=self.decimalLabel, command=lambda: self.on_click_numpad(self.decimalLabel), width=12, height=2).grid(row=5, column=0)

        #  create a static text field and put it in the window and
        self.statusTxt.set("Enter your pin number")
        self.statisLabel = Label(self.bottomFrame, textvariable=self.statusTxt).pack()

def main_function():
    parentWnd = Tk()
    #  set the title and window size
    #  create a window object
    parentWnd.title("Automatic Teller Machine (ATM)")
    parentWnd.geometry("650x450")
    parentWnd.resizable(width=FALSE, height=FALSE)
    app = MainWnd(parentWnd)
    app.mainloop()

if __name__ == '__main__':
    main_function()
