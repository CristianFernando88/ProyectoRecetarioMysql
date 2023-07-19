from Conexion import Conexion
class preparacionBd:
    _SELECCIONAR = 'SELECT * FROM preparacion WHERE receta_id = %s'
    _INSERTAR = '''INSERT INTO preparacion 
                (descripcion_paso,orden,receta_id) 
                VALUES (%s,%s,%s)'''
    
    _ACTUALIZAR = '''UPDATE preparacion SET 
                     descripcion_paso = %s, 
                     WHERE orden = %s and receta_id = %x
                  '''
    _ELIMINAR = 'DELETE FROM preparacion WHERE receta_id = %s'
    
    @classmethod
    def seleccionar(cls,id_receta):
        with Conexion.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(cls._SELECCIONAR,(id_receta,))
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
    receta = 1
    pasos = preparacionBd.seleccionar(receta)
    print(pasos)