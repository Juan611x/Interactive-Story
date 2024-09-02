from Sound_Service import Sound_Service
from Listener_Service import Listener_Service
import Text_Service
from Action_Node import ActionNode

from Node28	import Node28


def New_Operation():
    Text_Service.typing_effect("Propones un nuevo plan para recuperar lo perdido y demostrar tu lealtad.\n")

    Text_Service.Dialogue("Tengo un nuevo plan. Esta vez no fallaremos.")
    Text_Service.Dialogue("Eso espero. No podemos permitir más errores.", name= "Don Graziano")

    ##TODO: GO TO NODE 35

def Revenge():
    Text_Service.typing_effect("Decides que la mejor forma de redimirte es vengarte de quienes te traicionaron.\n")

    Text_Service.Dialogue("Debemos vengarnos. No pueden salirse con la suya.")
    Text_Service.Dialogue("La venganza puede ser dulce, pero también peligrosa. Procede con cuidado.", name= "Don Graziano")
    
    Node28.Start()

def Investigate():
    Text_Service.typing_effect("Crees que alguien te traicionó y decides investigar quién fue.\n")

    Text_Service.Dialogue("Alguien nos traicionó. Necesito saber quién fue.")
    Text_Service.Dialogue("Buena idea. Encuentra al traidor y tráelo ante mí.", name= "Don Graziano")

    ##TODO: GO TO NODE 36

def Actio_13():
    Text_Service.typing_effect("Logras escapar y vuelves con el Don, aunque has perdido la carga. El Don te da otra oportunidad.\n")

    Text_Service.typing_effect("Estás de vuelta en la oficina del Don, explicándole lo sucedido. Aunque decepcionado, el Don decide darte otra misión.\n")

    Text_Service.Dialogue("Perder la carga es un golpe duro, pero confío en ti. Te daré otra oportunidad.", name= "Don Graziano")
    Text_Service.Dialogue("Gracias, tío. No te decepcionaré.")

Node13 = ActionNode(Actio_13)
Desitions = {
    "Nueva operación": ActionNode(New_Operation),
    "Venganza": ActionNode(Revenge),
    "Investigar": ActionNode(Investigate)
}
Node13.set_SubNodes(Desitions)

