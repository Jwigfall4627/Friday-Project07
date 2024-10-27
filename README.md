# Friday-Project07
Hello, this is my friday project 7 containing all of the previous weeks friday projects 1-6. 

Friday Project One
---------------------------------------------------------------------------------------------------
Variables:
large_object: Stores a single large object (e.g., "airplane").
large_objects: Stores plural large objects (e.g., "mountains").
adjective: Stores an adjective (e.g., "shiny").
body_part: Stores a body part (e.g., "elbow").
restaurant: Stores the name of a restaurant (e.g., "Burger King").
food1 and food2: Store two types of food (e.g., "pizza" and "ice cream").

Functionality:
The program uses input() to collect the user’s words.
The collected words are then placed into a story template.
Finally, the story with the user’s words inserted is printed out.

User Prompting:
The program prints out instructions for the user.
It then prompts the user to input each required word.

Template Filling:
After gathering the words, it inserts them into a story template using f-string formatting.
The story variable contains the completed Mad Lib.
Output:

Finally, the program prints the entire story with the user's words filled in, giving them a unique and humorous tale.
This code is fully functional, and users only need to run the program to get started on thier mad lib adventure.

Friday Project Two
---------------------------------------------------------------------------------------------------
Greeting:
The program prints a message explaining its purpose to the user.
Random Number Generation:

main_numbers: The program generates a list of five numbers between 1 and 69 using randint.
powerball: It then generates one Powerball number between 1 and 26.
Formatting:

The main numbers are joined by a single space (" ".join(map(str, main_numbers))).
Three spaces are added between the main numbers and the Powerball number.
Output:

Finally, the program prints the complete ticket in the desired format.

Friday Project Three
---------------------------------------------------------------------------------------------------
Variables and functionality: 

import random: Imports Python's random module, which allows the program to generate a random number.
Game Start Prompt:

startOfGame: This variable stores the user’s response to the initial question, "Would you like to play a game?". The response is collected via input().
userStartOfGame: This variable is a preset string "Yes" representing the expected answer to start the game.
Starting the Game:

The if statement checks whether startOfGame (the user’s response) matches "Yes" (the expected answer stored in userStartOfGame).
If the user types "Yes," the game proceeds; otherwise, it ends with no further action.
Game Introduction and Number Generation:

If the game starts, a welcome message is displayed: "Welcome to my guessing game".
computerGeneratedNumber: This variable is assigned a random integer between 1 and 10 using random.randint(1, 10). This is the target number that the user needs to guess correctly.
User Input for Guessing:

UserGeneratedNumber: The variable stores the user's guess, converted to an integer using int(input()).
If the UserGeneratedNumber does not match computerGeneratedNumber, a while loop runs, asking the user to try again. Each time, the correct number (computerGeneratedNumber) is displayed for reference, and the user is prompted to enter another guess.
Once UserGeneratedNumber matches computerGeneratedNumber, the loop ends, and a congratulatory message ("congrats") is displayed.
Exiting the Game:

If the initial answer is not "Yes", the program does nothing further. The "Pleaes try again next time" statement is incorrectly formatted as a string and will not display.

Friday Project Four
---------------------------------------------------------------------------------------------------
trivia_questions: Stores the trivia questions as keys and their respective answers as values.

user_answer: Stores the user’s input for each question in the loop.

correct_answer: Temporarily holds the correct answer for each question during the loop to check against user_answer.
Loop and Conditional Statements:

The for loop iterates over each key-value pair in the dictionary.
Inside the loop, it prompts the user for their answer and checks it against the correct answer.
Feedback is provided based on whether the user’s answer is correct.

Friday Project Five
---------------------------------------------------------------------------------------------------
Functions:
Each function (red_text(), blue_text(), green_text(), yellow_text(), brown_text()) will take one parameter: text.
Each function will use ANSI escape codes to add color formatting to the input text and return the formatted string.
Variables:

text: The parameter for each function, which stores the user-inputted string to be displayed in color.
color_choice: Stores the color selected by the user in the main program logic.
user_text: Stores the text input provided by the user that will be colored based on their selection.
Main Program Logic:

Each color function is called and demonstrated by printing sample text in the respective color.
The program then prompts the user to choose a color and enter text to be displayed.
Using conditional statements, the program calls the appropriate function based on the user's color choice and prints the colored text.

Friday Project Six
---------------------------------------------------------------------------------------------------
Class and Attributes:
BankAccount class has three attributes:
self: Represents the instance of the object itself.
account_number: Stores the account number for the bank account.
balance: Stores the current balance of the account.
Methods:

deposit(): Takes an amount as input, adds it to the balance, and updates the account.
withdraw(): Takes an amount as input, checks if the balance is sufficient, and subtracts the amount if possible.
check_balance(): Returns the current balance of the account.
Variables in the Loop:

user_account_number: Stores the account number entered by the user for validation.
action: Stores the user's choice for deposit, withdrawal, or balance check.
amount: Stores the amount for deposit or withdrawal based on the user’s action.
