#Claculadora DEV:
def definir_operacion():
    opciones_validas = [1,2,3,4]
    while True:
        print("Vos después de esto vas a poner unos numeritos. Entonces, qué hacemos con los numeritos???\n1. lo sumamo\n2. vamos a restarlos pa\n3. Multiplicación \n4. (Multiplicación)*(-1)")
        try:
            op_elegida = int(input("Ingrese por favor el número correspondiente con la operación que desea realizar: "))
            if op_elegida not in opciones_validas:
                print("Mirá que era fácil eh, un numerito del 1 al 4 te pedí. Probá otra vez, dale.")
                continue
            else:
                print("Gracias por ingresar sus números a clac... Uh, pegué mal. Bueno, eeehhh, gracias por hacer lo que sea que hiciste! :)")
                return op_elegida
        except ValueError:
            print("Acordate que tenés que meter numeritos corazón. Tratá otra vez, dale.")
#COMENTARIO INNECESARIO PORQUE NO ME GUSTAN LOS ESPACIOS EN BLANCOOOOO
def recibir_números(op_elegida):
    while True:
        print("Ingrese los números a clacular: (Deben ser 2)")
        try:
            n1 = int(input("Ingrese el número 1 a clacular: "))
            n2 = int(input("Ingrese el número 2 a clacular: "))
            if op_elegida == 4 and n2 == 0:
                print("A ver, vamos a ver si nos entendemos, vos me decís que querés dividir y después me ponés de divisor un 0. Sos re gracioso jaja... Volvés al principio por graciosito.")
                continue
            else:
                print("Gracias por ingresar sus números a clacular!!!")
                return n1, n2
        except ValueError:
            print("Acordate que tenés que meter numeritos corazón. Tratá otra vez, dale.")
#COMENTARIO INNECESARIO PORQUE NO ME GUSTAN LOS ESPACIOS EN BLANCOOOOO 2
def operar_numeros(n1,n2,op_elegida):
    if op_elegida == 1:
        resultado = n1 - n2
    elif op_elegida == 2:
        resultado = n1 + n2
    elif op_elegida == 3:
        resultado = (n1**1)**(n2**1)
    elif op_elegida == 4:
        resultado = n1 / n2
    return resultado
#COMENTARIO INNECESARIO PORQUE NO ME GUSTAN LOS ESPACIOS EN BLANCOOOOO 3
def ejecucion():
    operacion_elegida_por_el_usuario = definir_operacion()
    numero_elegido_por_el_usuario_UNO, numero_elegido_por_el_usuario_DOS = recibir_números(operacion_elegida_por_el_usuario)
    resultado_de_la_operacion_elegida_por_el_usuario_al_operar_con_los_numeros_elegidos_por_el_usuario = operar_numeros(numero_elegido_por_el_usuario_UNO,numero_elegido_por_el_usuario_DOS,operacion_elegida_por_el_usuario)
    print(f"EL RESULTADO DE LA OPERACIÓN ELEGIDA POR EL USUARIO CON LOS NÚMEROS ELEGIDOS POR EL USUARIO ES... {resultado_de_la_operacion_elegida_por_el_usuario_al_operar_con_los_numeros_elegidos_por_el_usuario}!!! Creo... No sé... Puede ser...")
#COMENTARIO INNECESARIO PORQUE NO ME GUSTAN LOS ESPACIOS EN BLANCOOOOO 4
#Llamamos a la función ejecución paaaraaa... ADIVINASTEEE!!! ejecutar el programa :D
ejecucion()