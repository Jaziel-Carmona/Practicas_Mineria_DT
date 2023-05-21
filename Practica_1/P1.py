# PRACTICA 1: INTRODUCCION

# SELECCIONAR UN CONJUNTO DE DATOS DE NUESTRO INTERES

# Librerias
from tabulate import tabulate
#from typing import Tuple, List
import pandas as pd
#from datetime import datetime

#se escogio de Kaggle una Dataframe de 10 columnas las cuales son las siguientes:

# Data columns:

# name: The name of the game
# platform: Platform it was released
# r-date: date it was released
# score: average score given by critics (metascore)
# user score: average score given by users in the website
# developer: game developer
# genre: genre of the game (can be multiple)
# players: Number of players (some games don't have this information)
# critics: number of critics reviewing the game
# users: Number of metacritic users that reviewed the game

#El dataframe contiene 17,944 elementos

print("-------------- ADQUISICION DE DATOS ------------")


def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

df = pd.read_csv("games-data.csv")

# Imprime todos los datos
print_tabulate(df)

#print(df)
