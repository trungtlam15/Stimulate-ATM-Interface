from money.datebase import DataBase
from money.entity.account import Account
from money.screen.screen import Screen


class CreateAccountScreen(Screen):
    def choose_option(self):
        self.action()

    def action(self):
        account = input("enter_idcode: ")
        type = input("type: ")
        created_date = input("created date: ")
        name = input("name of user: ")
        expired_date = input("expired_date: ")
        balance = 0
        print("balance: ", balance)

        account = Account(account, type, created_date, name, expired_date, balance)
        DataBase.account_list.append(account)
