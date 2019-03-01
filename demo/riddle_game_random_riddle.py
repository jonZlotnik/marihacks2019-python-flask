import random

riddles = [
    {
        "riddle":   "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
        "solution": "A woodchuck would chuck as much as a woodchuck could chuck if a woodchuck could chuck wood."
    },
    {
        "riddle":   "Why did the chicken cross the road?",
        "solution": "To get to the other side."
    },
    {
        "riddle":   "What is a cation afraid of?",
        "solution": "A dogion."
    }
]

def get_random_riddle():
    riddle_id = random.randint(0, len(riddles)-1)
    return riddles[riddle_id]