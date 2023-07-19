from Conexion import Conexion
class recetaBd:
    _SELECCIONAR = 'SELECT * FROM recetas'
    _INSERTAR = '''INSERT INTO recetas 
                (nombre_receta,tiempo_preparacion,tiempo_coccion,fecha_creacion) 
                VALUES (%s,%s,%s,%s)'''
    
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
    
#receta = "Arroz con leche",20,30,datetime.datetime.now()
#print(recetaDatos.insertar(receta))
#print(recetaDatos.seleccionar())
#print(recetaDatos.insertar(receta))

buscado = "ensalada"
resultado = recetaBd.buscar(buscado)

print(resultado)
