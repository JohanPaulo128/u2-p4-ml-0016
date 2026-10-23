import pandas as pd
import numpy as np
# Johan Paulo Aros Reveles
n_filas = 5
n_columnas = 5
tag_columna = tuple('ABCDE') # etiquetas para las columnas de una tupla
print(tag_columna)
matriz = np.random.randint(1, 7, size = (n_filas, n_columnas))
print("Genera matriz de 5 filas por 5 columnas")
print("con numeros aleatrios comprendidos entre el 1 y el 10")
print(matriz) 
# La variable df es DataFrame
df = pd.DataFrame(matriz, columns = tag_columna)
print("--- La tabla o dataframe --- Johan Palo NC 0016")
print(df)
print("----- Johan Paulo Aros Reveles NC 0016 -----")