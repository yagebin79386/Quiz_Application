class Question:
    def __init__(self, text, options, correct_option_id):
        self.text = text
        self.options = options
        self.correct_option_id = correct_option_id
        
    def check_answer(self, answer):
        if answer == self.correct_option_id:
            return True
        else:
            return False
