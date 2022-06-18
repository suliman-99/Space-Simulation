from vpython import scene, button, slider, checkbox, color
import resources.config
from file import save_as


class Controls:
    def __init__(self, environment):
        self.environment = environment
        self.pause_button = None
        self.slider_value = 1

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
        self.environment.is_active = False
        self.slider.value = 1
        self.slider_value = 1
        self.checkbox.checked = False
        self.pause_button.text = '<b>Pause</b>'

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
        self.checkbox = checkbox(
            bind=self.on_cheked, text='Show Trail', checked=False)
