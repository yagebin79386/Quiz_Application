#1. Task Description
This project is intended to design a Quiz application using Python with User interface.
The quiz question is randomly generated as sample for the quiz, the Quiz relevant
data is saved then to the PostgreSQL db. And user should be able to choose the answer in
an interactive user interface and to the end, the window should show up the final score 
of the Quiz.

#2. Implement the Quiz
##2.1 Generate the Quiz content:
Question 1:
What is the correct way to declare a list in Python?
a) list = {1, 2, 3}
b) list = [1, 2, 3] (Correct)
c) list = (1, 2, 3)
d) list = <1, 2, 3>

Question 2:
Which of the following is used to create an immutable collection of items in Python?
a) List
b) Set
c) Tuple (Correct)
d) Dictionary

Question 3:
What will be the output of the following code?
python
Copy code
print(2 ** 3)
a) 5
b) 6
c) 8 (Correct)
d) 9
![image](https://github.com/user-attachments/assets/6eace848-1501-4fdb-90e5-f2da82703d6b)

##2.2 Write hard-coded CLI quiz application using the given quiz content
So the logic is to create the functions for question and answer to script namely question.py and option.py,
after that import the both functions in the main.py to call for the logical quiz.

##2.3 Create the Quiz database using pgAdmin4. You can find the sql save in this create_quiz_db.sql

##2.4 Call the data from created Quiz db using psycopg2 to rewrite the main.py to release the Q&A logic, please find the code in Quiz_db.py

##2.5 Using the library PyQt5 to create the UI to integrate the previous logic. Please find the code in Quiz_app.py.
