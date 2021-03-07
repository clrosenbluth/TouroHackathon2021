import tkinter as tk

"""
# Login page
class Home():
    top = tk.Tk()

    greeting = tk.Label(text="Welcome to Speed Type")
    greeting.pack()

    lbl = tk.Label(text="Copy the teacher's code here:")
    lbl.place(x=15, y=20)
    cod = tk.Entry(width=50)
    cod.get()
    cod.place(x=200, y=20)
    stu = tk.Button(text ="done",
                    width=20,
                    command = Students_Page())
    stu.place(x=300, y=20)
"""


# Page with the game on it
class StudentsPage:
    def __init__(self):
        # Set up the screen
        self.window = tk.Tk()
        self.window.geometry("1200x800")
        self.window.configure(background='#000000')

        # Text at top
        self.greeting = tk.Label(text="Welcome to Speed Type! \n"
                                      "Your teacher has uploaded some exciting new sentences.\n"
                                      "Test your accuracy and speed as you type them over!",
                                 width=60)
        self.greeting.place(x=20, y=20)

        # Display sentence to copy
        self.sent_label = tk.Label(text="Please copy the following: \n")
        self.sentence = tk.StringVar()
        self.sent_display = tk.Label(textvariable=self.sentence)
        self.sent_button = tk.Button(text="Next Sentence",
                                     width=30,
                                     command=self.show_sent)

        self.sent_label.place(x=20, y=50)
        self.sent_display.place(x=50, y=50)
        self.sent_button.place(x=80, y=50)

        # Place for typing
        #self.text_box = tk.Entry(width=60, height=6)
        self.text_box = tk.Entry(width=60)
        self.text_box.place(x=20, y=100)
        self.inp = ""

        """fin = tk.Button(text="Done",
                        width=20,
                        command=text_box.get(1.0, tk.END))"""
        self.fin = tk.Button(text="Done",
                             width=20,
                             command=self.get_input)
        self.fin.place(x=200, y=200)

        tk.mainloop()

    def get_input(self):
        self.inp = self.text_box.get()

        self.text_box.delete(0, 'end')


    def show_sent(self):
        sent_string = "Some line from the file"
        self.sentence = sent_string


my_page = StudentsPage()
