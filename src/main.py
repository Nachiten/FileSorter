import os
import glob
import time


def crearCarpetas():
    for extension in extension_set:
        try:
            os.makedirs(prefijo_carpeta + extension)
        except FileExistsError:
            continue


def ordenarArchivos():
    for file in files_list:
        fileExtension = file.rsplit(sep=".", maxsplit=1)
        try:
            os.rename(file, prefijo_carpeta + fileExtension[1] + "/" + file)
        except(OSError, IndexError):
            continue


def crearSetExtensiones():
    for file in files_list:
        extension = file.rsplit(sep=".", maxsplit=1)
        try:
            extension_set.add(extension[1])
        except IndexError:
            continue
    extension_set.remove("py")


def mostrarSetExtensiones():
    print("Extensiones encontradas: ")
    for unaExtension in extension_set:
        print(unaExtension, end=" ")
    print("")


try:
    # Cada cuantos segundos el software corre
    segundos = ""
    # Prefijo que se le pondrá a cada carpeta antes de la extension
    prefijo_carpeta = "files "

    # Get segundos input
    while True:
        print("Inserte cada cuanto tiempo desea que corra el programa (Enter para 5 segundos):")
        segundos = input()
        if segundos.isdigit():
            segundos = int(segundos)
            break
        elif segundos == "":
            segundos = 5
            break
        else:
            print("Error, debe ser un número entero o un Enter")

    # Do the same but for prefijo_carpeta
    while True:
        print("Inserte el prefijo para las carpetas (Enter para 'files '):")
        prefijo_carpeta = input()
        # Check if prefijo_carpeta is string, and no empty
        if prefijo_carpeta == "":
            prefijo_carpeta = "files "
            break
        # Check if variable is string
        elif not isinstance(prefijo_carpeta, str):
            print("Error, debe ser una cadena de caracteres valida o un Enter")
        else:
            break

    print("Ejecutando cada '" + str(segundos) + "' segundos, con prefijo '" + prefijo_carpeta + "'")

    while 1:
        # Variables Globales
        files_list = glob.glob("*")
        extension_set = set()

        crearSetExtensiones()
        mostrarSetExtensiones()
        crearCarpetas()
        ordenarArchivos()

        time.sleep(segundos)
except KeyboardInterrupt:
    print("Deteniendo programa...")
