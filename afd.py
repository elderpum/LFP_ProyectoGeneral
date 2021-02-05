class AFD(object):

    def __init__(self, nombre, estados, alfabeto, inicial, aceptacion, transiciones, mapaTransicion, gramatica ,gramaticaRegular):
        self.nombre = nombre
        self.estados = estados
        self.alfabeto = alfabeto
        self.inicial = inicial
        self.aceptacion = aceptacion
        self.transiciones = transiciones
        self.mapaTransicion = mapaTransicion
        self.gramatica = gramatica
        self.gramaticaRegular = gramaticaRegular

    def getMapaTransicion(self):
        return self.mapaTransicion
