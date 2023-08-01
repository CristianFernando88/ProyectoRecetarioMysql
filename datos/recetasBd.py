from Conexion import Conexion
from datetime import datetime
class recetaBd:
    _SELECCIONAR = 'SELECT * FROM recetas'
    _INSERTAR = '''INSERT INTO recetas 
                (nombre_receta,tiempo_preparacion,tiempo_coccion,fecha_creacion,etiqueta) 
                VALUES (%s,%s,%s,NOW(),%s)'''
    
    _ACTUALIZAR = '''UPDATE recetas SET 
                     nombre_receta = %s, 
                     tiempo_preparacion = %s
                     tiempo_coccion = %s
                     fecha_creacion = %s
                     WHERE id_receta = %s
                  '''
    _ELIMINAR = 'DELETE FROM recetas WHERE id_receta = %s'
    
    _BUSCAR = "SELECT * FROM recetas WHERE nombre_receta LIKE %s"
    
    @classmethod
    def seleccionar(cls):
        with Conexion.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
        return registros
        
    @classmethod
    def insertar(cls,nombre,preparacion,coccion,etiqueta):
        '''inserta los valores en la tabla receta
            receibe como parametro nombre,preparacion,coccion,etiqueta.
        ''' 
        trasaccion = False
        with Conexion.conectar()as conn:
            with Conexion.getCursor() as cr:
                valores = (nombre,preparacion,coccion,etiqueta)
                cr.execute(cls._INSERTAR,valores)
                trasaccion = True
            conn.commit()
        return trasaccion
    
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
if __name__ == "__main__":   
    receta = ("Arroz con leche",20,30,datetime.now(),"Postre Tradicional")
    print(recetaBd.insertar(receta[0],receta[1],receta[2],receta[4]))
    #print(recetaDatos.seleccionar())
    #print(recetaDatos.insertar(receta))

    '''buscado = "ensalada"
    resultado = recetaBd.buscar(buscado)

    print(resultado)'''
