import psycopg2

def get_questions_and_options():
    """
    Retrieve questions and options from the database.
    Returns:
        questions (list of tuples): List of (question_id, question_text).
        options (list of tuples): List of (option_text, option_correct).
    """
    conn = psycopg2.connect(
        dbname="Quiz",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    # Fetch all questions
    cur.execute("SELECT question_id, question_text FROM question")
    questions = cur.fetchall()

    # Fetch all options
    cur.execute("SELECT option_text, option_correct, question_id FROM option")
    options = cur.fetchall()

    conn.close()
    return questions, options


def play():
    """
    Interactive CLI quiz game.
    """
    # Retrieve questions and options
    questions, options = get_questions_and_options()
    score = 0

    # Interactive quiz logic
    for question in questions:
        question_num = str(question[0])
        print(question)
        question_options = [opt for opt in options if opt[2] == question[0]]

        index = 1
        for option in question_options:
            print(index, option[0])
            index += 1

        answer = int(input("Please input the correct answer")) - 1
        if 1 <= answer + 1 <= 4:
            if question_options[answer][1]:
                print("Correct!")
                score += 1
        else:
            print("Incorrect.")

    print("You have correctly answered", score, "/", len(questions), "questions.")


if __name__ == "__main__":
    # Call the interactive CLI function only when running this script directly
    play()
