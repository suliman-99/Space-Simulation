from vpython import button, slider, checkbox, color
import resources.config


class Controls:
    def __init__(self, canvas):
        self.canvas = canvas
        self.slider = None
        self.hot_restart_button = None
        self.save_state_button = None
        self.pause_button = None
        self.clear_trails_button = None
        self.show_trail_checkbox = None
        self.show_velocity_checkbox = None
        self.show_acceleration_checkbox = None

        self.slider_value = 1
        self.have_to_refresh = False
        self.have_to_save_state = False
        self.is_paused = False
        self.have_to_clear_trails = False
        self.show_trail = False
        self.show_velocity = True
        self.show_acceleration = True

        self.have_to_move_right = False
        self.have_to_move_left = False
        self.have_to_back_to_initial_state = False
        self.have_to_revers_focus_state = False
        self.have_to_revers_rotate_state = False

    def slider_on_changed(self, s):
        self.slider_value = s.value

    def hot_restart_function(self):
        self.have_to_refresh = True

    def save_state_function(self):
        self.have_to_save_state = True

    def pause_function(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.pause_button.text = '<b>Resume</b>'
        else:
            self.pause_button.text = '<b>Pause</b>'

    def clear_trails_function(self):
        self.have_to_clear_trails = True

    def show_trail_function(self, value):
        self.show_trail = value.checked

    def show_velocity_function(self, value):
        self.show_velocity = value.checked

    def show_acceleration_function(self, value):
        self.show_acceleration = value.checked

    def key_input(self, event):
        if event.key == 'd':
            self.have_to_move_right = True
        elif event.key == 'a':
            self.have_to_move_left = True
        elif event.key == 's':
            self.have_to_back_to_initial_state = True
        elif event.key == 'w':
            self.have_to_revers_focus_state = True
        elif event.key == 'r':
            self.have_to_revers_rotate_state = True

    def render(self):
        space = ' '*20
        self.slider = slider(bind=self.slider_on_changed, value=1,
                             min=resources.config.MIN_SPEED, max=resources.config.MAX_SPEED, length=1300)
        self.canvas.append_to_caption('\n\n')
        self.hot_restart_button = button(
            bind=self.hot_restart_function, text='<b>HOT RESTART!!</b>', color=color.black)
        self.canvas.append_to_caption(space)
        self.save_state_button = button(
            bind=self.save_state_function, text='<b>Save State</b>', color=color.blue)
        self.canvas.append_to_caption(space)
        self.pause_button = button(
            bind=self.pause_function, text='<b>Pause</b>', color=color.purple)
        self.canvas.append_to_caption(space)
        self.clear_trails_button = button(
            bind=self.clear_trails_function, text='<b>Clear trails</b>', color=color.purple)
        self.canvas.append_to_caption(space)
        self.show_trail_checkbox = checkbox(
            bind=self.show_trail_function, text='Show Trail', checked=self.show_trail)
        self.canvas.append_to_caption(space)
        self.show_velocity_checkbox = checkbox(
            bind=self.show_velocity_function, text='show velocity', checked=self.show_velocity)
        self.canvas.append_to_caption(space)
        self.show_acceleration_checkbox = checkbox(
            bind=self.show_acceleration_function, text='show acceleration', checked=self.show_acceleration)
        self.canvas.bind('keydown', self.key_input)
