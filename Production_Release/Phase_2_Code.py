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
def stock_api(choice):
    API_KEY = ("STOCK KEY HERE")
    URL = (f"https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={API_KEY}")
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
def email_api(calc_message): # Email API
    message = Mail(from_email = 'clee24@ramapo.edu',
    				to_emails ='clee24@ramapo.edu',
    				subject ='Stock Portfolio',
    				html_content = f"""<div>Investment: {calc_message['Investment']}</div>
                    <div>Number of each stock: {calc_message['Stocks']}</div>
                    <div>Remaining balance: {calc_message['Remainder']}</div>""")
    sg = SendGridAPIClient(api_key='EMAIL KEY HERE') 
    response = sg.send(message)
def calc_stock(investment, stock_info): # Calculate cost and number of stocks
    cost = 0.0
    stock_amount = 0
    email_message = {}
    for number in range(0, 4): # Adds all 4 stocks
        stock = float(stock_info[number]['price'])
        cost += stock # The cost to buy 1 of each stock
    stock_amount = int(investment // cost) # Number of each stock purchased
    total = round(stock_amount * cost,2) # Total cost of purchased stocks
    remainder = round(investment - total,2) # Remaining balance after purchase
    print(f"Investment: {total}\nNumber of each stock: {stock_amount}\nRemaining balance: {remainder}")
    email_message = {'Investment':total,
                     'Stocks': stock_amount,
                     'Remainder': remainder} # Dictionary information for email
    return(email_message)
def main(): # Main Program
    # Variables
    stock_choices = ("low", "active", "high")
    print("Welcome to Stock Portfolio Builder\n")
    while True: # while loop until correct input
        try: # try except ValueError
            # Inputs to investment and choice
            investment = int(input("How much would you like to invest into your stock portfolio? "))
            print("\nLow: Stocks with largest drop in value today.")
            print("Active: Stocks with the highest trading volume today.")
            print("High: Stocks with the largest rise in value today.\n")
            choice = input("Please choose between low, active or high stock performance: ")
            print("")
            if choice.lower() in stock_choices: # Checks if choice is in stock_choices
                break
            else:
                print("Please enter a valid input.")
        except ValueError:
            print("Please enter a valid input.")
    stock_info = stock_api(choice) # Get stock information
    calc_message = calc_stock(investment, stock_info) # Calculate stocks and investment 
    email_api(calc_message) # Email stock portfolio to user
if __name__ =="__main__":  
	main()
