class ColaEstatica:
    __tamCola = int(0)
    listaCola = []

    def __init__(self, tamCola):
        self.__tamCola = tamCola

    def Insertar(self, elemento):
        if self.ColaLlena():
            return False
        else:
            self.listaCola.append(elemento)
            return True

    def Quitar(self):
        if self.ColaVacia():
            return False
        else:
            return self.listaCola.pop(0)

    def ColaVacia(self):
        return len(self.listaCola) == 0

    def ColaLlena(self):
        return self.__tamCola == len(self.listaCola)

    def LimpiarCola(self):
        self.listaCola.clear()

    def MostrarFrente(self):
        return self.listaCola[0]

    def MostrarTamCola(self):
        return len(self.listaCola)

class ColaDinamica:
    listaCola = []

    def __init__(self):
        self.listaCola = []

    def Insertar(self, elemento):
        self.listaCola.append(elemento)
        return True

    def Quitar(self):
        if self.ColaVacia():
            return False
        else:
            return self.listaCola.pop(0)

    def ColaVacia(self):
        return len(self.listaCola) == 0

    def LimpiarCola(self):
        self.listaCola.clear()

    def MostrarFrente(self):
        return self.listaCola[0]

    def TamCola(self):
        return len(self.listaCola)

    def MostrarTamCola(self):
        return print(len(self.listaCola))

    def ImprimirCola(self):
        aux = self.MostrarFrente()
        while aux:
            print(aux, end=" -> ")
            self.Quitar()
        print("\n")

