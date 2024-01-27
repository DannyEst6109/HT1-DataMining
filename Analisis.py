import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kurtosis

# Cargar datos
datos = pd.read_csv("movies.csv")

# 1. Resumen de datos
print(datos.describe())

# 4.12. Asociación de ciertos meses de lanzamiento con mejores ingresos
datos["releaseMonth"] = pd.to_datetime(datos["releaseDate"]).dt.month
print(datos.groupby("releaseMonth")["revenue"].mean())

# 4.13. Meses con mejores ingresos y promedio de películas lanzadas por mes
print(datos["releaseMonth"].value_counts())
print(datos.groupby("releaseMonth")["revenue"].mean())

# 4.14. Correlación entre calificaciones y éxito comercial
plt.scatter(datos["voteAvg"], datos["revenue"])
plt.xlabel("Calificación")
plt.ylabel("Ingresos")
plt.title("Calificación vs Ingresos")
plt.show()

# 4.15. Género principal de las películas más largas
print(datos.nlargest(1, "runtime")[["genres", "runtime"]])


#5. EXTRAS
#¿Cuál es la correlación entre la popularidad y la duración de las películas?
plt.scatter(datos["popularity"], datos["runtime"])
plt.xlabel("Popularidad")
plt.ylabel("Duración")
plt.title("Correlación entre Popularidad y Duración")
plt.show()

#¿Cuál es el porcentaje de películas que tienen un enlace a su página principal?
porcentaje_con_homepage = (datos["homePage"].notnull().sum() / len(datos)) * 100
print(f"Porcentaje de películas con enlace a la página principal: {porcentaje_con_homepage:.2f}%")

#¿Cuál es la relación entre el presupuesto y los votos promedio de las películas?
plt.scatter(datos["budget"], datos["voteAvg"])
plt.xlabel("Presupuesto")
plt.ylabel("Votos Promedio")
plt.title("Relación entre Presupuesto y Votos Promedio")
plt.show()


#¿Cuántas películas tienen una calificación de votos promedio mayor a 8?
num_peliculas_votos_altos = len(datos[datos["voteAvg"] > 8])
print(f"Número de películas con votos promedio mayor a 8: {num_peliculas_votos_altos}")

#¿Cuál es la relación entre la cantidad de géneros y los ingresos de las películas?
datos["num_genres"] = datos["genres"].apply(lambda x: x.count("|") + 1)
plt.scatter(datos["num_genres"], datos["revenue"])
plt.xlabel("Cantidad de Géneros")
plt.ylabel("Ingresos")
plt.title("Relación entre Cantidad de Géneros e Ingresos")
plt.show()

#¿Cuántas películas fueron lanzadas en cada día de la semana?
datos["releaseDayOfWeek"] = pd.to_datetime(datos["releaseDate"]).dt.dayofweek
peliculas_por_dia_semana = datos["releaseDayOfWeek"].value_counts().sort_index()
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
peliculas_por_dia_semana.index = dias_semana
print(peliculas_por_dia_semana)
