import os
import time
import sys
from graphviz import Digraph
from afd import AFD
from ap import AP
from reportlab.pdfgen import canvas
from PIL import Image
from reportlab.lib.pagesizes import A4
import csv
import io
automataGeneral = dict()
cadenasPrincipal = dict()
cadenasSecundario = dict()
gramaticaGeneral = dict()
apPrincipal = dict()
apSecundario = dict()
ruta = os.path.join(os.sep, "Users", "Elder", "Desktop", "Repositorio", "AFD")
rutaGuardar = os.path.join(os.sep, "Users", "Elder", "Desktop", "Repositorio", "Guardados","")
print(" ")
print("----------Datos del estudiante----------")
print("#                                      #")
print("# Lenguajes formales y de programacion #")
print("#              Seccion: B-             #")
print("#           Carne: 201700761           #")
print("#                                      #")
print("----------------------------------------")
print(" ")
input("Presione enter para continuar")


def BorrarPantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def menu():
    # Función que limpia la pantalla y muestra nuevamente el menú
    # Estructura básica del menú
    BorrarPantalla()
    print('#####MENÚ PROYECTO 1#####')
    print("Selecciona una opción para navegar")
    print("\t1. Crear AFD")
    print("\t2. Crear Gramática")
    print("\t3. Evaluar Cadenas")
    print("\t4. Reportes")
    print("\t5. Cargar archivo de Entrada")
    print("\t6. Guardar archivo")
    print("\t7. Salir")
    print("#######################")

    while True:
        # Solicitamos una opción al usuario para poder navegar dentro del menú
        opcionMenu = input("Inserta un número para la navegación: ")

        if opcionMenu.isdigit() == True:
            opcionMenu = int(opcionMenu)
            if opcionMenu == 1:
                BorrarPantalla()
                menuAFD()
            elif opcionMenu == 2:
                BorrarPantalla()
                menuGramatica()
            elif opcionMenu == 3:
                BorrarPantalla()
                menuCadenas()
            elif opcionMenu == 4:
                BorrarPantalla()
                menuReportes()
            elif opcionMenu == 5:
                BorrarPantalla()
                menuCarga()
            elif opcionMenu == 6:
                BorrarPantalla()
                menuGuardar()
            elif opcionMenu == 7:
                menuPrincipal()
            else:
                print("\nIngrese una opción válida por favor. \n")
        else:
            print("\nIngrese una opción válida por favor. \n")

def menuAFD():
    BorrarPantalla()
    print("#####MENÚ AFD#####")
    print("\t1. Crear AFD desde cero")
    print("\t2. Ayuda")
    print("\t3. Salir al Menú Principal")
    print("##################")

    while True:
        # Solicitamos una opción al usuario para poder navegar dentro del menú
        opcionMenu = input("Inserta un número para la navegación: ")
        if opcionMenu.isdigit():
            opcionMenu = int(opcionMenu)
            if opcionMenu == 1:
                creacionAFD()
            elif opcionMenu == 2:
                print("Elder Anibal Pum Rojas\n201700761\nLenguajes Formales y de Programación 'B-'")
                menuAFD()
            elif opcionMenu == 3:
                print("Regresando al menú principal. \n")
                menu()
            else:
                print("\nIngrese una opción válida por favor. \n")
                print("#####MENÚ AFD#####")
                print("\t1. Crear AFD desde cero")
                print("\t2. Ayuda")
                print("\t3. Salir al Menú Principal")
                print("##################")
        else:
            print("\nIngrese una opción válida por favor. \n")

def menuGramatica():
    BorrarPantalla()
    print("#####MENÚ GRAMÁTICA#####")
    print("\t1. Crear Gramática desde cero")
    print("\t2. Ayuda")
    print("\t3. Salir al Menú Principal")
    print("########################")

    while True:
        # Solicitamos una opción al usuario para poder navegar dentro del menú
        opcionMenu = input("Insertar un número para la navegación: ")
        if opcionMenu.isdigit():
            opcionMenu = int(opcionMenu)
            if opcionMenu == 1:
                creacionGramatica()
            elif opcionMenu == 2:
                print("Elder Anibal Pum Rojas\n201700761\nLenguajes Formales y de Programación 'B-'")
                menuGramatica()
            elif opcionMenu == 3:
                print("Saliendo al Menú Principal")
                print()
                menu()
            else:
                print("\nIngrese una opción válida por favor. \n")
                print("#####MENÚ GRAMÁTICA#####")
                print("\t1. Crear Gramática desde cero")
                print("\t2. Ayuda")
                print("\t3. Salir al Menú Principal")
                print("########################")
        else:
            print("\nIngrese una opción válida por favor. \n")

def crearGramaticaDelAFDGenerado(gramatica, transicionPrimario, estadosAceptacion):
    for i in transicionPrimario:
        for j, k in transicionPrimario[i].items():
            agregarGramatica = i + " > " + j + " " + k
            gramatica.append(agregarGramatica)
            if i in estadosAceptacion:
                agregarGramatica = i + " > " + "epsilon"
                gramatica.append(agregarGramatica)
                break
            elif k in estadosAceptacion:
                agregarGramatica = k + " > " + "epsilon"
                gramatica.append(agregarGramatica)
                break
    return gramatica

def creacionAFD():
    BorrarPantalla()
    estados = []
    estadosAceptacion = []  # Estos son estados finales
    EstadoInicialLista = []
    transiciones = []
    alfabeto = []
    transicionPrimario = dict()
    transicionSecundaria = dict()
    gramatica = []

    # Primero empezamos pidiendo el nombre del AFD
    nombreAFD = input("\nIngrese el nombre del AFD: \n")
    # Segundo, empezamos agregando estados
    print("Ingrese la cantidad de estados que desea agregar al AFD:")
    numeroEstados = int(input())
    if numeroEstados == "":
        print("\nEste estado ya fue agregado con anterioridad. Por favor volver a intentarlo.\n")
        menuAFD()
    else:
        for i in range(1, numeroEstados + 1):
            nuevoEstado = input("Ingrese el estado: ")
            if nuevoEstado in estados:
                print("\nEste estado ya fue agregado con anterioridad. Por favor volver a intentarlo.\n")
                menuAFD()
            elif nuevoEstado == "":
                print("\nNo se permiten espacios vacíos. Por favor volver a intentarlo\n")
                menuAFD()
            else:
                estados.append(nuevoEstado)

    # Tercero, ingresamos el alfabeto
    print("\nIngrese la cantidad de alfabetos que existiran en el conjuto de terminales:")
    numeroAlfabeto = int(input())
    if numeroAlfabeto == "":
        print("\nEste estado ya fue agregado con anterioridad. Por favor volver a intentarlo.\n")
        menuAFD()
    else:
        for i in range(1, numeroAlfabeto + 1):
            nuevoAlfabeto = input("Ingrese el terminal: ")
            if nuevoAlfabeto in alfabeto:
                print("\nEste terminal ya fue agregado con anterioridad. Por favor volver a intentarlo\n")
                menuAFD()
            elif nuevoAlfabeto == "":
                print("No se permiten espacios vacíos. Por favor volver a intentarlo.")
                menuAFD()
            else:
                if nuevoAlfabeto.lower() == "epsilon":
                    print("\nNo se permiten transiciones con EPSILON. Esto solo es permitido en AFN.\n")
                    menuAFD()
                else:
                    alfabeto.append(nuevoAlfabeto.lower())

    # Ahora, vamos a ingresar el estado inicial y validar que este estado exista en el array de estados
    print()
    print("Ingrese el estado inicial del AFD:")
    EstadoInicial = input()
    if EstadoInicial == "":
        print("\nEste estado ya fue agregado con anterioridad. Por favor volver a intentarlo.\n")
        menuAFD()
    else:
        EstadoInicialLista.append(EstadoInicial.upper())
        if EstadoInicial in estados:
            # Desde acá vamos a continuar el proceso, ya que si el estado inicial no existe dentro del arreglo,
            # este debería de dejar de funcionar.
            # Ahora se definen los estados de aceptación/finales.
            print()
            print("Ingrese la cantidad de estados de aceptación que tendrá su AFD:")
            numeroEstadoAceptacion = int(input())
            if numeroEstadoAceptacion == "":
                print("No se aceptan espacios vacíos.")
                menuAFD()
            else:
                for i in range(1, numeroEstadoAceptacion + 1):
                    nuevoAceptacion = input("Ingrese el estado: ")
                    if nuevoAceptacion in estadosAceptacion:
                        print("Este estado de aceptación ya fue agregado con anterioridad. Por favor volver a intentarlo.")
                        menu()
                    elif nuevoAceptacion == "":
                        print("No se aceptan cadenas vacías.")
                        menuAFD()
                    else:
                        if nuevoAceptacion in estados:
                            estadosAceptacion.append(nuevoAceptacion.upper())
                        else:
                            print(
                            "El estado que se ingresó no existe dentro de los estados que se definieron anteriormente. Por favor, volver a intentarlo.")
                            print("Regresando al menú de AFD.")
                            menuAFD()
                # Ahora ya definidos los estados, alfabetos, estado inicial y los de aceptación, se procede a meter las transiciones
                print()
                print("////////////////////////")
                print("¿Cuál método quiere usar para ingresar los estados?")
                print("\t1. Método 1: Ingresando transición por transición")
                print("\t2. Método 2: Tabla de transiciones")
                while True:
                    # Solicitamos una opción al usuario para poder navegar dentro del menú
                    opcionMenu = input("Insertar un número para la navegación: ")
                    if opcionMenu.isdigit():
                        opcionMenu = int(opcionMenu)
                        if opcionMenu == 1:
                            print()
                            print("Ha seleccionado el método 1.")
                            print("Ingrese la cantidad de transiciones que desea para armar su AFD:")
                            numeroTransicion = int(input())
                            for i in range(1, numeroTransicion + 1):
                                print("Ingrese la transición:")
                                nuevaTransicion = input("")
                                if 'epsilon' in nuevaTransicion:
                                    print("No se permiten transiciones con epsilon.")
                                    menu()
                                else:
                                    transiciones.append(nuevaTransicion)
                                    transicionLimpia = nuevaTransicion.replace(",", "").replace(";", "").replace(" ", "")
                                    texto = list(transicionLimpia)
                                    estadoInicial = texto.pop(0)
                                    estadoFinal = texto.pop(0)
                                    trans = texto.pop(0)
                                    if estadoInicial not in estados:
                                        print("Uno de los estados iniciales no concuerda con los estados anteriormente "
                                              "planteados. Por favor vuelva a intentarlo.")
                                        menu()
                                    else:
                                        if estadoFinal not in estados:
                                            print("Uno de los estados de aceptación no concuerda con los estados "
                                                  "anteriormente planteados. Por favor vuelva a intentarlo.")
                                            menu()
                                        else:
                                            if trans not in alfabeto:
                                                print("Una de las transiciones no concuerda con el alfabeto planteado "
                                                      "anteriormente. Por favor volver a intentarlo.")
                                                menu()
                                            else:
                                                if estadoInicial in transicionPrimario:
                                                    transicionSecundaria = transicionPrimario.get(estadoInicial)
                                                    if trans in transicionSecundaria:
                                                        print("No se permiten sacar dos símbolos desde un mismo estado.")
                                                        print("Eso solo es permitido en los AFN. Volver a intentarlo, por favor.")
                                                        menuAFD()
                                                    else:
                                                        transicionSecundaria.update({trans : estadoFinal})
                                                        transicionPrimario.update({estadoInicial : transicionSecundaria})
                                                else:
                                                    transicionSecundaria = dict()
                                                    transicionSecundaria.update({trans : estadoFinal})
                                                    transicionPrimario.update({estadoInicial : transicionSecundaria})
                                                texto.clear()

                            g = Digraph('AFD', filename=nombreAFD, format='png')
                            g.attr(rankdir='LR', size='8,5')
                            g.attr('node', shape='doublecircle')
                            for e in estadosAceptacion:
                                g.node(e)

                            g.attr('node', shape='circle')
                            for i in transicionPrimario:
                                for j, k in transicionPrimario[i].items():
                                    g.edge(i, k, label=j)
                            g.render(directory=ruta, view=True)
                            crearGramaticaDelAFDGenerado(gramatica, transicionPrimario, estadosAceptacion)
                            agregarAutomata = AFD(nombreAFD, estados, alfabeto, EstadoInicial, estadosAceptacion, transiciones, transicionPrimario,gramatica, gramatica)
                            automataGeneral.update({nombreAFD : agregarAutomata})
                            print(transicionPrimario)
                            print(gramatica)
                            print()
                            print("AFD generado exitosamente")
                            print("Volviendo al menú principal")
                            menu()

                        elif opcionMenu == 2:
                            aceptacion = []
                            gramatica = []
                            print("\nHa seleccionado el método #2.\n")
                            nuevoTerminal = input("Ingrese los terminales: ").replace("[", "").replace("]", "").replace(" ", "")
                            terminal = nuevoTerminal.split(",")
                            print()
                            nuevoNT = input("Ingrese los no terminales: ").replace("[", "").replace("]", "").replace(" ", "")
                            noterminal = nuevoNT.split(",")
                            print()
                            nuevoDestino = input("Ingrese los destinos: ").replace("[", "").replace("]", "").replace(" ", "")
                            filas = nuevoDestino.split(";")

                            for posNoTerminal in range(len(noterminal)):
                                eInicial = noterminal[posNoTerminal]
                                fila = filas[posNoTerminal].split(",")
                                for posTerminal in range(len(terminal)):
                                    Trans = terminal[posTerminal]
                                    eFinal = fila[posTerminal]
                                    if eFinal == '-':
                                        aceptacion.append(eInicial)
                                    else:
                                        transiciones.append(
                                            eInicial + "," + eFinal + ";" + Trans)  # Esto para guardar registro de las transiciones, como en
                                        if eInicial in transicionPrimario:
                                            transicionSecundaria = transicionPrimario.get(eInicial)
                                            transicionSecundaria.update({Trans: eFinal})
                                            transicionPrimario.update({eInicial: transicionSecundaria})
                                        else:
                                            transicionSecundaria = dict()
                                            transicionSecundaria.update({Trans: eFinal})
                                            transicionPrimario.update({eInicial: transicionSecundaria})
                            # Ya que tenemos el diccionario de diccionarios, procedemos a graficar con graphviz
                            g = Digraph('AFD', filename=nombreAFD, format='png')
                            g.attr(rankdir='LR', size='8,5')
                            g.attr('node', shape='doublecircle')
                            for e in aceptacion:
                                g.node(e)

                            g.attr('node', shape='circle')
                            for i in transicionPrimario:
                                for j, k in transicionPrimario[i].items():
                                    g.edge(i, k, label=j)
                            g.render(directory=ruta, view=True)
                            crearGramaticaDelAFDGenerado(gramatica, transicionPrimario, estadosAceptacion)
                            agregarAutomata = AFD(nombreAFD, estados, alfabeto, EstadoInicial, estadosAceptacion, transiciones, transicionPrimario, gramatica, None)
                            automataGeneral.update({nombreAFD : agregarAutomata})
                            print(transicionPrimario)
                            print("AFD generado con éxito.\n Regresando al menú principal.\n")
                            menu()
                        else:
                            print("\nIngrese una opción válida por favor. \n")
                            print("////////////////////////")
                            print("¿Cuál método quiere usar para ingresar los estados?")
                            print("\t1. Método 1: Ingresando transición por transición")
                            print("\t2. Método 2: Tabla de transiciones")
                    else:
                        print("\nIngrese una opción válida por favor. \n")
                        print("Regresando al menú principal")
                        menu()
        else:
            print(
                "El estado que se ingresó no existe dentro de los estados que se definieron anteriormente. Por favor, volver a intentarlo.")
            menuAFD()

def creacionGramatica():
    BorrarPantalla()
    terminales = []
    noTerminales = []
    noTerminalInicial = []
    producciones = []
    produccionCorrejida = []
    NTdeAceptacion = []
    transicionPrimario = dict()
    transicionSecundaria = dict()

    #Primero que nada, vamos a pedirle un nombre para la gramática
    print()
    nombreGramatica = input("Ingresa el nombre de la gramática: ")
    print()

    #Ahora vamos a ingresar los no terminales
    cantidadNT = int(input("Ingrese la cantidad de no terminales que quiere agregar: "))
    if cantidadNT == "":
        print("No se aceptan cadenas vacías.")
        menuGramatica()
    else:
        print()
        for i in range(1, cantidadNT + 1):
            nuevoNoTerminal = input("Ingrese el no terminal: ")
            if nuevoNoTerminal == "":
                print("No se aceptan cadenas vacías.")
                menuGramatica()
            elif nuevoNoTerminal in noTerminales:
                print("Este no terminal ya fue agregado con anterioridad. Por favor volver a intentarlo.")
                menuGramatica()
            else:
                noTerminales.append(nuevoNoTerminal)
        print()

    #Ahora vamos a ingresar los terminales
    cantidadTerminales = int(input("Ingrese la cantidad de terminales que quiere agregar: "))
    print()
    if cantidadTerminales == "":
        print("No se aceptan cadenas vacías.")
        menuGramatica()
    else:
        for i in range(1, cantidadTerminales + 1):
            nuevoTerminal = input("Ingrese el terminal: ")
            if nuevoTerminal == "":
                print("No se aceptan cadenas vacías")
                menuGramatica()
            elif nuevoTerminal in terminales:
                print("Este terminal ya fue agregado con anterioridad. Por favor volver a intentarlo.")
                menuGramatica()
            else:
                terminales.append(nuevoTerminal)
        print()

    #Ahora vamos a ingresar el no terminal inicial
    ntInicial = input("Ingrese el Terminal inicial: ")
    if ntInicial == "":
        print("No se aceptan cadenas vacías.")
        menuGramatica()
    else:
        if ntInicial in noTerminales:
            #Se continua el proceso desde acá
            noTerminalInicial.append(ntInicial)
            print()

            #Ahora se ingresarán las producciones que se desean realizar
            cantidadProducciones = int(input("Ingrese la cantidad de producciones que desea agregar"))
            print()
            if cantidadProducciones == "":
                print("No se aceptan cadenas vacías.")
                menuGramatica()
            else:
                for i in range(1, cantidadProducciones + 1):
                    nuevaProduccion = input("Ingrese la nueva producción: ")
                    if nuevaProduccion == "":
                        print("No se aceptan cadenas vacías.")
                        menuGramatica()
                    else:
                        producciones.append(nuevaProduccion)
                        transicionLimpia = nuevaProduccion.replace(">", "").replace(" ", "")
                        texto = list(transicionLimpia)
                        primero = texto.pop(0)
                        segundo = texto.pop(0)
                        tercero = (texto[0:1] or ('default',))[0]
                        if 'epsilon' in nuevaProduccion:
                            NTdeAceptacion.append(primero)
                            producto = primero + " > " + "epsilon"
                            produccionCorrejida.append(producto)
                        else:
                            if primero in noTerminales:
                                if primero == segundo:  # Esto verifica la recursividad como A > A a
                                    primero = primero + "*"
                                    segundo = tercero
                                    tercero = primero
                                    producto = primero + " > " + segundo + " " + tercero
                                    produccionCorrejida.append(producto)
                                    if primero in transicionPrimario:
                                        transicionSecundaria = transicionPrimario.get(primero)
                                        if segundo in transicionSecundaria:
                                            print("No se permiten sacar dos símbolos desde un mismo estado.")
                                            print(
                                                "Eso solo es permitido en los AFN. Volver a intentarlo, por favor.")
                                            menuAFD()
                                        else:
                                            transicionSecundaria.update({segundo: tercero})
                                            transicionPrimario.update({primero: transicionSecundaria})
                                    else:
                                        transicionSecundaria = dict()
                                        transicionSecundaria.update({segundo: tercero})
                                        transicionPrimario.update({primero: transicionSecundaria})
                                    texto.clear()
                                elif segundo in terminales and tercero == 'default':  # Esto arregla el A > b A* y A > epsilon de la recursiva
                                    tercero = primero + "*"
                                    inicialLimpio = primero.replace("*", "")
                                    NTdeAceptacion.append(tercero)
                                    producto = inicialLimpio + " > " + segundo + " " + tercero
                                    produccionCorrejida.append(producto)
                                    producto2 = primero + "*" + " > " + "epsilon"
                                    produccionCorrejida.append(producto2)
                                    if primero in transicionPrimario:
                                        transicionSecundaria = transicionPrimario.get(inicialLimpio)
                                        if segundo in transicionSecundaria:
                                            print("No se permiten sacar dos símbolos desde un mismo estado.")
                                            print(
                                                "Eso solo es permitido en los AFN. Volver a intentarlo, por favor.")
                                            menuAFD()
                                        else:
                                            transicionSecundaria.update({segundo: tercero})
                                            transicionPrimario.update({inicialLimpio: transicionSecundaria})
                                    else:
                                        transicionSecundaria = dict()
                                        transicionSecundaria.update({segundo: tercero})
                                        transicionPrimario.update({primero: transicionSecundaria})
                                    texto.clear()
                                else:
                                    if segundo in terminales:
                                        if tercero in noTerminales:  # Acá se agregan las gramáticas regulares, sin recursividad
                                            producto = primero + " > " + segundo + " " + tercero
                                            produccionCorrejida.append(producto)
                                            if primero in transicionPrimario:
                                                transicionSecundaria = transicionPrimario.get(primero)
                                                if segundo in transicionSecundaria:
                                                    print("No se permiten sacar dos símbolos desde un mismo estado.")
                                                    print(
                                                        "Eso solo es permitido en los AFN. Volver a intentarlo, por favor.")
                                                    menuAFD()
                                                else:
                                                    transicionSecundaria.update({segundo: tercero})
                                                    transicionPrimario.update({primero: transicionSecundaria})
                                            else:
                                                transicionSecundaria = dict()
                                                transicionSecundaria.update({segundo: tercero})
                                                transicionPrimario.update({primero: transicionSecundaria})
                                            texto.clear()
                                        else:
                                            print("El símbolo no está definido dentro de los no terminales.")
                                            menuGramatica()
                                    else:
                                        print("La transición no está definido dentro de los terminales.")
                                        menuGramatica()
                            else:
                                print("El símbolo no está definido dentro de los no terminales.")
                                menuGramatica()

                g = Digraph('GRM', filename=nombreGramatica, format='png')
                g.attr(rankdir='LR', size='8,5')
                g.attr('node', shape='doublecircle')
                for e in NTdeAceptacion:
                    g.node(e)

                g.attr('node', shape='circle')
                for i in transicionPrimario:
                    for j, k in transicionPrimario[i].items():
                        g.edge(i, k, label=j)
                g.render(directory=ruta, view=True)
                if range(len(producciones)) == range(len(produccionCorrejida)):
                    agregarAutomata = AFD(nombreGramatica, noTerminales, terminales, ntInicial, NTdeAceptacion, producciones, transicionPrimario, producciones, None)
                    automataGeneral.update({nombreGramatica : agregarAutomata})
                else:
                    agregarAutomata = AFD(nombreGramatica, noTerminales, terminales, ntInicial, NTdeAceptacion, producciones, transicionPrimario, producciones, produccionCorrejida)
                    automataGeneral.update({nombreGramatica : agregarAutomata})
                print("Gramática resuelta correctamente y su correspondiente AFD generado con éxito.\nRegresando al menú principal.")
                menuAFD()

def menuCadenas():
    BorrarPantalla()
    print("#####MENÚ EVALUAR CADENAS#####")
    print("\t1. Solo validar cadena")
    print("\t2. Ruta en AFD")
    print("\t3. Expandir con Gramática")
    print("\t4. Ayuda")
    print("\t5. Salir")
    print("##############################")

    while True:
        # Solicitamos un número al usuario para poder navegar en el menú
        opcionMenu = input("Insertar un número para la evaluación: ")
        if opcionMenu.isdigit():
            opcionMenu = int(opcionMenu)
            if opcionMenu == 1:
                validarCadena()
            elif opcionMenu == 2:
                rutaAFD()
            elif opcionMenu == 3:
                expansionGramatica()
            elif opcionMenu == 4:
                print("Elder Anibal Pum Rojas\n201700761\nLenguajes Formales y de Programación 'B-'")
                menuCadenas()
            elif opcionMenu == 5:
                print("\nRegresando al menú principal.\n")
                menu()
            else:
                print("\nIngrese una opción válida por favor. \n")
        else:
            print("\nIngrese una opción válida por favor. \n")

def validarCadena():
    print("\nHa seleccionado la opción de únicamente validar cadenas.\n")
    cadena = input("Ingrese la cadena a evaluar: ")
    nombre = input("\ningrese el nombre de su AFD/Gramática que desea evaluar: ")
    gramaticaGuardada = automataGeneral.get(nombre)
    if gramaticaGuardada is not None:
        estadoInicial = gramaticaGuardada.inicial
        estadosAceptacion = gramaticaGuardada.aceptacion
        estadoFinal = None
        diccionario = gramaticaGuardada.mapaTransicion
        cadenaInvalida = False
        for letra in cadena:
            transiciones = diccionario.get(estadoInicial)
            estadoFinal = transiciones.get(letra)
            if estadoFinal is not None:
                estadoInicial = estadoFinal
            else:
                cadenaInvalida = True
                break
        if cadenaInvalida:
            print("Error. Cadena inválida.")
            if nombre in cadenasPrincipal:
                cadenasSecundario = cadenasPrincipal.get(nombre)
                if cadena in cadenasSecundario:
                    print("No se puede evaluar 2 veces la misma cadena. Por favor, volver a intentarlo.")
                    menuCadenas()
                else:
                    cadenasSecundario.update({cadena: cadenaInvalida})
                    cadenasPrincipal.update({nombre: cadenasSecundario})
            else:
                cadenasSecundario = dict()
                cadenasSecundario.update({cadena: cadenaInvalida})
                cadenasPrincipal.update({nombre: cadenasSecundario})
                print(cadenasPrincipal)
        else:
            if estadoFinal in estadosAceptacion:
                print("Cadena Válida.")
                if nombre in cadenasPrincipal:
                    cadenasSecundario = cadenasPrincipal.get(nombre)
                    if cadena in cadenasSecundario:
                        print("No se puede evaluar 2 veces la misma cadena. Por favor, volver a intentarlo.")
                        menuCadenas()
                    else:
                        cadenasSecundario.update({cadena: cadenaInvalida})
                        cadenasPrincipal.update({nombre: cadenasSecundario})
                else:
                    cadenasSecundario = dict()
                    cadenasSecundario.update({cadena: cadenaInvalida})
                    cadenasPrincipal.update({nombre: cadenasSecundario})
                    print(cadenasPrincipal)
                menuCadenas()
            else:
                print("Error. Cadena inválida")
                if nombre in cadenasPrincipal:
                    cadenasSecundario = cadenasPrincipal.get(nombre)
                    if cadena in cadenasSecundario:
                        print("No se puede evaluar 2 veces la misma cadena. Por favor, volver a intentarlo.")
                        menuCadenas()
                    else:
                        cadenasSecundario.update({cadena: cadenaInvalida})
                        cadenasPrincipal.update({nombre: cadenasSecundario})
                else:
                    cadenasSecundario = dict()
                    cadenasSecundario.update({cadena: cadenaInvalida})
                    cadenasPrincipal.update({nombre: cadenasSecundario})
                    print(cadenasPrincipal)
                menuCadenas()
    else:
        print("Error, no existe.")
        menuCadenas()

def rutaAFD():
    print("\nHa seleccionado la opción de validar cadenas en notación AFD.\n")
    cadena = input("Ingrese la cadena a evaluar: ")
    nombre = input("\ningrese el nombre de su AFD/Gramática que desea evaluar: ")
    gramaticaGuardada = automataGeneral.get(nombre)
    if gramaticaGuardada is not None:
        estadoInicial = gramaticaGuardada.inicial
        estadosAceptacion = gramaticaGuardada.aceptacion
        estadoFinal = None
        diccionario = gramaticaGuardada.mapaTransicion
        cadenaInvalida = False
        for letra in cadena:
            transiciones = diccionario.get(estadoInicial)
            estadoFinal = transiciones.get(letra)
            if estadoFinal is not None:
                estadoInicial = estadoFinal
                print(str(estadoInicial) + ", " + str(estadoFinal) + ", " + str(transiciones) + ";")
            else:
                cadenaInvalida = True
                break
        if cadenaInvalida:
            print("Error. Cadena inválida")
            if nombre in cadenasPrincipal:
                cadenasSecundario = cadenasPrincipal.get(nombre)
                if cadena in cadenasSecundario:
                    print("No se puede evaluar 2 veces la misma cadena. Por favor, volver a intentarlo.")
                    menuCadenas()
                else:
                    cadenasSecundario.update({cadena: cadenaInvalida})
                    cadenasPrincipal.update({nombre: cadenasSecundario})
            else:
                cadenasSecundario = dict()
                cadenasSecundario.update({cadena: cadenaInvalida})
                cadenasPrincipal.update({nombre: cadenasSecundario})
                print(cadenasPrincipal)
            menuCadenas()
        else:
            if estadoFinal in estadosAceptacion:
                print("Cadena Válida.")
                if nombre in cadenasPrincipal:
                    cadenasSecundario = cadenasPrincipal.get(nombre)
                    if cadena in cadenasSecundario:
                        print("No se puede evaluar 2 veces la misma cadena. Por favor, volver a intentarlo.")
                        menuCadenas()
                    else:
                        cadenasSecundario.update({cadena: cadenaInvalida})
                        cadenasPrincipal.update({nombre: cadenasSecundario})
                else:
                    cadenasSecundario = dict()
                    cadenasSecundario.update({cadena: cadenaInvalida})
                    cadenasPrincipal.update({nombre: cadenasSecundario})
                    print(cadenasPrincipal)
                menuCadenas()
            else:
                print("Error. Cadena inválida")
                if nombre in cadenasPrincipal:
                    cadenasSecundario = cadenasPrincipal.get(nombre)
                    if cadena in cadenasSecundario:
                        print("No se puede evaluar 2 veces la misma cadena. Por favor, volver a intentarlo.")
                        menuCadenas()
                    else:
                        cadenasSecundario.update({cadena: cadenaInvalida})
                        cadenasPrincipal.update({nombre: cadenasSecundario})
                else:
                    cadenasSecundario = dict()
                    cadenasSecundario.update({cadena: cadenaInvalida})
                    cadenasPrincipal.update({nombre: cadenasSecundario})
                    print(cadenasPrincipal)
                menuCadenas()
    else:
        print("Error, no existe.")
        menuCadenas()

def expansionGramatica():
    print("\nHa seleccionado la opción de validar cadenas utilizando notación de gramática regular.\n")
    cadena = input("Ingrese la cadena a evaluar: ")
    nombre = input("\ningrese el nombre de su AFD/Gramática que desea evaluar: ")
    gramaticaGuardada = automataGeneral.get(nombre)
    if gramaticaGuardada is not None:
        estadoInicial = gramaticaGuardada.inicial
        estadosAceptacion = gramaticaGuardada.aceptacion
        estadoFinal = None
        diccionario = gramaticaGuardada.mapaTransicion
        cadenaInvalida = False
        for letra in cadena:
            transiciones = diccionario.get(estadoInicial)
            estadoFinal = transiciones.get(letra)
            if estadoFinal is not None:
                estadoInicial = estadoFinal
                print(str(estadoInicial) + " > " + str(letra) + " " + str(estadoFinal))
            else:
                cadenaInvalida = True
                break
        if cadenaInvalida:
            print("Error. Cadena inválida")
            if nombre in cadenasPrincipal:
                cadenasSecundario = cadenasPrincipal.get(nombre)
                if cadena in cadenasSecundario:
                    print("No se puede evaluar 2 veces la misma cadena. Por favor, volver a intentarlo.")
                    menuCadenas()
                else:
                    cadenasSecundario.update({cadena: cadenaInvalida})
                    cadenasPrincipal.update({nombre: cadenasSecundario})
            else:
                cadenasSecundario = dict()
                cadenasSecundario.update({cadena: cadenaInvalida})
                cadenasPrincipal.update({nombre: cadenasSecundario})
                print(cadenasPrincipal)
            menuCadenas()
        else:
            if estadoFinal in estadosAceptacion:
                print("Cadena Válida.")
                if nombre in cadenasPrincipal:
                    cadenasSecundario = cadenasPrincipal.get(nombre)
                    if cadena in cadenasSecundario:
                        print("No se puede evaluar 2 veces la misma cadena. Por favor, volver a intentarlo.")
                        menuCadenas()
                    else:
                        cadenasSecundario.update({cadena: cadenaInvalida})
                        cadenasPrincipal.update({nombre: cadenasSecundario})
                else:
                    cadenasSecundario = dict()
                    cadenasSecundario.update({cadena: cadenaInvalida})
                    cadenasPrincipal.update({nombre: cadenasSecundario})
                    print(cadenasPrincipal)
                menuCadenas()
            else:
                print("Error. Cadena inválida")
                if nombre in cadenasPrincipal:
                    cadenasSecundario = cadenasPrincipal.get(nombre)
                    if cadena in cadenasSecundario:
                        print("No se puede evaluar 2 veces la misma cadena. Por favor, volver a intentarlo.")
                        menuCadenas()
                    else:
                        cadenasSecundario.update({cadena: cadenaInvalida})
                        cadenasPrincipal.update({nombre: cadenasSecundario})
                else:
                    cadenasSecundario = dict()
                    cadenasSecundario.update({cadena: cadenaInvalida})
                    cadenasPrincipal.update({nombre: cadenasSecundario})
                    print(cadenasPrincipal)
                menuCadenas()
    else:
        print("Error, no existe.")
        menuCadenas()

def menuReportes():
    BorrarPantalla()
    print("#####MENÚ REPORTES#####")
    print("\t1. Ver detalle")
    print("\t2. Generar reporte en PDF")
    print("\t3. Ayuda")
    print("\t4. Salir")
    print("##############################")

    while True:
        # Solicitamos un número al usuario para poder navegar en el menú
        opcionMenu = input("Insertar un número para la evaluación: ")
        if opcionMenu.isdigit():
            opcionMenu = int(opcionMenu)
            if opcionMenu == 1:
                reporteDetalle()
            elif opcionMenu == 2:
                generarPDF()
            elif opcionMenu == 3:
                print("Elder Anibal Pum Rojas\n201700761\nLenguajes Formales y de Programación 'B-'")
                menuCadenas()
            elif opcionMenu == 4:
                print("\nRegresando al menú principal.\n")
                menu()
            else:
                print("\nIngrese una opción válida por favor. \n")
        else:
            print("\nIngrese una opción válida por favor. \n")

def reporteDetalle():
    print("\nHa seleccionado la opción #1\n")
    nombre = input("Ingrese el nombre de su AFD/Gramática que desea evaluar: ")
    nombreGuardado = automataGeneral.get(nombre)
    if nombreGuardado is not None:
        estadosGuardados = nombreGuardado.estados
        alfabetoGuardado = nombreGuardado.alfabeto
        inicialGuardado = nombreGuardado.inicial
        aceptacionGuardado = nombreGuardado.aceptacion
        transicionGuardado = nombreGuardado.transiciones
        revisarTransicion = transicionGuardado[0]
        if ',' in revisarTransicion:
            print("Detalle del AFD:")
            print(nombre)
            print("El alfabeto es:")
            print(alfabetoGuardado)
            print("Los estados son:")
            print(estadosGuardados)
            print("Los estados de aceptación son:")
            print(aceptacionGuardado)
            print("El estado inicial es:")
            print(inicialGuardado)
            print("Y las transiciones son:")
            print(transicionGuardado)
            print()
            print("Detalle mostrado con éxito.\nVolviendo al menú principal.\n")
            time.sleep(5)
            menuReportes()
        else:
            print("Detalle de la gramática:")
            print(nombre)
            print("Los no terminales son:")
            print(estadosGuardados)
            print("Los terminales son:")
            print(alfabetoGuardado)
            print("El no terminal inicial es:")
            print(inicialGuardado)
            print("Las producciones son:")
            print(transicionGuardado)
            print()
            print("Detalle mostrado con éxito.\nVolviendo al menú principal.\n")
            time.sleep(5)
            menuReportes()
    else:
        print("Error. No existe")
        menuReportes()

def generarPDF():
    rutaArchivo = os.path.join(os.sep, "Users", "Elder", "Desktop", "Repositorio", "AFD", "")
    print("\nHa seleccionado la opción #2\n")
    nombre = input("Ingrese el nombre del AFD/Gramática a reportar: ")
    listaCadenasValidas = []
    listaCadenasInvalidas = []
    nombreGuardadoObjeto = automataGeneral.get(nombre)
    if nombreGuardadoObjeto is not None:
        img = Image.open(rutaArchivo + nombre + ".png")
        estadosGuardados = nombreGuardadoObjeto.estados
        alfabetoGuardado = nombreGuardadoObjeto.alfabeto
        inicialGuardado = nombreGuardadoObjeto.inicial
        aceptacionGuardado = nombreGuardadoObjeto.aceptacion
        transicionGuardado = nombreGuardadoObjeto.transiciones
        gramaticaGuardada = nombreGuardadoObjeto.gramatica
        gramaticaRegularGuardada = nombreGuardadoObjeto.gramaticaRegular
        cadenasEvaluadas = cadenasPrincipal.get(nombre)
        if cadenasEvaluadas is not None:
            for llave, valor in cadenasEvaluadas.items():
                if valor:#La cadena es inválida
                    listaCadenasInvalidas.append(llave)
                else:#La cadena es válida
                    listaCadenasValidas.append(llave)
        w, h = A4
        pdf = canvas.Canvas(filename=nombre+".pdf")
        pdf.setTitle("Reporte_" + nombre)
        text = pdf.beginText(50, h - 50)
        text.setFont("Times-Roman", 12)
        text.textLine("AFD")
        text.textLine("Alfabeto:")
        for x in alfabetoGuardado:
            text.textLine("-" + x)
        text.textLine("Estados:")
        for x in estadosGuardados:
            text.textLine("-" + x)
        text.textLine("Estado inicial: " + inicialGuardado)
        text.textLine("Estados de aceptación:")
        for x in aceptacionGuardado:
            text.textLine("-" + x)
        text.textLine()
        text.textLine("Gramática")
        text.textLine("No terminales:")
        for x in estadosGuardados:
            text.textLine("-" + x)
        text.textLine("Terminales:")
        for x in alfabetoGuardado:
            text.textLine("-" + x)
        text.textLine("Estado inicial: " + inicialGuardado)
        text.textLine("Producciones: ")
        for x in gramaticaGuardada:
            text.textLine("-" + x)
        text.textLine("Gramática sin recursividad por la izquierda.")
        text.textLine("Producciones:")
        if gramaticaRegularGuardada is not None:
            for x in gramaticaRegularGuardada:
                text.textLine(x)
        else:
            text.textLine("No tiene recursividad por la izquierda.")
        text.textLine()
        text.textLine("Cadenas evaluadas.")
        text.textLine("Todas las cadenas evaluadas:")
        for x in cadenasEvaluadas:
            text.textLine("-" + x)
        text.textLine("Todas las cadenas válidas:")
        for x in listaCadenasValidas:
            text.textLine("-" + x)
        text.textLine("Todas las cadenas inválidas:")
        for x in listaCadenasInvalidas:
            text.textLine("-" + x)
        text.textLine()
        text.textLine("AFD Generado")
        pdf.drawText(text)
        pdf.drawInlineImage(img, 100, 0)
        pdf.save()
        print("Reporte generado en la carpeta raíz del proyecto. Regresando al menú principal.")
        menu()

    else:
        print("Error. No existe")
        menuReportes()

def menuCarga():
    BorrarPantalla()
    print("#####MENÚ CARGA DE ARCHIVOS#####")
    print("\t1. Cargar archivo .afd")
    print("\t2. Cargar archivo .grm")
    print("\t3. Ayuda")
    print("\t4. Salir")
    print("##############################")

    while True:
        # Solicitamos un número al usuario para poder navegar en el menú
        opcionMenu = input("Insertar un número para la evaluación: ")
        if opcionMenu.isdigit():
            opcionMenu = int(opcionMenu)
            if opcionMenu == 1:
                cargarAFD()
            elif opcionMenu == 2:
                cargaGramatica()
            elif opcionMenu == 3:
                print("Elder Anibal Pum Rojas\n201700761\nLenguajes Formales y de Programación 'B-'")
                menuCarga()
            elif opcionMenu == 4:
                print("\nRegresando al menú principal.\n")
                menu()
            else:
                print("\nIngrese una opción válida por favor. \n")
        else:
            print("\nIngrese una opción válida por favor. \n")

def cargarAFD():
    print("\nHa seleccionado la opción #1.\n")
    path = input("\nIngrese la ruta del archivo: ")
    estados = []
    alfabeto = []
    estadosAceptacion = []
    transiciones = []
    gramatica = []
    transicionPrincipal = dict()
    transicionSecundaria = dict()
    while True:
        nombre, extension = os.path.splitext(path)
        if extension == ".afd":
            nombreAFD = nombre
            break
        else:
            path = input("\nIngrese la ruta del archivo: ")

    with open(path, "r") as archivo:
        for linea in archivo:
            transicion = linea.replace(";",",").replace(","," ").split()
            inicial = transicion.pop(0)
            final = transicion.pop(0)
            trans = transicion.pop(0)
            banderaEstado1 = transicion.pop(0)
            banderaEstado2 = transicion.pop(0)
            if banderaEstado1 == 'false':
                bandera1 = False
            else:
                bandera1 = True
            if banderaEstado2 == 'false':
                bandera2 = False
            else:
                bandera2 = True
            if inicial in estados or final in estados:
                print("Este estado ya está agregado, se va a saltear: " + inicial)
            else:
                estados.append(inicial)
                if final in estados:
                    print("Este estado ya está agregado, se va a saltear: " + final)
                else:
                    estados.append(final)
            if trans in alfabeto:
                print("Esta transición ya está agregada, se va a saltear: " + trans)
            else:
                alfabeto.append(trans)
            if bandera1:
                if inicial in estadosAceptacion:
                    print("No se puede agregar este estado a los de aceptación ya que ya fue agregado.")
                else:
                    estadosAceptacion.append(inicial)
            else:
                print("No es un estado de aceptación: " + inicial)
            if bandera2:
                if final in estadosAceptacion:
                    print("No se puede agregar este estado a los de aceptación ya que ya fue agregado.")
                else:
                    estadosAceptacion.append(final)
            else:
                print("No es un estado de aceptación: " + final)
            transiciones.append(inicial + "," + final + ";" + trans)
            if inicial in transicionPrincipal:
                transicionSecundaria = transicionPrincipal.get(inicial)
                if trans in transicionSecundaria:
                    print("No se permiten sacar dos símbolos desde un mismo estado.")
                    print("Eso solo es permitido en los AFN. Volver a intentarlo, por favor.")
                    menuCarga()
                else:
                    transicionSecundaria.update({trans: final})
                    transicionPrincipal.update({inicial: transicionSecundaria})
            else:
                transicionSecundaria = dict()
                transicionSecundaria.update({trans: final})
                transicionPrincipal.update({inicial: transicionSecundaria})
            transicion.clear()
        estadoInicial = estados[0]

        g = Digraph('AFD', filename=nombreAFD, format='png')
        g.attr(rankdir='LR', size='8,5')
        g.attr('node', shape='doublecircle')
        for e in estadosAceptacion:
            g.node(e)

        g.attr('node', shape='circle')
        for i in transicionPrincipal:
            for j, k in transicionPrincipal[i].items():
                g.edge(i, k, label=j)
        g.render(directory=ruta, view=True)
        crearGramaticaDelAFDGenerado(gramatica, transicionPrincipal, estadosAceptacion)
        agregarAutomata = AFD(nombreAFD, estados, alfabeto, estadoInicial, estadosAceptacion, transiciones,transicionPrincipal, gramatica, None)
        automataGeneral.update({nombreAFD: agregarAutomata})
        print("AFD generado con éxito.\n Regresando al menú principal.\n")
        menu()

def cargaGramatica():
    print("\nHa seleccionado la opción #2.\n")
    path = input("\nIngrese la ruta del archivo: ")
    noTerminales = []
    terminales = []
    ntAceptacion = []
    producciones = []
    produccionCorrejida = []
    transicionPrimario = dict()
    transicionSecundaria = dict()

    while True:
        nombre, extension = os.path.splitext(path)
        if extension == ".grm":
            nombreGramatica = nombre
            break
        else:
            path = input("\nIngrese la ruta del archivo: ")

    with open(path, "r") as archivo:
        for linea in archivo:
            producciones.append(linea)
            texto = linea.replace(">", "").split()
            primero = texto.pop(0)
            segundo = texto.pop(0)
            tercero = (texto[0:1] or ('default',))[0]
            noTerminales.append(primero)
            if segundo in noTerminales:
                terminales.append(tercero)
            else:
                noTerminales.append(tercero)
                terminales.append(segundo)
            if 'epsilon' in linea:
                ntAceptacion.append(primero)
                producto = primero + " > " + "epsilon"
                produccionCorrejida.append(producto)
            else:
                if primero in noTerminales:
                    if primero == segundo:  # Esto verifica la recursividad como A > A a
                        primero = primero + "*"
                        segundo = tercero
                        tercero = primero
                        producto = primero + " > " + segundo + " " + tercero
                        produccionCorrejida.append(producto)
                        if primero in transicionPrimario:
                            transicionSecundaria = transicionPrimario.get(primero)
                            if segundo in transicionSecundaria:
                                print("No se permiten sacar dos símbolos desde un mismo estado.")
                                print(
                                    "Eso solo es permitido en los AFN. Volver a intentarlo, por favor.")
                                menu()
                            else:
                                transicionSecundaria.update({segundo: tercero})
                                transicionPrimario.update({primero: transicionSecundaria})
                        else:
                            transicionSecundaria = dict()
                            transicionSecundaria.update({segundo: tercero})
                            transicionPrimario.update({primero: transicionSecundaria})
                        texto.clear()
                    elif segundo in terminales and tercero == 'default':  # Esto arregla el A > b A* y A > epsilon de la recursiva
                        tercero = primero + "*"
                        inicialLimpio = primero.replace("*", "")
                        ntAceptacion.append(tercero)
                        producto = inicialLimpio + " > " + segundo + " " + tercero
                        produccionCorrejida.append(producto)
                        producto2 = primero + "*" + " > " + "epsilon"
                        produccionCorrejida.append(producto2)
                        if primero in transicionPrimario:
                            transicionSecundaria = transicionPrimario.get(inicialLimpio)
                            if segundo in transicionSecundaria:
                                print("No se permiten sacar dos símbolos desde un mismo estado.")
                                print(
                                    "Eso solo es permitido en los AFN. Volver a intentarlo, por favor.")
                                menu()
                            else:
                                transicionSecundaria.update({segundo: tercero})
                                transicionPrimario.update({inicialLimpio: transicionSecundaria})
                        else:
                            transicionSecundaria = dict()
                            transicionSecundaria.update({segundo: tercero})
                            transicionPrimario.update({primero: transicionSecundaria})
                        texto.clear()
                    else:
                        if segundo in terminales:
                            if tercero in noTerminales:  # Acá se agregan las gramáticas regulares, sin recursividad
                                producto = primero + " > " + segundo + " " + tercero
                                produccionCorrejida.append(producto)
                                if primero in transicionPrimario:
                                    transicionSecundaria = transicionPrimario.get(primero)
                                    if segundo in transicionSecundaria:
                                        print("No se permiten sacar dos símbolos desde un mismo estado.")
                                        print(
                                            "Eso solo es permitido en los AFN. Volver a intentarlo, por favor.")
                                        menu()
                                    else:
                                        transicionSecundaria.update({segundo: tercero})
                                        transicionPrimario.update({primero: transicionSecundaria})
                                else:
                                    transicionSecundaria = dict()
                                    transicionSecundaria.update({segundo: tercero})
                                    transicionPrimario.update({primero: transicionSecundaria})
                                texto.clear()
                            else:
                                print("El símbolo no está definido dentro de los no terminales.")
                                menu()
                        else:
                            print("La transición no está definido dentro de los terminales.")
                            menu()
                else:
                    print("El símbolo no está definido dentro de los no terminales.")
                    menu()
        ntInicial = noTerminales[0]
        g = Digraph('GRM', filename=nombreGramatica, format='png')
        g.attr(rankdir='LR', size='8,5')
        g.attr('node', shape='doublecircle')
        for e in ntAceptacion:
            g.node(e)

        g.attr('node', shape='circle')
        for i in transicionPrimario:
            for j, k in transicionPrimario[i].items():
                g.edge(i, k, label=j)
        g.render(directory=ruta, view=True)
        if range(len(producciones)) == range(len(produccionCorrejida)):
            texto = "No tiene recursividad por la Izquierda."
            agregarAutomata = AFD(nombreGramatica, noTerminales, terminales, ntInicial, ntAceptacion, producciones, transicionPrimario, texto)
            automataGeneral.update({nombreGramatica: agregarAutomata})
        else:
            agregarAutomata = AFD(nombreGramatica, noTerminales, terminales, ntInicial, ntAceptacion, producciones, transicionPrimario, produccionCorrejida)
            automataGeneral.update({nombreGramatica: agregarAutomata})
        print("Gramática resuelta correctamente y su correspondiente AFD generado con éxito.\nRegresando al menú principal.")
        menuAFD()

def menuGuardar():
    BorrarPantalla()
    print("#####MENÚ CARGA DE ARCHIVOS#####")
    print("\t1. Guardar archivo")
    print("\t2. Ayuda")
    print("\t3. Salir")
    print("##############################")

    while True:
        # Solicitamos un número al usuario para poder navegar en el menú
        opcionMenu = input("Insertar un número para la evaluación: ")
        if opcionMenu.isdigit():
            opcionMenu = int(opcionMenu)
            if opcionMenu == 1:
                BorrarPantalla()
                guardarArchivo()
            elif opcionMenu == 2:
                print("Elder Anibal Pum Rojas\n201700761\nLenguajes Formales y de Programación 'B-'")
                menuGuardar()
            elif opcionMenu == 3:
                print("\nRegresando al menú principal.\n")
                menu()
            else:
                print("\nIngrese una opción válida por favor. \n")
        else:
            print("\nIngrese una opción válida por favor. \n")

def guardarArchivo():
    print("\nHa seleccionado la opción de guardar un archivo.\n")
    nombre = input("\ningrese el nombre de su AFD/Gramática que desea evaluar: ")
    nombreObjeto = automataGeneral.get(nombre)
    if nombreObjeto is not None:
        estadoInicial = nombreObjeto.inicial
        estados = nombreObjeto.estados
        alfabeto = nombreObjeto.alfabeto
        aceptacion = nombreObjeto.aceptacion
        transiciones = nombreObjeto.transiciones
        gramaticaRegular = nombreObjeto.gramaticaRegular
        revisarTransicion = transiciones[0]
        if ',' in revisarTransicion:
            extensionAFD = ".afd"
            file = open(rutaGuardar + nombre + extensionAFD, "w")
            for linea in transiciones:
                transicionLimpia = linea.replace(",", "").replace(";", "").replace(" ", "")
                texto = list(transicionLimpia)
                inicial = texto.pop(0)
                final = texto.pop(0)
                trans = texto.pop(0)
                if inicial in estados and inicial in aceptacion:
                    if trans in alfabeto:
                        bandera1 = 'true'
                    else:
                        print("El alfabeto no está definido. Volviendo al menú principal.")
                        menu()
                elif inicial in estados and inicial not in aceptacion:
                    if trans in alfabeto:
                        bandera1 = 'false'
                    else:
                        print("El alfabeto no está definido. Volviendo al menú principal.")
                        menu()
                else:
                    print("Estado no existe en los definidos. Volviendo al menú principal.")
                    menu()
                if final in estados and final in aceptacion:
                    if trans in alfabeto:
                        bandera2 = 'true'
                    else:
                        print("Estado no existe en los definidos. Volviendo al menú principal.")
                        menu()
                elif final in estados and final not in aceptacion:
                    if trans in alfabeto:
                        bandera2 = 'false'
                    else:
                        print("Estado no existe en los definidos. Volviendo al menú principal.")
                        menu()
                else:
                    print("Estado no existe en los definidos. Volviendo al menú principal.")
                    menu()
                file.write(inicial+","+final+","+trans+";"+bandera1+","+bandera2 + "\n")
            file.close()
            print("Archivo .afd guardado con éxito.")
            menu()
        else:
            extensionGRM = ".grm"
            file = open(rutaGuardar + nombre + extensionGRM, "w")
            for linea in transiciones:
                transicionLimpia = linea.replace(">", "").replace(" ", "")
                texto = list(transicionLimpia)
                primero = texto.pop(0)
                segundo = texto.pop(0)
                tercero = (texto[0:1] or ('default',))[0]
                if 'epsilon' in linea:
                    file.write(primero + " > " + "epsilon")
                else:
                    if primero in estados:
                        if primero == segundo:  # Esto verifica la recursividad como A > A a
                            primero = primero + "*"
                            segundo = tercero
                            tercero = primero
                            file.write(primero + " > " + segundo + " " + tercero + "\n")
                        elif segundo in alfabeto and tercero == 'default':
                            tercero = primero + "*"
                            inicialLimpio = primero.replace("*", "")
                            file.write(inicialLimpio + " > " + segundo + " " + tercero + "\n")
                            file.write(primero + "*" + " > " + "epsilon" + "\n")
                        else:
                            if segundo in alfabeto:
                                if tercero in estados:  # Acá se agregan las gramáticas regulares, sin recursividad
                                    file.write(primero + " > " + segundo + " " + tercero + "\n")
            file.close()
            print("Archivo .grm guardado con éxito.")
            menu()

def menuPrincipal():
    BorrarPantalla()
    print("#####MENÚ PRINCIPAL#####")
    print("\t1. Menú Proyecto #1")
    print("\t2. Menú Proyecto #2")
    print("\t3. Salir")
    print("##############################")

    while True:
        # Solicitamos un número al usuario para poder navegar en el menú
        opcionMenu = input("Insertar un número para la evaluación: ")
        if opcionMenu.isdigit():
            opcionMenu = int(opcionMenu)
            if opcionMenu == 1:
                BorrarPantalla()
                menu()
            elif opcionMenu == 2:
                BorrarPantalla()
                menuProyecto2()
            elif opcionMenu == 3:
                BorrarPantalla()
                sys.exit()
            else:
                print("\nIngrese una opción válida por favor. \n")
        else:
            print("\nIngrese una opción válida por favor. \n")

def menuProyecto2():
    BorrarPantalla()
    print("#####MENÚ PROYECTO 2#####")
    print("\t1. Ingresar / Modificar Gramática")
    print("\t2. Generar Autómata de Pila")
    print("\t3. Validar Cadena")
    print("\t4. Salir")
    print("##############################")

    while True:
        # Solicitamos un número al usuario para poder navegar en el menú
        opcionMenu = input("Insertar un número para la evaluación: ")
        if opcionMenu.isdigit():
            opcionMenu = int(opcionMenu)
            if opcionMenu == 1:
                BorrarPantalla()
                crearGramaticaT2()
            elif opcionMenu == 2:
                BorrarPantalla()
                generarAP()
            elif opcionMenu == 3:
                BorrarPantalla()
                validarCadenaAP()
            elif opcionMenu == 4:
                BorrarPantalla()
                menuProyecto2()
            else:
                print("\nIngrese una opción válida por favor. \n")
        else:
            print("\nIngrese una opción válida por favor. \n")

def crearGramaticaT2():
    terminales = []
    noTerminales = []
    producciones = []
    esNombreRepetido = False
    listaProdRaiz = []

    while True:
        nombreG2 = input("\nIngrese el nombre de su gramática: \n")
        if nombreG2 == "":
            print("Por favor, llenar este campo.\n")
        else:
            break

    nombreGramatica = gramaticaGeneral.get(nombreG2)
    if nombreGramatica is not None: #Si no es nulo, el nombre ya fue ingresado anteriormente.
        esNombreRepetido = True
    else:
        esNombreRepetido = False #Si es nulo, el nombre aún no ha sido ingresado.

    if esNombreRepetido:
        print("Gramática ya ingresada. Iniciando proceso de modificación.\n")
        terminalesGramatica = nombreGramatica.terminales
        ntGramatica = nombreGramatica.noTerminales
        produccionesGramatica = nombreGramatica.producciones
        inicialGramatica = nombreGramatica.inicial
        del gramaticaGeneral[nombreG2]
        while True:
            preguntaTerminal = input("\n¿Desea ingresar nuevos terminales? <Si-No> \n")
            if preguntaTerminal == "":
                print("Por favor, llenar este campo.\n")
            elif preguntaTerminal == "No":
                break
            elif preguntaTerminal == "Si":
                terminalesGramatica = []
                while True:
                    ingresarNumeroTerminal = input("Ingrese el número de terminales: \n")
                    try:
                        ingresarNumeroTerminal = int(ingresarNumeroTerminal)
                        if ingresarNumeroTerminal == "":
                            print("Por favor, llenar este campo.\n")
                        else:
                            break
                    except ValueError:
                        print("Atención, únicamente se aceptan números. Volver a intentarlo.")
                for i in range(1, ingresarNumeroTerminal + 1):
                    while True:
                        ingresarNuevoTerminal = input("Ingrese el nuevo terminal: \n")
                        if ingresarNuevoTerminal == "":
                            print("Por favor, llenar este campo.\n")
                        elif ingresarNuevoTerminal in terminalesGramatica:
                            print("Por favor, ingrese un terminal distinto, no se aceptan repetidos.\n")
                        elif ingresarNuevoTerminal.isupper():
                            print("Por favor, ingresar únicamente letras minúsculas.\n")
                        else:
                            break
                    terminalesGramatica.append(ingresarNuevoTerminal)
                break
            else:
                print("Responda únicamente con Si o No, por favor volver a intentarlo.\n")

        while True:
            preguntaNoTerminal = input("\n¿Desea ingresar nuevos no terminales? <Si-No> \n")
            if preguntaNoTerminal == "":
                print("Por favor, llenar este campo.\n")
            elif preguntaNoTerminal == "No":
                break
            elif preguntaNoTerminal == "Si":
                ntGramatica = []
                while True:
                    ingresarNumeroNT = input("Ingrese el número de terminales: \n")
                    try:
                        ingresarNumeroNT = int(ingresarNumeroNT)
                        if ingresarNumeroNT == "":
                            print("Por favor, llenar este campo.\n")
                        else:
                            break
                    except ValueError:
                        print("Atención, únicamente se aceptan números. Volver a intentarlo.")
                for i in range(1, ingresarNumeroNT + 1):
                    while True:
                        ingresarNuevoNT = input("Ingrese el nuevo terminal: \n")
                        if ingresarNuevoNT == "":
                            print("Por favor, llenar este campo.\n")
                        elif ingresarNuevoNT in ntGramatica:
                            print("Por favor, ingrese un terminal distinto, no se aceptan repetidos.\n")
                        elif ingresarNuevoNT.isupper():
                            print("Por favor, ingresar únicamente letras minúsculas.\n")
                        else:
                            break
                    ntGramatica.append(ingresarNuevoNT)
                break
            else:
                print("Responda únicamente con Si o No, por favor volver a intentarlo.\n")

        while True:
            preguntaProduccion = input("\n¿Desea ingresar nuevas producciones? <Si-No> \n")
            if preguntaProduccion == "":
                print("Por favor, llenar este campo.\n")
            elif preguntaProduccion == "No":
                break
            elif preguntaProduccion == "Si":
                produccionesGramatica = []
                while True:
                    ingresarNumeroProduccion = input("Ingrese el número de producciones: \n")
                    try:
                        ingresarNumeroProduccion = int(ingresarNumeroProduccion)
                        if ingresarNumeroProduccion == "":
                            print("Por favor, llenar este campo.\n")
                        else:
                            break
                    except ValueError:
                        print("Atención, únicamente se aceptan números. Volver a intentarlo.")
                for i in range(1, ingresarNumeroProduccion + 1):
                    while True:
                        ingresarNuevaProduccion = input("Ingrese la nueva producción: \n")
                        if ingresarNuevaProduccion == "":
                            print("Por favor, llenar este campo.\n")
                        elif ingresarNuevaProduccion in produccionesGramatica:
                            print("Por favor, ingrese un terminal distinto, no se aceptan repetidos.\n")
                        else:
                            break
                    produccionesGramatica.append(ingresarNuevaProduccion)
                break
            else:
                print("Responda únicamente con Si o No, por favor volver a intentarlo.\n")

        while True:
            print("\nEstas son las producciones ingresadas dentro de su gramática:\n")
            print("Las producciones son: ", produccionesGramatica)
            preguntaBorrar = input("\n¿Desea borrar alguna producción ingresada? <Si-No> \n")
            if preguntaBorrar == "":
                print("Por favor, llenar este campo.\n")
            elif preguntaBorrar == "No":
                break
            elif preguntaBorrar == "Si":
                while True:
                    ingresarBorrado = input("Ingrese la producción que desea borrar: \n")
                    if ingresarBorrado == "":
                        print("Por favor, llenar este campo.\n")
                    elif ingresarBorrado in produccionesGramatica:
                        produccionesGramatica.remove(ingresarBorrado)
                        break
                    else:
                        print("No se encontró la producción a borrar, revise la lista y vuelva a intentarlo.\n")
            else:
                print("Responda únicamente con Si o No, por favor volver a intentarlo.\n")

        # Acá vamos a crear el mapa mejor, si se borran producciones no hay problema
        del apPrincipal[nombreG2]
        for i in produccionesGramatica:
            produccionLimpia = i.replace(" ", "")
            partirProduccion = produccionLimpia.split(">")
            noTerminalInicial = partirProduccion.pop(0)
            produccionResultante = partirProduccion.pop(0)
            if nombreG2 in apPrincipal:
                apSecundario = apPrincipal.get(nombreG2)
                if noTerminalInicial in apSecundario:
                    listaProdRaiz.append(produccionResultante)
                    apSecundario.update({noTerminalInicial: listaProdRaiz})
                    apPrincipal.update({nombreG2: apSecundario})
                else:
                    listaProdRaiz = []
                    listaProdRaiz.append(produccionResultante)
                    apSecundario.update({noTerminalInicial: listaProdRaiz})
                    apPrincipal.update({nombreG2: apSecundario})
            else:
                apSecundario = dict()
                listaProdRaiz = []
                listaProdRaiz.append(produccionResultante)
                apSecundario.update({noTerminalInicial: listaProdRaiz})
                apPrincipal.update({nombreG2: apSecundario})

        while True:
            preguntaInicial = input("\n¿Desea ingresar un nuevo estado inicial? <Si-No> \n")
            if preguntaInicial == "":
                print("Por favor, llenar este campo.\n")
            elif preguntaInicial == "No":
                break
            elif preguntaInicial == "Si":
                ingresarNuevoInicial = input("Por favor, ingrese el estado inicial de la gramática: ")
                print()
                if ingresarNuevoInicial == "":
                    print("Por favor, llenar este campo.\n")
                elif ingresarNuevoInicial in ntGramatica:
                    inicialGramatica = ingresarNuevoInicial
                    break
                else:
                    print("Por favor, volver a intentarlo.\n")
            else:
                print("Responda únicamente con Si o No, por favor volver a intentarlo.\n")
        #Ahora guardamos los datos nuevamente.
        guardarGramatica = AP(nombreG2, terminalesGramatica, ntGramatica, produccionesGramatica, inicialGramatica)
        gramaticaGeneral.update({nombreG2: guardarGramatica})
        print(apPrincipal)
        print("\nProceso de guardado de gramática completado. Volviendo al menú.\n")
        menuProyecto2()

    else: #Gramática nueva
        while True:
            numeroTerminales = input("Ingrese el número de terminales: \n")
            try:
                numeroTerminales = int(numeroTerminales)
                if numeroTerminales == "":
                    print("Por favor, llenar este campo.\n")
                else:
                    break
            except ValueError:
                print("Atención, únicamente se aceptan números. Volver a intentarlo.")

        for i in range(1, numeroTerminales + 1):
            while True:
                ingresarTerminal = input("Ingrese el terminal: \n")
                if ingresarTerminal == "":
                    print("Por favor, llenar este campo.\n")
                elif ingresarTerminal in terminales:
                    print("Por favor, ingrese un terminal distinto, no se aceptan repetidos.\n")
                elif ingresarTerminal.isupper():
                    print("Por favor, ingresar únicamente letras minúsculas.\n")
                else:
                    break
            terminales.append(ingresarTerminal)

        while True:
            numeroNT = input("Ingrese el número de no terminales: \n")
            try:
                numeroNT = int(numeroNT)
                if numeroNT == "":
                    print("Por favor, llenar este campo.\n")
                else:
                    break
            except ValueError:
                print("Atención, únicamente se aceptan números. Volver a intentarlo.")

        for i in range(1, numeroNT + 1):
            while True:
                ingresarNT = input("Ingrese el no terminal: \n")
                if ingresarNT == "":
                    print("Por favor, llenar este campo.\n")
                elif ingresarNT in noTerminales:
                    print("Por favor, ingrese un no terminal distinto, no se aceptan repetidos.\n")
                elif ingresarNT.islower():
                    print("Por favor, ingresar únicamente letras mayúsculas.\n")
                else:
                    break
            noTerminales.append(ingresarNT)

        while True:
            numeroProducciones = input("Ingrese el número de producciones: \n")
            try:
                numeroProducciones = int(numeroProducciones)
                if numeroProducciones == "":
                    print("Por favor, llenar este campo.\n")
                else:
                    break
            except ValueError:
                print("Atención, únicamente se aceptan números. Volver a intentarlo.")

        for i in range(1, numeroProducciones + 1):
            while True:
                ingresarProduccion = input("Ingrese la producción: \n")
                if ingresarProduccion == "":
                    print("Por favor, llenar este campo.\n")
                elif ingresarProduccion in producciones:
                    print("Por favor, ingrese una producción distinta, no se permiten repetir producciones.\n")
                else:
                    break
            producciones.append(ingresarProduccion)

        while True:
            print("\nEstas son las producciones ingresadas dentro de su gramática:\n")
            print("Las producciones son: ", producciones)
            preguntaBorrarP = input("\n¿Desea borrar alguna producción ingresada? <Si-No> \n")
            if preguntaBorrarP == "":
                print("Por favor, llenar este campo.\n")
            elif preguntaBorrarP == "No":
                break
            elif preguntaBorrarP == "Si":
                while True:
                    ingresarBorrado = input("Ingrese la producción que desea borrar: \n")
                    if ingresarBorrado == "":
                        print("Por favor, llenar este campo.\n")
                    elif ingresarBorrado in producciones:
                        producciones.remove(ingresarBorrado)
                        break
                    else:
                        print("No se encontró la producción a borrar, revise la lista y vuelva a intentarlo.\n")
            else:
                print("Responda únicamente con Si o No, por favor volver a intentarlo.\n")

        #Acá vamos a crear el mapa mejor, si se borran producciones no hay problema
        for i in producciones:
            produccionLimpia = i.replace(" ", "")
            partirProduccion = produccionLimpia.split(">")
            noTerminalInicial = partirProduccion.pop(0)
            produccionResultante = partirProduccion.pop(0)
            if nombreG2 in apPrincipal:
                apSecundario = apPrincipal.get(nombreG2)
                if noTerminalInicial in apSecundario:
                    listaProdRaiz.append(produccionResultante)
                    apSecundario.update({noTerminalInicial : listaProdRaiz})
                    apPrincipal.update({nombreG2 : apSecundario})
                else:
                    listaProdRaiz = []
                    listaProdRaiz.append(produccionResultante)
                    apSecundario.update({noTerminalInicial : listaProdRaiz})
                    apPrincipal.update({nombreG2 : apSecundario})
            else:
                apSecundario = dict()
                listaProdRaiz = []
                listaProdRaiz.append(produccionResultante)
                apSecundario.update({noTerminalInicial : listaProdRaiz})
                apPrincipal.update({nombreG2 : apSecundario})

        while True:
            ingresarInicial = input("Por favor, ingrese el estado inicial de la gramática: ")
            print()
            if ingresarInicial == "":
                print("Por favor, llenar este campo.\n")
            elif ingresarInicial in noTerminales:
                break
            else:
                print("Por favor, volver a intentarlo.\n")
        guardarGramatica = AP(nombreG2, terminales, noTerminales, producciones, ingresarInicial)
        gramaticaGeneral.update({nombreG2: guardarGramatica})
        print(apPrincipal)
        print("\nProceso de guardado de gramática completado. Volviendo al menú.\n")
        menuProyecto2()

def generarAP():
    while True:
        nombreAP = input("\nIngrese el nombre de su gramática: \n")
        if nombreAP == "":
            print("Por favor, llenar este campo.\n")
        else:
            break
    objetoGramatica = gramaticaGeneral.get(nombreAP)

    if objetoGramatica is not None: #Si no es nulo, el nombre ya fue ingresado anteriormente.
        ntInicial = objetoGramatica.inicial
        produccionesGramatica = objetoGramatica.producciones
        terminalesGramatica = objetoGramatica.terminales
        noTerminalesGramatica = objetoGramatica.noTerminales
        g = Digraph('finite_state_machine', filename=nombreAP, format='png')
        g.attr(rankdir='LR', size='8,5')
        g.attr('edge', overlap='false', splines='true')
        g.attr('node', shape='doublecircle')
        g.node("f")

        g.attr('node', shape='circle')
        g.edge("i", "p", label= "λ,λ;#")
        g.edge("p", "q", label="λ,λ;" + ntInicial)
        for i in produccionesGramatica:
            produccionLimpia = i.replace(" ", "")
            partirProduccion = produccionLimpia.split(">")
            ntInicialGramatica = partirProduccion.pop(0)
            produccionResultante = partirProduccion.pop(0)
            g.edge("q", "q", label="λ," + ntInicialGramatica + ";" + produccionResultante)
        for i in terminalesGramatica:
            g.edge("q", "q", label=i + "," + i + ";λ")
        g.edge("q", "f", label="λ,#;λ")
        g.render(directory=ruta, view=True)

        textoTerminales = ', '.join(terminalesGramatica)
        textoNoTerminales = ', '.join(noTerminalesGramatica)
        simbolosPila = textoTerminales + ", " + textoNoTerminales + ", #"

        print("\n#####SÉXTUPLA DEL AP GENERADO#####")
        print("S: {i, p, q, f}")
        print("Σ: {" + textoTerminales + "}")
        print("Γ: {" + simbolosPila + "}")
        print("L: i")
        print("F: f")
        print("T: ")
        print("\t-  (i, λ, λ; p, #)")
        print("\t-  (p, λ, λ; q, " + ntInicial + ")")
        for i in produccionesGramatica:
            produccionLimpia = i.replace(" ", "")
            partirProduccion = produccionLimpia.split(">")
            ntInicialGramatica = partirProduccion.pop(0)
            produccionResultante = partirProduccion.pop(0)
            print("\t-  (q, q, λ; " + ntInicialGramatica + ", " + produccionResultante + ")")
        for i in terminalesGramatica:
            print("\t-  (q, q, " + i + "; " + i + ", λ)")
        print("\t-  (q, λ, #; f, λ)")
        print("\nAutómata de Pila generado con éxito, volviendo al menú del proyecto 2.\n")
        BorrarPantalla()
        menuProyecto2()
    else:
        print("\nError, el nombre no existe.\n")
        BorrarPantalla()
        menuProyecto2()

def validarCadenaAP():
    esCadenaValida = False
    cadenaVacia = False
    pila = []
    cambioEnPila = []
    mapaGraficadorArbol = dict()
    while True:
        nombreAP = input("\nIngrese el nombre de su gramática: \n")
        if nombreAP == "":
            print("Por favor, llenar este campo.\n")
        else:
            break
    objetoGramatica = gramaticaGeneral.get(nombreAP)

    if objetoGramatica is not None:
        produccionCorrejida = dict()
        noTerminal = objetoGramatica.noTerminales
        ntInicial = objetoGramatica.inicial
        producciones = objetoGramatica.producciones
        terminales = objetoGramatica.terminales
        listaContenedoraProd = []
        listaGraficadora = []

        #Vamos a quitar recursividad por la izquierda
        for i in producciones:
            produccionLimpia = i.replace(" ", "")
            partirProduccion = produccionLimpia.split(">")
            noTerminalInicial = partirProduccion.pop(0)
            produccionResultante = partirProduccion.pop(0)
            listaProduccion = list(produccionResultante)
            validarNTsinRecursividad = noTerminalInicial + "*"
            if noTerminalInicial == listaProduccion[0]:
                listaContenedoraProd = []
                noTerminalSacado = listaProduccion.pop(0)
                noTerminalSacado = noTerminalSacado + "*"
                epsilon = "epsilon"
                listaProduccion.append(noTerminalSacado)
                listaContenedoraProd.append(listaProduccion)
                listaContenedoraProd.append(epsilon)
                produccionCorrejida.update({noTerminalSacado : listaContenedoraProd})
                noTerminal.append(noTerminalSacado)
            elif len(listaProduccion) == 1 and listaProduccion[0] in terminales and validarNTsinRecursividad in produccionCorrejida:
                listaContenedoraProd = []
                nuevoNT = noTerminalInicial + "*"
                listaProduccion.append(nuevoNT)
                listaContenedoraProd.append(listaProduccion)
                produccionCorrejida.update({noTerminalInicial : listaContenedoraProd})
            else:
                if noTerminalInicial in produccionCorrejida:
                    if validarNTsinRecursividad in produccionCorrejida:
                        nuevoNT = noTerminalInicial + "*"
                        listaProduccion.append(nuevoNT)
                        listaContenedoraProd.append(listaProduccion)
                        produccionCorrejida.update({noTerminalInicial: listaContenedoraProd})
                    else:
                        listaContenedoraProd.append(listaProduccion)
                        produccionCorrejida.update({noTerminalInicial: listaContenedoraProd})
                elif validarNTsinRecursividad in produccionCorrejida:
                    listaContenedoraProd = []
                    nuevoNT = noTerminalInicial + "*"
                    listaProduccion.append(nuevoNT)
                    listaContenedoraProd.append(listaProduccion)
                    produccionCorrejida.update({noTerminalInicial: listaContenedoraProd})
                else:
                    listaContenedoraProd = []
                    listaContenedoraProd.append(listaProduccion)
                    produccionCorrejida.update({noTerminalInicial: listaContenedoraProd})
        pila.insert(0, "#")
        pila.insert(0, ntInicial)
        while True:
            cadena = input("\nIngrese la cadena a evaluar: \n")
            if cadena == "":
                print("Por favor, llenar este campo.\n")
            else:
                break
        cambioEnPila.insert(0, ['(Pila)$'+'(Entrada)$'+ '(Transicion)'])
        cambioEnPila.append(['(λ)$('+cadena+')$'+'(i, λ, λ; p, #)'])
        cambioEnPila.append(['(#)$('+cadena + ')$'+'(p, λ, λ; q, '+ntInicial+')'])
        listaCadena = list(cadena)
        for i in range(0, len(cadena)):
            if len(listaCadena) == 0:
                cadenaVacia = True
            else:
                cadenaVacia = False
            letraInicialCadena = cadena[i]
            letraPila = pila.__getitem__(0)
            if letraPila in noTerminal:
                lista = produccionCorrejida.get(letraPila)
                for j in lista:
                    prod = j
                    if prod[0] == letraInicialCadena:
                        cambioEnPila.append(['('+''.join(pila) + ')$('+ ''.join(listaCadena) + ')$'+
                                             '(q, λ, ' + letraPila + '; q, ' + ''.join(prod) + ')'])
                        raiz = pila.pop(0)
                        for a in prod:
                            if raiz in mapaGraficadorArbol:
                                listaGraficadora.append(a)
                                mapaGraficadorArbol.update({raiz : listaGraficadora})
                            else:
                                listaGraficadora = []
                                listaGraficadora.append(a)
                                mapaGraficadorArbol.update({raiz : listaGraficadora})
                        prod.reverse()
                        for i in prod:
                            pila.insert(0, i)
                        prod.reverse()
                        break
                    elif len(prod) == 1 and prod[0] in noTerminal:
                        letra = prod[0]
                        cambioEnPila.append(['('+''.join(pila) + ')$('+ ''.join(listaCadena) + ')$'+
                                             '(q, λ, ' + pila.__getitem__(0) + '; q, ' + ''.join(prod) + ')'])
                        raiz = pila.pop(0)
                        for a in prod:
                            if raiz in mapaGraficadorArbol:
                                listaGraficadora.append(a)
                                mapaGraficadorArbol.update({raiz : listaGraficadora})
                            else:
                                listaGraficadora = []
                                listaGraficadora.append(a)
                                mapaGraficadorArbol.update({raiz : listaGraficadora})
                        pila.insert(0, letra)
                        letraPila = pila.__getitem__(0)
                        if letraPila in noTerminal:
                            lista = produccionCorrejida.get(letraPila)
                            for k in lista:
                                prod = k
                                if prod[0] == letraInicialCadena:
                                    for a in prod:
                                        if raiz in mapaGraficadorArbol:
                                            listaGraficadora.append(a)
                                            mapaGraficadorArbol.update({raiz: listaGraficadora})
                                        else:
                                            listaGraficadora = []
                                            listaGraficadora.append(a)
                                            mapaGraficadorArbol.update({raiz: listaGraficadora})
                                    cambioEnPila.append(['('+''.join(pila)+')$('+ ''.join(listaCadena)+')'+'$'+ '(q, λ, ' + letra + '; q, '+ ''.join(prod)+')'])
                                    raiz = pila.pop(0)
                                    prod.reverse()
                                    for i in prod:
                                        pila.insert(0, i)
                                    prod.reverse()
                                    break
                    else:
                        lista = produccionCorrejida.get(letraPila)
                        for l in lista:
                            prod = l
                            if prod == 'epsilon':
                                if cadenaVacia:
                                    cambioEnPila.append(
                                        ['('+''.join(pila)+')$('+ '-----'+')$'+ '(q, λ, ' + letraPila + '; q, epsilon']
                                    )
                                else:
                                    cambioEnPila.append(['('+''.join(pila)+')$('+ ''.join(listaCadena)+')$'+ '(q, λ, ' + letraPila + '; q, epsilon)'])
                                raiz = pila.pop(0)
                                for a in prod:
                                    if raiz in mapaGraficadorArbol:
                                        listaGraficadora.append(a)
                                        mapaGraficadorArbol.update({raiz: listaGraficadora})
                                    else:
                                        listaGraficadora = []
                                        listaGraficadora.append(a)
                                        mapaGraficadorArbol.update({raiz: listaGraficadora})
                                break

            if letraInicialCadena == pila[0]:
                cambioEnPila.append(['('+''.join(pila) + ')$('+ ''.join(listaCadena)+')' + '$'+
                                     '(q, ' + letraInicialCadena + ', ' + letraInicialCadena + '; q, λ)'])
                letraCadenaInicial = listaCadena.pop(0)
                pila.pop(0)

        for q in range(0, len(pila) - 1):
            letraPila = pila.__getitem__(0)
            lista = produccionCorrejida.get(letraPila)
            for w in lista:
                prod = w
                if prod == 'epsilon':
                    if cadenaVacia:
                        cambioEnPila.append(
                            ['('+''.join(pila) + ')$(' + '-----'+')' + '$' + '(q, λ, ' + letraPila + '; q, epsilon)']
                        )
                    else:
                        cambioEnPila.append(
                            ['('+''.join(pila) + ')$(' + ''.join(listaCadena)+')'+ '(q, λ, ' + letraPila + '; q, epsilon)'])
                    raiz = pila.pop(0)
                    if raiz in mapaGraficadorArbol:
                        listaGraficadora.append(prod)
                        mapaGraficadorArbol.update({raiz: listaGraficadora})
                    else:
                        listaGraficadora = []
                        listaGraficadora.append(prod)
                        mapaGraficadorArbol.update({raiz: listaGraficadora})
                    break

        if pila[0] == "#":
            cambioEnPila.append(['(#$)'+'(-----)'+'$'+'(q, λ, #; f, λ)'])
            cambioEnPila.append(['(-----)$(-----)$(ACEPTACIÓN)'])
            raiz = pila.pop(0)
            print("\nCadena Válida\n")
            esCadenaValida = True
        else:
            print("\nError, cadena inválida\n")
            BorrarPantalla()
            menuProyecto2()

        if esCadenaValida == True:
            #Acá voy a crear el archivo CSV
            myFile = open(nombreAP + '.csv', 'w', encoding="utf-8")
            with myFile:
                writer = csv.writer(myFile)
                writer.writerows(cambioEnPila)
            print("\nGenerando reporte.\n")

            #Acá se crea el árbol de expresiones
            u = Digraph('unix', filename=nombreAP, node_attr={'color': 'lightblue2', 'style': 'filled'})
            u.attr(size = '6,6')

            for llave in mapaGraficadorArbol:
                obtenerLista = mapaGraficadorArbol.get(llave)
                for i in obtenerLista:
                    u.edge(llave, i)
            u.render(directory=ruta, view=True)
            menuProyecto2()

    else:
        print("\nError, el nombre no existe.\n")
        BorrarPantalla()
        menuProyecto2()

menuPrincipal()