# Define the trivia questions and answers
trivia_questions = {
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What is the capital of Japan?": "Tokyo",
    "Which element has the atomic number 1?": "Hydrogen",
    "In what year did the Titanic sink?": "1912"
}

# Greeting message
print("Welcome to the Trivia Quiz! Answer each question to the best of your ability.\n")

# Loop through the dictionary and ask each question
for question, correct_answer in trivia_questions.items():
    # Display the question
    print(question)
    
    # Get the user's answer
    user_answer = input("Your answer: ")
    
    # Check if the user's answer matches the correct answer
    if user_answer.strip().lower() == correct_answer.lower():
        print("Correct!\n")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.\n")

print("Thank you for playing the Trivia Quiz!") 