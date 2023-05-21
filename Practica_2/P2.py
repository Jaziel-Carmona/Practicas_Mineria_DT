# PRACTICA_2: LIMPIEZA DE DATOS 

# Librerias
import pandas as pd
#from datetime import datetime

print("ADQUIRIMOS LOS DATOS")

# Lectura de nuestro dataframe
df = pd.read_csv("games-data.csv")

print("\nDATAFRAME ORIGINAL\n")
print(df)

print("\n\nDATAFRAME LIMPIO\n")

#Renombrando los nombres de las columnas de nuestro dataframe
df.columns = ["Nombre", "Plataforma", "Fecha_estreno", "Puntuacion", "Puntuacion_usuario",
                "Desarrollador", "Genero", " Num_jugadores", "Criticas", "Usuarios"]


# Limpieza de datos nulos
df.dropna()

#print("COMANDO df.groupby()")     Prueba
#print(df.groupby("Plataforma"))

# Limpieza de los juegos con promedio de 0
condicion = df[df["Usuarios"] == 0].index
df = df.drop(condicion)
condicion = df[df["Criticas"] == 0].index
df = df.drop(condicion)

# limpieza de valores basura
condicion = df[df["Puntuacion_usuario"] == "tbd"].index

df = df.drop(condicion)

df = df.sort_values("Puntuacion_usuario")

df.to_csv("games-data-clean.csv")

dfc = pd.read_csv("games-data-clean.csv")

def convertirPuntuacionUsuarios(puntuacion):
    return puntuacion*10
dfc["Puntuacion_usuario"] = dfc["Puntuacion_usuario"].apply(convertirPuntuacionUsuarios)
dfc = dfc.drop(dfc[dfc["Puntuacion_usuario"] == 0].index)

dfc.to_csv("games-data-clean.csv", index=False)

print(dfc)

print("\n[Antes de la limpieza] filas = 17944     [Despues] filas = 16641")

