
#PRACTICA 5: PRUEBAS ESTADISTICAS

from scipy.stats import shapiro
import scipy.stats as stats
#import numpy as np
import pandas
#import seaborn as sns
#import pingouin as pg

df = pandas.read_csv("games-data-clean.csv")

#Ahora para la prueba Estaditica

users = df.iloc[:, 5]

# prueba estadistica para comprobar si se presneta una distribucion normal
# hipotesis nula = las distribuciones de los grupos son iguales
# hipotesis alterna = las distribuciones de los grupos son diferentes

estadistico, p = shapiro(users)

print("Iniciando prueba/n")
if p<0.05:
    print("HA - las distribuciones de los grupos son diferentes (Sin distribucion normal)")
else:
    print("HN - las distribuciones de los grupos son iguales (Con distribucion normal)")    
print("Prueba finalizada\n\n")

# #Una segunda prueba
# criticas = df.iloc[:, 9]

# estadistico, p2 = shapiro(criticas)

# print("Iniciando prueba\n")
# if p2<0.05:
#     print("HA - las distribuciones de los grupos son diferentes (Sin distribucion normal)")
# else:
#     print("HN - las distribuciones de los grupos son iguales (Con distribucion normal)")    
# print("Prueba finalizada\n\n")

#Otro tipo de prueba
print("\nIniciando prueba")
Puntuacion = df["Puntuacion"]
Criticas = df["Criticas"]

# Wilcoxon
print(stats.wilcoxon(Puntuacion, Criticas))
print("\nPrueba finalizada")


# #Para realizar una comparacion entre PS y XBOX que son las marcas mas conocidas y mayor competencia


# #Para el primero realizamos un filtro de cada una de las compañias de videojuegos
# def CPyM(nombre):
#     if (nombre == "PlayStation5" or nombre == "PlayStation" or nombre == "PlayStationVita" or 
#         nombre == "PSP" or nombre == "PlayStation3" or nombre == "PlayStation2" or nombre == "PlayStation4"):
#         return "PlayStation"
#     elif (nombre == "Xbox" or nombre == "XboxOne" or nombre == "XboxSeriesX" or nombre == "Xbox360"):
#         return "Xbox"
#     elif(nombre == "Dreamcast" or nombre == "Stadia"):
#         return "OTRO"
#     elif(nombre == "PC"):
#         return "PC_Gamer"
#     else:
#         return "Nintendo"
    
# #Aplicamos el filtro
# df["Marca"] = df["Plataforma"].apply(CPyM)
# df_M = df[["Nombre", "Plataforma", "Marca","Puntuacion_usuario"]]
# df_M = df_M.rename_axis("id")

# #Guardamos el nuevo Dataframe
# df_M.to_csv("Plataformas_Comp.csv")

# #Crearemos apartir del anterior dataframe otro dataframe para poder realizar la Prueba Estadistica
# #Sera un Dataframe de PS y XBOX los primero 3000 registros con buen puntaje
# df_MP = pandas.read_csv("Plataformas_Comp.csv") #leemos el dataframe
# df_PS = df_MP[df_MP["Marca"]=="PlayStation"]
# df_PS = df_PS[["Puntuacion_usuario", "Marca"]].sort_values("Puntuacion_usuario",ascending=False).head(3000)

# df_XB = df_MP[df_MP["Marca"]=="Xbox"]
# df_XB = df_XB[["Puntuacion_usuario", "Marca"]].sort_values("Puntuacion_usuario", ascending=False).head(3000)

# df_PX = pandas.concat([df_PS,df_XB])
# df_PX.to_csv("Play_Station y XBOX mejores puntajes.csv")


# # Comparar que grupo sale mejor puntuado 
# df_PXX = pandas.read_csv("Play_Station y XBOX mejores puntajes.csv")

# print(pg.homoscedasticity(data=df_PXX,dv="Puntuacion_usuario", group="Marca", method='levene'))

# df_PSN = df_PXX[df_PXX["Marca"] == "PlayStation"]
# v_PS = df_PSN.iloc[:,0]
# df_XBX = df_PXX[df_PXX["Marca"] == "Xbox"]
# v_XB = df_XBX.iloc[:,0]

# print(pg.mwu(x=v_PS, y=v_XB,alternative='two-sided'))




