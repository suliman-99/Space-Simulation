from vpython import vector


class Camera:
    def __init__(self, environment):
        self.x = environment.canvas.camera.pos.x
        self.y = environment.canvas.camera.pos.y
        self.z = environment.canvas.camera.pos.z
        self.environment = environment
        self.position = environment.canvas.camera.pos
        self.planets_array = environment.planets_array
        self.is_focused = False
        self.focus_on = 0

    def back_to_initial_position(self):
        self.is_focused = False
        self.position.x = vector(self.x, self.y, self.z)

    def update(self):
        x = self.planets_array[self.focus_on].pos.x
        y = self.planets_array[self.focus_on].pos.y
        z = self.planets_array[self.focus_on].pos.z
        # self.environment.canvas.center = vector(x, y, z)
        x = x - self.planets_array[self.focus_on].radius * 2
        y = y + self.planets_array[self.focus_on].radius * 2
        z = z - self.planets_array[self.focus_on].radius * 2
        self.environment.canvas.camera.pos = vector(x, y, z)

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
        # self.focus_on_center()

    def move_left(self):
        self.is_focused = True
        self.focus_on = self.focus_on - 1
        if self.focus_on == 0:
            self.focus_on = len(self.planets_array)

    def unfocus(self):
        self.is_focused = False

    def focus(self):
        self.is_focused = True
