#datos para la conexion a base de datos

dataBaseName = "proyectobd"
userName = "root"
userPassword = ""
conecctionPort = 3306
server="localhost"

#creando la conexion a base de datos
dataBaseConnection =f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{conecctionPort}/{dataBaseName}"
