from datos.Conexion import Conexion as conexion
from datetime import datetime
from clases.Receta import Receta
from datos.Config import credenciales
import mysql.connector
from mysql.connector import errors
class Servicios:
    '''
    Esta clase realiza todas las transacciones con la base de datos
    '''
    # INSERTS
    
    def insertReceta(nombre,preparacion,coccion,etiqueta,favorito):
        '''inserta los valores en la tabla receta
            receibe como parametro nombre,preparacion,coccion,etiqueta.
            returna el id del insertado o none sino se inserto
        ''' 
        conn = conexion.conectar()
        cr = conexion.getCursor()
        consulta = '''INSERT INTO RECETAS 
                      (nombre,t_preparacion,t_coccion,creacion,etiqueta,favorito)
                       VALUES(%s,%s,%s,NOW(),%s,%s);
                    '''
        cr.execute(consulta,(nombre,preparacion,coccion,etiqueta,favorito,))
        conn.commit()
        cr.execute("SELECT last_insert_id() from recetas;")
        id_insert = cr.fetchone()
        conn.close()
        print(id_insert)
        if id_insert[0] > 0:
            return id_insert[0]
        else:
            return None
    
    def insertIngrediente(nombre):
        '''inserta los valores en la tabla receta
            receibe como parametro nombre.
        ''' 
        trasaccion = False
        with conexion.conectar()as conn:
            with conexion.getCursor() as cr:
                valores = (nombre)
                consulta = '''INSERT INTO ingredientes 
                              (nombre)
                              VALUES(%s);
                           '''
                cr.execute(consulta,(nombre,))
                trasaccion = True
            conn.commit()
        return trasaccion
    
    def insertPaso(descripcion,orden,recetaId):
        '''inserta los valores en la tabla receta
            receibe como parametro nombre,orden,recetaId.
        ''' 
        trasaccion = False
        with conexion.conectar()as conn:
            with conexion.getCursor() as cr:
                consulta = '''INSERT INTO preparacion 
                              (descripcion,orden,receta_id)
                              VALUES(%s,%s,%s);
                           '''
                cr.execute(consulta,(descripcion,orden,recetaId,))
                trasaccion = True
            conn.commit()
        return trasaccion
    
    def insertPaso2(id_paso,descripcion,orden,recetaId):
        '''inserta los valores en la tabla receta
        incluyendo el id de paso
        ''' 
        trasaccion = False
        with conexion.conectar()as conn:
            with conexion.getCursor() as cr:
                consulta = '''INSERT INTO preparacion 
                              VALUES(%s,%s,%s,%s);
                           '''
                cr.execute(consulta,(id_paso,descripcion,orden,recetaId,))
                trasaccion = True
            conn.commit()
        return trasaccion
    
    def insertRI(recetaId,ingId,unidad,cantidad):
        '''inserta los valores en la tabla receta_ingrediente
            receibe como parametro nombre,orden,recetaId.
        ''' 
        trasaccion = False
        with conexion.conectar()as conn:
            with conexion.getCursor() as cr:
                consulta = '''INSERT INTO receta_ingrediente 
                              (receta_id,ing_id,unidad,cantidad)
                              VALUES(%s,%s,%s,%s);
                           '''
                cr.execute(consulta,(recetaId,ingId,unidad,cantidad,))
                trasaccion = True
            conn.commit()
        return trasaccion
    
    def insertRI2(idrxi,recetaId,ingId,unidad,cantidad):
        '''inserta ingrediente de una receta incluyendo el id
        ''' 
        trasaccion = False
        with conexion.conectar()as conn:
            with conexion.getCursor() as cr:
                consulta = '''INSERT INTO receta_ingrediente 
                              VALUES(%s,%s,%s,%s,%s);
                           '''
                cr.execute(consulta,(idrxi,recetaId,ingId,unidad,cantidad,))
                trasaccion = True
            conn.commit()
        return trasaccion
    
    #CONSULTAS
    
    def consultaRecetas():
        '''retorna las recetas en la tabla recetas'''
        conn = conexion.conectar()
        cursor = conexion.getCursor()
        consulta = 'SELECT * FROM recetas'
        cursor.execute(consulta)
        recetas = cursor.fetchall()
        conn.close()
        return recetas
    
    def consultaReceta(recetaId):
        '''retorna las recetas en la tabla recetas'''
        conn = conexion.conectar()
        cursor = conexion.getCursor()
        consulta = 'SELECT * FROM recetas WHERE id_receta = %s'
        cursor.execute(consulta,(recetaId,))
        recetas = cursor.fetchall()
        conn.close()
        return recetas
     
    def consultaRecetaIng(recetaId):
        '''retorna los ingrredientes de una receta'''
        conn = conexion.conectar()
        cursor = conexion.getCursor()
        consulta = '''SELECT  receta_ingrediente.id_rxi,ingredientes.nombre,
                    receta_ingrediente.unidad,receta_ingrediente.cantidad
                    FROM recetas
                    INNER JOIN receta_ingrediente
                    ON recetas.id_receta = receta_ingrediente.receta_id
                    INNER JOIN ingredientes
                    ON receta_ingrediente.ing_id = ingredientes.id_ing
                    WHERE recetas.id_receta = %s
                    '''
        cursor.execute(consulta,(recetaId,))
        ingredientes = cursor.fetchall()
        conn.close()
        return ingredientes
    
    def consultaRecetaPas(recetaId):
        '''retorna los ingrredientes de una receta'''
        with conexion.conectar() as conn:
            with conexion.getCursor() as cursor:
                consulta = '''SELECT  preparacion.id_preparacion,preparacion.orden,preparacion.descripcion
                              FROM recetas
                              INNER JOIN preparacion
                              ON recetas.id_receta = preparacion.receta_id
                              WHERE recetas.id_receta = %s
                           '''
                cursor.execute(consulta,(recetaId,))
                recetas = cursor.fetchall()
        return recetas
    
    def cons_existe_Ing(ingrediente_nombre):
        '''Consulta si existe el ingrediente en la tabla ingrediente y retorna la posicion
        o None si no existe'''
        with conexion.conectar() as conn:
            with conexion.getCursor() as cursor:
                consulta = '''SELECT * FROM ingredientes WHERE ingredientes.nombre = %s'''
                cursor.execute(consulta,(ingrediente_nombre,))
                resultado = cursor.fetchall()
        if len(resultado) > 0 : 
            return resultado[0][0]
        else:
            return None
    
    #ELIMINAR
    
    def eliminarRecetaBd(recetaId):
        '''elimina una receta atraves de su id recetaId.
        ''' 
        trasaccion = False
        with conexion.conectar()as conn:
            with conexion.getCursor() as cr:
                consulta = '''DELETE FROM recetas
                              WHERE id_receta = %s
                           '''
                cr.execute(consulta,(recetaId,))
                trasaccion = True
            conn.commit()
        return trasaccion

    def eliminarPasosRecteaId(recetaId):
        '''elimina los pasos de una receta, atravez
            de su id
        ''' 
        trasaccion = False
        with conexion.conectar()as conn:
            with conexion.getCursor() as cr:
                consulta = '''DELETE FROM preparacion
                              WHERE receta_id = %s
                           '''
                cr.execute(consulta,(recetaId,))
                trasaccion = True
            conn.commit()
        return trasaccion
    
    def eliminarIngRecteaId(recetaId):
        '''elimina los ingredientes de una receta, atravez
            de su id
        ''' 
        trasaccion = False
        with conexion.conectar()as conn:
            with conexion.getCursor() as cr:
                consulta = '''DELETE FROM receta_ingrediente
                              WHERE receta_id = %s
                           '''
                cr.execute(consulta,(recetaId,))
                trasaccion = True
            conn.commit()
        return trasaccion
    
    def eliminarIngId(ing_id):
        '''elimina ingrediente de una receta, atravez
            de su id
        ''' 
        trasaccion = False
        with conexion.conectar()as conn:
            with conexion.getCursor() as cr:
                consulta = '''DELETE FROM receta_ingrediente
                              WHERE id_rxi = %s
                           '''
                cr.execute(consulta,(ing_id,))
                trasaccion = True
            conn.commit()
        return trasaccion

    #UPDATES
    
    def actualizarRecetaBd(nombre,tiempo_p,tiempo_c,etiqueta,favorito,id):
        '''Actualiza una receta de la bd a travez de su id
        receibe 
        ''' 
        trasaccion = False
        with conexion.conectar()as conn:
            with conexion.getCursor() as cr:
                consulta = '''UPDATE recetas SET 
                     nombre = %s, 
                     t_preparacion = %s,
                     t_coccion = %s,
                     etiqueta = %s,
                     favorito = %s
                     WHERE id_receta = %s
                  '''
                cr.execute(consulta,(nombre,tiempo_p,tiempo_c,etiqueta,favorito,id))
                trasaccion = True
            conn.commit()
        return trasaccion 
   
    def actualizarIng_recetaBd(id,unidad,cantidad):
        '''Actualiza una ingrediente de una receta
           unidad y cantidad
        ''' 
        trasaccion = False
        with conexion.conectar()as conn:
            with conexion.getCursor() as cr:
                consulta = '''UPDATE receta_ingrediente SET 
                     unidad = %s,
                     cantidad = %s
                     WHERE id_rxi = %s
                  '''
                cr.execute(consulta,(unidad,cantidad,id,))
                trasaccion = True
            conn.commit()
        return trasaccion 
    
    def actualizarPaso_recetaBd(id,paso,orden):
        '''Actualiza una ingrediente de una receta
           unidad y cantidad
        ''' 
        trasaccion = False
        with conexion.conectar()as conn:
            with conexion.getCursor() as cr:
                consulta = '''UPDATE preparacion SET 
                     descripcion = %s,
                     orden = %s
                     WHERE id_preparacion = %s
                  '''
                cr.execute(consulta,(paso,orden,id,))
                trasaccion = True
            conn.commit()
        return trasaccion 

    def create_if_not_exists():
        """Crea la base de datos y la tabla si no existen.
        
        Esto asegura que la aplicacion funcione aunque no
        exista la base de datos previamente.
        Si es necesario que exista el usuario (con sus respectivos permisos)
        en el servidor.
        """
        create_database = "CREATE DATABASE IF NOT EXISTS %s" %credenciales["database"]
        create_table_receta = """CREATE TABLE IF NOT EXISTS recetas(
                                    id_receta INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
                                    nombre VARCHAR(60),
                                    t_preparacion SMALLINT,
                                    t_coccion SMALLINT,
                                    creacion DATE,
                                    etiqueta VARCHAR(60),
                                    favorito BOOLEAN DEFAULT FALSE
                                )ENGINE = InnoDB;"""
        create_table_ingredientes = """CREATE TABLE IF NOT EXISTS ingredientes(
                                        id_ing INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
                                        nombre VARCHAR(60)
                                    )ENGINE = InnoDB;"""
        create_table_receta_ingrediente = """CREATE TABLE IF NOT EXISTS receta_ingrediente(
                                                id_rxi INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
                                                receta_id INT,
                                                ing_id INT,
                                                unidad VARCHAR(30),
                                                cantidad VARCHAR(30),
                                                CONSTRAINT fk_receta FOREIGN KEY(receta_id) REFERENCES recetas(id_receta) ON DELETE CASCADE,
                                                CONSTRAINT fk_ingrediente FOREIGN KEY(ing_id) REFERENCES ingredientes(id_ing)
                                            )ENGINE = InnoDB;"""
        create_table_preparacion = """CREATE TABLE IF NOT EXISTS preparacion(
                                    id_preparacion INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
                                    descripcion VARCHAR(255),
                                    orden TINYINT,
                                    receta_id INT,
                                    CONSTRAINT fk_receta_p FOREIGN KEY (receta_id) REFERENCES recetas(id_receta) ON DELETE CASCADE
                                )ENGINE = InnoDB;"""
                           
        try:
            conn = mysql.connector.connect(user=credenciales["user"],
                                        password=credenciales["password"],
                                        host="127.0.0.1")
            cur = conn.cursor()
            cur.execute(create_database)
            cur.execute("USE %s" %credenciales["database"])
            cur.execute(create_table_receta)
            cur.execute(create_table_ingredientes)
            cur.execute(create_table_receta_ingrediente)
            cur.execute(create_table_preparacion)
            conn.commit()
            conn.close()
        except errors.DatabaseError as err:
            print("Error al conectar o crear la base de datos.", err)
            raise
    
if __name__ == "__main__":
    #recetas = Servicios.getRecetasdb()
    #print(recetas)
    '''receta = ("Asado",60,120,"Comida Regional")
    
    receta1 = Receta()
    receta1.nombre = receta[0]
    receta1.tiempoPreparacion = receta[1]
    receta1.tiempoCocion = receta[2]
    receta1.etiqueta = receta[3]
    
    print(Servicios.insertar(receta1.nombre))'''
    #print(Servicios.insertReceta("Alfajor",30,20,"Postre",False))
    #print(Servicios.insertIngrediente("Papa"))
    #print(Servicios.insertPaso("Pelar la papa",1,6))
    #print(Servicios.insertRI(6,1,"kg",1))
    '''print(Servicios.consultaRecetas())
    print(conexion._conn)
    print(conexion.conectar().is_connected())
    
    print(conexion.getCursor())
    print(Servicios.consultaRecetaIng(2))
    print(Servicios.consultaRecetaPas(2))
    
    print(Servicios.consultaReceta(1))'''
    
    #print(Servicios.cons_existe_Ing("mayonesa"))
    #insertado = Servicios.insertReceta("PRUEBA 2",10,20,"PRUEBA",True)
    #print(Servicios.consultaReceta(insertado))
    
    #print(Servicios.eliminarRecetaBd(22))
    
    
    #print(Servicios.actuaizarRecetaBd("Ensalada rusa",20,20,"Ensaladas",True,1))
    #print(Servicios.actualizarIng_recetaBd(1,"kg",2))
    # print(Servicios.actualizarPaso_recetaBd(1,"Cortar las verduras en cubos",1))
    print(Servicios.eliminarIngId(23))