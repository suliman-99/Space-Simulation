from gui.app import AppContext, TkinterApp
from gui.screens.choose_demo import ChooseDemoScreen
from tkinter import CENTER, Button, filedialog, messagebox

from gui.screens.planet_number import PlanetNumberScreen


class HomeScreen(TkinterApp):
    def __init__(self, context: AppContext):
        self.button4 = None
        self.button1 = None
        self.button3 = None
        self.button2 = None
        self.context = context
        self.filename = None

        self.initial_state()

        self.context.app.mainloop()

    def initial_state(self):
        self.initial_widgets()
        self.initial_position()

    def initial_widgets(self):
        self.button2 = Button(self.context.app, text='Input Demo Data', height=2, width=20, command=self.input_demo)
        self.button1 = Button(self.context.app, text='Our Cool Demos', height=2, width=20, command=self.choose_demo)
        self.button3 = Button(self.context.app, text='Read Demo From File', height=2, width=20, command=self.read_demo)
        self.button4 = Button(self.context.app, text='Run', height=2, width=20, command=self.run)

    def read_demo(self):
        self.filename = filedialog.askopenfilename(filetypes=(("Text Files", "*.txt"),), initialdir='./demos')
        self.context.environment.scan_from_file(self.filename)

    def initial_position(self):
        self.button1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.button2.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.button3.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.button4.place(relx=0.5, rely=0.8, anchor=CENTER)

    def input_demo(self):
        self.pop()
        PlanetNumberScreen(self.context)

    def choose_demo(self):
        self.pop()
        ChooseDemoScreen(self.context)

    def run(self):
        if self.filename is not None:
            self.context.environment.run()
        else:
            messagebox.showerror("Error", "No Cool Demo has been loaded!!")
