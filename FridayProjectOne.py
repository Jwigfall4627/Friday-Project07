# Instructions for the user
print("Welcome to the Mad Lib game!")
print("Please follow the prompts and enter words as requested to create a fun story.\n")

# Collecting words from the user
large_object = input("Enter a large object: ")
large_objects = input("Enter large objects (plural): ")
adjective = input("Enter an adjective: ")
body_part = input("Enter a body part: ")
restaurant = input("Enter the name of a restaurant: ")
food1 = input("Enter a type of food: ")
food2 = input("Enter another type of food: ")

# Story template with placeholders for the variables
story = f"""
Once upon a time, there was a massive {large_object} that blocked the path of some {large_objects}.
Everyone in the village thought it was very {adjective}.
Then, one brave soul decided to poke it with their {body_part}.
To everyone's surprise, it led them to a hidden {restaurant} where everything was free!
They ate {food1} and {food2} until they were stuffed and lived happily ever after.
"""

# Display the completed Mad Lib story
print("\nHere's your Mad Lib story!")
