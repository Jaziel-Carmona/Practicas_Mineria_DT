
#PRACTICA 4: VISUALIZACION DE DATOS

# graficar la informacion 
from gzip import FNAME
import matplotlib.pyplot as plt
import numpy as np
import pandas
# import statsmodels.api as sm
# from statsmodels.formula.api import ols
import seaborn as sns


df = pandas.read_csv("games-data-clean.csv")


# GRAFICA DE BARRAS
df_pl = df.groupby(['Plataforma']).size().reset_index(name="Numero de Juegos")
plataformas = df_pl.iloc[:, 0]
df_pl.set_index("Plataforma", inplace=True)

#Generamos la grafica de barras
print("Generando grafica de barras..........")
df_pl.plot(kind='bar', color = 'limegreen' ,width=0.9)
#sns.displot(data=df_pl ,palette='viridis')
df_pl.plot = plt.gcf()

#Ajustamos el tamaño en que se nos muestra la grafica porque sino sale cortada
df_pl.plot.set_figheight(8)
df_pl.plot.set_figwidth(8)

#Ponemos el titulo y hacemos ajustes de las subtramas de la parte superior e inferior de la grafica
plt.subplots_adjust(top=0.9, bottom=0.275)
plt.title("Numero de Juegos de cada plataforma")
#sns.set()
df_pl.plot.savefig("Barras -- Numero de juegos de cada plataforma.png")
plt.clf()
print("Grafica de barras creada con exito")

#GRAFICA DE HISTOGRAMAS 

#Pruebas de graficas usando la libreria seaborn sns 
print("Generando grafica de Puntuaciones de Juegos......")
sns.displot(df["Puntuacion"], color = 'darkorange')
plt.title("Puntacion de juegos más frecuentes")
graf_hist = plt.gcf()
graf_hist.set_figheight(10)
graf_hist.set_figwidth(10)
plt.savefig('Graficas puntuaciones de juegos mas frecuentes.png')
print("Histograma 1 creado con exito")
plt.clf()

print("Generando grafica de puntuaciones de criticas.....")
sns.displot(df["Criticas"], color = 'slateblue')
plt.title("Puntacion de criticas más frecuentes")
graf_histo2 = plt.gcf()
graf_histo2.set_figheight(10)
graf_histo2.set_figwidth(10)
plt.savefig('Graficas de puntuaciones de criticas mas frecuentes.png')
print("Histograma 1 creado con exito")
plt.clf()


# GRAFICA DE PASTEL

#Para la grafica de pastel haremos una division como se poseen varias plataformas o mejor dicho consolas
#englobaremos todas las consolas en una sola compañia
print("generando grafica de pastel............")
def Clasif_compania(nombre):
    if (nombre == "PSP" or nombre == "PlayStation" or nombre == "PlayStation2" or nombre == "PlayStation3" or nombre == "PlayStation4" or nombre == "PlayStationVita"):
        return "PlayStation"
    elif (nombre == "Xbox" or nombre == "Xbox360" or nombre == "XboxOne" or nombre == "XboxSeriesX"):
        return "XBOX"
    elif(nombre == "PC"):
        return "PC_GAMER"
    elif(nombre == "Dreamcast" or nombre == "Stadia"):
        return "OTRO"
    else:
        return "NINTENDO"
    
#realizamos el filtro en la columna de Platforma
df["Compania"] = df["Plataforma"].apply(Clasif_compania)

df_compania = df[["Nombre", "Plataforma", "Compania"]]
df_compania = df_compania.rename_axis("id")

df_game_comp = df.groupby(["Compania"]).size().reset_index(name="Juegos de cada Compania")

valores = df_game_comp.iloc[:,1] 

#Preparamos las etiquetas de las graficas y los colores de cada uno de los segmentos
etiquetas = ["NINTENDO","OTRO","PC_GAMER","PlayStation","XBOX"]
colores = ["red", "gray", "goldenrod", "deepskyblue","springgreen"]

#creamos la grafica de pastel
plt.pie(valores, labels=etiquetas, autopct="%0.1f %%", radius=4, center=(4, 4), colors=colores)
plt.axis("equal")
plt.title("Porcentaje de de juegos de cada Compañia")
plt.subplots_adjust(top=0.8, bottom=0.1)


#Ajustamos el tamaño en que se nos muestra la grafica porque sino sale cortada
graf_compania = plt.gcf()
graf_compania.set_figheight(9)
graf_compania.set_figwidth(9)

graf_compania.savefig("Pastel -- Numero de juegos de Cada Compañia.png")
plt.clf()

print("Grafica de pastel generada exitosamente")


# GRAFICA DE CAJAS

#Primeramente usaremos la libreria sns para hacer la prueba de creacion de esta grafica
print("Generando grafica de cajas de puntuaciones de usuario.....")
sns.boxplot(x = df["Plataforma"], y = df["Puntuacion_usuario"])

#Ponemos titulo y rotamos las etiquetas para que no se empalmen
plt.title("Puntaciones de usuarios en cada Plataforma")
plt.xticks(rotation=90)
plt.subplots_adjust(left=0.07, right=0.95, top=0.9, bottom=0.25)
graf_cajas = plt.gcf()
graf_cajas.set_figheight(16)
graf_cajas.set_figwidth(16)
print("Grafica de caja creada con exito")
plt.savefig('CAJAS G1 -- Puntuacion de usuario  en Plataformas.png')
plt.clf()



# Crearemos una segunda grafica sin el uso de SNS 
# Obtenemos los datos
print("Generando grafica de cajas de puntuaciones de usuario.....")
dt = (df.groupby("Plataforma")["Puntuacion_usuario"].agg(lambda x:list(x)))
labels = dt.index
fig, ax = plt.subplots()

#Creamos la grafica
ax.boxplot(dt,
           patch_artist=True,
           boxprops = dict(facecolor = "aqua"))
ax.set_xticks(np.arange(1, len(labels) + 1), labels=labels)

#Le ponemos las etiquetas y titulo, ademas de rotar las etiquetas
plt.xlabel("Plataformas",size=16)
plt.ylabel("puntuaciones de usuarios",size=16)
plt.title("Puntaciones de usuarios en cada Plataforma",size=20)
plt.xticks(rotation=90)
plt.subplots_adjust(left=0.07, right=0.95, top=0.9, bottom=0.25)

#Ajustamos el tamaño y guardamos
grafica_cajas = plt.gcf()
grafica_cajas.set_figheight(14)
grafica_cajas.set_figwidth(14)
print("Grafica de caja creada con exito")
grafica_cajas.savefig("CAJAS G2 -- Puntuaciones de usuarios en Plataformas.png")
plt.clf()