from colorama import init, Fore, Back, Style
import os


class ActionNode:
    def __init__(self, Action, SubNodes = {}):
        self.Action = Action
        self.SubNodes = SubNodes

        init(autoreset=True)

    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def Start(self):
        self.Action()
        if(len(self.SubNodes) != 0):
            valid = True
            print()
            while(valid):
                options = self.SubNodes.keys()
                print(Fore.LIGHTGREEN_EX + Style.BRIGHT + 'Escoge una opción...')
                print( Fore.LIGHTYELLOW_EX + "  ".join(options))

                opction = input(Fore.BLUE)
                print(Fore.RESET)
                if(opction in options):
                    valid = False
                    self.clear()
                    self.SubNodes[opction].Start()
                
                else:
                    print(Fore.LIGHTRED_EX + 'Opcion invalida...')

    def set_SubNodes(self, SubNodes):
        self.SubNodes = SubNodes


