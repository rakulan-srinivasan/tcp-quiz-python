# Questions from https://www.radiotimes.com/quizzes/pub-quiz-science/

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

    window = Tk()
    window.title('TCP Quiz - Science Quiz Server')
    window.geometry('800x600+320+10')
    window.resizable(0,0)
    # window.update
    
    title_frame = Frame(window,bg='#88B2CC',width=800,height=50)
    title_frame.pack()

    global questions_frame    
    questions_frame = Frame(window,bg='#E7D4C0',width=800,height=500)
    questions_frame.pack()
    
    global button_frame
    button_frame = Frame(window,width=800,height=50)
    button_frame.pack()

    global helv12
    helv12 = ('Helvetica', 12, 'bold')
    button_response_colour = '#DE3163'
        
    title = StringVar()
    title_label = Label(title_frame,textvariable = title,width=800,bg='#88B2CC',font = helv12,justify='center')
    title.set("Welcome to TCP SCIENCE Quiz!")
    title_label.pack(padx=10,pady=10)

    def on_enter_button_frame(e):
            e.widget['background']='#6495ED'
    def on_leave_button_frame(e):
            e.widget['background']='#E98973'

    global previous_button
    # previous_icon = PhotoImage(file=r'baseline_skip_previous_black_24dp.png')
    previous_button = Button(button_frame,text=' Previous',font=helv12,height=80,bg='#E98973',width=10,activebackground=button_response_colour,compound=LEFT,command=previous)
    previous_button.pack(side=LEFT,padx=(10,200),pady=10)
    previous_button.bind('<Enter>',on_enter_button_frame)
    previous_button.bind('<Leave>',on_leave_button_frame)
    
    
    global next_button
    #next_icon = PhotoImage(file=r'baseline_skip_next_black_24dp.png')
    next_button = Button(button_frame,text='Next ',font=helv12,height=80,bg='#E98973',width=10,activebackground=button_response_colour,compound=RIGHT,command=next)
    next_button.pack(side=RIGHT,padx=(200,10),pady=10)
    next_button.bind('<Enter>',on_enter_button_frame)
    next_button.bind('<Leave>',on_leave_button_frame)

    window.update

    global option_selected
    option_selected = IntVar()

    radio_buttons()
    
    display_questions()
    display_options()
    window.update()
    window.mainloop()
    pass

def radio_buttons():
    options_list = []
    y_position = 100
    while len(options_list)<4:
        radio_button = Radiobutton(questions_frame,text="",bg=questions_frame['bg'],variable=option_selected,value=len(options_list)+1,font=helv12)
        options_list.append(radio_button)
        radio_button.place(x=130,y=y_position)
        y_position+=50
    return options_list

def previous():
    global question_no
    option_selected.get(selections[question_no])
    if question_no>=1:
        previous_button['state']=NORMAL
        selections[question_no]=option_selected.get()
        #option_selected.get(selections[question_no])
        question_no-=1
    #count_text.set(question_no)
    #count_text.update()
        print(selections,question_no)
        display_questions()
        display_options()
    else:
        previous_button['state']=DISABLED
    pass

def next():
    global question_no
    if question_no<8:
        next_button['state']=NORMAL
        selections[question_no]=option_selected.get()
        question_no += 1
    #count_text.set(question_no)
    #count_text.update()
        display_questions()
        display_options()
        print(selections,question_no)
    elif question_no==8:
        check_answers()
        pass
    else:
        next_button['state']=DISABLED
    pass

def display_questions():
    global question
    question = Label(questions_frame,text=questions[question_no],font=helv12,width=58,bg=questions_frame['bg'],anchor='w',justify='center')    
    question.place(x=100,y=50)
    pass

def display_options():
    option_value=0
    option_selected.set(0)
    for option in options[question_no]:
        radio_buttons()[option_value]['text'] = ('   '+option+'\t\t\t')
        option_value+=1
    pass

def check_answers():
    right_answers=0
    wrong_answers=0
    for i in range(9):
        if selections[i]==answers[i]:
            right_answers+=1
        else:
            wrong_answers+=1
    messagebox.showinfo('Results','{} Correct\n{} Incorrect\nScore = {:.2f} %'.format(right_answers,wrong_answers,right_answers*100/9))
    os.sys.exit()


#start_quiz()