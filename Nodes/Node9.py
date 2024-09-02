from Sound_Service import Sound_Service
from Listener_Service import Listener_Service
import Text_Service
from Action_Node import ActionNode


def ___():
    pass

    ##TODO: GO TO NODE 27

def Actio_9():
    Text_Service.typing_effect("Decides delegar la tarea de entregar el paquete a uno de tus subordinados, pero todo sale mal. El paquete es robado en un violento enfrentamiento, y ahora debes enfrentar al Don.\n")

    Text_Service.Dialogue("¡¿Qué demonios pasó?! ¿Cómo pudiste ser tan estúpido para confiar algo tan importante a otro?", name= "Don Graziano")
    Text_Service.Dialogue("No pensé que las cosas se complicarían tanto. Pero lo solucionaré, Don.")
    Text_Service.Dialogue("Más te vale. O empezarás a pagar con tu vida", name= "Don Graziano")

Node9 = ActionNode(Actio_9)
Desitions = {
    "recuperar ": ActionNode(),
}
Node9.set_SubNodes(Desitions)

