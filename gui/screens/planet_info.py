import random
from tkinter import Entry, Label, CENTER, Button, messagebox, filedialog
from vpython import color
from resources.config import object_colors, button_colors, FLEXIBILITY
from gui.app import TkinterApp, AppContext
from gui.screens.save_demo import SaveDemoScreen
from core.file import get_relative_path
from core.planet import Planet
from core.vector import Vector


class PlanetInfoScreen(TkinterApp):
    def __init__(self, context: AppContext, planet_number: int, current_planet: int):
        self.textures_menu = None
        self.texture_button = None
        self.color_label = None
        self.color_button = None
        self.context = context
        self.object_color = next(object_colors)

        self.planets_data = self.context.environment.planets_array
        self.error = None
        self.planet_label = None
        self.pop_button = None
        self.button1 = None
        self.button2 = None
        self.planet = None
        self.texture = None
        self.planet_number = planet_number
        self.current_planet = current_planet

        self.labels: list[Label] = []
        self.enteries: list[Entry] = []

        self.initial_state()

    def initial_state(self):
        self.initial_widgets()
        self.initial_position()
        self.add_input_field("planet mass : ", .5, .4)
        self.add_vector_input_field("planet position : ", .5, .45)
        self.add_input_field("planet radius : ", .5, .5)
        self.add_vector_input_field("planet velocity : ", .5, .55)
        self.add_color_button(.5, .6)
        self.add_texture_button(.5, .65)
        self.add_input_field("Flexibility : ", .5, .7)
        self.enteries[-1].insert(0, f'{FLEXIBILITY}')
        self.add_input_field("Hours per Spin : ", .5, .75)

    def initial_widgets(self):
        self.pop_button = Button(
            self.context.app, text='back', height=1, width=9, command=self.back)
        self.planet_label = Label(
            self.context.app, text=f'planet number {self.current_planet + 1}', height=1, width=15)
        self.button2 = Button(self.context.app, text='random',
                              height=1, width=15, command=self.randomize)
        self.add_next_button()

    def initial_position(self):
        self.pop_button.place(relx=.2, rely=.1, anchor=CENTER)
        self.button1.place(relx=.58, rely=.85, anchor=CENTER)
        self.button2.place(relx=.42, rely=.85, anchor=CENTER)
        self.planet_label.place(relx=.5, rely=.25, anchor=CENTER)

    def add_input_field(self, label, x, y):
        self.enteries.append(Entry(self.context.app))
        self.labels.append(Label(self.context.app, text=label, width=20))
        self.labels[-1].place(relx=x - 0.1, rely=y, anchor=CENTER)
        self.enteries[-1].place(relx=x + 0.1, rely=y, anchor=CENTER)

    def add_vector_input_field(self, label, x, y):
        self.enteries.append(Entry(self.context.app, width=4))
        self.enteries.append(Entry(self.context.app, width=4))
        self.enteries.append(Entry(self.context.app, width=4))
        self.labels.append(Label(self.context.app, text=label, width=20))
        self.labels[-1].place(relx=x - 0.1, rely=y, anchor=CENTER)
        self.enteries[-1].place(relx=x + 0.06, rely=y, anchor=CENTER)
        self.enteries[-2].place(relx=x + 0.1, rely=y, anchor=CENTER)
        self.enteries[-3].place(relx=x + 0.14, rely=y, anchor=CENTER)

    def add_color_button(self, x, y):
        self.color_button = Button(
            self.context.app, text='Change Color', command=self.change_color)
        self.color_label = Button(
            self.context.app, text='', width=3, height=1, bg=next(button_colors))
        self.color_label.place(relx=x + 0.1, rely=y, anchor=CENTER)
        self.color_button.place(relx=x - 0.1, rely=y, anchor=CENTER)

    def choose_texture(self):
        self.paint_white()
        file = filedialog.askopenfile(filetypes=(
            ("Text Files", "*.jpg"),), initialdir='./assets/textures')
        self.texture = get_relative_path(file.name) + '\n'
        file.close()

    def add_texture_button(self, x, y):
        self.texture_button = Button(
            self.context.app, width=20, text='planet texture', command=self.choose_texture)
        self.texture_button.place(relx=x, rely=y, anchor=CENTER)

    def paint_white(self):
        self.object_color = color.white

    def change_color(self):
        self.color_label.config(bg=next(button_colors))
        self.object_color = next(object_colors)

    def add_next_button(self):
        if self.current_planet == self.planet_number - 1:
            self.button1 = Button(
                self.context.app, text='finish', height=1, width=15, command=self.finish)
        else:
            self.button1 = Button(
                self.context.app, text='next', height=1, width=15, command=self.next)

    def read_input(self):
        try:
            mass = float(self.enteries[0].get())
            x = float(self.enteries[1].get())
            y = float(self.enteries[2].get())
            z = float(self.enteries[3].get())
            pos = Vector(x, y, z)
            radius = float(self.enteries[4].get())
            x = float(self.enteries[5].get())
            y = float(self.enteries[6].get())
            z = float(self.enteries[7].get())
            planet_color = self.object_color
            flexibility = float(self.enteries[8].get())
            spin_hours = float(self.enteries[9].get())
        except ValueError:
            self.error = 'invalid input!!'
            return
        velocity = Vector(x, y, z)
        self.planet = Planet(mass, radius, pos, velocity, planet_color,
                             flexibility, spin_hours,
                             self.texture, self.context.environment.canvas)
        self.validate_input()
        if self.error == '':
            self.planets_data.append(self.planet)

    def validate_input(self):
        if self.planet.texture == None:
            self.planet.texture = './assets/textures/sun.jpg\n'
        if self.planet.velocity.length() >= 300000000:
            self.error = 'velocity must be less that 300,000,000 m/s'
        else:
            self.error = ''

    def next(self):
        self.read_input()
        if self.error == '':
            self.pop()
            PlanetInfoScreen(self.context, self.planet_number,
                             self.current_planet + 1)
        else:
            messagebox.showerror('Error', self.error)

    def back(self):
        if self.current_planet == 0:
            self.pop()
            from gui.screens.planet_number import PlanetNumberScreen
            PlanetNumberScreen(self.context)
            self.planets_data.clear()
        else:
            self.planets_data.pop()
            self.pop()
            PlanetInfoScreen(self.context, self.planet_number,
                             self.current_planet - 1)

    def finish(self):
        self.read_input()
        if self.error == '':
            self.pop()
            SaveDemoScreen(self.context)
        else:
            messagebox.showerror('Error', self.error)

    def clear_fields(self):
        self.enteries[0].delete(0, 'end')
        self.enteries[1].delete(0, 'end')
        self.enteries[2].delete(0, 'end')
        self.enteries[3].delete(0, 'end')
        self.enteries[4].delete(0, 'end')
        self.enteries[5].delete(0, 'end')
        self.enteries[6].delete(0, 'end')
        self.enteries[7].delete(0, 'end')

    def randomize(self):
        mass = random.randint(10000000, 10000000000)
        pos_x = random.randint(-100000000, 100000000)
        pos_y = random.randint(-100000000, 100000000)
        pos_z = random.randint(-100000000, 100000000)
        radius = random.randint(1, 1000000000)
        v_x = random.randint(-100000000, 100000000)
        v_y = random.randint(-100000000, 100000000)
        v_z = random.randint(-100000000, 100000000)
        spin_hours = random.randint(-100, 100)
        self.clear_fields()
        self.change_color()
        self.enteries[0].insert(0, f'{mass}')
        self.enteries[1].insert(0, f'{pos_x}')
        self.enteries[2].insert(0, f'{pos_y}')
        self.enteries[3].insert(0, f'{pos_z}')
        self.enteries[4].insert(0, f'{radius}')
        self.enteries[5].insert(0, f'{v_x}')
        self.enteries[6].insert(0, f'{v_y}')
        self.enteries[7].insert(0, f'{v_z}')
        self.enteries[9].insert(0, f'{spin_hours}')
