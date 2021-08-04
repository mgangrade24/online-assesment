

https://user-images.githubusercontent.com/57436780/128131046-c9a60b1d-9fde-467a-996b-82992693837e.mp4

# online-assesment
This is an online assesment platform made by Mousam, Nirmal and Abhishek.
The web application is made over the python's flask framework as backend, uses Jinja2 as the templating engine and for frontend we have used HTML/CSS/JS and Bootstrap4.

Frontend part is done by Nirmal.
Backend part in flask is done by Mousam.
And, javascript functionallity and the file handling is done by Abhishek.

A deployed version can be checked here: https://online-assessment-final.herokuapp.com/


## We worked for the following specifications:

1. Assessment shall be MCQ pattern
2. There must be a question pool for the assessment: We used a csv file conating questions, options and the correct answer.
3. The questions displayed in the assessment shall be only from that pool
4. Number of questions in the pool shall be more than questions displayed
5. Set a time limit for the assessment (individual timer for a question/optional): Test gets auto submitted after the given time ends.
6. Question order shall be shuffled for each candidate appearing: Questions get shuffled after we restart the application.
7. Assessment score shall be generated at the time of submission
