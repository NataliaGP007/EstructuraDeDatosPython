"""
Escribir un programa en el que se manejen un total de n = 5 pilas: P1, P2, P3, P4
y P5. La entrada de datos serán pares de enteros (i,j) tal que 1 ≤ abs(i) ≤ n. De
tal forma que el criterio de selección de pila será:
• Si i es positivo, debe insertarse el elemento j en la pila Pi.
• Si i es negativo, debe eliminarse el elemento j de la pila Pi.
• Si i es cero, fin del proceso de entrada.
Los datos de entrada se introducen por teclado. Cuando termina el proceso el programa
debe escribir el contenido de la n Pilas en pantalla.
"""
from Pila import PilaDinamica
class solucion:
    P1 = PilaDinamica()
    P2 = PilaDinamica()
    P3 = PilaDinamica()
    P4 = PilaDinamica()
    P5 = PilaDinamica()

    # Este metodo permite ingresar los numeros enteros, y con el primer dijito se determina en que
    # numero de pila se guardara el segundo elemento si el primer digito es positivo, miesntras el
    # primer digito no sea 0.
    def entradaDatos(self):
        par = input().split(",")
        Pi = abs(int(par[0]))

        while Pi != 0:

            if Pi == 1:
                if int(par[0]) > 0:
                    self.P1.push(par[1])
            elif Pi == 2:
                if int(par[0]) > 0:
                    self.P2.push(par[1])
            elif Pi == 3:
                if int(par[0]) > 0:
                    self.P3.push(par[1])
            elif Pi == 4:
                if int(par[0]) > 0:
                    self.P4.push(par[1])
            elif Pi == 5:
                if int(par[0]) > 0:
                    self.P5.push(par[1])
            else:
                print("El primer entero que ingrese debe ser mayor o igual a -5 y menor o igual a 5")

            par = input().split(",")
            Pi = abs(int(par[0]))

    # Este metodo muestra en pantalla en contenido de las Pilas.
    def mostrarPilas(self):
        self.P1.ImprimirPila(), print("P1", "\n")
        self.P2.ImprimirPila(), print("P2", "\n")
        self.P3.ImprimirPila(), print("P3", "\n")
        self.P4.ImprimirPila(), print("P4", "\n")
        self.P5.ImprimirPila(), print("P5", "\n")

if __name__ == "__main__":
    prueba = solucion()
    prueba.entradaDatos()
    prueba.mostrarPilas()