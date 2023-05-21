
#PRACTICA 7: CLASIFICACION DE DATOS

import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier


# Leemos los datos del dataframe
df = pd.read_csv("games-data-clean.csv")

# seleccionamos 2 plataformas y se realiza un filtro 
df_ag = df.query('Plataforma == "PlayStation" or Plataforma == "WiiU"')

#asignamos un valor
def Asig_valor(nombre):
    if nombre == "PlayStation":
        return 0
    else:
        return 1

df_ag = df_ag.drop(df_ag[df_ag["Puntuacion_usuario"] == 0].index)

df_ag["Plataforma"] = df_ag["Plataforma"].apply(Asig_valor)

df_ag["Puntuacion_usuario"] = df_ag["Puntuacion_usuario"]

PS = df_ag[df_ag["Plataforma"] == 0]

WiiU = df_ag[df_ag["Plataforma"] == 1]

# procesar los datos
data = df_ag[["Puntuacion", "Puntuacion_usuario"]]
clase = df_ag["Plataforma"] 

# generamos un escalador
escalador = preprocessing.MinMaxScaler()
data = escalador.fit_transform(data)

#Modelo
clasificador = KNeighborsClassifier(n_neighbors=3)
clasificador.fit(data, clase)

# datos para realizar la clasificacion
criti = 47
users = 55

# escalamos y buscamos la probabilidad que el escalador pertenece a una clase o a otra clase
NewG = escalador.transform([[criti,users]])
NewG = [[criti,users]]
print("Clase", clasificador.predict(NewG))
print("Probabilidad por clase", clasificador.predict_proba(NewG))

# graficamos las graficas de dispersion
plt.scatter(PS["Puntuacion"], PS["Puntuacion_usuario"],
            marker=".", s=150, color="darkorange", label="PlayStation(Clase: 1)")
plt.scatter(WiiU["Puntuacion"], WiiU["Puntuacion_usuario"],
            marker=".", s=150, color="c", label="WiiU (Clase: 0)")
plt.scatter(criti, users, marker="P", s=150,
            color="limegreen", label="Juego Estrenado")

plt.ylabel("Usuarios")
plt.xlabel("Puntuacion")
plt.legend(bbox_to_anchor=(1, 0.2))
plt.savefig("Grafica de Agrupacion 2.png")

