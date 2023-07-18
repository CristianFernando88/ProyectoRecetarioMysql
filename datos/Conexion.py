import mysql.connector
from Config import credenciales
from mysql.connector import errors
class Conexion:
    _conn = None
    _cursor = None

    @classmethod
    def conectar(cls):
        if cls._conn is None:
            try:
                cls._conn = mysql.connector.connect(**credenciales)
                return cls._conn
            except errors.DatabaseError as e:
                print(f"No se pudo concetar a la base: {e}")
        else:
            return cls._conn
    
    @classmethod
    def getCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.conectar().cursor()
                return cls._cursor
            except errors.DatabaseError as e:
                print("Problema para retornar conexion");
        else:
            return cls._cursor
       

if __name__ == "__main__":
    '''conn = mysql.connector.connect(user='root',password = '1088',host='localhost',database = 'sakila')

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM actor")

    rs = cursor.fetchall()

    conn.close()

    print(rs)'''

    conexion =  Conexion.conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM receta")
    consulta = cursor.fetchall()
    conexion.close_conn()
    print(consulta)


