# 1. Computer asks user a riddle
print("\nHow much wood would a woodchuck chuck if a woodchuck could chuck wood?")

# 2. User inputs an answer.
user_answer = input("\nPlease enter your answer on the next line: \n\n>>")

# 3. Computer saves user’s answer to a persistent file.

with open('persistent_answers.txt', 'a') as persistent_answers_file:
    persistent_answers_file.write(f"{user_answer} \n")

# 4. Computer checks answer against correct answer.
correct_answer = "A woodchuck would chuck as much as a woodchuck could chuck if a woodchuck could chuck wood."

# 5. Computer responds with a message letting the user know how they did.
if correct_answer.lower() is user_answer.lower():
    print("\nCorrect!")
else:
    print(f"\nIncorrect.\n\nThe answer is:\n{correct_answer}")

# 6. They can see all the responses from the past entries.
with open('persistent_answers.txt', 'r') as persistent_answers_file:
    print("\n\nPrevious answers submitted:\n")
    for line in persistent_answers_file:
        print(f"{line}")
