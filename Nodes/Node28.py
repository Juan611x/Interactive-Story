from Sound_Service import Sound_Service
from Listener_Service import Listener_Service
import Text_Service
from Action_Node import ActionNode


def Withdrawal():
    Text_Service.typing_effect("Decides apostar todo en un ataque frontal. Aunque es una demostración de poder, tu familia está mal preparada y rápidamente es abrumada por la fuerza superior de los rusos. Terminas siendo emboscado y asesinado en la refriega final. El juego termina con la muerte del protagonista y la caída de su familia.\n")


def Defend():
    Text_Service.typing_effect("Decides fortificar tu base y esperar a que los rusos vengan a ti. Sin embargo, el asedio es brutal y los recursos empiezan a escasear. En un acto de desesperación, los rusos lanzan un ataque devastador, rompiendo las defensas y matándote en la sala de mando mientras intentas hacer tu última llamada de auxilio.\n")


def Stroke():
    Text_Service.typing_effect("Decides que la mejor opción es retirarte y reagruparte. Sin embargo, mientras intentas escapar, te das cuenta de que los rusos ya te tienen rodeado. Un traidor en tus filas te vende a los rusos, y terminas siendo capturado y ejecutado, dejando a tu familia sin líder y a merced de sus enemigos.\n")


def Actio_28():
    Text_Service.typing_effect("La guerra que tanto temías ha comenzado. Las calles están llenas de sangre y caos, mientras las balas vuelan y las lealtades se ponen a prueba. Tu base de operaciones, una mansión fortificada en las afueras de la ciudad, se convierte en el centro de mando de tu familia. Los informes de bajas llegan constantemente, y cada minuto cuenta para tomar decisiones que podrían cambiar el curso de la batalla.\n")

    Text_Service.Dialogue("Jefe, los rusos han tomado el puerto. Estamos perdiendo terreno rápidamente. Necesitamos contraatacar ahora o estaremos acabados.", name= "Aliados")
    Text_Service.Dialogue("¡Maldita sea! No podemos dejar que se salgan con la suya. Reúnan a los hombres, vamos a enseñarles quién manda en esta ciudad.")
    Text_Service.Dialogue("Pero, jefe... no tenemos los números para un asalto directo. Quizás deberíamos considerar una retirada estratégica.", name= "Aliados")
    Text_Service.Dialogue("No, no hay marcha atrás ahora. Si retrocedemos, estaremos muertos. Es todo o nada.")



Node28 = ActionNode(Actio_28)
Desitions = {
    "Ataque": ActionNode(Withdrawal),
    "Defender": ActionNode(Defend),
    "Retirada": ActionNode(Stroke)
}
Node28.set_SubNodes(Desitions)

