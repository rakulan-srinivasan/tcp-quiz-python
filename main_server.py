from tkinter import *
from tkinter import messagebox
import socket
from datetime import datetime

import science_quiz
import comp_fun_quiz
import gk_quiz

class main_server():

    def menu(self,status): 
        global window
        window = Tk()
        window_icon = PhotoImage(file=r'outline_quiz_black_24dp.png')
        window.iconphoto(False,window_icon)
        window.title('TCP Quiz - Prime Server')
        window.geometry('300x410+10+10')
        window.resizable(0,0)

        title_frame = Frame(window,bg='#88B2CC',width=400,height=50)
        title_frame.pack()
        title_frame.propagate(0)
        button_frame = Frame(window,bg='#E7D4C0',width=400,height=210)
        button_frame.pack()
        button_frame.propagate(0)
        next_frame = Frame(window,bg='#E98973',width=400,height=50)
        next_frame.pack()
        next_frame.propagate(0)
        connection_status_frame = Frame(window,bg='#658EA9',width=400,height=50)
        connection_status_frame.pack()
        connection_status_frame.propagate(0)
        author_frame = Frame(window,width=400, height=50)
        author_frame.pack()

        helv12 = ('Helvetica', 12, 'bold')
        button_response_colour = '#DE3163'
        
        title = StringVar()
        title_label = Label(title_frame,textvariable = title,bg='#88B2CC',font = helv12,justify='center')
        title.set("Welcome to TCP Quiz!")
        title_label.pack(padx=10,pady=10)

        def on_enter_button_frame(e):
            e.widget['background']='#6495ED'
        def on_leave_button_frame(e):
            e.widget['background'] = '#E7D4C0'

        global science_button
        science_icon = PhotoImage(file=r'outline_science_black_24dp.png')
        science_button = Button(button_frame, text=" Science",image=science_icon,height=50,bg='#E7D4C0', activebackground=button_response_colour,font=helv12,width=280,compound=LEFT,relief='raised',command=lambda:self.button_click('Science'))
        science_button.pack(padx=10,pady=(10,5))
        science_button.bind('<Enter>',on_enter_button_frame)
        science_button.bind('<Leave>',on_leave_button_frame)

        global comp_fun_button
        comp_fun_icon = PhotoImage(file=r'outline_computer_black_24dp.png')
        comp_fun_button = Button(button_frame, text=" Computer Fundamentals",image=comp_fun_icon,height=50,bg='#E7D4C0', activebackground=button_response_colour,font=helv12,width=280,compound=LEFT,command=lambda:self.button_click('Computer Fundamentals'))
        comp_fun_button.pack(padx=10,pady=(5,5))
        comp_fun_button.bind('<Enter>',on_enter_button_frame)
        comp_fun_button.bind('<Leave>',on_leave_button_frame)

        global gk_button
        gk_icon = PhotoImage(file=r'outline_psychology_black_24dp.png')
        gk_button = Button(button_frame, text=' General Knowledge',image=gk_icon,height=50,bg='#E7D4C0', activebackground=button_response_colour,font=helv12,width=280,compound=LEFT,command=lambda:self.button_click('General Knowledge'))
        gk_button.pack(padx=10,pady=(5,10))
        gk_button.bind('<Enter>',on_enter_button_frame)
        gk_button.bind('<Leave>',on_leave_button_frame)

        def on_enter_next_frame(e):
            e.widget['background']='#6495ED'
        def on_leave_next_frame(e):
            e.widget['background'] = '#E98973'

        global confirm_button
        confirm_icon = PhotoImage(file=r'outline_thumb_up_off_alt_black_24dp.png')
        confirm_button = Button(next_frame, text=" Confirm",image=confirm_icon,height=30,bg='#E98973', activebackground=button_response_colour,compound=LEFT,command=lambda:self.button_click('Confirm'))
        confirm_button.pack(side=LEFT,padx=10,pady=10)
        confirm_button.bind('<Enter>',on_enter_next_frame)
        confirm_button.bind('<Leave>',on_leave_next_frame)

        global reset_button
        reset_icon = PhotoImage(file=r'outline_restart_alt_black_24dp.png')
        reset_button = Button(next_frame,text='Reset',image=reset_icon,height=30,bg='#E98973', activebackground=button_response_colour,compound=LEFT,command=lambda:self.button_click('Reset'))
        reset_button.pack(side=LEFT,padx=10,pady=10)
        reset_button.bind('<Enter>',on_enter_next_frame)
        reset_button.bind('<Leave>',on_leave_next_frame)

        global next_button
        next_icon = PhotoImage(file=r'outline_launch_black_24dp.png')
        next_button = Button(next_frame, text=" Proceed",image=next_icon,height=30,bg='#E98973', activebackground=button_response_colour,font=helv12,compound=LEFT,command=lambda:self.button_click('Proceed'))
        next_button.pack(side=RIGHT,padx=10,pady=10)
        next_button.bind('<Enter>',on_enter_next_frame)
        next_button.bind('<Leave>',on_leave_next_frame)

        connection_icon = PhotoImage(file=r'outline_link_black_24dp.gif')
        global connection_status
        global connection_label
        connection_status = StringVar()
        connection_label = Label(connection_status_frame,textvariable = connection_status,bg=connection_status_frame['bg'],image=connection_icon,compound=LEFT,justify='center')
        connection_status.set(status)
        connection_label.pack(padx=10,pady=10)

        author_label = Label(author_frame,text='Rakulan Srinivasan\n123015085 - SASTRA Deemed University',justify='center')
        author_label.pack(padx=10, pady=10)

        def on_close():
            try:
                print()
                messagebox.showinfo('Quiz Termination','Attempted to Close Quiz\nTerminating on Confirmation!')
                server_socket.close()
                print('Attempted to Close Quiz - Quiz Terminated!')
                window.destroy()
                pass
            except (ConnectionResetError,ConnectionAbortedError):
                window.destroy() 

        window.protocol('WM_DELETE_WINDOW', on_close)
        window.mainloop()

    def confirm(self,science_button,comp_fun_button,gk_button):
        science_button['state']=DISABLED
        comp_fun_button['state']=DISABLED
        gk_button['state']=DISABLED
        pass
    def reset(self,science_button,comp_fun_button,gk_button):
        science_button['state']=NORMAL
        comp_fun_button['state']=NORMAL
        gk_button['state']=NORMAL
        pass
    def proceed(self,quiz):
        if quiz == 'Science':
            science_quiz.start_quiz()
            pass
        elif quiz == 'Computer Fundamentals':
            comp_fun_quiz.start_quiz()
            pass
        elif quiz == 'General Knowledge':
            gk_quiz.start_quiz()
            
    def button_click(self,clicks,click_history=['Start']):
        top=len(click_history)-1
        if len(click_history) > 0:
            #print('1',clicks,click_history[top],len(click_history),end=', ')
            click_history.append(clicks)
            if click_history[top]!=click_history[top-1]:
                top=top+1
            #print("top={}".format(top))
        if clicks == 'Confirm':
            print('Selected Quiz: ',click_history[top-1])
            self.confirm(science_button,comp_fun_button,gk_button)
        elif clicks == 'Reset':
            print('Options are Reset')
            self.reset(science_button,comp_fun_button,gk_button)
        elif click_history[top] == 'Proceed' and click_history[top-1] == 'Confirm':
            reset_button['state']=DISABLED
            confirm_button['state']=DISABLED
            print('Confirmed Quiz: ', click_history[top-2])
            self.proceed(str(click_history[top-2]))
        pass

def main():
    try:
        global server_socket
        server_socket = socket.socket()
        port = 20000               
        server_socket.bind((socket.gethostname(), port))        
        print ('Socket bound to (\'{}\', {})'.format(socket.gethostname(),port))
        server_socket.listen(5)
        global client_socket          
        while True:
            client_socket, addr = server_socket.accept()
            print('SYN from Client at ',datetime.now())
            client_socket.send('ACK from Server'.encode())
            print('ACK to Client at ',datetime.now())
            print('Connected to {} '.format(addr))
            print(client_socket.recv(1024).decode(),'at',datetime.now())
            main_object = main_server()
            main_object.menu('Connected to {} '.format(addr))
    except OSError:
        pass

if __name__ == "__main__":
    main()