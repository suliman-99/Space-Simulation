from vpython import *


class terminal_scanner:
    @staticmethod
    def scanInt(low, hight, sentens):
        print(sentens)
        ret = ''
        while not isinstance(ret, int) or ret < low or ret > hight:
            try:
                ret = int(input("Pleas enter an intger number between " +
                          str(low) + " and " + str(hight) + " : "))
            except ValueError:
                continue
        return ret

    @staticmethod
    def scanInt2(sentens):
        print(sentens)
        ret = ''
        while not isinstance(ret, int):
            try:
                ret = int(input("Pleas enter an intger number : "))
            except ValueError:
                continue
        return ret

    @staticmethod
    def scanFloat(low, hight, sentens):
        print(sentens)
        ret = ''
        while not isinstance(ret, float) or ret < low or ret > hight:
            try:
                ret = float(input("Pleas enter an float number between " +
                            str(low) + " and " + str(hight) + " : "))
            except ValueError:
                continue
        return ret

    @staticmethod
    def scanFloat2(sentens):
        print(sentens)
        ret = ''
        while not isinstance(ret, float):
            try:
                ret = float(input("Pleas enter an float number : "))
            except ValueError:
                continue
        return ret

    @staticmethod
    def scanColor(sentens):
        print(sentens)
        ret = terminal_scanner.scanInt(1, 10, """
        Pleas choos the color you want : 
        Red : 1
        Green : 2
        Blue : 3
        Yellow : 4
        Orange : 5
        Cyan : 6
        Purple : 7
        Gray  : 8
        Black : 9
        White : 10
        """)
        switcher = {
            1: color.red,
            2: color.green,
            3: color.blue,
            4: color.yellow,
            5: color.orange,
            6: color.cyan,
            7: color.purple,
            8: color.gray(0.5),
            9: color.black,
            10: color.white,
        }
        return switcher[ret]
