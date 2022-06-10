from tkinter import Entry, Label, CENTER, Button

from gui.app import TkinterApp, AppContext
from file import save_on_file
from vector import Vector


class PlanetInfoScreen(TkinterApp):
    def __init__(self, context: AppContext, planet_number: int):
        self.button1 = None
        self.button2 = None
        self.context = context
        self.planet_number = planet_number
        self.enteries = []
        self.labels = []

        self.initial_state()

    def initial_state(self):
        self.initial_widgets()
        self.initial_position()
        self.add_input_field("planet mass : ", 0.5, 0.4)
        self.add_vector_input_field("planet position : ", 0.5, 0.45)
        self.add_input_field("planet radius : ", 0.5, 0.5)
        self.add_vector_input_field("planet velocity : ", 0.5, 0.55)

    def add_input_field(self, label, x, y):
        self.enteries.append(Entry(self.context.app))
        self.labels.append(Label(self.context.app, text=label))
        self.labels[-1].place(relx=x - 0.05, rely=y, anchor=CENTER)
        self.enteries[-1].place(relx=x + 0.05, rely=y, anchor=CENTER)

    def add_vector_input_field(self, label, x, y):
        self.enteries.append(Entry(self.context.app, width=2))
        self.enteries.append(Entry(self.context.app, width=2))
        self.enteries.append(Entry(self.context.app, width=2))
        self.labels.append(Label(self.context.app, text=label))
        self.labels[-1].place(relx=x - 0.05, rely=y, anchor=CENTER)
        self.enteries[-1].place(relx=x + 0.0, rely=y, anchor=CENTER)
        self.enteries[-2].place(relx=x + 0.05, rely=y, anchor=CENTER)
        self.enteries[-3].place(relx=x + 0.1, rely=y, anchor=CENTER)

    def initial_widgets(self):
        self.button1 = Button(self.context.app, text='next', height=1, width=15, command=self.next)
        self.button2 = Button(self.context.app, text='random', height=1, width=15, command=self.randomize)

    def initial_position(self):
        self.button1.place(relx=0.58, rely=0.85, anchor=CENTER)
        self.button2.place(relx=0.42, rely=0.85, anchor=CENTER)

    def read_input(self):
        mass = float(self.enteries[0].get())
        x = float(self.enteries[1].get())
        y = float(self.enteries[2].get())
        z = float(self.enteries[3].get())
        pos = Vector(x, y, z)
        radius = float(self.enteries[4].get())
        x = float(self.enteries[5].get())
        y = float(self.enteries[6].get())
        z = float(self.enteries[7].get())
        velocity = Vector(x, y, z)
        self.context.environment.add_planet(mass, radius, pos, velocity)

    def next(self):
        self.read_input()
        if self.planet_number == 1:
            save_on_file(self.context.environment.planets_array)
            self.context.environment.run()
        self.pop()
        PlanetInfoScreen(self.context, self.planet_number - 1)

    def randomize(self):
        pass
