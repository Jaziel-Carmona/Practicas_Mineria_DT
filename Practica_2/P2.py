# PRACTICA_2: LIMPIEZA DE DATOS 

# Librerias
import pandas as pd
from datetime import datetime

print("---------------------------------------------- ADQUISICION DE DATOS-----------------------------------------")

# Lectura de nuestro dataframe
df = pd.read_csv("games-data.csv")

print("\n---------------------------------------------------DATA ORIGINAL----------------------------------------------\n")
print(df)

print("\n\n---------------------------------------------- DATA CLEANING --------------------------------------------\n")

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

print(dfc)

print("\n[Antes de la limpieza] filas = 17944     [Despues] filas = 16641")

