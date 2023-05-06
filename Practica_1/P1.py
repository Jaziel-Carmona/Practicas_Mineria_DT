# PRACTICA 1: SELECCIONAR UN CONJUNTO DE DATOS DE NUESTRO INTERES

# Librerias
from tabulate import tabulate
#from typing import Tuple, List
import pandas as pd
#from datetime import datetime

#se escogio una Dataframe de 10 columnas las cuales son las siguientes:
# name 
# platform 
# r-date 
# score
# user score
# developer : desarrollador de juegos
# genre
# players
# crítics 
# users

#El dataframe contiene 17,944 elementos

print("-------------- ADQUISICION DE DATOS ------------")


def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

df = pd.read_csv("games-data.csv")

# Imprime todos los datos
print_tabulate(df)

#print(df)
