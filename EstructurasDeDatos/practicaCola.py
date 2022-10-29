"""
Escribir un método que tenga como argumentos dos colas del mismo tipo y devuelva cierto si
las dos colas son idénticas.
"""
from Cola import ColaDinamica
class practicaCola:
    cola1 = ColaDinamica()
    cola2 = ColaDinamica()
    x = []
    y = []

    # Este metodo compara compara dos colas y devuelve cierto si son identicas.
    def ingresarDatos(self):
        self.x = input().split(" ")
        self.y = input().split(" ")

    def crearColas(self):
        for f in range(len(self.x)):
            self.cola1.Insertar(self.x[f])

        for f in range(len(self.y)):
            self.cola2.Insertar(self.y[f])

    def CompararColas(self):
        if self.cola1.TamCola() == self.cola2.TamCola():
            n = 0
            tamComun = self.cola1.TamCola()
            for x in range(tamComun):
                if self.cola1.MostrarFrente() == self.cola2.MostrarFrente():
                    self.cola1.Quitar()
                    self.cola2.Quitar()
                    n += 1
                else:
                    pass

            if n == tamComun:
                print("Cierto")
            else:
                print("Falso")
        else:
            print("Falso")

if __name__ == "__main__":

    prueba = practicaCola()
    prueba.ingresarDatos()
    prueba.crearColas()
    prueba.CompararColas()