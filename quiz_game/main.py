from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []  # create an empty list for assignment purposes
for question in question_data:  # for loop to run through each question in the list of dictionaries
    question_text = question['text']        # grabs the text from the dict
    question_answer = question['answer']    # grabs the answer from the dict
    new_question = Question(question_text, question_answer)  # assigns the current text and answer to a variable
    # and passes that variable to the Question Class for storage
    question_bank.append(new_question)      # appends each question (text and answer) to the list, same as above

quiz = QuizBrain(question_bank)             # creates a variable from the QuizBrain class. in this situation its
# num of questions and a list of questions
quiz.next_question()                        # calls the module next question

while quiz.questions_remaining():
    quiz.next_question()

print('Congrats! You have completed the quiz')
print(f'Your final score was: {quiz.score}/{quiz.question_num}')
