from gui.app import TkinterApp
from gui.screens.home import HomeScreen
from testing.debug import enable_debug_mode


def main():
    enable_debug_mode()
    TkinterApp(home=HomeScreen)


if __name__ == '__main__':
    main()
