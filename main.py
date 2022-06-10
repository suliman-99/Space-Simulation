from gui.app import TkinterApp
from gui.screens.home import HomeScreen
from testing.debug import debug_config


def main():
    debug_config()  
    TkinterApp(home=HomeScreen)


if __name__ == '__main__':
    main()
