from Sound_Service import Sound_Service
from Listener_Service import Listener_Service
import Text_Service
from Action_Node import ActionNode

from Node7 import Node7
from Node8 import Node8
from Node9 import Node9

def Delegate():
    Text_Service.Dialogue("Tío, creo que sería mejor si alguien más se encargara de esto. Tengo otros asuntos que atender.")
    Text_Service.Dialogue("¿Delegar? Espero que sepas lo que estás haciendo. No todos son dignos de confianza." , name= "Don Graziano")
    print()

    Node9.Start()

def Investigate():
    Text_Service.Dialogue("Claro, tío, pero me gustaría saber qué hay en el paquete. ¿Es algo importante?")
    Text_Service.Dialogue("La curiosidad puede ser peligrosa, sobrino. Pero si insistes, investiga con cuidado. No quiero sorpresas.", name= "Don Graziano")
    print()

    Node8.Start()

def Collect():
    Text_Service.Dialogue("No te preocupes, tío. Iré de inmediato y traeré el paquete.")
    Text_Service.Dialogue("Eso espero. La lealtad es lo más valioso en nuestra familia." , name= "Don Graziano")
    print()

    Node7.Start()

def Actio_3():
    Text_Service.typing_effect("La atmósfera es tensa; puedes sentir la decepción en sus ojos. Sin embargo, en lugar de castigarte, te ofrece una segunda oportunidad. Te explica que hay una misión menor que necesita ser atendida: recoger un “paquete” de un aliado de la familia.\n")
    Text_Service.Dialogue("Sobrino, me has decepcionado, pero todos merecen una segunda oportunidad. Hay un paquete que necesita ser recogido de uno de nuestros aliados. Es una tarea sencilla, pero importante. No me falles esta vez.\n", name= "Don Graziano")

Node3 = ActionNode(Actio_3)
Desitions = {
    "Recoger": ActionNode(Collect),
    "Investigar": ActionNode(Investigate),
    "Delegar": ActionNode(Delegate)
}
Node3.set_SubNodes(Desitions)

