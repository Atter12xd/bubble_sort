def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]


lista = [12, 98, 75, 52, 62, 20, 8 ,7]
print("lista desordenada", lista)  
bubble_sort(lista)
print("lista ordenada", lista) 