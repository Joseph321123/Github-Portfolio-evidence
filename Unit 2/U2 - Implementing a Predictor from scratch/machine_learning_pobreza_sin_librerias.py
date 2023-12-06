# -*- coding: utf-8 -*-
"""Machine_Learning- pobreza-sin_librerias.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QD9bkI-ciLNngWbB3TyPDzQK3r5G0sG5

# codigo sin librerias en diferentes celdas
"""

#las unicas 2 librerias que usaremos son estas ya que sin la pandas no podriamos completar el trabajo ya que nos haria falta muchas funciones
import pandas as pd
import numpy as np

csv_path = '/content/Indicadores_municipales_sabana_DA.csv'
df = pd.read_csv(csv_path, encoding = 'latin-1')

df.head()

print(df.N_ic_rezedu)

# en esta parte se utiliza la liberia de pandas y se elimina las filas vacias
#df = df.dropna(subset=['N_ic_rezedu'])

# Calcula la cantidad de valores faltantes en cada columna

valores_faltantes_por_columna = df.isna().sum()

# Calcula la cantidad total de valores faltantes en el DataFrame

cantidad_total_valores_faltantes = df.isna().sum().sum()

# Imprime la cantidad de valores faltantes por columna

print(valores_faltantes_por_columna)

# Imprime la cantidad total de valores faltantes

print("Cantidad total de valores faltantes:", cantidad_total_valores_faltantes)

# Rellena todos los valores faltantes con un valor constante, por ejemplo, 0

df = df.fillna(0)

print(df.N_ic_rezedu)

#df.tail()

#print(df)

# Keep the first 5 columns and the training column
columnas_a_mantener = ['ent', 'nom_ent', 'mun', 'nom_mun', 'N_ic_rezedu']
df = df[columnas_a_mantener]

# Now df contains only the columns you want to keep
print(df)

df = pd.DataFrame(df)

# Agrupar por valores de la primera columna (Col1)
grupo = df.groupby('ent')

# Calcular la suma de la quinta columna (Col6) para cada grupo
suma_col6 = grupo['N_ic_rezedu'].sum()

# Calcular la media para cada grupo
media_por_grupo = suma_col6 / grupo.size()

# Calcular la media final
media_final = media_por_grupo.mean()

# Imprimir las medias por grupo y la media final
#print("Medias por grupo:")
#print(media_por_grupo)
#print("\nMedia final:")
#print(media_final)



# Calcular el valor mínimo, medio y máximo
valor_minimo = suma_col6.min()
valor_medio = suma_col6.median()
valor_maximo = suma_col6.max()

# Imprimir las medias por grupo y la media final
print("Medias por grupo:")
print(media_por_grupo)
print("\nMedia final:")
print(media_final)
print("\nValor Mínimo:", valor_minimo)
print("Valor Medio:", valor_medio)
print("Valor Máximo:", valor_maximo)

# Clasificar en "bajo", "medio" y "alto" según la suma de Col6
def clasificar(suma):
    if suma <= valor_minimo:
        return 'Bajo'
    elif suma <= valor_medio:
        return 'Medio'
    else:
        return 'Alto'

clasificacion = suma_col6.apply(clasificar)

# Asociar la clasificación con los valores de la tercera columna (Col5)
#resultados = df.groupby('ent')['nom_mun'].max().reset_index()
#resultados['Clasificacion'] = clasificacion
#print(resultados)
for clasificacion_final, grupo in df.groupby('ent'):
   print(f"Grupo {clasificacion_final} - Clasificación: {clasificacion[clasificacion_final]}")
   print(grupo)
   print('\n')

"""# Codigo sin librerias en una sola celda"""

#las unicas 2 librerias que usaremos son estas ya que sin la pandas no podriamos completar el trabajo ya que nos haria falta muchas funciones
import pandas as pd
import numpy as np

#agregamos nuestro dataset
csv_path = '/content/Indicadores_municipales_sabana_DA.csv'
df = pd.read_csv(csv_path, encoding = 'latin-1')

#vemos todos los datos del dataset
df.head()

#observamos los datos de la columna que utilizaremos
print(df.N_ic_rezedu)

# Calcula la cantidad de valores faltantes en cada columna

valores_faltantes_por_columna = df.isna().sum()

# Calcula la cantidad total de valores faltantes en el DataFrame

cantidad_total_valores_faltantes = df.isna().sum().sum()

# Imprime la cantidad de valores faltantes por columna

print(valores_faltantes_por_columna)

# Imprime la cantidad total de valores faltantes

print("Cantidad total de valores faltantes:", cantidad_total_valores_faltantes)

# Rellena todos los valores faltantes con un valor constante, por ejemplo, 0

df = df.fillna(0)

# Keep the first 5 columns and the training column
columnas_a_mantener = ['ent', 'nom_ent', 'mun', 'nom_mun', 'N_ic_rezedu']
df = df[columnas_a_mantener]

# Now df contains only the columns you want to keep
print(df)

# aqui lo que hacemos es poner que df seria nuestro dataset
df = pd.DataFrame(df)

# Agrupar por valores de la primera columna (Col1)
grupo = df.groupby('ent')

# Calcular la suma de la quinta columna (Col6) para cada grupo
suma_col6 = grupo['N_ic_rezedu'].sum()

# Calcular la media para cada grupo
media_por_grupo = suma_col6 / grupo.size()

# Calcular la media final
media_final = media_por_grupo.mean()



# Calcular el valor mínimo, medio y máximo
valor_minimo = suma_col6.min()
valor_medio = suma_col6.median()
valor_maximo = suma_col6.max()

# Imprimir las medias por grupo y la media final
print("Medias por grupo:")
print(media_por_grupo)
print("\nMedia final:")
print(media_final)
print("\nValor Mínimo:", valor_minimo)
print("Valor Medio:", valor_medio)
print("Valor Máximo:", valor_maximo)



# Clasificar en "bajo", "medio" y "alto" según la suma de Col6
def clasificar(suma):
    if suma <= valor_minimo:
        return 'Bajo'
    elif suma <= valor_medio:
        return 'Medio'
    else:
        return 'Alto'

clasificacion = suma_col6.apply(clasificar)

# los datos aqui se estan nombrando de acuerdo a la clasificasion, de acuerdo a las iteraciones y nos lo imprime
for clasificacion_final, grupo in df.groupby('ent'):
   print(f"Grupo {clasificacion_final} - Clasificación: {clasificacion[clasificacion_final]}")
   print(grupo)
   print('\n')