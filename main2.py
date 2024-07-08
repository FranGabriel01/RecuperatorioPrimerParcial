from funciones2 import *
peliculas = None  #Con esto se fija que se cargo

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
        
    match opcion:
        case '1':
            if peliculas is None:  # Con este if en los cases se verifica si se cargo el archivo csv.
                nombre_archivo = input("Ingrese el nombre del archivo CSV: ")
                peliculas = cargar_csv(nombre_archivo)
                print("Archivo cargado exitosamente.")
            else:
                print("Ya has cargado el archivo CSV.")
        
        case '2':
            if peliculas is not None:
                imprimir_lista(peliculas)
            else:
                print("Debes cargar el archivo CSV primero.")
        
        case '3':
            if peliculas is not None:
                peliculas = list(map(asignar_rating, peliculas))
                print("Ratings asignados.")
            else:
                print("Debes cargar el archivo CSV primero.")
        
        case '4':
            if peliculas is not None:
                peliculas = list(map(asignar_genero, peliculas))
                print("Géneros asignados.")
            else:
                print("Debes cargar el archivo CSV primero.")
        
        case '5':
            if peliculas is not None:
                genero = input("Ingrese el género a filtrar (drama, comedia, acción, terror): ")
                peliculas_filtradas = filtrar_por_genero(peliculas, genero)
                nombre_archivo = f"{genero}.csv"
                with open(nombre_archivo, 'w') as file:
                    writer = csv.DictWriter(file, fieldnames=["id_peli", "titulo", "genero", "rating"])
                    writer.writeheader()
                    writer.writerows(peliculas_filtradas)
                print(f"Archivo filtrado por {genero} guardado como {nombre_archivo}.")
            else:
                print("Debes cargar el archivo CSV primero.")
        
        case '6':
            if peliculas is not None:
                peliculas = ordenar_peliculas(peliculas)
                imprimir_lista(peliculas)
            else:
                print("Debes cargar el archivo CSV primero.")
        
        case '7':
            if peliculas is not None:
                informar_mejor_rating(peliculas)
            else:
                print("Debes cargar el archivo CSV primero.")
        
        case '8':
            if peliculas is not None:
                nombre_archivo = input("Ingrese el nombre del archivo JSON para guardar: ")
                guardar_peliculas(peliculas, nombre_archivo)
                print(f"Películas guardadas en {nombre_archivo}.")
            else:
                print("Debes cargar el archivo CSV primero.")
        
        case '9':
            print("Saliendo del programa...")
            break
        
        case _:
            print("Opción no válida. Intente nuevamente.")
