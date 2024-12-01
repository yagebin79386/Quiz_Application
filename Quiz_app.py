import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
from Quiz_db import get_questions_and_options

import psycopg2


class Quiz(QWidget):
    def __init__(self):
        super().__init__()
        
        #initialize class attributes
        self.score_count = 0
        self.question_num = 1
        self.questions = []
        self.options = []
         
        #load data from the database
        self.get_db_data()

        #create the layout instance for the widget
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        #set up the initial page
        self.page(self.question_num)

    def get_db_data(self):
            self.questions, self.options = get_questions_and_options()        

    def on_click(self, option_num):
        #check if the selected option is correct
        current_question_id = self.questions[self.question_num -1][0]
        current_options = [opt for opt in self.options if opt[2] == current_question_id]

        if current_options[option_num][1]:
            self.score_count += 1                
        
        self.question_num += 1
        
        #check if there are more questions
        if self.question_num <= len(self.questions):
            self.page(self.question_num)
        else:
            self.show_final_score(self.score_count)
        
            
                        
                 
    def page(self, question_num):
        self.clear_layout()
        
        #set window property
        self.setWindowTitle("The Quiz about Python")
        self.setGeometry(100, 100, 600, 400)
        
        #get the current questions and options
        current_question = self.questions[question_num - 1][1]
        current_question_id = self.questions[question_num - 1][0]
        current_options = [opt for opt in self.options if opt[2] == current_question_id]
        #Set Labels        
        self.label_t = QLabel(f"This is question {question_num}", self)
        self.label_t.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_t, 0, 0, 1, 2)

        
        self.label_q = QLabel(current_question, self)        
        self.label_q.setStyleSheet("""
            QLabel {
                background-color: #f0f8ff;  /* Light blue background */
                border: 2px solid #4682b4;  /* Steel blue border */
                border-radius: 10px;
                font-size: 18px;  /* Larger font for the question */
                font-weight: bold;
                color: #2f4f4f;  /* Dark slate gray text */
                padding: 10px;
            }
        """)
        self.label_q.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.label_q, 1, 0, 1, 2)
        
        self.label_s = QLabel(f"Score: {self.score_count}/{len(self.questions)}", self)
        self.layout.addWidget(self.label_s, 0, 2, 1, 1)
    
        #Set buttons
        self.buttons = []
        for i, (choice, is_correct, *_) in enumerate(current_options):
            button = QPushButton(choice, self)
            button.setStyleSheet("""
                QPushButton {
                    background-color: lightblue;
                    border: 2px solid black;
                    border-radius: 10px;
                    padding: 10px;
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: lightgreen;
                }
            """)
            #connect the button to a function with ordinal data
            button.clicked.connect(lambda checked, option_num=i: self.on_click(option_num))
            self.buttons.append(button)

            #ad button to grid layout
            row = 2 + i //2
            column = (i+1) % 2
            self.layout.addWidget(button, row, column)
                
    #clear the existing layout before reassigning self.layout
    def clear_layout(self):
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    
    #print final score when over
    def show_final_score(self, score_count):
        # Debugging print statements
        print(f"DEBUG: Final score: {self.score_count}")
        print(f"DEBUG: Total questions: {len(self.questions)}")

        # Clear the current layout
        self.clear_layout()

        # Update the window title
        self.setWindowTitle("Quiz Finished")

        # Add the final score label
        final_score_label = QLabel(f"Quiz Complete! Your final score: {self.score_count}/{len(self.questions)}")
        final_score_label.setStyleSheet("""
            QLabel {
                background-color: #f0f8ff;  /* Light blue background */
                border: 10px solid #4682b4;  /* Steel blue border */
                border-radius: 10px;
                font-size: 18px;  /* Larger font for the question */
                font-weight: bold;
                color: #2f4f4f;  /* Dark slate gray text */
                padding: 10px;
            }
        """)
        final_score_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(final_score_label)

        # Force layout refresh
        self.resize(self.width() - 1, self.height() - 1)
        self.resize(self.width() + 1, self.height() + 1)




# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create QApplication first
    window = Quiz()               # Create the Quiz widget
    window.show()                 # Display the widget
    app.exec_()         # Start the event loop





