import matplotlib.pyplot as plt
import numpy as np
import time

def bubble_sort(arr, visualize=False):
    n = len(arr)
    if visualize:
        plt.ion()  # Activar el modo interactivo para gráficos en vivo
        fig, ax = plt.subplots()
        bars = ax.bar(range(n), arr, color='b')
        plt.title("Bubble Sort")
        plt.xlabel("Índice")
        plt.ylabel("Valor")
        plt.ylim(0, max(arr) + 10)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Intercambiar los elementos
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                
                if visualize:
                    # Actualizar gráfico
                    for bar, height in zip(bars, arr):
                        bar.set_height(height)
                    plt.pause(0.1)  # Pausa para mostrar el cambio visualmente

        if not swapped:
            break

    if visualize:
        plt.ioff()  # Desactivar el modo interactivo
        plt.show()  # Mostrar el gráfico final

def quick_sort(arr):
    """ Implementación del algoritmo Quick Sort """
    def quick_sort_recursive(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_recursive(arr, low, pi-1)
            quick_sort_recursive(arr, pi+1, high)
    
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1

    quick_sort_recursive(arr, 0, len(arr) - 1)

def measure_time(func, arr):
    """ Mide el tiempo de ejecución de una función de ordenamiento """
    start_time = time.time()
    func(arr)
    return time.time() - start_time

# Ejemplo de uso con visualización
if __name__ == "__main__":
    lista = [64, 34, 25, 12, 22, 11, 90, 77, 45, 6]
    
    # Ordenamiento con Bubble Sort
    print("Lista desordenada:", lista)
    print("Ordenando con Bubble Sort...")
    bubble_sort(lista, visualize=True)
    print("Lista ordenada con Bubble Sort:", lista)
    
    # Ejemplo de uso con Quick Sort
    lista_2 = [64, 34, 25, 12, 22, 11, 90, 77, 45, 6]
    time_bubble_sort = measure_time(lambda x: bubble_sort(x), lista.copy())
    print(f"Tiempo de Bubble Sort: {time_bubble_sort:.6f} segundos")

    print("\nOrdenando con Quick Sort...")
    time_quick_sort = measure_time(lambda x: quick_sort(x), lista_2)
    print(f"Lista ordenada con Quick Sort: {lista_2}")
    print(f"Tiempo de Quick Sort: {time_quick_sort:.6f} segundos")
