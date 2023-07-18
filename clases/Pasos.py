class Pasos:
    '''La clase representa a un paso o instruccion de la preparacion de la receta'''
    def __init__(self,orden,instruccion):
        '''El constructor recibe como parametro el n° de orden del paso
            y la instruccion de lo que se debe hacer en el mismo
        '''
        self._orden = orden
        self._instruccion = instruccion

    #Getters y Setters
    @property
    def orden(self):
        return self._orden
    
    @orden.setter
    def orden(self,orden):
        self._orden = orden
    
    @property
    def instruccion(self):
        return self._instruccion
    
    @instruccion.setter
    def instruccion(self,instruccion):
        self._instruccion = instruccion

    def getDic(self):
        '''Retorna un diccioinariocon los atributos de la instancia'''
        diccionario = {"orden":self._orden, "instruccion": self._instruccion}
        return diccionario
    
    def __str__(self):
        '''Retorna un diccioinariocon los atributos de la instancia'''
        return f'Paso {self._orden}: {self._instruccion}'
    
if __name__ == "__main__":
    paso1 = Pasos(1,"Colocar Agua en una olla")
    print(paso1)
    print(paso1.getDic())