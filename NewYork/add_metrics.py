import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from geopy.geocoders import GoogleV3
import math

df = pd.read_csv('datasets/income_cu_traffic.csv')

income = df["Income"]
density = df["Density"]
traffic = df['Traffic']
lat_cart = df["Latitude"]
lon_cart = df["Longitude"]


df = pd.read_csv('department_initial.csv')
lat_shop = df["Latitude"]
lon_shop = df["Longitude"]

length_shop = len(lat_shop)
length_cart = len(lat_cart)

saved_cartier = 0
income_list = []
density_list = []
traffic_list = []
# Se parcurg magazinele
for i in range(length_shop):
    min = 99999999999
    for j in range(length_cart):
        dist = math.sqrt(math.pow((lat_shop[i] - lat_cart[j]), 2) + math.pow((lon_shop[i] - lon_cart[j]), 2))
        if dist < min:
            min = dist
            saved_cartier = j
    traffic_list.append(traffic[saved_cartier])
    income_list.append(income[saved_cartier])
    density_list.append(density[saved_cartier])

df['Income'] = income_list
df['Density'] = density_list
df['Traffic'] = traffic_list

df.to_csv('department_enhanced.csv', index=False)