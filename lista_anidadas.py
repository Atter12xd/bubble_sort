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

# Ejemplo de uso con listas anidadas
if __name__ == "__main__":
    listas_anidadas = [[3, 'apple'], [1, 'banana'], [4, 'cherry'], [2, 'date']]
    print("Lista desordenada:", listas_anidadas)
    bubble_sort(listas_anidadas, key=lambda x: x[0])  # Ordenar por el primer elemento de la sublista
    print("Lista ordenada por el primer elemento de la sublista:", listas_anidadas)
