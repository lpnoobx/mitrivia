def saludo():
    print("Bienvenido a mi trivia sobre la Independencia del Perú")
    print("Pondremos a prueba tus conocimientos")


def validar_respuesta(respuesta):

    while respuesta not in ("a", "b", "c", "d", "e"):
        respuesta = input(
            "Debes responder a,b,c,d o e . Ingrese nuevamente tu respuesta : ")
        respuesta = respuesta.lower()

    return respuesta


def run():
    correctas = 0
    repetir = "si"
    while repetir == "si":
        saludo()
        nombre = input("Ingrese su nombre : ")
        print(
            "Hola " + nombre +
            " responde  las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:"
        )
        print("******Pregunta número 1 *******")
        print("*******************************")
        print("1.¿En que año se declaró la idependencia del Perú?")
        print("a. 1831")
        print("b. 1821")
        print("c. 1828")
        print("d. 1825")
        print("e. 1811")
        respuesta1 = input("Ingrese la alternativa correcta : ")
        respuesta1 = respuesta1.lower()
        #print(respuesta1)
        validar_respuesta(respuesta1)

        if respuesta1 == "b":
            print("Respuesta CORRECTA ,sigamos con más preguntas")
            correctas = correctas + 1
        else:
            print("RESPUESTA EQUIVOCADA,sigamos con más preguntas ")
        print("**************************")
        print("******Pregunta número 2 *******")
        print("*******************************")
        print("2. ¿En que año se realizó la batalla de Ayacucho?")
        print("a. 1831")
        print("b. 1821")
        print("c. 1828")
        print("d. 1825")
        print("e. 1824")
        respuesta2 = input("Ingrese la alternativa correcta : ")
        respuesta2 = respuesta2.lower()
        validar_respuesta(respuesta2)

        if respuesta2 == "e":
            print("Respuesta CORRECTA ,sigamos con más preguntas")
            correctas = correctas + 1
        else:
            print("RESPUESTA EQUIVOCADA,sigamos con más preguntas ")
        print("**************************")
        print("******Pregunta número 3 *******")
        print("*******************************")
        print("3. ¿En que año se nació El general José de San Martín?")
        print("a. 1771")
        print("b. 1781")
        print("c. 1778")
        print("d. 1772")
        print("e. 1774")
        respuesta3 = input("Ingrese la alternativa correcta : ")
        respuesta3 = respuesta3.lower()
        validar_respuesta(respuesta3)

        if respuesta3 == "c":
            print("Respuesta CORRECTA ,hemos terminado")
            correctas = correctas + 1
        else:
            print("RESPUESTA EQUIVOCADA,hemos terminado ")
        correctas = str(correctas)
        print("En total respondio correctamente : " + correctas +
              " de 3 preguntas ")
        print("**************************")

        repetir1 = input(
            "Ingresa SI para repetir la trivia , sino ingrese cualquier caracter para terminar: "
        )
        repetir1 = repetir1.lower()
        if repetir1 == "si":
            repetir = "si"
            correctas = 0
        else:
            repetir = "no"


if __name__ == "__main__":
    run()
