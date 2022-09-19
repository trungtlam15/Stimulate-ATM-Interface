
class Screen:
    def show_menu(self):
        print("1 checking")
        print("2 saving")


    def choose_option(self):
        count = 0
        while count <= 3:
            self.show_menu()
            choose_option = input("your option is: ")
            if float(choose_option) > 0 and float(choose_option) < 3:
                print("choose type of account")
                self.action(float(choose_option))
                break
            print(choose_option)
            count += 1

    def action(self,choose_option):
        pass
