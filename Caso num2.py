class Nodo:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, codigo, descripcion):
        nuevo = Nodo(codigo, descripcion)
        # TODO 1: agrega el nodo al final sin perder los anteriores
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.codigo, actual.descripcion)
            actual = actual.siguiente


class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        # TODO 2 completado: agregar el elemento a la cima
        self.items.append(elemento)

    def desapilar(self):
        # TODO 3 completado: devolver y eliminar el último elemento;
        # controlar el caso de pila vacía
        if not self.items:
            print("La pila está vacía.")
            return None
        return self.items.pop()


class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        # TODO 4 completado: agregar el elemento al final
        self.items.append(elemento)

    def desencolar(self):
        # TODO 5 completado: devolver y eliminar el primer elemento;
        # controlar el caso de cola vacía (reto individual, versión 02)
        if not self.items:
            print("la cola está vacía. no hay solicitudes para atender.")
            return None
        return self.items.pop(0)


# Pruebas de la versión 02: Clínica veterinaria
if __name__ == "__main__":
    lista = ListaEnlazada()
    pila = Pila()
    cola = Cola()

    solicitudes = [
        ("V01", "cacuna"),
        ("V02", "control"),
        ("V03", "emergencia"),
    ]

    print("=== LISTA ENLAZADA ===")
    for codigo, descripcion in solicitudes:
        lista.agregar(codigo, descripcion)
    print("solicitudes registradas:")
    lista.mostrar()

    print("\n=== PILA (LIFO) ===")
    for solicitud in solicitudes:
        pila.apilar(solicitud)
    print("desapilar (último agregado primero):", pila.desapilar())
    print("siguiente elemento de la pila:", pila.desapilar())

    print("\n=== COLA (FIFO) ===")
    for solicitud in solicitudes:
        cola.encolar(solicitud)
    print("desencolar (primero agregado primero):", cola.desencolar())
    print("siguiente solicitud:", cola.desencolar())
    print("ultima solicitud:", cola.desencolar())

    print("\n=== PRUEBA DE COLA VACÍA (RETO INDIVIDUAL) ===")
    resultado = cola.desencolar()
    print("resultado al intentar desencolar una cola vacía:", resultado)
