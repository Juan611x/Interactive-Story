from Sound_Service import Sound_Service
from Listener_Service import Listener_Service
import Text_Service
from Action_Node import ActionNode


def Actio_17():
    Text_Service.typing_effect("Intentas interrogar a Luca")

    Text_Service.typing_effect("Llevas a Luca a una habitación aislada en el sótano del almacén. La habitación está apenas iluminada por una bombilla colgante, creando sombras inquietantes en las paredes. El aire es denso y cargado de tensión. Luca está atado a una silla, sus manos temblorosas y su rostro pálido.\n")

    Text_Service.Dialogue("Luca, sabes que no toleramos la traición. Habla, y tal vez puedas salvar tu vida.")
    Text_Service.Dialogue("(mirando alrededor, nervioso) No es tan simple, jefe. Los rusos… ellos tienen algo sobre mí.", name= "Luca")
    Text_Service.Dialogue("¿Qué tienen? ¿Qué te hicieron hacer?")
    Text_Service.Dialogue("(sudando) “Me obligaron a pasarles información. Si no lo hacía, iban a matar a mi familia.", name= "Luca")
    Text_Service.Dialogue("Podrías haber venido a nosotros. Podríamos haberte protegido.")
    Text_Service.Dialogue("No lo entiendes. Ellos… ellos son implacables.", name= "Luca")
    Text_Service.Dialogue("Hablarás, Luca. Y más te vale que sea la verdad.")
    Text_Service.Dialogue("(mirando fijamente) “Lo siento, jefe. No puedo dejar que esto continúe.", name= "Luca")

    Text_Service.typing_effect("Mientras hablas, notas que Luca está cada vez más inquieto. Sus ojos se mueven frenéticamente, buscando una salida. De repente, en un movimiento rápido y desesperado, saca un arma oculta en su bota. Antes de que puedas reaccionar, dispara. Sientes un dolor agudo en el pecho y caes al suelo. La habitación se oscurece mientras tu visión se desvanece.\n")

    Text_Service.typing_effect("Luca te asesina y tu historia termina aquí")

    Text_Service.typing_effect("La noticia de tu muerte se esparce rápidamente. El Don Graziano, devastado por la pérdida de su sobrino, jura venganza contra los rusos y cualquier traidor que se cruce en su camino. La guerra entre las familias se intensifica, y el nombre de Luca se convierte en sinónimo de traición y cobardía.\n")

Node17 = ActionNode(Actio_17)


