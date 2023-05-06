#PRACTICA 3: ESTADISTICA DESCRIPTIVA

import pandas

# Lee el conjunto de datos
df_c = pandas.read_csv("games-data-clean.csv")

#NOTA: se les cambio los nombres a las columnas en la practica anterior
#ademas de usarse el dataframe ya limpio


#Puntuacion MIN de un usuario
print("La puntuacion minima de los usuarios es: ")
print(df_c["Puntuacion_usuario"].min())

#Puntuacion MAX de un usuario
print("\nLa puntuacion maxima de los usuarios es: ")
print(df_c["Puntuacion_usuario"].max())

#Puntuacion de usuario mas repetida (MODA)
print("\nLa puntuacion de usuario más repetida(moda) es: ")
print(df_c["Puntuacion_usuario"].mode())

#print(df_c[df_c["Puntuacion_usuario"] >= 77]["Nombre"].count())

#SUMATORIA de todos los Usuarios que han jugado los videojuegos
print("\nTotal de usuarios que han jugado a los videojuegos: ")
print(df_c["Usuarios"].sum())

#Puntuacion MIN de un juego
print("\nLa puntuancion minima dada a un videojuego es: ")
print(df_c["Puntuacion"].min())

#Puntuacion MAX de un juego
print("\nLa puntuacion maxima dada a un videojuego es: ")
print(df_c["Puntuacion"].max())

#Puntuacion de juego mas repetida (MODA)
print("\nLa puntuacion dada a los videojuegos más repetida(moda) es: ")
print(int(df_c["Puntuacion"].mode()))

#Cantidad de veces que aparece  la moda de puntuacion
print(df_c[df_c["Puntuacion"] == 80]["Nombre"].count())

#SUMATORIA de las puntucaciones que se le dieron a los juegos
print("\nSumatoria de las puntuaciones dadas a los videojuegos: ")
print(df_c["Puntuacion"].sum())

# print("La desviacion media de la cantidad de usuarios que criticaron un juego es: ")
# print(df_c["Usuarios"].mad())

#Media
print("\nCalculo del promedio de la cantidad de usuarios que han jugado algun videojuego: ")
print(df_c["Usuarios"].mean())

#Varianza
print("\nCalculo de la varianza de la cantidad de usuarios que han jugado algun videojuego: ")
print(df_c["Usuarios"].var())

#Asimetria
print("\nCalculo de la Asimetria de la cantidad de usuarios que han jugado algun videojuego: ")
print(df_c["Usuarios"].skew())

#Kurtosis
print("\nCalculo de la kurtosis de la cantidad de usuarios que han jugado algun videojuego: ")
print(df_c["Usuarios"].kurt())
print("\n")

#Conteo apartir de cierto valor
print("\nCantidad de juegos que tienen una puntuacion de usuario mayor o igual que 95: ")
print(df_c[df_c["Puntuacion_usuario"] >= 95]["Nombre"].count())

print("\nCantidad de juegos que tienen una puntuacion mayor o igual que 95: ")
print(df_c[df_c["Puntuacion"] >= 95]["Nombre"].count())

#TOP 1 de juego con mas criticas
df_c = df_c.sort_values("Criticas")
print("\nEl juego con mas criticas")
print(df_c.tail(1))

#Juego con menos criticas
print("\nEl juego con menos criticas")
print(df_c.head(1))

#TOP 3 juegos con mejor puntuacion de usuarios
df_c = df_c.sort_values("Puntuacion_usuario")
print("\nLos juegos con mejor puntuacion de usuarios")
print(df_c.tail(3))

#TOP 3 juegos con mayor cantidad de usuarios
df_c = df_c.sort_values("Usuarios")
print("\nLos juegos con más usuarios")
print(df_c.tail(3)) 

#Juego con menos criticas
print("\nEl juego con menos usuarios")
print(df_c.head(3))

#TOP 3 juegos con mayor puntuacion
df_c = df_c.sort_values("Puntuacion")
print("\nLos juegos con mejor puntuacion")
print(df_c.tail(3))

#Cantidad de veces que se repite la moda del numero de usuarios
print("\nMODA de usuarios que dieron una puntuacion a un juego: ")
print(int(df_c["Usuarios"].mode()))
print(df_c[df_c["Usuarios"] == 5]["Nombre"].count())

#Cantidad de veces que se repite la moda del numero de criticas
print("\nMODA de criticos  que dieron una puntuacion a un juego: ")
print(int(df_c["Criticas"].mode()))
print(df_c[df_c["Criticas"] == 7]["Criticas"].count())


