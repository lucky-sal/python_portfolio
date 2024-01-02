class QuizBrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):

        current_question = self.question_list[self.question_num]  # from the list of questions, grabs the current question list and assigns it to this object
        self.question_num += 1
        user_answer = input(f'Q.{self.question_num}: {current_question.text} (True/False)?: ')
        self.check_answer(user_answer, current_question.answer)

    def questions_remaining(self):
        return self.question_num < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('Correct!')
        else:
            print('Sorry that was incorrect')
        print(f'The correct answer was {correct_answer}')
        print(f'Your current score is: {self.score}/{self.question_num}\n\n')