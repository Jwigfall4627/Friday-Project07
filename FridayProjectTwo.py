import random

# Greeting message
print("Welcome to the Powerball Number Generator!")
print("This program will generate a Powerball ticket for you with five main numbers and one Powerball number.\n")

# Generate five main numbers between 1 and 69
main_numbers = [random.randint(1, 69) for _ in range(5)]

# Generate one Powerball number between 1 and 26
powerball = random.randint(1, 26)

# Format the ticket with spaces between numbers
ticket = " ".join(map(str, main_numbers)) + "   " + str(powerball)

# Display the generated ticket
print("Your Powerball numbers are:")
print(ticket)
