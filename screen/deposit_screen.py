from money.datebase import DataBase
from money.screen.screen import Screen


class DepositScreen(Screen):
    def action(self, action_number):
        amount = input("enter the amount: ")
        account = None
        if action_number == 1:
            for i in DataBase.account_list:
                if i.type == "checking":
                    account = i
        elif action_number == 2:
            for i in DataBase.account_list:
                if i.type == "saving":
                    account = i

        if account.balance != None:
            account.balance += float(amount)
            print(account.balance)










