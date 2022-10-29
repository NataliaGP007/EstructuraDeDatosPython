"""
Escribir un programa para obtener una lista doblemente enlazada con los caracteres
de una cadena leída desde el teclado. Cada nodo de la lista tendrá un carácter. Una vez
que se haya creado la lista, ordenarla alfabéticamente y escribirla en pantalla.
"""

from ListaDoblementeEnlazada import *
class PracticaLista():
    __listaCadena = []

    # Este metodo permite ingresar una linea de caracteres desde la consola, para despues convertirla en una lista
    # y ordena los elementos en orden alfabetico.
    def ordenarDatos(self):
        cadenaCaracteres = input()
        self.__listaCadena = list(cadenaCaracteres)
        self.__listaCadena.sort()

    # En este metodo se crea una lista doblemente enlazada en la cual se agregar los elemento de una lista normal.
    def crearLista(self):
        lista = ListaDoblementeEnlazada()
        lista.agregarInicio(self.__listaCadena[0])
        self.__listaCadena.pop(0)

        for f in self.__listaCadena:
            lista.agregarFinal(f)

        lista.recorrerInicio()

if __name__ == "__main__":
    prueba = PracticaLista()
    prueba.ordenarDatos()
    prueba.crearLista()