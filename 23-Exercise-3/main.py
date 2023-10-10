print("==========================================================================")
print("Welcome To Kaun Banega Crorepati".center(70))
print("==========================================================================")

current_question = 0
cash = 0
amount = 50_000

# Define the questions, options and answers
questions_list = ["What is the capital of France?", "Which planet is known as the 'Red Planet'?",
                  "Which of the following is not a primary color used in color theory?",
                  "Which famous physicist formulated the theory of relativity, E=mc^2?"]
options_list = [["London", "Paris", "New York", "Dublin"], ["Mars", "Jupiter", "Mercury", "Venus"],
                ["Red", "Blue", "Yellow", "Black"],
                ["Albert Einstein", "Stephen Hawking", "Isaac Newton", "Nikola Tesla"]]
answers_list = [1, 0, 3, 0]

# Display the questions and options
while True:
    # Check if the questions are over or not
    if current_question >= len(questions_list):
        break
    else:
        print("\n==========================================================================")
        print(questions_list[current_question])
        print(options_list[current_question])
        user_answer = int(input("Enter your answer (1, 2, 3, 4): "))
        correct_answer = answers_list[current_question]

        # Check if the answer is correct or not
        if correct_answer == (user_answer - 1):
            cash += amount
            print("You have won " + "$" + str(cash))
        else:
            if cash > 0:
                cash -= amount
                print("\n Oops! That was a wrong answer. Now you have " + "$" + str(cash) + ".")
            else:
                if cash == 0:
                    print("You have not won any money.")
                else:
                    print("You have $" + str(cash) + ".")
        current_question += 1
        print("==========================================================================\n")

max_amount = amount * len(questions_list)

# Display the final result
if cash == max_amount:
    print("Yippee! You have answered all the questions correctly. and You received" + " $" + str(cash) + ".")
else:
    if cash == 0:
        print("Sorry, You have not won any money.")
    else:
        print("You have won " + "$" + str(cash) + ".")
