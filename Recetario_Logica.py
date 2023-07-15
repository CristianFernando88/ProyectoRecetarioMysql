from Recetario_Servicios import RecetasCrud as rc
from Receta import Receta
from Pasos import Pasos
from Ingrediente import Ingrediente
import random
class RecetarioLogica:
    '''Interactuca con los objetos receta y el archivo json donde se guardaran los datos'''
    def __init__(self,ruta_archivo):
        self.ruta = ruta_archivo
        self.archivo = rc(ruta_archivo)
        
    
    def getRecetas(self):
        '''obtiene una lista de objetos recetas'''
        lista_diccionario = self.archivo.get_recetas()
        #print(lista_diccionario)
        lista = []
        for dic in lista_diccionario:
            #print(dic)
            receta = Receta(dic["nombre"],dic["preparacion"],dic["coccion"])
            #print(dic["ingredientes"])
            #print()
            aux_i = []
            aux_p = []
            for ing in dic["ingredientes"]:
                ingrediente = Ingrediente(ing["nombre"],ing["unidad"],ing["cantidad"])
                aux_i.append(ingrediente)
                #print(ingrediente)
                #receta.agregar_ingrediente(ingrediente)
            #print(len(aux_i))
            receta.ingredientes = aux_i
            for p in dic["pasos"]:
                paso = Pasos(p["orden"],p["instruccion"])
                #receta.agregar_paso(paso)
                aux_p.append(paso)
            receta.lista_pasos = aux_p
            receta.creacion = dic["creacion"]
            receta.etiqueta = dic["etiqueta"]
            receta.favorito = dic["favorito"]
            lista.append(receta)
        return lista
    
    def buscarRecetaNombre(self,nombre):
        '''retorna la posicion de un obj receta por nombre'''
        return self.archivo.buscar_receta_nombre(nombre)
    
    def buscarRecetaEtiqueta(self,etiqueta):
        '''retorna la posicion de un obj receta por nombre'''
        return self.archivo.buscar_receta_etiqueta(etiqueta)

    def agregarReceta(self,receta):
        '''agrega una receta al archivo'''
        if self.archivo.buscar_receta_nombre(receta.nombre) == -1:
            self.archivo.agregar_receta(receta.getDic())
            return True
        return False
    
    def getReceta(self,nombre):
        '''retorna una receta mediante el nombre'''
        recetas = self.getRecetas()
        pos = self.archivo.buscar_receta_nombre(nombre)
        if pos != -1:
            return recetas[pos]
        else:
            return None
        
    def modificaReceta(self,receta,pos):
        '''modifica una receta de una posicion dada'''
        self.archivo.modificar_receta(pos,receta.getDic())

    def eliminarReceta(self,pos):
        '''elimina una receta'''
        self.archivo.eliminar_receta(pos)

    def retorna_aleatorio(self):
        lista = self.getRecetas()
        return random.choice(lista)
        



if __name__ == "__main__":
    rl = RecetarioLogica("Recetario.json")
    receta = rl.getReceta("Arroz con leche")
    #print(rl.getRecetas())
    for r in rl.getRecetas():
        print(r.getDic())
        print()
    #print(receta)
    #print(receta.getDic())