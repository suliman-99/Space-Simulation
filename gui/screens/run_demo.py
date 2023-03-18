from tkinter import Button, CENTER
from gui.app import TkinterApp, AppContext


class RunDemoScreen(TkinterApp):
    def __init__(self, context: AppContext):
        self.button2 = None
        self.button1 = None
        self.context = context
        self.initial_state()

    def initial_state(self):
        self.initial_widgets()
        self.initial_position()

    def initial_widgets(self):
        self.button1 = Button(self.context.app, text='Run Simulation', height=2, width=20, command=self.run)
        self.button2 = Button(self.context.app, text='Back to HomePage', height=2, width=20, command=self.back)

    def initial_position(self):
        self.button1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.button2.place(relx=0.5, rely=0.6, anchor=CENTER)

    def back(self):
        self.pop()
        from gui.screens.home import HomeScreen
        HomeScreen(self.context)

    def run(self):
        self.run_environment()
