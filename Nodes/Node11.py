from Sound_Service import Sound_Service
from Listener_Service import Listener_Service
import Text_Service
from Action_Node import ActionNode

from Node28 import Node28

def Counterattack():
    Text_Service.typing_effect("Sientes que la mejor defensa es un buen ataque. Propones un plan para golpear a los rusos antes de que ellos puedan reaccionar.\n")

    Text_Service.Dialogue("Debemos atacar primero. Si los golpeamos ahora, no tendrán tiempo de reaccionar.")
    Text_Service.Dialogue("Interesante… pero arriesgado. Me gusta tu espíritu.", name= "Don Graziano")

    Node28.Start()

def Truce():
    Text_Service.typing_effect("Crees que una tregua podría evitar más derramamiento de sangre. Propones negociar con los rusos.\n")

    Text_Service.Dialogue("Quizás deberíamos ofrecer una tregua. Podríamos evitar más conflictos.")
    Text_Service.Dialogue("Una tregua… Podría funcionar, pero debemos ser cautelosos.", name= "Don Graziano")

    ##TODO: GO TO NODE 31

def Wait():
    Text_Service.typing_effect("Decides que lo mejor es esperar y ver qué hacen los rusos antes de actuar.")

    Text_Service.Dialogue("Deberíamos esperar. Ver qué hacen ellos primero.")
    Text_Service.Dialogue("Paciencia… A veces es la mejor estrategia. Pero debemos estar preparados.", name= "Don Graziano")

    ##TODO: GO TO NODE 32

def Actio_11():
    Text_Service.typing_effect("e encuentras en la oficina del Don, un lugar lujosamente decorado con muebles de caoba y cuadros antiguos. El Don te recibe con una sonrisa, pero su expresión se torna seria al hablar de los rusos.\n")

    Text_Service.Dialogue("Bien hecho, muchacho. Tu lealtad no pasará desapercibida. Pero ahora, tenemos un problema mayor. Los rusos no dejarán esto así.", name= "Don Graziano")
    Text_Service.Dialogue("Lo sé, tío. Estoy listo para lo que venga.")


Node11 = ActionNode(Actio_11)
Desitions = {
    "Contraataque": ActionNode(Counterattack),
    "Tregua": ActionNode(Truce),
    "Esperar": ActionNode(Wait)
}
Node11.set_SubNodes(Desitions)

