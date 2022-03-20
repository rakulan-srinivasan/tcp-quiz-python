from tkinter import *
from json import *
import os
from tkinter import messagebox

question_no=0
selections = [0]*9
with open('science_questions.json') as sqj:
    science_quiz_json = load(sqj)
questions = (science_quiz_json['question'])
options = (science_quiz_json['options'])
answers = (science_quiz_json[ 'answer'])

def start_quiz():
    gk_window = Tk()
    gk_window.title('TCP Quiz - Science Quiz Server')
    gk_window.geometry('800x600+320+10')
    gk_window.resizable(0,0)

    title_frame = Frame(gk_window, bg='#88B2CC', width=800, height=50)
    title_frame.pack()
    
    global questions_frame
    questions_frame = Frame(gk_window, bg='#E7D4C0', width=800, height=500)
    questions_frame.pack()

    global button_frame
    button_frame = Frame(gk_window, width=800, height=50)
    button_frame.pack()

    global helv12
    helv12 = ('Helvetica', 12, 'bold')
    button_response_color = '#DE3163'

    title_label = Label(title_frame, text = 'Welcome to TCP Science Quiz', width = 800, bg = '#88B2CC', font=helv12, justify='center')
    title_label.pack(padx=10,pady=10)

    def on_enter_button_frame(e):
        e.widget['background']= '#6495ED'
    def on_leave_button_frame(e):
        e.widget['background']='#E98973'

    global previous_button
    previous_button = Button(button_frame, text=' Previous',font=helv12, height=80, bg='#E98973',width=10, activebackground=button_response_color, command=previous)    
    previous_button.pack(side=LEFT,padx=(10,200),pady=10)
    previous_button.bind('<Enter>',on_enter_button_frame)
    previous_button.bind('<Leave>',on_leave_button_frame)

    global next_button
    next_button = Button(button_frame, text='Next ',font=helv12, height=80, bg='#E98973',width=10, activebackground=button_response_color, command=next)    
    next_button.pack(side=RIGHT,padx=(200,10),pady=10)
    next_button.bind('<Enter>',on_enter_button_frame)
    next_button.bind('<Leave>',on_leave_button_frame)

    global option_selected
    option_selected = IntVar(master=questions_frame, value=0)

    display_questions()
    display_options()
    gk_window.update()
    gk_window.mainloop()  
    pass

def previous():
    global question_no
    if question_no>0:
        previous_button['state']=NORMAL
        option_selected.set(selections[question_no])
        question_no -= 1
        display_questions()
        display_options()
    else:
        previous_button['state']=DISABLED

def next():
    global question_no
    if question_no in range(8):
        next_button['state']=NORMAL
        selections[question_no]=option_selected.get()
        question_no+=1
        display_questions()
        display_options()
        if question_no == 8:
            next_button['text']='Submit '         
    else:
        next_button['state']=DISABLED
        previous_button['state']=DISABLED
        check_answers()

def display_questions():
    for widgets in questions_frame.winfo_children():
        widgets.destroy()
    global question
    question = Label(questions_frame,text=questions[question_no],font=helv12,width=58,bg=questions_frame['bg'],anchor='w',justify='center')
    question.place(x=100,y=50)

def display_options():
    options_list = []
    y_position = 100
    while len(options_list)<4:
        radio_button = Radiobutton(questions_frame, text=options[question_no][len(options_list)], bg = questions_frame['bg'],variable=option_selected, value=len(options_list)+1, font=helv12)
        option_selected.set(0)
        options_list.append(radio_button)
        radio_button.place(x=130,y=y_position)
        y_position+=50

def check_answers():
    right_answers=0
    wrong_answers=0
    for i in range(9):
        if selections[i] == answers[i]:
            right_answers+=1
        else:
            wrong_answers+=1
    messagebox.showinfo('Results','{} Correct\n{} Incorrect\nScore = {:.2f} %'.format(right_answers,wrong_answers,right_answers*100/9))
    os.sys.exit()

#start_quiz()
