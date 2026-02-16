import pandas as pd
import glob
import os

# 1. Definir la ruta donde están tus archivos
# Si están en la misma carpeta que tu script, usa '*.sav'
patron_archivos = "*.sav" 

# 2. Obtener la lista de los 10 archivos automáticamente
lista_archivos = glob.glob(patron_archivos)
print(f"Se encontraron {len(lista_archivos)} archivos.")

# 3. Lista para almacenar los DataFrames temporalmente
lista_dfs = []

# 4. Bucle para leer cada archivo y agregarlo a la lista
for archivo in lista_archivos:
    # Leemos el archivo .sav
    # convert_categoricals=True mantiene las etiquetas (ej: "Hombre" en vez de 1)
    df_temp = pd.read_spss(archivo, convert_categoricals=False)
    
    # Opcional: Crear una columna para saber de qué archivo vino cada dato
    df_temp['origen_archivo'] = os.path.basename(archivo)
    
    lista_dfs.append(df_temp)

# 5. Unir (concatenar) todos los DataFrames en uno solo
# ignore_index=True resetea el índice para que vaya de 0 a N seguido
df_total = pd.concat(lista_dfs, ignore_index=True)

# 6. Verificación rápida
print(f"Dimensiones finales: {df_total.shape}")
print(df_total.head())

# 7. Exportar a CSV (formato manejable)
df_total.to_csv("datos_unificadosF.csv", index=False, encoding='utf-8-sig')

print("¡Éxito! Archivo 'datos_unificados.csv' creado.")