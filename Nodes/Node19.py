from Sound_Service import Sound_Service
from Listener_Service import Listener_Service
import Text_Service
from Action_Node import ActionNode


def Actio_19():
    Text_Service.typing_effect("La entrega del paquete fue impecable, pero apenas regresas a tu territorio, comienzas a escuchar susurros entre tus hombres. El paquete que entregaste no es un simple encargo, sino algo que podría poner en peligro a todos. Los rumores se propagan como un fuego incontrolable, alimentando el miedo y la incertidumbre en tu organización. Algunos de tus hombres más veteranos, aquellos que han sobrevivido a las peores batallas contigo, empiezan a mirarte con escepticismo.\n")
    Text_Service.typing_effect("En las sombras de tu club, un lugar que solía ser un santuario de lealtad, ahora sientes la tensión. Los murmullos en las esquinas, las miradas furtivas, todo te indica que la situación es más grave de lo que parece. Decides mantener la fachada de normalidad, pero no puedes ignorar el creciente malestar entre tus filas.")

    Text_Service.typing_effect('Una noche, mientras revisas las cuentas en tu oficina, recibes una llamada de Jony "El Flaco", uno de tus lugartenientes más confiables.\n')

    Text_Service.Dialogue("Jefe, no sé cómo decirte esto, pero la gente está nerviosa. Dicen que ese paquete podría ser una bomba de tiempo... que podría volarnos a todos si no tenemos cuidado.", name= "Jony")
    Text_Service.Dialogue("Son solo rumores, Tony. La gente siempre habla cuando no tiene nada mejor que hacer.")
    Text_Service.Dialogue("Lo sé, jefe, pero... estos rumores vienen de muy arriba. Gente que no suele equivocarse. Quizás deberíamos tomar precauciones.", name= "Jony")
    Text_Service.Dialogue("Precauciones... ya hemos tomado suficientes. Diles a los hombres que se concentren en su trabajo y dejen de escuchar chismes.")

Node19 = ActionNode(Actio_19)
Desitions = {
    "Calla Rumores" : ActionNode()
}
