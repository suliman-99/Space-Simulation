from logging import debug
from tkinter import Entry, Label, CENTER, Button, StringVar, messagebox
from gui.app import TkinterApp, AppContext
from gui.screens.planet_info import PlanetInfoScreen


class PlanetNumberScreen(TkinterApp):
    def __init__(self, context: AppContext):
        self.pop_button = None
        self.button = None
        self.label = None
        self.entry = None
        self.context = context
        self.initial_state()

    def initial_state(self):
        self.initial_widgets()
        self.initial_position()

    def initial_widgets(self):
        self.entry = Entry(self.context.app)
        self.pop_button = Button(self.context.app, text='back', height=1, width=9, command=self.back)
        self.label = Label(self.context.app, text="planet number : ")
        self.button = Button(self.context.app, text='next', height=2, width=20, command=self.next)

    def initial_position(self):
        self.pop_button.place(relx=.2, rely=.1, anchor=CENTER)
        self.label.place(relx=0.45, rely=0.5, anchor=CENTER)
        self.entry.place(relx=0.55, rely=0.5, anchor=CENTER)
        self.button.place(relx=0.5, rely=0.6, anchor=CENTER)

    def show_error(self):
        self.entry.delete(0, 'end')
        messagebox.showerror("Error", "enter a valid number between 1 and 100 please")

    def next(self):
        try:
            planet_number = int(self.entry.get())
        except ValueError:
            self.show_error()
            return
        if planet_number < 1:
            self.show_error()
            return

        debug(type(planet_number))
        self.pop()
        PlanetInfoScreen(self.context, planet_number, 0)

    def back(self):
        self.pop()
        from gui.screens.home import HomeScreen
        HomeScreen(self.context)
