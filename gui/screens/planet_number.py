from logging import debug
from tkinter import Entry, Label, CENTER, Button
from gui.app import TkinterApp, AppContext
from gui.screens.planet_info import PlanetInfoScreen


class PlanetNumberScreen(TkinterApp):
    def __init__(self, context: AppContext):
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
        self.label = Label(self.context.app, text="planet number : ")
        self.button = Button(self.context.app, text='next', height=2, width=20, command=self.next)

    def initial_position(self):
        self.label.place(relx=0.45, rely=0.5, anchor=CENTER)
        self.entry.place(relx=0.55, rely=0.5, anchor=CENTER)
        self.button.place(relx=0.5, rely=0.6, anchor=CENTER)

    def next(self):
        planet_number = int(self.entry.get())
        debug(type(planet_number))
        self.pop()
        PlanetInfoScreen(self.context, planet_number)
