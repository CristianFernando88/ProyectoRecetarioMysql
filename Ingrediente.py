class Ingrediente:
    '''La clase representa un ingrediente
        que tiene como atributos nombre, medida y cantidad
    '''
    def __init__(self,nombre,unidadMedida,cantidad):
        '''Constructor recibe como parametro 
            los atributos de nombre unidad y cantidad
        '''
        self.nombre = nombre
        self.unidad_medida = unidadMedida
        self.cantidad = cantidad

    def getDic(self):
        '''Retorna un diccionario con los atributos de la instancia'''
        diccionario = {"nombre":self.nombre,"unidad":self.unidad_medida,"cantidad":self.cantidad}
        return diccionario
    def __str__(self):
        '''Retorna un string con informacion de la instancia'''
        return f"{self.nombre}, {self.cantidad} {self.unidad_medida}"
    

if __name__ == "__main__":
    mi_ingrediente = Ingrediente("Sal","gramos",5)
    print(mi_ingrediente.getDic())
    print(mi_ingrediente)
        