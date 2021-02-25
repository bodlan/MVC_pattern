import tkinter as tk
import controller
import model


class Main:
    def __init__(self,master):
        self.intro="""
    Welcome to database of a students in our course!
    Program uses CRUD operations on database such as:
    C-Create student, R-Read,view student,
    U-Update information about student, D-Delete student from db
    """
        self.master=master
        self.frame_intro=tk.Frame()
        self.frame_buttons=tk.Frame()

        self.introduction=tk.Label(self.frame_intro,text=self.intro)
        self.introduction.pack()

        self.button1=tk.Button(
            self.frame_buttons,
            text='Create',
            width=30,

        )
        self.button1.pack()
        self.button1.bind("<Button-1>",controller.create)

        self.button2=tk.Button(
            self.frame_buttons,
            text='Read',
            width=30,
        )
        self.button2.pack()
        self.button2.bind("<Button-1>", controller.read)

        self.button3=tk.Button(
            self.frame_buttons,
            text='Update',
            width=30,
        )
        self.button3.pack()
        self.button3.bind("<Button-1>", controller.update)

        self.button4=tk.Button(
            self.frame_buttons,
            text='Delete',
            width=30,
        )
        self.button4.pack()
        self.button4.bind("<Button-1>", controller.delete)

        self.button5=tk.Button(
            self.frame_buttons,
            text='Exit',
            width=30,
        )
        self.button5.pack()
        self.button5.bind("<Button-1>",exit)

        self.frame_intro.pack()
        self.frame_buttons.pack()



class Create:
    def __init__(self,master):
        self.master=master
        self.frame_label=tk.Frame(self.master)
        self.frame_input=tk.Frame(self.master)
        self.frame_button=tk.Frame(self.master)
        self.label=tk.Label(self.frame_label,text='Add a student to a db')
        self.label.pack()

        self.name_label=tk.Label(self.frame_input,text='Name')
        self.name=tk.Entry(self.frame_input,width=30)
        self.name_label.pack()
        self.name.pack()

        self.surname_label = tk.Label(self.frame_input, text='Surname')
        self.surname = tk.Entry(self.frame_input, width=30)
        self.surname_label.pack()
        self.surname.pack()

        self.year_label = tk.Label(self.frame_input, text='Years old')
        self.year = tk.Entry(self.frame_input, width=30)
        self.year_label.pack()
        self.year.pack()

        self.course_label = tk.Label(self.frame_input, text='Course')
        self.course = tk.Entry(self.frame_input, width=30)
        self.course_label.pack()
        self.course.pack()

        self.email_label = tk.Label(self.frame_input, text='Email')
        self.email = tk.Entry(self.frame_input, width=30)
        self.email_label.pack()
        self.email.pack()

        self.button=tk.Button(
            self.frame_button,
            text='Submit',
            width=30,
            command=controller.close_window
        )
        self.button.pack()
        self.button.bind("<Button-1>",controller.handler_click)

        self.frame_label.pack()
        self.frame_input.pack()
        self.frame_button.pack()

class Read:
    def __init__(self,master):
        self.master=master
        self.frame_label=tk.Frame(self.master)
        self.frame_output=tk.Frame(self.master)
        self.label=tk.Label(self.frame_label,text='Read')
        self.label.pack()
        self.text_box=tk.Text(self.frame_output)
        self.text_box.insert("1.0",model.read_all())
        self.text_box.pack()
        self.frame_label.pack()
        self.frame_output.pack()

class Update:
    def __init__(self,master):
        self.master=master
        self.frame_input=tk.Frame(self.master)
        self.frame_button=tk.Frame(self.master)
        self.old_label=tk.Label(self.frame_input,text='Update')
        self.old=tk.Entry(self.frame_input,width=30)
        self.old_label.pack()
        self.old.pack()

        self.new_label=tk.Label(self.frame_input,text='Update with')
        self.new=tk.Entry(self.frame_input,width=30)
        self.new_label.pack()
        self.new.pack()
        self.button=tk.Button(
            self.frame_button,
            text='Submit',
            width=30,
            command=controller.update_info
        )
        self.button.pack()
        self.frame_input.pack()
        self.frame_button.pack()


class Delete:
    def __init__(self,master):
        self.master=master
        self.label_frame=tk.Frame(self.master)
        self.input_frame=tk.Frame(self.master)
        self.button_frame=tk.Frame(self.master)
        self.label=tk.Label(self.label_frame,text='Delete')
        self.label.pack()

        self.name_label=tk.Label(self.input_frame,text='Name')
        self.surname_label=tk.Label(self.input_frame,text='Surname')
        self.name=tk.Entry(self.input_frame,width=30)
        self.surname=tk.Entry(self.input_frame,width=30)
        self.name_label.pack()
        self.name.pack()
        self.surname_label.pack()
        self.surname.pack()
        self.button=tk.Button(
            self.button_frame,
            text='Submit',
            command=controller.delete_student
                              )
        self.button.pack()
        self.label_frame.pack()
        self.input_frame.pack()
        self.button_frame.pack()

