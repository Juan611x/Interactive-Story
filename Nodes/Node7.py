from Sound_Service import Sound_Service
from Listener_Service import Listener_Service
import Text_Service
from Action_Node import ActionNode

from Node19 import Node19
from Node20 import Node20
from Node21 import Node21

def Ignore():
    Text_Service.typing_effect("Decides que es mejor no preguntar demasiado y mantienes la boca cerrada, confiando en el Don.\n")

    Node19.Start()

def Investigate():
    Text_Service.typing_effect("Tu curiosidad te lleva a investigar más profundamente. Quieres saber qué llevaste exactamente.\n")

    Node20.Start()

def Confront():
    Text_Service.typing_effect("No puedes dejar de preguntarte qué hay en el paquete. Decides enfrentarte al Don y pedirle explicaciones.\n")

    Node21.Start()

def Actio_7():
    Text_Service.typing_effect("Entregas el paquete al contacto del Don en una bodega abandonada. La transacción se realiza sin incidentes, pero mientras sales del lugar, comienzas a escuchar rumores en las calles sobre lo que podría haber dentro de ese paquete.\n")

    Text_Service.Dialogue("Buen trabajo, chico. El Don estará complacido. Asegúrate de que nadie se entere de esto, ¿entiendes?", name= "Contacto")
    Text_Service.Dialogue("Seguro. ¿Pero qué había dentro de ese paquete? La calle está empezando a hablar.")
    Text_Service.Dialogue("No es asunto tuyo. Solo recuerda a quién sirves.", name= "Contacto")

Node7 = ActionNode(Actio_7)
Desitions = {
    "Ignorar": ActionNode(Ignore),
    "Investigar": ActionNode(Investigate),
    "Confrontar": ActionNode(Confront)
}
Node7.set_SubNodes(Desitions)

