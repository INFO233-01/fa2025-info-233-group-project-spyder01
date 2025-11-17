# Group Project Phase I

INFO-233 Group Project – Phase I – Project Definition
Project Name:
Team Name:

1.	Define the problem you are trying to solve. 
2.	How does your program help to solve the problem?
3.	Who will be the users of this program. Detail at least two Use Cases
a.	Use Case 1
b.	Use Case 2
4.	What technology is available to solve the problem?  Identify the specific APIs and Modules to be used for the program.
5.	Detail the sequence of the program- What is the flow of the program? How does a user use the program. 

a.	Break up the work in parts to allow the developers to work on the coding in the next phase. Have at least as many parts as there are team members: Some examples can be: User Input, Communications – APIs, Modules, Function Declaration, Research, Exception Handling

## STOCK PORTFOLIO BUILDER

**Stock Portfolio Builder (SPB)** by Spyder01 will help people build a diversified stock portfolio. The program is intended for any new to veteran level investors of the stock market. For example, veterans would likely use it to create a new diversified portfolio. A new investor may focus more on the statistics displayed about each stock while building his first portfolio.

**Stock Portfolio Builder (SPB)** works by asking the user for an investment amount and stocks the user is interested in. SPB will use the Yahoo Stocks API to look up information on the user’s stocks. SPB will display selected information on the stocks and individually ask how many stocks the user would like to purchase. The amount will be subtracted from the total amount and displayed after each input. After the last stock, SPB will display the contents of the stock portfolio and ask if the user would like to make any changes. If changes are required, a menu with options will appear to assist in changes to the stock portfolio until the user is satisfied. 

### Stock Portfolio Builder Input and Output

1. APP : How much would you like to invest into your stock portfolio?
2. USER : 10000
3. APP : Which stocks are you interested in?
4. USER : TSLA, COST, WMT, META, NVDA
5. APP : {Displays information about each stock}
6. APP : {Asks how much user wants of each stock individually}
7. USER : {Inputs the number of stocks for each one}
8. APP : {Displays stock portfolio}
9. APP : Would you like to make any changes?
10. USER : No
11. APP : Thank you for using Stock Portfolio Builder.

### Stock Portfolio Builder Program Breakdown
- Modules
- Functions 
- Error Handling
- User Input
- Variables
- Communication
