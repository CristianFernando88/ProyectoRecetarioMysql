import random
from mysql.connector import errors
from clases.Receta import Receta
from clases.Ingrediente import Ingrediente
from clases.Pasos import Pasos
from ServiciosRecetario import Servicios as servicios
class Logica:
    def getRecetas():
        '''Recupera todas las recetas en la bd'''
        recetas = []
        recetasbd = servicios.consultaRecetas()
        for r in  recetasbd:
            receta = Receta()
            receta.id,receta.nombre,receta.tiempoPreparacion,receta.tiempoCocion,receta.creacion,receta.etiqueta,receta.favorito= r
            ingredientesbd = servicios.consultaRecetaIng(receta.id)
            receta.ingredientes = []
            for id,nombre,unidad,cantidad in ingredientesbd:
                ingrediente = Ingrediente(nombre,unidad,cantidad,id)
                #receta.ingredientes.append(ingrediente)
                receta.agregar_ingrediente(ingrediente)
            
            pasos = servicios.consultaRecetaPas(receta.id)
            receta.lista_pasos = []
            for idPaso,orden,paso in pasos:
                paso = Pasos(orden,paso,idPaso)
                receta.agregar_paso(paso)
            
            recetas.append(receta)
            
        return recetas
    
    def getReceta(idReceta):
        '''Recupera una receta a traves de su id'''
        receta = None
        receta_consulta= servicios.consultaReceta(idReceta)[0]
        if receta_consulta != ():
            receta = Receta()
            receta.id,receta.nombre,receta.tiempoPreparacion,receta.tiempoCocion,receta.creacion,receta.etiqueta,receta.favorito= receta_consulta
            ing_consulta = servicios.consultaRecetaIng(receta.id)
            if len(ing_consulta) > 0:
                receta.ingredientes = []
                for id,nombre,unidad,cantidad in ing_consulta:
                    ingrediente = Ingrediente(nombre,unidad,cantidad,id)
                    #receta.ingredientes.append(ingrediente)
                    receta.agregar_ingrediente(ingrediente)
            pas_consulta = servicios.consultaRecetaPas(receta.id)
            if len(pas_consulta) > 0:
                receta.lista_pasos = []
                for idPaso,orden,paso in pas_consulta:
                    paso = Pasos(orden,paso,idPaso)
                    receta.agregar_paso(paso)               
        return receta
    
    def get_ing(idReceta):
        '''retorna los ingredientes de una receta'''
        ing_consulta = servicios.consultaRecetaIng(idReceta)
        if len(ing_consulta) > 0:
            ingredientes = []
            for id,nombre,unidad,cantidad in ing_consulta:
                ingrediente = Ingrediente(nombre,unidad,cantidad,id)
                #receta.ingredientes.append(ingrediente)
                ingredientes.append(ingrediente)
        return ingredientes
         
    def get_aleatorio():
        lista = servicios.consultaRecetas()
        aleatorio = random.choice(lista)
        receta = Logica.getReceta(aleatorio[0])
        return receta
    
    def guardarReceta(receta):
        try:
            insertado = servicios.insertReceta(receta.nombre,receta.tiempoPreparacion,receta.tiempoCocion,receta.etiqueta,receta.favorito)
            for ing in receta.ingredientes:
                pos_exist = servicios.cons_existe_Ing(ing.nombre)
                if pos_exist is None:
                    servicios.insertIngrediente(ing.nombre)
                    pos_exist = servicios.cons_existe_Ing(ing.nombre)
                servicios.insertRI(insertado,pos_exist,ing.unidad_medida,ing.cantidad)
            for paso in receta.lista_pasos:
                servicios.insertPaso(paso.instruccion,paso.orden,insertado)
            return True
        except errors.DatabaseError as e:
            return False
    
    def guardar_ingredientes(ingredientes,receta_id):
        '''guarda una lista de ingredientes de una receta'''
        for ing in ingredientes:
            pos_exist = servicios.cons_existe_Ing(ing.nombre)
            if pos_exist is None:
                servicios.insertIngrediente(ing.nombre)
                pos_exist = servicios.cons_existe_Ing(ing.nombre)
            servicios.insertRI(receta_id,pos_exist,ing.unidad_medida,ing.cantidad)
     
    def actulizarReceta(receta):
        try:
            servicios.actualizarRecetaBd(receta.nombre,receta.tiempoPreparacion,receta.tiempoCocion,receta.etiqueta,receta.favorito,receta.id)
            servicios.eliminarIngRecteaId(receta.id)
            for ing in receta.ingredientes:
                if ing.id != None:
                    id_ing = servicios.cons_existe_Ing(ing.nombre)
                    servicios.insertRI2(ing.id,receta.id,id_ing,ing.unidad_medida,ing.cantidad)
                else:
                    id_ing = servicios.cons_existe_Ing(ing.nombre)
                    if id_ing == None:
                        servicios.insertIngrediente(ing.nombre)
                    servicios.insertRI(receta.id,servicios.cons_existe_Ing(ing.nombre),ing.unidad_medida,ing.cantidad)
            
            servicios.eliminarPasosRecteaId(receta.id)
            for paso in receta.lista_pasos:
                if paso.id != None:
                    servicios.insertPaso2(paso.id,paso.instruccion,paso.orden,receta.id)
                else:
                    servicios.insertPaso(paso.instruccion,paso.orden,receta.id)
                
            '''ingredientesbd = Logica.get_ing(receta.id)
            ingredientes_agregar = filter(lambda i: i.id == None,receta.ingredientes)
            ings_con_id = filter(lambda i: i.id != None,receta.ingredientes)
            Logica.guardar_ingredientes(ingredientes_agregar,receta.id)
            lista_eliminar = []
            for ing_bd in ingredientesbd:
                encontrado = False
                for ing in ings_con_id:
                    if ing_bd.id == ing.id:
                        encontrado = True
                        break
                if encontrado:
                    lista_eliminar.append(ing_bd)
            for eliminado in lista_eliminar:
                servicios.eliminarIngId(eliminado.id)'''          
            
        except Exception as e:
            print(f"Ah aocurrido un error {e}")
            
    def eliminarReceta(id_receta):
        '''elimina una receta por su id'''
        servicios.eliminarRecetaBd(id_receta)
        
                
if __name__ == "__main__":
    '''for receta in Logica.getRecetas():
        print("Receta".center(50,"*"))
        print(receta)
        print("Lista Ingredeientes".center(50,"-"))
        for ing in receta.ingredientes:
            print(ing)
        print("Lista Pasos".center(50,"-"))
        for paso in receta.lista_pasos:
            print(paso)
    #print(servicios.consultaRecetaIng(2))  
    #print(Logica.getRecetas())'''
    '''print(Logica.getReceta(2))
    for i in Logica.getReceta(2).ingredientes:
        print(i)
    for p in Logica.getReceta(2).lista_pasos:
        print(p)'''
        
    print(Logica.get_aleatorio())
    