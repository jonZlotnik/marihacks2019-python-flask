# -------------------------------- #
#   Riddle Game v3 (Refactoring)
#   Functions
#   By: Jon Zlotnik
# -------------------------------- #

user_answers_filename = "user_answers.txt"

def get_riddle():
    riddle = "What lie has everybody in this room told to some of the largest organizations in the world?"
    return f"\n{riddle}"


def get_correct_answer():
    correct_answer =  "I have read and agree to the Terms & Conditions."
    return correct_answer


def cli_get_user_answer():
    user_input = input(" >> ")
    return user_input


def append_user_answer_to_file(filename, answer):
    with open(user_answers_filename, 'a') as user_answers_file:
        user_answers_file.write(f"{answer}\r")


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True
    else:
        return False


def get_past_answers_from_file(filename):
    with open(user_answers_filename, 'r') as user_answers:
        past_answers = user_answers.readlines()
    return past_answers

if __name__ == "__main__":

    # 1. Computer asks a riddle
    print(get_riddle())

    # 2. User inputs an answer
    user_answer = cli_get_user_answer()

    # 3. Computer saves user’s answer to a persistent file
    append_user_answer_to_file(user_answers_filename, user_answer)

    # 4. Computer checks answer against correct answer
    # 5. Computer responds with a message letting the user know how they did.
    if check_answer(user_answer, get_correct_answer()):
        print("Correct!!!")
    else:
        print("Incorrect.")
    
    # 6. Computer shows past user attempts at the riddle.
    print("\nPrevious answers given:")
    print( get_past_answers_from_file(user_answers_filename) )
    
