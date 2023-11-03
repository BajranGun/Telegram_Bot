from WelcomePage import WelcomePage

class Main():
    def __init__(self):
        self.MyWelcome = WelcomePage()
    
    def run_main(self):
        self.MyWelcome.run()

if __name__ == "__main__":
    new_main = Main()
    new_main.run_main()