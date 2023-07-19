from Conexion import Conexion
class ingredienteBd:
    _SELECCIONAR = 'SELECT * FROM ingredientes'
    _INSERTAR = '''INSERT INTO ingredientes 
                (nombre_ingrediente) 
                VALUES (%s)'''
    
    _ACTUALIZAR = '''UPDATE recetas SET 
                     nombre_receta = %s, 
                     tiempo_preparacion = %s
                     tiempo_coccion = %s
                     fecha_creacion = %s
                     WHERE id_receta = %s
                  '''
    _ELIMINAR = 'DELETE FROM ingredientes WHERE id_ingrdiente = %s'
    
    _BUSCAR = "SELECT * FROM ingredientes WHERE nombre_ingrediente LIKE %s"
    
    @classmethod
    def seleccionar(cls):
        with Conexion.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
        return registros
        
    @classmethod
    def insertar(cls,receta):
        with Conexion.conectar()as conn:
            with Conexion.get_cursor() as cr:
                valores = (receta[0],receta[1],receta[2],receta[3])
                cr.execute(cls._INSERTAR,valores)
            conn.commit()
    
    @classmethod
    def eliminar(cls,id):
        with Conexion.conectar()as conn:
            with Conexion.get_cursor() as cr:
                cr.execute(cls._ELIMINAR,id)
            conn.commit()

    @classmethod
    def actualizar(cls,receta):
        with Conexion.conectar() as conn:
            with Conexion.get_cursor() as cr:
                parametros = (receta.nombre,receta.tiempo_prep,receta.tiempo_coc,receta.fecha_crea,receta.id)
                cr.execute(cls._ACTUALIZAR,parametros)
            conn.commit()
            
    @classmethod
    def buscar(cls,buscado):
        b = f"{buscado}%"
        resultado = None
        with Conexion.conectar() as conn:
            with Conexion.getCursor() as cr:
                cr.execute(cls._BUSCAR,(b,))
                resultado = cr.fetchall()
        return resultado
    
    @classmethod
    def seleccion_all(cls):
        resultado = None
        with Conexion.conectar() as conn:
            with Conexion.getCursor() as cr:
                cr.execute(cls._SELECCIONAR)
                resultado = cr.fetchall()
        return resultado
    
if __name__ == "__main__":
    buscado = "zanahoria"
    resultado = ingredienteBd.buscar(buscado)
    print(resultado)