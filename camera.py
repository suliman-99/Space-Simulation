from vpython import vector


class Camera:
    def __init__(self, environment):
        self.z = None
        self.y = None
        self.x = None
        self.environment = environment
        self.position = environment.canvas.camera.pos
        self.planets_array = environment.planets_array
        self.is_focused = False
        self.focus_on = 0

    def save_state(self):
        self.x = self.environment.canvas.camera.pos.x
        self.y = self.environment.canvas.camera.pos.y
        self.z = self.environment.canvas.camera.pos.z

    def back_to_initial_position(self):
        self.is_focused = False
        self.environment.canvas.camera.pos = vector(self.x, self.y, self.z)

    def update(self):
        x_p = self.planets_array[self.focus_on].pos.x
        y_p = self.planets_array[self.focus_on].pos.y
        z_p = self.planets_array[self.focus_on].radius * 15
        self.environment.canvas.camera.pos = vector(x_p, y_p, z_p)

    def focus_on_center(self):
        x = self.planets_array[self.focus_on].pos.x
        y = self.planets_array[self.focus_on].pos.y
        z = self.planets_array[self.focus_on].pos.z
        self.environment.canvas.center = vector(x, y, z)

    def move_right(self):
        self.is_focused = True
        self.focus_on = self.focus_on + 1
        if self.focus_on == len(self.planets_array):
            self.focus_on = 0
        self.update()
        # self.focus_on_center()

    def move_left(self):
        self.is_focused = True
        self.focus_on = self.focus_on - 1
        if self.focus_on < 0:
            self.focus_on = len(self.planets_array) - 1
        self.update()

    def unfocus(self):
        self.is_focused = False

    def focus(self):
        self.is_focused = True
