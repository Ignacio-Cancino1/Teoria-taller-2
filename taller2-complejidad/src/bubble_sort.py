def bubble_sort(arr):
    """
    Implementación clásica de Bubble Sort.
    Ordena una lista comparando pares adyacentes.
    Complejidad: O(n^2)
    """
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
