"""
INFO-233 Group Project
Project Name: Stock Portfolio Builder
Team Name: Spyder01
Group 1
"""
# Modules
import requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
# Functions
def stock_api(): # Stock API
    pass 
API_KEY="API KEY GOES HERE"
URL = f"https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={API_KEY}"
def stock_api(choice):
response = requests.get(URL)
data = response.json()

low = data.get("top_losers", [])
active = data.get("most_actively_traded", [])
high = data.get("top_gainers", [])

if choice == "low":
    return low[:4]
elif choice == "active":
    return active[:4]
elif choice == "high":
    return high[:4]
return []
def mail_api(): # Email API
    message = Mail(from_email = 'whatevermail@gmail.com',
    				to_emails ='whateveremail@gmail.com',
    				subject ='Testing the SendGrid API for our group project',
    				html_content ='Hello, this is to see if I called the API correctly.')
	sg = SendGridAPIClient(api_key='') 
	response = sg.send(message)
	print(response.status_code, response.body)
def calc_stock(investment, stock_info): # Calculate cost and number of stocks
    pass
    # cost = stock_info[4 stocks] # The cost to buy 1 of each stock
    # stock_amount = investment / cost # Number of each stock purchased
    # total = stock_amount * cost # Total cost of purchased stocks
    # return stock_amount, total # Returns total and number of stocks
def main(): # Main Program
    # Variables
    stock_choices = ("low", "active", "high")
    print("Welcome to Stock Portfolio Builder\n")
    while True:
        try:
            # Inputs to investment and choice
            investment = int(input("How much would you like to invest into your stock portfolio? "))
            print("\nLow: Stocks with largest drop in value today.")
            print("Active: Stocks with the highest trading volume today.")
            print("High: Stocks with the largest rise in value today.\n")
            choice = input("Please choose between low, active or high stock performance: ")
            if choice.lower() in stock_choices:
                break
            else:
                print("Please enter a valid input.")
        except ValueError:
            print("Please enter a valid input.")
#    stock_info = stock_api(choice) # get 4 stock prices and info
#    stock_amount, total_cost = calc_stock(investment, stock_info) # Calculate invesment split between stocks
#    mail_api # email stock portfolio to user
if __name__ =="__main__":  
	main()
