from Sound_Service import Sound_Service
from Listener_Service import Listener_Service
import Text_Service
from Action_Node import ActionNode


def Ignore():
    Text_Service.Dialogue("No hay tiempo para dudas. Tenemos un trabajo que hacer. ¡Vamos!")
    Text_Service.Dialogue("(en voz baja) “Espero que no seamos los próximos…", name= "Maton 1")

    ##TODO: GO TO NODE 43

def Motivate():
    Text_Service.Dialogue("Sé que esto fue difícil de ver, pero Marco nos puso a todos en peligro. Necesitamos estar unidos y fuertes. Confío en cada uno de ustedes.")
    Text_Service.Dialogue("Entendemos, jefe. Estamos contigo.", name= "Maton 1")

    ##TODO: GO TO NODE 43

def Actio_16():
    Text_Service.typing_effect("Eliminas al traidor, pero esto levanta sospechas entre tus hombres sobre tu brutalidad.")

    Text_Service.typing_effect("Después de descubrir la traición de Luca, decides que no puede quedar impune. En un acto de determinación, lo eliminas frente a tus hombres. La atmósfera se vuelve tensa, y puedes sentir las miradas de tus hombres, algunos de ellos cuestionando tu decisión.\n")

    Text_Service.Dialogue("Marco nos traicionó. No podemos permitir que la deslealtad se propague en nuestras filas.")
    Text_Service.Dialogue("(murmurando) “¿Era necesario matarlo así?", name= "Maton 1")
    Text_Service.Dialogue("¿Quién será el próximo?", name= "Maton 2")

    Text_Service.typing_effect("La eliminación de Marco ha sembrado dudas y miedo entre tus hombres. Debes decidir cómo manejar esta situación para mantener el control y la lealtad de tu equipo.\n")

Node16 = ActionNode(Actio_16)
Desitions = {
    "Ignorar": ActionNode(Ignore),
    "Motivar": ActionNode(Motivate)
}
Node16.set_SubNodes(Desitions)

