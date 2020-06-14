import os
import glob
import time

print("Inserte cada cuanto tiempo desea que corra el programa (segundos):")
# Obtener segundos
segundos = int(input())




def crearCarpetas():
    for extension in extension_set:
        try:
            os.makedirs("Archivos_" + extension)
        except FileExistsError:
            continue


def ordenarArchivos():
    for file in files_list:
        fextension = file.rsplit(sep=".", maxsplit=1)
        try:
            os.rename(file, "Archivos_" + fextension[1] + "/" + file)
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


while 1:
    # Variables Globales
    files_list = glob.glob("*")
    extension_set = set()

    crearSetExtensiones()

    mostrarSetExtensiones()

    crearCarpetas()
    ordenarArchivos()

    time.sleep(segundos)
