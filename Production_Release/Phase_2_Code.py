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
def stock_api(choice): # Gets stock information and returns info
    # Variables
    API_KEY = "STOCK API KEY HERE"
    URL = f"https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={API_KEY}"
    response = requests.get(URL) # API get call
    data = response.json() # Variable for get data
    low = data.get("top_losers", [])
    active = data.get("most_actively_traded", [])
    high = data.get("top_gainers", [])
    if choice == "low": # if elif else to check choice
        selected = low[:4]
    elif choice == "active":
        selected = active[:4]
    elif choice == "high":
        selected = high[:4]
    else:
        selected = []
    stock_dict = {}
    for i, stock in enumerate(selected): # for loop to create stock_dict
        stock_dict[f"Stock {i+1}"] = {
            "symbol": stock.get("ticker"),
            "price": stock.get("price"),
            "change_amount": stock.get("change_amount"),
            "change_percentage": stock.get("change_percentage")}
    stock_string = "Stock Information:\n"
    stock_string += "-----------------------------------\n"
    for key, info in stock_dict.items(): # for loop to create stock_string
        stock_string += (
            f"{key}:\n"
            f"  Symbol: {info['symbol']}\n"
            f"  Price: ${info['price']}\n"
            f"  Change: {info['change_amount']} ({info['change_percentage']})\n"
            f"-----------------------------------\n")
    print(stock_string) # Output stock_string: stock information
    stock_message = "<h2><b>Stock Information</b><br></h2>"
    for key, info in stock_dict.items(): # for loop to create stock_string for email
        stock_message += (
            f"<b>{key}</b><br>"
            f"  Symbol: {info['symbol']}<br>"
            f"  Price: ${info['price']}<br>"
            f"  Change: {info['change_amount']} ({info['change_percentage']})<br><br>")
    return selected, stock_message # Return selected, stock_string
def email_api(calc_message, stock_string): # Emails information to user
    email_address = input("\nEnter your email address: ")
    message = Mail(from_email = 'clee24@ramapo.edu',
    				to_emails = email_address,
    				subject ='Stock Portfolio',
    				html_content = f"{stock_string}<br>{calc_message}")
    sg = SendGridAPIClient(api_key='EMAIL API KEY HERE') 
    response = sg.send(message)
    print("\nYour email has been sent.\nThank you for using Stock Portfolio Builder.")
def calc_stock(investment, stock_dict): # Calculate cost and number of stocks
    cost = 0.0
    stock_amount = 0
    email_message = {}
    for number in range(0, 4): # Adds all 4 stocks
        stock = float(stock_dict[number]['price'])
        cost += stock # The cost to buy 1 of each stock
    stock_amount = int(investment // cost) # Number of each stock purchased
    total = round(stock_amount * cost,2) # Total cost of purchased stocks
    remainder = round(investment - total,2) # Remaining balance after purchase
    print(f"Starting Balance: ${investment}\nVolume of each stock: {stock_amount}\n"
          f"Investment: ${total}\nEnding balance: ${remainder}")
    calc_string = (f"""<h2><b>Investment Information</b></h2><br>
                   <b>Starting Balance</b>: ${investment}<br><br>
                   <b>Volume of each stock</b>: {stock_amount}<br><br>
                   <b>Investment</b>: ${total}<br><br>
                   <b>Ending Balance</b>: ${remainder}<br><br>""")
    return calc_string # Return output for email
def main(): # Main Program
    # Variables
    stock_choices = ("low", "active", "high")
    print("\nWelcome to Stock Portfolio Builder.\n")
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
    stock_dict, stock_string = stock_api(choice) # Get stock information
    calc_message = calc_stock(investment, stock_dict) # Calculate stocks and investment
    while True: # while True loop for email input
        email = input("\nDo you want this information emailed to you?\nYes or No: ")
        if email.lower() == "yes": # if elif else check if user wants email
            email_api(calc_message, stock_string) # Email stock portfolio to user
            break
        elif email.lower() == "no":
            break
        else:
            print(f"{email} is not a valid input.")       
if __name__ =="__main__":  
	main()
