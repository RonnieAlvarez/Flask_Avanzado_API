###### Cómo usar usar los recuros para para el módulo 4

1. Crea y activa tu entorno virtual

   `python3 -m venv venv`

   Mac & Linux `source venv/bin/activate`

   Windows `venv\Scripts\activate.bat`

2. Instala el framework y las dependencias en tu entorno virtual:

   `pip install -r requirements.txt `

3. Crear tu base de datos Postgresql

   `sudo -u username_db psql`

   `create database edteamapidb;`

   `\c edteamapidb;`

4. Actualiza la cadena de conexión a tu base de datos en los archivos `config/dev.py` & `config/prod.py`

5. Levanta tu servidor

   ​	`flask run`

Las demás configuraciones y creación de archivos los vemos directamente en las clases.

**No olvides que puedes poner tus dudas en la plataforma de EDteam o escribir un DM. Con gusto te estaré apoyando.** 

Att: Prof. Kevin Guzmán