from pyfiglet import Figlet
from colorama import Fore, init

init()


def produce_font():  # wordart and tips
    f = Figlet(font='slant')
    ascii_art = Fore.LIGHTBLUE_EX + f.renderText('Eipher')
    print(ascii_art + "Welcome to Eipher Password Dictionary Generator!")
    print("--------------------------------- ------------------")
    print("|| [ 001]              Random string arrangement  ||")
    print("|| [ 002]         Random combination arrangement  ||")
    print("|| [exit]                         Exit procedure  ||")
    print("------------------------------------- --------------")

