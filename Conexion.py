import mysql.connector

class Coneccion:
    def __init__(self):
        self.__user = 'root'
        self.__pass = '1088'
        self.__host = 'localhost'
        self.__db = 'supermarket'
        self.__conn = None
        self.__cursor = None
    def conectar(self):
        try:
            self.__conn = mysql.connector.connect(user=self.__user,password = self.__pass,host=self.__host,database = self.__db)
            self.__cursor = self.__conn.cursor()
        except Exception as e:
            print(f"No se pudo concetar a la base: {e}")
    
    def close_conn(self):
        try:
            self.__conn.close()
        except Exception as e:
            print(f"Error al cerrar la conexion: {e}")

    def consulta(self,query):
        rs = None
        try:
            self.__cursor.execute(query)
            rs = self.__cursor.fetchall()
        except Exception as e:
            print(f"No se pudo realizar la consulta: {e}")
        
        return rs


if __name__ == "__main__":
    '''conn = mysql.connector.connect(user='root',password = '1088',host='localhost',database = 'sakila')

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM actor")

    rs = cursor.fetchall()

    conn.close()

    print(rs)'''

    conexion =  Coneccion()
    conexion.conectar()
    resultado_consulta = conexion.consulta("SELECT * FROM producto")
    conexion.close_conn()
    print(resultado_consulta)


