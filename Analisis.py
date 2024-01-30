import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kurtosis

# Cargar datos
datos = pd.read_csv("movies.csv", encoding='ISO-8859-1')

# 1. Resumen de datos
print(datos.describe())


# 4.1. Top 10 películas con más presupuesto
top_budget = datos.nlargest(10, "budget")[["title", "budget"]]
print(top_budget)

# 4.2. Top 10 películas con más ingresos
top_revenue = datos.nlargest(10, "revenue")[["title", "revenue"]]
print(top_revenue)

# 4.3. Película con más votos
top_vote_count = datos.nlargest(1, "voteCount")[["title", "voteCount"]]
print(top_vote_count)

# 4.4. Peor película según votos
worst_movie = datos.nsmallest(1, "voteAvg")[["title", "voteAvg"]]
print(worst_movie)

# 4.5. Histograma de películas por año
datos["releaseYear"] = pd.to_datetime(datos["releaseDate"]).dt.year
plt.hist(datos["releaseYear"], bins=100)
plt.xlabel("Año")
plt.ylabel("Cantidad de películas")
plt.title("Cantidad de películas por año")
plt.show()

# 4.6. Género principal de las 20 películas más recientes
top_20_recent_genres = datos.nlargest(20, "releaseYear")["genres"].str.split("|", expand=True).stack().value_counts().index[0]
print(f"Género principal de las 20 películas más recientes: {top_20_recent_genres}")

# Gráfico de barras de géneros
genres_counts = datos["genres"].str.split("|", expand=True).stack().value_counts()
plt.bar(genres_counts.index, genres_counts.values)
plt.xlabel("Género")
plt.ylabel("Cantidad de películas")
plt.title("Cantidad de películas por género")
plt.xticks(rotation=90)
plt.show()

# 4.7. Género principal de películas con mayores ingresos
top_revenue_genre = datos.loc[datos.groupby("genres")["revenue"].idxmax()][["genres", "revenue"]]
print(top_revenue_genre)

# 4.8. Influencia de la cantidad de actores en los ingresos
print(datos[["actorsAmount", "revenue"]].sort_values(by="revenue", ascending=False).head())

# 4.9. Influencia de la cantidad de hombres y mujeres en el reparto en la popularidad y los ingresos
print(datos[["castWomenAmount", "popularity"]].sort_values(by="popularity", ascending=False).head())
print(datos[["castMenAmount", "popularity"]].sort_values(by="popularity", ascending=False).head())
print(datos[["castWomenAmount", "revenue"]].sort_values(by="revenue", ascending=False).head())
print(datos[["castMenAmount", "revenue"]].sort_values(by="revenue", ascending=False).head())

# 4.10. Directores de las 20 películas mejor calificadas
top_rated_directors = datos.nlargest(20, "voteAvg")[["director", "voteAvg"]]
print(top_rated_directors)

# 4.11. Correlación entre presupuestos y ingresos
plt.scatter(datos["budget"], datos["revenue"])
plt.xlabel("Presupuesto")
plt.ylabel("Ingresos")
plt.title("Presupuesto vs Ingresos")
plt.show()

# 4.12. Asociación de ciertos meses de lanzamiento con mejores ingresos
print("4.12")
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

datos["genres"] = datos["genres"].fillna("")

datos["num_genres"] = datos["genres"].apply(lambda x: x.count("|") + 1 if "|" in x else 1)
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
