# PROBANDO COMANDOS EN EL CONJUNTO DE DATOS ESCOGIDO EN LA TAREA #1

# Libreria necesarias
from tabulate import tabulate
from typing import Tuple, List
import pandas as pd
from datetime import datetime

print("-------------- IMPORTACION DE LOS DATOS ------------")

#print("\nCOMANDO -> pandas.read_csv()")
# Lee el conjunto de datos

def print_tabulate(df: pd.Practica_2):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

df = pd.read_csv("games-data.csv")


# Imprime todos los datos, todas las columnas
print_tabulate(df)
