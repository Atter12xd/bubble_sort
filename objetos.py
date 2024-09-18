class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f"{self.nombre} ({self.edad})"

def bubble_sort(arr, key=lambda x: x):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if key(arr[j]) > key(arr[j+1]):
                # Intercambiar los elementos
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # Si no se realizaron intercambios, la lista ya está ordenada
        if not swapped:
            break

# Ejemplo de uso con objetos
if __name__ == "__main__":
    personas = [
        Persona("Alice", 30),
        Persona("Bob", 25),
        Persona("Charlie", 35),
        Persona("David", 28)
    ]
    print("Lista desordenada:", personas)
    bubble_sort(personas, key=lambda x: x.edad)
    print("Lista ordenada por edad:", personas)
