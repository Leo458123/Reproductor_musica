import os
import pygame

def siguientes():
    return 0
def reproducir_musica(playlist_path):
    # Inicializar pygame
    pygame.init()

    # Verificar si el archivo de playlist existe
    if not os.path.isfile(playlist_path):
        print(f'El archivo de playlist "{playlist_path}" no existe.')
        return

    # Leer el archivo de playlist y obtener la lista de rutas de música
    with open(playlist_path, 'r') as playlist_file:
        music_paths = [line.strip() for line in playlist_file]

    # Reproducir cada canción en la playlist
    for music_path in music_paths:
        # Verificar si el archivo de música existe
        if os.path.isfile(music_path):

            # Esperar a que la música termine de reproducirse
            while True:
                # menu inicial, deberia esta aqui el cargar la playlist y el poder iniciar con la reproduccion
                print("-----BIENVENIDO------")
                print("0. EMPEZAR, 5 salir ")
            while True:
                # Mostrar el menú interactivo del reproductor y donde se controle la musica. Opcciones que deberian estar


                print("---- Menú ----")
                print("0. Emepzar o repetir")
                print("1. Siguiente cancion")
                print("2. Pausar")
                print("3. Reproducir")
                print("4. Mostrar lista")
                print("5. Salir")
                print(f'Musica reprodiciendo"{music_path}" ')

                opcion = input("Ingrese el número de opción: ")
                if opcion == "0":
                    # Configurar la música
                    pygame.mixer.music.load(music_path)

                    # Reproducir la música

                    pygame.mixer.music.play(-1)
                if opcion == "1":
                    # Permitir al usuario elegir una nueva canción
                    pygame.mixer.music.stop()
                    break
                elif opcion == "2":
                    # Pausar la reproducción de música
                    pygame.mixer.music.pause()
                elif opcion == "3":
                    # Reanudar la reproducción de música
                    pygame.mixer.music.unpause()
                elif opcion == "4":

                    pass

                elif opcion == "5":
                    # Salir del bucle y finalizar pygame
                    pygame.mixer.music.stop()
                    pygame.quit()
                    return
                else:
                    print("Opción inválida. Por favor, elija una opción válida.")


        else:
            print(f'El archivo de música "{music_path}" no existe.')

    # Finalizar pygame

# Ruta del archivo de playlist

# comando para exportar un archivo py a ejecutable .exe:  pyinstaller main.py --onefile

playlist_path = r"C:\Users\HP\Documents\musica_lista\lista.txt"

# Llamar a la función para reproducir la música
reproducir_musica(playlist_path)
