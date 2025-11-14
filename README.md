# 📘 Taller 2 — Complejidad Algorítmica (INFO1148)

Este repositorio contiene el código desarrollado para el **Taller 2 de la asignatura INFO1148**, cuyo objetivo es analizar y comparar el rendimiento de tres algoritmos clásicos de ordenamiento:

- **Bubble Sort**
- **Merge Sort**
- **Quick Sort**

El trabajo combina **análisis teórico** (complejidad temporal y espacial) y **evaluación empírica** mediante pruebas reales en Python, generando tablas de tiempos y un gráfico comparativo utilizado en el informe escrito.

---

## 📂 Estructura del Proyecto

taller2-complejidad/
│
├── src/
│ ├── bubble_sort.py # Implementación de Bubble Sort
│ ├── merge_sort.py # Implementación de Merge Sort
│ ├── quick_sort.py # Implementación de Quick Sort
│ ├── medir_algoritmos.py # Script principal: genera tiempos y gráfico
│
├── results/
│ ├── grafico_tiempos.png # Gráfico generado por el experimento
│ ├── tiempos.csv # Datos numéricos del experimento
│
├── README.md # Este archivo
└── manual_de_usuario.pdf # Manual usado en el informe (opcional)

yaml
Copiar código

---

## 🧪 Descripción del experimento

El archivo principal `medir_algoritmos.py`:

- Genera listas aleatorias de distintos tamaños.
- Ejecuta cada algoritmo múltiples veces (10 repeticiones).
- Promedia los tiempos para minimizar fluctuaciones.
- Genera un archivo `.csv` con los resultados.
- Produce un gráfico comparativo `grafico_tiempos.png`.

Tamaños evaluados:

100, 500, 1000, 2000, 5000, 10000

yaml
Copiar código

---

## ⚙️ Requisitos

- Python 3.8 o superior
- Librería `matplotlib`

Instalación:

```bash
pip install matplotlib
▶️ Cómo ejecutar el experimento
Clonar el repositorio:

bash
Copiar código
git clone https://github.com/USUARIO/taller2-complejidad.git
Entrar a la carpeta:

bash
Copiar código
cd taller2-complejidad/src
Ejecutar el script principal:

bash
Copiar código
python medir_algoritmos.py
Revisar los resultados en:

bash
Copiar código
results/tiempos.csv
results/grafico_tiempos.png
📊 Ejemplo de gráfico generado
(El siguiente archivo se genera automáticamente al ejecutar el experimento)

bash
Copiar código
results/grafico_tiempos.png
📄 Informe del Taller
El informe fue desarrollado en LaTeX, siguiendo la rúbrica del curso.
Se adjuntó en la plataforma de la universidad junto con este código.

🧑‍💻 Integrantes del Grupo
Integrante 1 — correo@correo.cl

Integrante 2 — correo@correo.cl

Integrante 3 — correo@correo.cl

📜 Licencia (opcional)
Este proyecto puede utilizarse con fines académicos y educativos.

¡Gracias por revisar este trabajo!
Cualquier consulta adicional o mejora es bienvenida.
