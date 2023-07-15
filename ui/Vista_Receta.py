import tkinter as tk
from tkinter import font,ttk,messagebox
from Receta import Receta
class VistaReceta:
    '''crea una ventana que muestra una receta'''
    def __init__(self,parent,receta):
        self.parent = parent
        self.receta = receta
        self.ventana = tk.Toplevel(self.parent)
        self.ventana.title("Receta")
        
        self.ventana.width=335
        self.ventana.height=450
        self.screenwidth = self.ventana.winfo_screenwidth()
        self.screenheight = self.ventana.winfo_screenheight()
        self.alignstr = '%dx%d+%d+%d' % (self.ventana.width, self.ventana.height, (self.screenwidth - self.ventana.width) / 2, (self.screenheight - self.ventana.height) / 2)
        self.ventana.geometry(self.alignstr)
        self.ventana.resizable(False,False)
        
        self.nombre = self.receta.nombre.upper()
        #self.imagen = imagen
        self.tiempoPreparacion = self.receta.tiempoPreparacion
        self.tiempoCocion = self.receta.tiempoCocion
        self.ingredientes = self.receta.ingredientes
        self.lista_pasos = self.receta.lista_pasos
        self.creacion = self.receta.creacion
        self.etiqueta = self.receta.etiqueta
        self.favorito = self.receta.favorito
        self.crear_widget()
        self.agregar_contenido()
        
    def crear_widget(self):
        self.lbl_nombre = tk.Label(self.ventana,text=self.nombre,font = font.Font(family="Times",size=18),fg="DarkOrange4")
        self.lbl_nombre.grid(row=0,column=0,padx=5,pady=5)
        self.cuadro_texto = tk.Text(self.ventana,width=40,height=24)
        self.cuadro_texto.grid(row=1,column=0,padx=5,pady=5)
    
    def agregar_contenido(self):
        self.cuadro_texto.insert('end',"PREPARACION:\n")
        self.cuadro_texto.insert('end',self.tiempoPreparacion+" min."+"\n")
        self.cuadro_texto.insert('end',"COCCION:\n")
        self.cuadro_texto.insert('end',self.tiempoCocion+" min."+"\n")
        self.cuadro_texto.insert('end',"INGREDIENTES:\n")
        for ing in self.ingredientes:
            self.cuadro_texto.insert('end',f'{ing}\n')
        self.cuadro_texto.insert('end',"PASOS:\n")
        for p in self.lista_pasos:
            self.cuadro_texto.insert('end',f'{p}\n')
            
        self.cuadro_texto.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    receta1 = Receta("arroz con leche","10 min","60 min")
    v = VistaReceta(root,receta1)
    root.mainloop()