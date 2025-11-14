def merge_sort(arr):
    """
    Implementación de Merge Sort.
    Complejidad: O(n log n)
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    izquierda = merge_sort(arr[:mid])
    derecha = merge_sort(arr[mid:])
    return merge(izquierda, derecha)


def merge(left, right):
    resultado = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1

    resultado.extend(left[i:])
    resultado.extend(right[j:])
    return resultado
