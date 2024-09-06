import time
import sys
from colorama import init, Fore, Back, Style
from Player import Player


def typing_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
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

def Give_Options(text, options, player):
    print()
    while True:
        print(Fore.LIGHTYELLOW_EX + text + Fore.RESET + ' ' + Fore.MAGENTA + ' '.join(options) + Fore.RESET)
        # print(Fore.LIGHTCYAN_EX, end='')
        value = input().strip().lower()
        # print(Fore.RESET, end='')
        if value not in [op.strip().lower() for op in options]:
            if value in ['hel', 'salud', 'vida', 'health']:
                print('Tu vida actual es: ' + Fore.RED + str(player.health) + Fore.RESET ) 
                continue
            elif value in ['inventario', 'inv', 'inventory', 'opjetos']:
                if len(player.inventory) == 0:
                    print(Fore.LIGHTYELLOW_EX + 'No tienes opjetos en tu inventario...' + Fore.RESET)
                for op in player.inventory:
                    print(Fore.LIGHTYELLOW_EX + '> ' + Fore.RESET + op)
                continue
            elif value in ['salir', 'exit']:
                exit(0)
            else:
                print(Fore.RED + 'Opcion invalida...' + Fore.RESET)
                continue
        print()
        return value


# player = Player()
# player.inventory = ['espada', 'lapara']
# player.health = 3
# value = Give_Options('Deseas usar tu linterna ?', ['Si', 'No'], player)
# print(value)

