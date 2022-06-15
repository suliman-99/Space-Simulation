from gui.app import AppContext, TkinterApp
from gui.screens.choose_demo import ChooseDemoScreen
from tkinter import CENTER, Button, filedialog, messagebox

from gui.screens.planet_number import PlanetNumberScreen
from gui.screens.run_demo import RunDemoScreen


class HomeScreen(TkinterApp):
    def __init__(self, context: AppContext):
        self.button1 = None
        self.button2 = None
        self.button3 = None
        self.context = context
        self.filename = None

        self.initial_state()

        self.context.app.mainloop()

    def initial_state(self):
        self.initial_widgets()
        self.initial_position()

    def initial_widgets(self):
        self.button1 = Button(self.context.app, text='Interesting Simulations', height=2, width=20,
                              command=self.choose_demo)
        self.button2 = Button(self.context.app, text='Create new Simulation', height=2, width=20,
                              command=self.input_demo)
        self.button3 = Button(self.context.app, text='Simulation From File', height=2, width=20,
                              command=self.read_demo)

    def read_demo(self):
        self.context.environment.clear_data()
        self.filename = filedialog.askopenfilename(filetypes=(("Text Files", "*.txt"),), initialdir='./demos')
        self.context.environment.scan_from_file(self.filename)
        if self.filename is not None:
            self.pop()
            RunDemoScreen(self.context)
        else:
            messagebox.showerror("Error", "No Simulation has been loaded!!")

    def initial_position(self):
        self.button1.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.button2.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.button3.place(relx=0.5, rely=0.7, anchor=CENTER)

    def input_demo(self):
        self.pop()
        PlanetNumberScreen(self.context)

    def choose_demo(self):
        self.pop()
        ChooseDemoScreen(self.context)

    def run(self):
        self.run_environment()
