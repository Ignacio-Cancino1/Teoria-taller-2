def quick_sort(arr):
    """
    Implementación clásica de Quick Sort.
    Divide la lista según un pivote.
    Complejidad promedio: O(n log n)
    Peor caso: O(n^2)
    """
    if len(arr) <= 1:
        return arr

    piv = arr[len(arr) // 2]
    menores = [x for x in arr if x < piv]
    iguales = [x for x in arr if x == piv]
    mayores = [x for x in arr if x > piv]

    return quick_sort(menores) + iguales + quick_sort(mayores)
