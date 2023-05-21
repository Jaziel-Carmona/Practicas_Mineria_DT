
#PRACTICA 9: DATA CLUSTERING

import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

def Met_Codo_KValues():
    # encontramos el valor para "K" con el metodo
    SSE_k = []
    valor_i = []
    for i in range(1,11):
        kmeans = KMeans(init="random",n_clusters=i, n_init=10, max_iter=100, random_state=40)
        kmeans.fit(datosEscalados)
        SSE_k.append(kmeans.inertia_)
        valor_i.append(i)

    #Generamos la grafica y le ponermos los titulos
    plt.title("Clusters -- Juegos de PlayStation")
    plt.xlabel("Numero de Agrupaciones (Clusters)")
    plt.ylabel("Inercia")
    plt.plot(valor_i, SSE_k)
    plt.savefig("Grafica de Clusters de PS.png")
    plt.clf()



# Adquirimos los datos del dataframe
df = pd.read_csv("games-data-clean.csv")
df_ps = df[df["Plataforma"] == "PlayStation"]

# Obtenemos los datos de Puntuacion y Criticas
data = df_ps[["Puntuacion", "Criticas"]]

# Declaramos una variable de escalador y comenzamos la escalacion
escalador = MinMaxScaler().fit(data.values)
datosEscalados = pd.DataFrame(escalador.fit_transform(data.values), columns=["Puntuacion", "Criticas"])

# Valores de K
# k_valor = 3
# k_valor = 4
k_valor = 5

kmeans = KMeans(init="random",n_clusters=k_valor, n_init=10, max_iter=100, random_state=40)
kmeans.fit(datosEscalados)

# lista para asignar los valores al grupo
dt_agrup = datosEscalados.assign(Grupo=kmeans.labels_)

print("\nGenerando graficas........\n\n")
# Colores de los clusters
colores = ["aqua", "crimson", "forestgreen", "goldenrod", "mediumslateblue"]

#Scatters
for i in range(k_valor):
    cd_temp = dt_agrup[dt_agrup["Grupo"] == i]
    plt.scatter(kmeans.cluster_centers_[i][0], kmeans.cluster_centers_[i][1]
                ,s=300,marker="X",color=colores[i])
    plt.scatter(cd_temp["Puntuacion"],cd_temp["Criticas"],marker="o", alpha=0.8
                ,s=40,color=colores[i])

#Generamos la grafica y le ponermos los titulos
plt.title("Clusters en Juegos de PlayStation")
plt.ylabel("Puntuacion General del juego")
plt.xlabel("Criticas")
plt.savefig("PS Clusters K = 5.png")
plt.clf()

Met_Codo_KValues()

print("Grficas creadas con exito")
