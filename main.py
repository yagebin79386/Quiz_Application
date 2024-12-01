from question import Question
from option import Option
import psycopg2

options = []
questions = []

options.append(Option(1, "list = {1, 2, 3}"))
options.append(Option(2, "list = [1, 2, 3]"))
options.append(Option(3, "list = (1, 2, 3)"))
options.append(Option(4, "list = <1, 2, 3>"))
questions.append(Question("What is the correct way to declare a list in Python?", options, 2))
options = []

options.append(Option(5, "List"))
options.append(Option(6, "Set"))
options.append(Option(7, "Tuple"))
options.append(Option(8, "Dictionary"))
questions.append(Question("Which of the following is used to create an immutable collection of items in Python?", options, 3))
options = []


options.append(Option(1, "5"))
options.append(Option(2, "6"))
options.append(Option(3, "8"))
options.append(Option(4, "9"))
questions.append(Question("What will be the output of the following code?", options, 3))

score = 0

for question in questions:
    print(question.text)
    for option in question.options:
        print(option.option_id, "-", option.text)
    answer = int(input("Please input the correct answer"))
    if (question.check_answer(answer)):
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

print("Quiz completed. Your score is", score, "/", len(questions))



##Function to call db
def play():
    conn = psycopg2.connect(
    dbname = "quiz",
    user = "postgres",
    password="admin",
    host="localhost",
    port="5432"    
    )
    cur.execute("select question_id, question_text from question")
    questiondb = cur.fetchall()
    for question in questiondb:
        question_num = question[0]
        print(question)
        cur.execute("select option_text from option where question_id = "+ question_num +"")
        options =
