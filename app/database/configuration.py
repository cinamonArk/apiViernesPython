from sqlalchemy import create_engine, event
from sqlalchemy import sessionmakert
from sqlalchemy.engine import engine 
#conexion a base de datos
#Nombre de la base de datos
dataBaseName= "gestionbd"

#usuario de la base de datos 
userName = "root"

#contraseña del usuario 
UserPassword=""

#servidor de conexion
servidorLocalHost = "localhost"

#Puerto de conexion 
ConnectionPort="3306"

#creando la conexion
conexionToDataBase=f"mysql"