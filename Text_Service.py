import time
import sys
from colorama import init, Fore, Back, Style


def typing_effect(text, delay=0.03):
    # for char in text:
    #     sys.stdout.write(char)
    #     sys.stdout.flush()
    #     time.sleep(delay)
    # print()
    time.sleep(delay)
    print(text)

def typing_with_deletion(text, delay=0.03, delete_delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    time.sleep(1)
    for char in text:
        sys.stdout.write('\b \b')
        sys.stdout.flush()
        time.sleep(delete_delay)
    print()

def blinking_cursor(text, delay=0.03, cursor_delay=0.5, ticks = 5):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    count = ticks
    while count > 0:
        sys.stdout.write('|')
        sys.stdout.flush()
        time.sleep(cursor_delay)
        sys.stdout.write('\b \b')
        sys.stdout.flush()
        time.sleep(cursor_delay)
        count -= 1

def Dialogue(text, *, delay = 0.5, name = 'You'):
    character = Fore.MAGENTA + f'({name})' + Fore.RESET + " : "
    print(character, end="")
    typing_effect(text)
    time.sleep(delay)
    

