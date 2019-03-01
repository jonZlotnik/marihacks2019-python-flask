
# Some initial variables

riddle = "What lie has everybody in this room told to some of the largest organizations in the world?"

correct_answer =  "I have read and agree to the Terms & Conditions."

user_answers_filename = "user_answers.txt"


# Computer asks user a riddle
print(f"\n{riddle}")

# User inputs an answer.
user_input = input(" >> ")

# Persist user's answer to the file. (Append if other answers already submitted)
with open(user_answers_filename, 'a', newline='') as user_answers_file:
    user_answers_file.write(f"{user_input}\r")

# Computer checks answer against correct answer and tells the user how they did.
if user_input == correct_answer:
    print("Correct!!!")
else:
    print("Incorrect.")
    
# Print all answers from file
print("\nPrevious answers given:")
with open(user_answers_filename, 'r', newline='') as user_answers:
    for answer in user_answers:
        print("---")
        print(answer)
