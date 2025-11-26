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
    API_KEY = "STOCK API KEY HERE"
    URL = f"https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={API_KEY}"
    response = requests.get(URL)
    data = response.json()
    low = data.get("top_losers", [])
    active = data.get("most_actively_traded", [])
    high = data.get("top_gainers", [])
    if choice == "low":
        selected = low[:4]
    elif choice == "active":
        selected = active[:4]
    elif choice == "high":
        selected = high[:4]
    else:
        selected = []
    stock_dict = {}
    # Build stock_string OUTSIDE the loop
    stock_string = "\nStock Information:\n-----------------------------------\n"
    for stock in selected:
        ticker = stock.get("ticker")
        overview_url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey={API_KEY}"
        overview_data = requests.get(overview_url).json()
        company_name = overview_data.get("Name", ticker)
        description = overview_data.get("Description", "Description is unavailable.")
        short_description = description[:250] + "..." if len(description) > 250 else description
        stock_dict[company_name] = {
            "symbol": ticker,
            "price": stock.get("price"),
            "change_amount": stock.get("change_amount"),
            "change_percentage": stock.get("change_percentage"),
            "description": short_description}
        # Append to text summary
        stock_string += (
            f"{company_name}\n"
            f"  Symbol: {ticker}\n"
            f"  Price: ${stock.get('price')}\n"
            f"  Change: {stock.get('change_amount')} ({stock.get('change_percentage')})\n"
            f"  Description: {short_description}\n"
            f"-----------------------------------\n")
    print(stock_string)
    # Build email HTML
    stock_message = "<h2><b>Stock Information</b></h2><br>"
    for name, info in stock_dict.items():
        stock_message += (
            f"<b>{name}</b><br>"
            f"<b>Symbol</b>: {info['symbol']}<br>"
            f"<b>Price</b>: ${info['price']}<br>"
            f"<b>Change</b>: {info['change_amount']} ({info['change_percentage']})<br>"
            f"<b>Description</b>: {info['description']}<br><br>")
    return selected, stock_message
def email_api(calc_message, stock_string): # Emails information to user
    email_address = input("\nEnter your email address: ")
    message = Mail(from_email = 'clee24@ramapo.edu',
    				to_emails = email_address,
    				subject ='Stock Portfolio',
    				html_content = f"{stock_string}<br>{calc_message}")
    sg = SendGridAPIClient(api_key='EMAIL API KEY HERE') 
    sg.send(message)
    print("\nYour email has been sent. Don't forget to check your spam folder."
          "\nThank you for using Stock Portfolio Builder.")
def calc_stock(investment, stock_dict): # Calculate cost and number of stocks
    cost = 0.0
    stock_amount = 0
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
    intro = ("SPB will ask you for the amount you would like to invest."
            " SPB will then ask to choose between high, active, or low stock performance." 
            " Based on your choice, 4 stocks and their information will be displayed." 
            " The investment amount will be divided among the 4 stocks." 
            " SPB will ask if you want the stock portfolio emailed to you, and then ask for your email.\n")
    print("\nWelcome to Stock Portfolio Builder (SPB).\n")
    print(intro)
    while True: # while loop until correct input
        try: # try except ValueError
            # Inputs to investment and choice
            print("How much would you like to invest into your stock portfolio?")
            investment = int(input("Please enter an amount in $100 increments: "))
            if investment % 100 == 0:
                print("\nChoose from the following 3 stock categories:\n"
                      "\nLow: Stocks that have dropped the most today."
                      "\nActive: Stocks that were traded the most today."
                      "\nHigh: Stocks that have increased the most today.\n")
                answer = input("Please enter low, active or high: ")
            else:
                print(f"{investment} is not an increment of $100")
                continue
            if answer.lower() in stock_choices: # Checks if choice is in stock_choices
                choice = answer.lower()   
                break
            else:
                print("Please enter a valid input.\n")
        except ValueError:
            print("Please enter a valid input.\n")
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
