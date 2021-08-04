

https://user-images.githubusercontent.com/57436780/128131046-c9a60b1d-9fde-467a-996b-82992693837e.mp4

# online-assesment
This is an online assesment platform made by Mousam, Nirmal and Abhishek.
The web application is made over the python's flask framework as backend, uses Jinja2 as the templating engine and for frontend we have used HTML/CSS/JS and Bootstrap4.

Frontend part is done by Nirmal.
Backend part in flask is done by Mousam.
And, javascript functionallity and the file handling is done by Abhishek.

A deployed version can be checked here: https://online-assessment-final.herokuapp.com/


## Tech Stack Used:
1. Frontend: HTML5, CSS3, Javascript
2. Backend: Python 3.8, Flask 1.1.2, Jinja2 2.11.2
3. Database: csv file


## Project Setup:
1. Clone this repository in your local system.
2. Local system must have python pre-installed in it.
3. Open the command prompt in the project folder and execute following commands:
  * `pip install Flask`
  * `pip install Jinja2`
4. After installing the above dependencies just run the `<controller.py>` file.
5. This will run the project over http://127.0.0.1:5000/
6. For the reshuffling property of the project, the `controller.py` file need to be re-run.


## Deployment:
For deployment we have used `Heroku` as a platform. The project works fine there too, only the restarting of the server again is not possible on heroku so there it can show the similar questions again, but in the local machine we can re-run the flask app to get different and the shuffled questions from the pool.




## We worked for the following specifications:

1. Assessment shall be MCQ pattern
2. There must be a question pool for the assessment: We used a csv file conating questions, options and the correct answer.
3. The questions displayed in the assessment shall be only from that pool
4. Number of questions in the pool shall be more than questions displayed
5. Set a time limit for the assessment (individual timer for a question/optional): Test gets auto submitted after the given time ends.
6. Question order shall be shuffled for each candidate appearing: Questions get shuffled after we restart the application.
7. Assessment score shall be generated at the time of submission
