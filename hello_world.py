from random import randrange

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

getch = _Getch()


def hra():
    pc = randrange(0, 3)
    human = int(input("Zadej cislo (0 - kámen, 1 - nůžky ,2 - papír)"))
    kamen = 0
    nuzky = 1
    papir = 2
    if pc == kamen:
        if human == kamen:
            print("eště ráz1")
        elif human == nuzky:
            print("skoro1")
        elif human == papir:
            pc = "kamen"
            print("vyhráls, počítač měl", pc)
    elif pc == papir:
        if human == papir:
            print("eště ráz2")
        elif human == kamen:
            print("skoro2")
        elif human == nuzky:
            pc = "papir"
            print("vyhráls, počítač měl", pc)
    elif pc == nuzky:
        if human == nuzky:
            print("eště ráz3")
        elif human == papir:
            print("skoro3")
        elif human == kamen:
            pc = "nuzky"
            print("vyhráls, počítač měl", pc)


key = getch
while key != input(chr(27)):
    enter = input("Zmáčkni enter pro novou hru")
    if enter == "":
        hra()
    print("nebo esc pro konec.")
