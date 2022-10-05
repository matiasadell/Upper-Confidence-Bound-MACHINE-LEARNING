#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 12:41:01 2019

@author: juangabriel
"""

# Upper Confidence Bound (UCB)

# Importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Cargar el dataset
dataset = pd.read_csv("Ads_CTR_Optimisation.csv")

# Algoritmo de UCB
import math
N = 10000
d = 10
number_of_selections = [0] * d      # Cantidad de seleccion de anuncios, 0 * n significa que va a haber la misma cantidad de 0 que los anuncios
sums_of_rewards = [0] * d           # Cantidad de clicks que tuvieron los anuncios
ads_selected = []
total_reward = 0
for n in range(0, N):       # Cantidad de rondas de los usuarios
    max_upper_bound = 0     # Anuncio mas clickeado
    ad = 0
    for i in range(0, d):       # Cantidad de rondas de los anuncios
        if(number_of_selections[i]>0):      # Hacemos esto para que las primeras 10 rondas es para recaber informacion y las demas para sacar
            average_reward = sums_of_rewards[i] / number_of_selections[i]       # La recompensa media del anuncio i hasta la ronda n
            delta_i = math.sqrt(3/2*math.log(n+1)/number_of_selections[i])      # Formula del intervalo de confianza
            upper_bound = average_reward + delta_i          # Formula del intervalo de confianza
        else:
            upper_bound = 1e400
            
        if upper_bound > max_upper_bound:      
            max_upper_bound = upper_bound        # Conseguimos el anuncio mas clickeado
            ad = i
    ads_selected.append(ad)
    number_of_selections[ad] = number_of_selections[ad] + 1
    reward = dataset.values[n, ad]
    sums_of_rewards[ad] = sums_of_rewards[ad] + reward
    total_reward = total_reward + reward
    
    
    
# Histograma de resultados
plt.hist(ads_selected)
plt.title("Histograma de anuncios")
plt.xlabel("ID del Anuncio")
plt.ylabel("Frecuencia de visualización del anuncio")
plt.show()
    
    
    