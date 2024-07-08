import csv
import random
import json
import os

def clearconsole() -> None:
    """
    Esta función borra la pantalla de la consola en Python esperando la entrada del usuario y luego
    llamando al comando 'cls' para borrar la pantalla.
    """
    _= input('Presione enter para continuar...')
    os.system('cls')


def mostrar_menu():
    #Esta funcion se encarga de imprimir el menu
    print("\nMenú:")
    print("1) Cargar archivo .CSV")
    print("2) Imprimir lista")
    print("3) Asignar rating")
    print("4) Asignar género")
    print("5) Filtrar por género")
    print("6) Ordenar películas")
    print("7) Informar Mejor Rating")
    print("8) Guardar películas")
    print("9) Salir")



import csv
import random
import json

def cargar_csv(nombre_archivo):
    """
    Carga el contenido de un archivo CSV en una lista de diccionarios
    
    Recibe el nombre del archivo CSV a cargar

    Retorna: Una lista de diccionarios donde cada diccionario representa una película
    """
    peliculas = []
    with open(nombre_archivo, mode='r', encoding='utf-8-sig') as file:
        leer = csv.DictReader(file, fieldnames=["id_peli", "titulo", "genero", "rating"])
        for row in leer:
            peliculas.append(row)
    return peliculas

def imprimir_lista(peliculas):
    """
    Imprime la lista de películas en la consola

    Recibe:peliculas (list): Una lista de diccionarios donde cada diccionario representa una película.
    """
    for pelicula in peliculas:
        print(pelicula)

def asignar_rating(pelicula):
    """
    Asigna un rating aleatorio a una película

    Recibe: Un diccionario que representa una película

    Retorna: El diccionario de la película con el rating asignado
    """
    rating = random.randint(10, 100) / 10.0
    pelicula['rating'] = round(rating, 1)
    return pelicula

def asignar_genero(pelicula):
    """
    Asigna un género aleatorio a una película.

    Recibe un diccionaro que representa una película.

    Retorna: El diccionario de la película con el género asignado.
    """
    genero_numero = random.randint(1, 4)
    generos = {1: 'drama', 2: 'comedia', 3: 'accion', 4: 'terror'}
    pelicula['genero'] = generos[genero_numero]
    return pelicula

def filtrar_por_genero(peliculas, genero):
    """
    Filtra las películas por género.

    Recibe: Una lista de diccionarios donde cada diccionario representa una película.
            El género por el cual filtrar las películas.

    Retorna: Una lista de diccionarios de películas que coinciden con el género especificado.
    """
    peliculas_filtradas = []
    for pelicula in peliculas:
        if pelicula['genero'] == genero:
            peliculas_filtradas.append(pelicula)
    return peliculas_filtradas

def ordenar_peliculas(peliculas):
    """
    Ordena las películas por género y rating descendente usando el método de burbujeo.
    Recibe: Una lista de diccionarios donde cada diccionario representa una película.
    Retorna: La lista de diccionarios de películas ordenada por género y rating descendente.
    """
    n = len(peliculas)
    for i in range(n):
        for j in range(0, n-i-1):
            if (peliculas[j]['genero'] > peliculas[j+1]['genero']) or \
               (peliculas[j]['genero'] == peliculas[j+1]['genero'] and float(peliculas[j]['rating']) < float(peliculas[j+1]['rating'])):
                peliculas[j], peliculas[j+1] = peliculas[j+1], peliculas[j]
    return peliculas

def informar_mejor_rating(peliculas):
    """
    Imprime el título y rating de la película con el mejor rating.

    Recibe: Una lista de diccionarios donde cada diccionario representa una película.
    """
# Verificar si hay películas cargadas
    if peliculas is not None and len(peliculas) > 0:
        mejor_rating = float(peliculas[0]['rating'])
        mejor_pelicula = peliculas[0]

        
        for pelicula in peliculas:
            rating_actual = float(pelicula['rating'])
            if rating_actual > mejor_rating:
                mejor_rating = rating_actual
                mejor_pelicula = pelicula
        print(f"Mejor película: {mejor_pelicula['titulo']} con rating {mejor_pelicula['rating']}")
    else:
        print("No hay películas cargadas.")

def guardar_peliculas(peliculas, nombre_archivo):
    """
    Guarda la lista de películas en un archivo JSON.

    Recibe: Una lista de diccionarios donde cada diccionario representa una película.
            El nombre del archivo JSON donde se guardarán las películas.
    """
    with open(nombre_archivo, 'w') as file:
        json.dump(peliculas, file, ensure_ascii=False, indent=4)
