# questions = [
#     {
#         "question": "1. What is the output of print(2 * 3 ** 2)?",
#         "A": "12",
#         "B": "18",
#         "C": "36",
#         "D": "None of the above",
        
#     },
#     {
#         "question": "2. Which data type is **immutable** in Python?",
#         "A": "List",
#         "B": "Dictionary",
#         "C": "Tuple",
#         "D": "Set",
        
#     },
#     {
#         "question": "3. Which keyword is used to create a function in Python?",
#         "A": "func",
#         "B": "define",
#         "C": "def",
#         "D": "function",
        
#     },
#     {
#         "question": "4. What does the len() function do?",
#         "A": "Returns the largest number",
#         "B": "Returns the length of an object",
#         "C": "Deletes an element",
#         "D": "Converts to integer",
        
#     },
#     {
#         "question": "5. Which operator is used for floor division?",
#         "A": "/",
#         "B": "//",
#         "C": "% ",
#         "D": "**",
        
#     }
# ]

# def score_calculation(user_answer):

  
  
# counter = 0
# indexing = 0

# while counter <= 5:
#   print(questions[indexing])
#   user_choice = input("Choose options (A/B/C/D):").lower()
#   indexing+=1
#   counter+=1
#   print(score_calculation(user_choice))   


questions = [
    {
        "question": "1. What is the output of print(2 * 3 ** 2)?",
        "A": "12",
        "B": "18",
        "C": "36",
        "D": "None of the above"
    },
    {
        "question": "2. Which data type is immutable in Python?",
        "A": "List",
        "B": "Dictionary",
        "C": "Tuple",
        "D": "Set"
    },
    {
        "question": "3. Which keyword is used to create a function in Python?",
        "A": "func",
        "B": "define",
        "C": "def",
        "D": "function"
    },
    {
        "question": "4. What does the len() function do?",
        "A": "Returns the largest number",
        "B": "Returns the length of an object",
        "C": "Deletes an element",
        "D": "Converts to integer"
    },
    {
        "question": "5. Which operator is used for floor division?",
        "A": "/",
        "B": "//",
        "C": "% ",
        "D": "**"
    }
]

correct_ans = ['a', 'c', 'c', 'b', 'b']
score = 0

def score_calculation(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True
    else:
        return False


for i in range(5):
    q = questions[i]
    print(q)
    print(f"{q['question']}\nA. {q['A']}\nB. {q['B']}\nC. {q['C']}\nD. {q['D']}\n")

    user_choice = input("Choose option (A/B/C/D): ").lower()

    if score_calculation(user_choice, correct_ans[i]):
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {correct_ans[i].upper()}\n")

print(f"Test Over! You scored {score}/5 ({score * 20}%)")
