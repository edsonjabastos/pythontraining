class Question:
    def __init__(self,
                 q_text,
                 q_answer,
                 q_category,
                 q_type,
                 q_difficulty,
                 q_incorrect_answers
                 ):
        print("Creating question...")
        self.text = q_text
        self.answer = q_answer
        self.category = q_category
        self.type = q_type
        self.difficulty = q_difficulty
        self.incorrect_answers = q_incorrect_answers

# q1 = Question('2+3=5', 'True')
