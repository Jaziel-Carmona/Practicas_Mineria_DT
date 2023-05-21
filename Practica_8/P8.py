
#PRACTICA 8: FORECASTING

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import datetime

#Adquirimos los datos
df = pd.read_csv("games-data-clean.csv")

#Como trabajaremos a traves del campo de fecha_estreno
#realizaremos una funcion para cambiar el formato de fecha que tenemos

def CambioformatoFecha(fecha):
    fechaSeparada = fecha.split()
    cam = ""
    if(fechaSeparada[0] == "January"):
        fechaSeparada[0] = "01"
    elif(fechaSeparada[0] == "February"):
        fechaSeparada[0] = "02"
    elif(fechaSeparada[0] == "March"):
        fechaSeparada[0] = "03"
    elif(fechaSeparada[0] == "April"):
        fechaSeparada[0] = "04"
    elif(fechaSeparada[0] == "May"):
        fechaSeparada[0] = "05"
    elif(fechaSeparada[0] == "June"):
        fechaSeparada[0] = "06"
    elif(fechaSeparada[0] == "July"):
        fechaSeparada[0] = "07"
    elif(fechaSeparada[0] == "August"):
        fechaSeparada[0] = "08"
    elif(fechaSeparada[0] == "September"):
        fechaSeparada[0] = "09"
    elif(fechaSeparada[0] == "October"):
        fechaSeparada[0] = "10"
    elif(fechaSeparada[0] == "November"):
        fechaSeparada[0] = "11"
    elif(fechaSeparada[0] == "December"):
        fechaSeparada[0] = "12"
    for i in range(len(fechaSeparada[1])-1):
        cam += fechaSeparada[1][i]
    fechaSeparada[1] = cam
    fechaFormateada = str(
        fechaSeparada[1]+"/"+fechaSeparada[0]+"/"+fechaSeparada[2])
    return datetime.strptime(str(fechaFormateada), "%d/%m/%Y")

#Por fin jalo la funciooooooooonnnn Anteriooooooorrrrrrrr!!!! WUUUUUUUUUUUU

#Se aplica el cambio de formato al campo de fecha de estreno
df["Fecha_estreno"] = df["Fecha_estreno"].map(CambioformatoFecha)

# Cantidad de juegos por año
def juegosFecha(fecha):
    f_Text = str(fecha)
    return str(f_Text[0])+str(f_Text[1])+str(f_Text[2])+str(f_Text[3])

#Aplicamos los juegos por año
df["Año"] = df["Fecha_estreno"].apply(juegosFecha)

#Declaramos listas vacias
años = []
Pri_5 = []
Ult_5 = []
J_Cant = []
Pri5_Cant = []
Ult5_Cant = []

# Realizamos un filtro de los juegos que hay por año
for i in range(1995,2021):
    # todos los años
    numeroJuegos = len(df[df["Año"]==str(i)])

    años.append(i)
    J_Cant.append(numeroJuegos)
    if i < 2000:    #Para los juegos del (1995 a 1999)
        Pri_5.append(i)
        Pri5_Cant.append(numeroJuegos)
    if i > 2015:    #Para los juegos del (2016 a 2021)
        Ult_5.append(i)
        Ult5_Cant.append(numeroJuegos)

print("Generando grafica..........")
# realizamos una conversion de nuestras listas con el apoyo de la libreria Numpy
an = np.array(años)
an_p5 = np.array(Pri_5)
an_u5 = np.array(Ult_5)

ju = np.array(J_Cant)
ju_p5 = np.array(Pri5_Cant)
ju_u5 = np.array(Ult5_Cant)


# creamos instacias de regresion lineal
Rlt = LinearRegression()
Rlp5 = LinearRegression()
Rlu5 = LinearRegression()

# le pasamos los datos
Rlt.fit(an.reshape(-1, 1), ju)
Rlp5.fit(an_p5.reshape(-1, 1), ju_p5)
Rlu5.fit(an_u5.reshape(-1, 1), ju_u5)

# Para generar los trazos de las lineas definimos una
def linea(x,m,b):
    return m*x+b      # y = m*x + b

# graficamos las lineas y los puntos
plt.plot(años, [linea(x, Rlt.coef_,Rlt.intercept_) for x in años], color='red')
plt.plot(Pri_5, [linea(x, Rlp5.coef_,Rlp5.intercept_) for x in Pri_5], color='limegreen')
plt.plot(Ult_5, [linea(x, Rlu5.coef_,Rlu5.intercept_) for x in Ult_5], color='black')
plt.scatter(años, J_Cant,s=80, color="darkblue", marker="h")

# Ajustamos los titulos y las etiquetas
plt.ylabel("Numero de Juegos")
plt.xlabel("Años de estreno")
plt.savefig("Grafica de Prediccion de Estrenos de Juegos.png")
plt.clf

print("Grafica generada con exito")
