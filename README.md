# tcp-quiz-python
   
Project: Quiz using TCP in Python
Author: Rakulan Srinivasan

Development Platform: Visual Studio Code  
Language: Python 3.10 for Application
	  JSON for Static Data
Libraries used: ‘tkinter’ for GUI
		‘socket’ for establishing TCP connection
		‘os’ for Communication with the Operating System
		‘json’ for data extraction from JSON files
Application: TCP/IP Transport and Application Layer


Scripts: TCPclient.py
	 main_server.py
	 science_quiz.py
	 gk_quiz.py
	 comp_fun_quiz.py

Data Files: science_questions.json
	    gk_questions.json
	    comp_fun_questions.json

Image Files: baseline_check_black_24dp.png
	     baseline_skip_next_black_24dp.png
	     baseline_skip_previous_black_24dp.png
	     outline_computer_black_24dp.png
	     outline_launch_black_24dp.png
	     outline_link_black_24dp.gif
	     outline_psychology_black_24dp.png
	     outline_restart_black_24dp.png
	     outline_science_black_24dp.png
	     outline_thumb_up_off_alt_black_24dp.png
	     outline_quiz_black_24dp.png

About: The project contains some python (.py) scripts for the client-server model discussed.
The main_server.py gives the Main Menu as a start page. The main_server.py and the TCPclient.py has to be run at first
to establish a connection between the quiz server and client. Once the main menu opens after connection, the user can select
the subject and proceedd to the respective quizzes.
The questions, options and answers, for each of the subjects are stored in JSON (.json) files,
which are parsed in the respective python scripts, called upon requirement.

Working: Once the user selects their subject, the respective quiz opens, with questions with multiple choices,
with option to select only one answer. The user can anytime perform bi-direction traversal through the questions,
and change their options, if needed. Once the user arrives at the last question, the 'Next' button acts as a submit
button to end the quiz. The scores are calculated based on the correct options available on the respective JSON files
and are displayed in a Message Box. Once the user, gets the scores and acknowledges, the quiz terminates and the main_server.py
becomes unresponsive.
