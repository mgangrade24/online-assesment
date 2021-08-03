import random, csv
from flask import Flask, render_template, request

app = Flask(__name__)


class Question:
    q_id = -1
    question = ""
    option1 = ""
    option2 = ""
    option3 = ""
    option4 = ""
    correctOption = -1

    def __init__(self, q_id, question, option1, option2, option3, option4, correctOption):
        self.q_id = q_id
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.correctOption = correctOption

    def getCorrectOption(self):
        if self.correctOption == 1:
            return self.option1
        elif self.correctOption == 2:
            return self.option2
        elif self.correctOption == 3:
            return self.option3
        elif self.correctOption == 4:
            return self.option4
    


#List to fetch Question object from csv file.
qlist = []

with open('static/questions/questions.csv', newline='') as f:
  reader = csv.reader(f)
  for row in reader:
      id = int(row[0])
      ques = row[1]
      op1 = row[2]
      op2 = row[3]
      op3 = row[4]
      op4 = row[5]
      corr = int(row[6])


      q = Question(id,ques,op1,op2,op3,op4,corr)
      qlist.append(q)




n = 5 #Number of questions to display
questions_list = random.sample(qlist, n) #shuffeled list






@app.route('/')
def index():
    return render_template('index.html', total = n)

@app.route("/quiz")
def quiz():
    return render_template('quiz.html', question_list = questions_list)

@app.route("/submitquiz", methods=['POST', 'GET'])
def submit():
    correct = 0
    for question in questions_list:
        question_id = str(question.q_id)
        selected_option = request.form.get(question_id)
        correct_option = question.getCorrectOption()
        if selected_option == correct_option:
            correct = correct + 1



        
    correct = str(correct)

    msg = "You scored "+ correct
    return render_template("score.html", score = correct, total = n)


if __name__ == '__main__':
    app.run(debug=True)
