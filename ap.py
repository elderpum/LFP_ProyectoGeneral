class AP(object):

    def __init__(self, nombre, terminales, noTerminales, producciones, inicial):
        self.nombre = nombre
        self.terminales = terminales
        self.noTerminales = noTerminales
        self.producciones = producciones
        self.inicial = inicial