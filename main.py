from turtle import width
from enviroment import *


def main():
    enviroment = Enviroment()
    enviroment.scan_from_file()
    enviroment.run()


if __name__ == '__main__':
    main()
