
# Some initial variables

riddle = "What lie has everybody in this room told to some of the largest organizations in the world?"

correct_answer =  "I have read and agree to the Terms & Conditions."


# 1. Computer asks user a riddle

print(riddle)


# 2. User inputs an answer.

user_input = input(" >> ")


# 3. Computer checks answer against correct answer and tells the user how they did.

if user_input == correct_answer:
    print("Correct!!!")
else:
    print("Incorrect.")
