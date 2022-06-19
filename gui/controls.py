from vpython import button, slider, checkbox, color
import resources.config
from file import save_as


class Controls:
    def __init__(self, environment, camera):
        self.velocity_checkbox = None
        self.acceleration_checkbox = None
        self.save_button = None
        self.clear_trail = None
        self.checkbox = None
        self.restart_button = None
        self.slider = None
        self.environment = environment
        self.pause_button = None
        self.slider_value = 1
        self.focus_on = 0
        self.camera = camera

    def on_changed(self, s):
        self.slider_value = s.value
        self.environment.set_time_speed(self.slider_value)

    def clear_trails(self):
        self.environment.clear_trails()

    def on_pressed(self):
        if self.environment.time_speed == 0:
            self.pause_button.text = '<b>Pause</b>'
            self.environment.set_time_speed(self.slider_value)
        else:
            self.pause_button.text = '<b>Resume</b>'
            self.environment.set_time_speed(0)

    def on_saved(self):
        save_as(self.environment.planets_array,
                self.environment.time_scale, 'saved_state')

    def on_cheked(self, value):
        self.environment.set_trail_state(value.checked)

    def restart_demo(self):
        self.environment.clear_arrows()
        self.environment.is_active = False
        self.slider.value = 1
        self.slider_value = 1
        self.checkbox.checked = False
        self.acceleration_checkbox.checked = False
        self.velocity_checkbox.checked = False
        self.pause_button.text = '<b>Pause</b>'

    def key_input(self, event):
        if event.key == 'right':
            self.camera.move_right()
        elif event.key == 'left':
            self.camera.move_left()
        elif event.key == ' ':
            self.camera.back_to_initial_position()
        elif event.key == 'f':
            if self.camera.is_focused:
                self.camera.unfocus()
            else:
                self.camera.focus()

    def show_velocity(self, value):
        if value.checked:
            self.environment.velocity_arrows_start()
        else:
            self.environment.velocity_arrows_stop()

    def show_acceleration(self, value):
        if value.checked:
            self.environment.acceleration_arrows_start()
        else:
            self.environment.acceleration_arrows_stop()

    def render(self):
        space = '\t\t\t\t'
        self.environment.canvas.append_to_caption('\n')
        self.slider = slider(bind=self.on_changed, value=1,
                             min=resources.config.MIN_SPEED, max=resources.config.MAX_SPEED, length=1300)
        self.environment.canvas.append_to_caption('\n\n')
        self.environment.canvas.append_to_caption(space)
        self.restart_button = button(
            bind=self.restart_demo, text='<b>HOT RESTART!!</b>', color=color.black)
        self.environment.canvas.append_to_caption(space)
        self.save_button = button(
            bind=self.on_saved, text='<b>Save State</b>', color=color.blue)
        self.environment.canvas.append_to_caption(space)
        self.pause_button = button(
            bind=self.on_pressed, text='<b>Pause</b>', color=color.purple)
        self.environment.canvas.append_to_caption(space)
        self.clear_trail = button(
            bind=self.clear_trails, text='<b>Clear trails</b>', color=color.purple)
        self.environment.canvas.append_to_caption(space)
        self.checkbox = checkbox(bind=self.on_cheked, text='Show Trail', checked=False)
        self.environment.canvas.append_to_caption('\n\n')
        self.environment.canvas.append_to_caption(space * 2)
        self.velocity_checkbox = checkbox(bind=self.show_velocity, text='show velocity', checked=True)
        self.environment.canvas.append_to_caption(space * 2)
        self.acceleration_checkbox = checkbox(bind=self.show_acceleration, text='show acceleration', checked=True)
        self.environment.canvas.bind('keydown', self.key_input)
