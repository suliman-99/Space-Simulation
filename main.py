from gui.app import TkinterApp
from gui.screens.home import HomeScreen


def main():
    TkinterApp(home=HomeScreen)


if __name__ == '__main__':
    main()
