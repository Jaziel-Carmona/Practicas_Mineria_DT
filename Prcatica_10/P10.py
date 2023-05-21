
#PRACTICA 10: ANALISIS DE TEXTO

from wordcloud import WordCloud
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# Lectura de datos
df_nb = pd.read_csv("games-data-clean.csv")

# text = " ".join(Plataforma for Plataforma in df_nb.Plataforma)

# # Creando un word_cloud con texto argumento con el metodo .generate() 
# wc = WordCloud(collocations = False, background_color = 'white').generate(text)

# # Mostrar los datos generados
# plt.imshow(wc, interpolation='bilinear')
# plt.axis("off")
# plt.savefig('Plataformas_nube.png')
# plt.show()

print("\nCreando el word_cloud normal....... procesando los datos")

text2 = " ".join(Genero for Genero in df_nb.Genero)

# Creando un word_cloud con texto argumento con el metodo .generate() 
wc2 = WordCloud(collocations = False, background_color = 'black').generate(text2)

# Mostrar los datos generados
plt.imshow(wc2, interpolation='bilinear')
plt.axis("off")
plt.savefig('Generos_nube.png')
plt.show()

print("\nNube creada con exito")

# guardamos el texto de todas las filas en un archivo txt
DataTextDes=""

def filtroDes(renglon):
    global DataTextDes
    DataTextDes += str(renglon+" ")

df_nb["Desarrollador"].apply(filtroDes)

# Creamos y guardamos los datos en un archivo txt
arch = open("Data_Developers.txt", mode="w")
arch.write(DataTextDes)
arch.close()

# Leemos los datos del archivo txt
arch = open("Data_Developers.txt", mode="r")
DataTextDes = arch.read()
arch.close()

print("\nCreando el word_cloud con forma....... procesando los datos")

# Creamos la nube de texto con las forma de una imagen seleccionada .png
mascaraDes = np.array(Image.open("Pacman.png"))

nubeDes = WordCloud(max_words=2250, mask=mascaraDes,margin=10, random_state=1).generate(DataTextDes)
default_colors = nubeDes.to_array()

plt.figure()
plt.axis("off")
plt.title("Word_cloud Con forma")
plt.imshow(default_colors, interpolation="bilinear")

nubeDes.to_file("PacmanNube_Desarrolladores.png")

print("\nNube creada con exito")



