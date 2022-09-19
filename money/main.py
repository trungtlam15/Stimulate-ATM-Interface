from money.datebase import DataBase
from money.entity.account import Account
from money.main_menu import MainMenu


def log_in():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "admin":
        return True
    else:
        return False


if __name__ == '__main__':
    is_login = log_in()

    # account = Account(123, "checking", "07/12/2022", "admin", "09", 234)
    # DataBase.account_list.append(account)

    # todo use is_login later
    if True:
        print("Successfully log in")
        main_menu = MainMenu()
        main_menu.choose_option()
    else:
        print("Fail to log in")
