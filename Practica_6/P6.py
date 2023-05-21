
#PRACTICA 6: MODELOS LINEALES

import matplotlib.pyplot as plt
import pandas
import numpy as np
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression

#Leemos con pandas nuestro dataframe
df = pandas.read_csv("games-data-clean.csv")

df["Puntuacion_usuario"] = df["Puntuacion_usuario"]
df = df.drop(df[df["Puntuacion_usuario"] == 0].index)

#Seleccionamos las columnas
puntuacion = df.iloc[:, 4] #Almacenamos la puntuacion de los juegos
usuarios = df.iloc[:, 5] #Almacenamos la puntuacion de los usuarios

puntuacionAr = np.array(puntuacion)
usuariosAr = np.array(usuarios)

# Realizamos la prueba de correlacion
Correlacion = pearsonr(puntuacion,usuarios)
print("Coeficiente de correlación de Pearson: ", Correlacion[0])
print("P-value: ",Correlacion[1])

# Regresion Lineal 
Rl = LinearRegression()

# Introducimos los datos
Rl.fit(puntuacionAr.reshape(-1, 1), usuariosAr)

# Parametros estimados
print('Pendiente(m) = '+ str(Rl.coef_) +
      ', Interseccion(b) = ' + str(Rl.intercept_))

# Calculamos el trazo de la linea 
def linea(x):
    return 0.589328*x+28.06489179

# Creamos el grafico
plt.plot(puntuacion, [linea(i) for i in puntuacion], color='red') #Trazo la recta de regresion
plt.scatter(puntuacion, usuarios, label='data', color='dodgerblue', marker='.')

#Ponemos los titulos y etiquetas
plt.xlabel("Puntuacion juego", size=12)
plt.ylabel("Puntuacion usuarios", size=12)
plt.title('Grafica RL - Puntuacion vs Puntuacion Usuarios')
plt.savefig("Grafica de RL Puntuacion de Juego vs Usuarios.png")
plt.clf


