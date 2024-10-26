# Define functions for each color
def red_text(text):
    return f"\033[91m{text}\033[0m"  # ANSI escape code for red

def blue_text(text):
    return f"\033[94m{text}\033[0m"  # ANSI escape code for blue

def green_text(text):
    return f"\033[92m{text}\033[0m"  # ANSI escape code for green

def yellow_text(text):
    return f"\033[93m{text}\033[0m"  # ANSI escape code for yellow

def brown_text(text):
    return f"\033[33m{text}\033[0m"  # ANSI escape code for brown

# Demonstrate each function with sample text
print(red_text("This is red text."))
print(blue_text("This is blue text."))
print(green_text("This is green text."))
print(yellow_text("This is yellow text."))
print(brown_text("This is brown text."))

# Main program logic for user input
print("\nChoose a color to display your text:")
color_choice = input("Enter a color (red, blue, green, yellow, brown): ").strip().lower()
user_text = input("Enter the text you want to display in this color: ")

# Display the user's text in the chosen color
if color_choice == "red":
    print(red_text(user_text))
elif color_choice == "blue":
    print(blue_text(user_text))
elif color_choice == "green":
    print(green_text(user_text))
elif color_choice == "yellow":
    print(yellow_text(user_text))
elif color_choice == "brown":
    print(brown_text(user_text))
else:
    print("Sorry, that color option is not available.")
