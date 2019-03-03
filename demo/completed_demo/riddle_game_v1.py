# -------------------------------- #
#   Riddle Game v1 (Basics)
#   Variables, Input, Conditionals
#   By: Jon Zlotnik
# -------------------------------- #

# Some initial variables
riddle = "What lie has everybody told to some of the largest organizations in the world?"
correct_answer =  "I have read and agree to the Terms & Conditions."


# Computer asks user a riddle
print(riddle)


# User inputs an answer.
user_input = input(" >> ")


# Computer checks answer against correct answer and tells the user how they did.
if user_input == correct_answer:
    print("Correct!!!")
else:
    print("Incorrect.")
