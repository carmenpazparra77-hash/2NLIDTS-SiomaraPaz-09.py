class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def imprimir(self):
        actual = self.cabeza
        print("Los valores de la lista son: ", end="")
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

    def borrar(self):
        actual = self.cabeza
        while actual:
            print(f"Elemento borrado: {actual.dato}")
            actual = actual.siguiente
        self.cabeza = None
        print("Lista vaciada correctamente.")

# Programa principal
def main():
    print("[*] Actividad 09 - Lista Enlazada Simple\n")
    
    try:
        tamano = int(input("[+] Cantidad de elementos: "))
    except ValueError:
        print("[!] Debes ingresar un número")
        return

    if tamano <= 0:
        print("[!] Cantidad no válida")
        return

    lista = ListaEnlazada()

    for i in range(tamano):
        valor = int(input(f"Ingrese el valor {i+1}: "))
        lista.agregar(valor)

    lista.imprimir()
    lista.borrar()

if __name__ == "__main__":
    main()
