from money.screen.create_account_screen import CreateAccountScreen
from money.screen.deposit_screen import DepositScreen
from money.screen.list_transaction_screen import ListTransScreen
from money.screen.make_payment_screen import MakePaymentScreen
from money.screen.view_account_screen import ViewAccountScreen
from money.screen.withdraw_screen import WithdrawScreen


class MainMenu:
    def show_menu(self):
        print ("choose the option")
        print ("1 deposit")
        print ("2 withdraw")
        print ("3 make payment")
        print ("4 view account")
        print ("5 create account")
        print ("6 show infor")
        print ("7 transaction")
        print ("8 log out")

    def show_screen_by_option(self,choose_opt):
        screen = None

        if choose_opt == 1:
            screen = DepositScreen()
        elif choose_opt == 2:
            screen = WithdrawScreen()
        elif choose_opt == 3:
            screen = MakePaymentScreen()
        elif choose_opt == 4:
            screen = ViewAccountScreen()
        elif choose_opt == 5:
            screen = CreateAccountScreen()
        elif choose_opt == 7:
            screen = ListTransScreen()
        elif choose_opt == 8:
            print("Bye and see you")

        if screen != None:
            screen.choose_option()

    def choose_option(self):
        number_of_fail = 0
        while True:
            if number_of_fail > 4:
                break

            self.show_menu()
            choose_option = input("your option is: ")
            choose_opt = float(choose_option)
            if choose_opt > 0 and choose_opt < 9:
                print("option is correct")
                self.show_screen_by_option(choose_opt)

            print(choose_option)
            number_of_fail += 1






