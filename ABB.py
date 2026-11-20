
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    # Algoritmo de insercion
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, actual, valor):
        if valor < actual.valor:
            if actual.izquierdo is None:
                actual.izquierdo = Nodo(valor)
            else:
                self._insertar(actual.izquierdo, valor)

        elif valor > actual.valor:
            if actual.derecho is None:
                actual.derecho = Nodo(valor)
            else:
                self._insertar(actual.derecho, valor)

        else:
            print("El valor ya existe en el arbol.")

    # Algoritmo de busqueda
    def buscar(self, valor):
        actual = self.raiz

        while actual is not None:
            if valor == actual.valor:
                return True
            elif valor < actual.valor:
                actual = actual.izquierdo
            else:
                actual = actual.derecho

        return False

    # Recorrido Preorden: Raiz, Izquierda, Derecha
    def preorden(self, nodo):
        if nodo is not None:
            print(nodo.valor, end=" ")
            self.preorden(nodo.izquierdo)
            self.preorden(nodo.derecho)

    # Recorrido Inorden: Izquierda, Raiz, Derecha
    def inorden(self, nodo):
        if nodo is not None:
            self.inorden(nodo.izquierdo)
            print(nodo.valor, end=" ")
            self.inorden(nodo.derecho)

    # Recorrido Postorden: Izquierda, Derecha, Raiz
    def postorden(self, nodo):
        if nodo is not None:
            self.postorden(nodo.izquierdo)
            self.postorden(nodo.derecho)
            print(nodo.valor, end=" ")


# Programa principal
arbol = ArbolBinarioBusqueda()

while True:
    print("\n===== ARBOL BINARIO DE BUSQUEDA =====")
    print("1. Insertar elemento")
    print("2. Buscar elemento")
    print("3. Recorrido Preorden")
    print("4. Recorrido Inorden")
    print("5. Recorrido Postorden")
    print("6. Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        try:
            valor = int(input("Ingresa el valor: "))
            arbol.insertar(valor)
            print("Elemento insertado.")
        except ValueError:
            print("Ingresa un numero entero valido.")

    elif opcion == "2":
        try:
            valor = int(input("Ingresa el valor a buscar: "))

            if arbol.buscar(valor):
                print("El elemento SI existe en el arbol.")
            else:
                print("El elemento NO existe en el arbol.")
        except ValueError:
            print("Ingresa un numero entero valido.")

    elif opcion == "3":
        print("Recorrido Preorden:")
        arbol.preorden(arbol.raiz)
        print()

    elif opcion == "4":
        print("Recorrido Inorden:")
        arbol.inorden(arbol.raiz)
        print()

    elif opcion == "5":
        print("Recorrido Postorden:")
        arbol.postorden(arbol.raiz)
        print()

    elif opcion == "6":
        print("Programa finalizado.")
        break

    else:
        print("Opcion no valida.")
