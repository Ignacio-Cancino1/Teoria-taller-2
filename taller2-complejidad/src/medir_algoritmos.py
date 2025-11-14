import time
import random
import matplotlib.pyplot as plt

# ==========================
# IMPORTAR ALGORITMOS
# ==========================

from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

# ==========================
# FUNCIÓN DE MEDICIÓN
# ==========================

def medir_tiempo(algoritmo, lista, repeticiones=10):
    """
    Mide el tiempo promedio de ejecución de un algoritmo.

    algoritmo: función del algoritmo a evaluar
    lista: lista base a ordenar
    repeticiones: número de ejecuciones para promediar
    """
    tiempos = []
    for _ in range(repeticiones):
        copia = lista.copy()
        inicio = time.perf_counter()
        algoritmo(copia)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return sum(tiempos) / repeticiones

# ==========================
# EXPERIMENTO
# ==========================

def ejecutar_experimento():
    tamanos = [100, 500, 1000, 2000, 5000, 10000]
    tiempos_bubble = []
    tiempos_merge = []
    tiempos_quick = []

    print("Iniciando experimento...\n")

    for n in tamanos:
        print(f"Probando con n = {n}...")

        lista = [random.randint(0, 100000) for _ in range(n)]

        tiempos_bubble.append(medir_tiempo(bubble_sort, lista))
        tiempos_merge.append(medir_tiempo(merge_sort, lista))
        tiempos_quick.append(medir_tiempo(quick_sort, lista))

    # Guardar en CSV
    with open("results/tiempos.csv", "w") as f:
        f.write("n,bubble,merge,quick\n")
        for i in range(len(tamanos)):
            f.write(f"{tamanos[i]},{tiempos_bubble[i]},{tiempos_merge[i]},{tiempos_quick[i]}\n")

    print("\nTiempos guardados en results/tiempos.csv")

    # Graficar
    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, tiempos_bubble, marker="o", label="Bubble Sort")
    plt.plot(tamanos, tiempos_merge, marker="o", label="Merge Sort")
    plt.plot(tamanos, tiempos_quick, marker="o", label="Quick Sort")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Comparación de Algoritmos de Ordenamiento")
    plt.grid(True)
    plt.legend()
    plt.savefig("results/grafico_tiempos.png")
    plt.show()

    print("Gráfico generado en results/grafico_tiempos.png")

# ==========================
# EJECUCIÓN
# ==========================

if __name__ == "__main__":
    ejecutar_experimento()
