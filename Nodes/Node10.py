from Sound_Service import Sound_Service
from Listener_Service import Listener_Service
import Text_Service
from Action_Node import ActionNode

from Node28 import Node28


def War():
    Text_Service.typing_effect("Te preparas para enfrentarte directamente a los rusos.\n")

    Node28.Start()

def Alliances():
    Text_Service.typing_effect("Entiendes que la guerra no se gana solo. Buscas formar alianzas con otras familias o grupos para fortalecer tu posición.")

    Node28.Start()


def Actio_10():
    Text_Service.typing_effect("Tras un enfrentamiento exitoso con los rusos, envías un mensaje claro, pero esto solo sirve para avivar las llamas. Una guerra entre las familias es inminente, y debes decidir tu próximo movimiento.\n")

    Text_Service.Dialogue("Los rusos no van a tomar esto a la ligera. Es solo cuestión de tiempo antes de que contraataquen.", name= "Aliado")
    Text_Service.Dialogue("Que vengan. Esta vez, nos aseguraremos de que no se levanten.")

Node10 = ActionNode(Actio_10)
Desitions = {
    "Guerra": ActionNode(War),
    "Alianzas": ActionNode(Alliances)
}
Node10.set_SubNodes(Desitions)

