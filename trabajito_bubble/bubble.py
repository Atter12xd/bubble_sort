
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Intercambiar los elementos
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # Si no se realizaron intercambios, la lista ya está ordenada
        if not swapped:
            break

# Ejemplo de uso con una lista de al menos 10 elementos
if __name__ == "__main__":
    lista = [64, 34, 25, 12, 22, 11, 90, 77, 45, 6]
    print("Lista desordenada:", lista)
    bubble_sort(lista)
    print("Lista ordenada:", lista)
