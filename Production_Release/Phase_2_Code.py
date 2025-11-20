"""
INFO-233 Group Project
Project Name: Stock Portfolio Builder
Team Name: Spyder01
Group 1
"""
# Modules
#IMPORTS HERE
# Functions
def stock_api(): # Stock API
    pass
def mail_api(): # Email API
    pass
def calc_stock(investment, stock_info): # Calculate
    pass
def main(): # Main Program
    # Variables
    stock_choices = ("low", "active", "high")
    print("Welcome to Stock Portfolio Builder")
    while True:
        try:
            # Inputs to investment and choice
            investment = int(input("How much would you like to invest into your stock portfolio? "))
            choice = input("Please choose between low, active or high stock performance: ")
            if choice.lower() in stock_choices:
                break
            else:
                print("Please enter a valid input.")
        except ValueError:
            print("Please enter a valid input.")
    stock_info = stock_api(choice) # get 4 stock prices and info
    calc_stock(investment, stock_info) # Calculate invesment split between stocks
    mail_api # email api
if __name__ =="__main__":  
	main()
