import json
from Receta import Receta
from Pasos import Pasos
from Ingrediente import Ingrediente
class RecetasCrud:
    '''interactua con el archivo json
        agrega, modifica, elimina y busca
        recetas en el archivo json
    '''
    def __init__(self,ruta):
        '''recibe la ruta del archivo e inicializa el mismo si este no exite'''
        self.ruta = ruta
        self.existe_archivo()

    def get_recetas(self):
        '''retorna una lista de diccionario con la informacion de la receta'''
        lista = []
        with open(self.ruta,"r") as archivo:
                lista = json.load(archivo)
        return lista
    
    def agregar_receta(self,receta):
        '''Recibe un parametro de tipo diccionario que contiene los datos de la receta'''
        recetas = []
        recetas = self.get_recetas()
        recetas.append(receta)
        with open(self.ruta,"w") as archivo:
            json.dump(recetas,archivo)
        
    def buscar_receta_nombre(self,nombre):
        '''
        Retorna la posicion de una receta dentro de una lista,
        a travez de su nombre pasado como parametro
        '''
        lista = self.get_recetas()
        pos = -1
        for i in range(0,len(lista)):
            if lista[i]["nombre"].lower() == nombre.lower():
                pos = i
                return pos
        return pos
    
    def buscar_receta_etiqueta(self,etiqueta):
        '''
        Retorna la posicion de una receta dentro de una lista,
        a travez de su etiqueta pasado como parametro
        '''
        lista = self.get_recetas()
        pos = -1
        for i in range(0,len(lista)):
            if lista[i]["etiqueta"].lower() == etiqueta.lower():
                pos = i
                return pos
        return pos
    
    def eliminar_receta(self,pos):
        '''elimina una receta del archivo json por posicion'''
        lista = self.get_recetas()
        del lista[pos]
        with open(self.ruta,"w") as archivo:
                json.dump(lista,archivo)
    
    def modificar_receta(self,pos,receta_dic):
        '''modifica una receta en el json'''
        lista = self.get_recetas()
        lista[pos] = receta_dic
        with open(self.ruta,"w") as archivo:
                json.dump(lista,archivo)
        '''receta["nombre"] = receta_dic["nombre"]
        receta["preparacion"] = receta_dic["preparacion"]
        receta["coccion"] = receta_dic["coccion"]
        receta["ingredientes"] = receta_dic["ingredientes"]
        receta["pasos"] = receta_dic["pasos"] 
        receta["etiqueta"] = self.etiqueta,
        "favorito": self.favorito '''
        
    def existe_archivo(self):
        '''verifica la existencia del archivo en caso contrario lo crea'''
        lista = []
        try:
            with open(self.ruta,"r") as archivo:
                lista = json.load(archivo)
        except:
            with open(self.ruta,"w") as archivo:
                json.dump(lista,archivo)

        
if __name__ == "__main__":
    crud = RecetasCrud("Recetario.json")
    '''receta1 = Receta("arroz con leche","10 min","60 min")

    ingrediente1 = Ingrediente("leche","Lt",1)
    ingrediente2 = Ingrediente("Arroz","gs",250)
    
    receta1.agregar_ingrediente(ingrediente1)
    receta1.agregar_ingrediente(ingrediente2)
    
    paso1 = Pasos(1,"Lavar el Arroz")
    paso2 = Pasos(2,"Poner la Leche a fuego lento 10 min")
    receta1.agregar_paso(paso1)
    receta1.agregar_paso(paso2)'''

    #receta1 = Receta("arroz con leche","10 min","60 min")
    #print(crud.buscar_receta_nombre("Arroz con leche"))
    #pos = crud.buscar_receta_nombre("Anchi")
    #print(pos)
    #crud.modificar_receta(pos,receta1.getDic())
    print(crud.get_recetas())
    
    
    
    #crud.eliminar_receta(pos)
    #crud.agregar_receta(receta1.getDic())
    #print(len(crud.recetas))
    #print(crud.recetas)
    #for receta in crud.recetas:
        #print(receta["nombre"])
