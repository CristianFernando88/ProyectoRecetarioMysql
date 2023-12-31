import tkinter as tk
from tkinter import ttk,messagebox
from .Vista_AgregarModificar import Vista_Agregar
from LogicaRecetario import Logica as log_recetario
from .Vista_Receta import VistaReceta as vr
import datetime as dt


class Recetario(ttk.Frame):
    '''crea la ventana principal de la aplicación'''
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.width=575
        self.parent.height=400
        self.screenwidth = self.winfo_screenwidth()
        self.screenheight = self.winfo_screenheight()
        self.alignstr = '%dx%d+%d+%d' % (self.parent.width, self.parent.height, (self.screenwidth - self.parent.width) / 2, (self.screenheight - self.parent.height) / 2)
        self.parent.geometry(self.alignstr)
        self.parent.title("RECETARIO")
        self.parent.iconbitmap('imagenes/icono.ico')
        self.crear_widgets()
        self.cargar_receta_dia()
        self.llenar_tabla_recetas()

    def crear_widgets(self):
        
        self.buscado = tk.StringVar()
       # self.fitlro = tk.StringVar()
        
        self.lbl_filtro = tk.Label(self.parent,text="Seleccione filtro: ")
        self.lbl_filtro.grid(row=1,column=0,pady=5,padx=5)
        
        self.cbo_filtro = ttk.Combobox(self.parent,state="readonly",values=("","Nombre","Etiqueta"),width=10)
        self.cbo_filtro.grid(row=1,column=1,pady=5,padx=5)
        
        self.entry_buscar = tk.Entry(self.parent,width=25,textvariable=self.buscado)
        self.entry_buscar.grid(row=1,column=2,pady=5,sticky=tk.EW,padx=10)

        self.btn_buscar = tk.Button(self.parent,text="Buscar Receta",command=self.busqueda_receta)
        self.btn_buscar.grid(row=1,column=3,sticky=tk.W)
        
        
        self.lbl_receta_dia = ttk.Label(self.parent,text="Receta del dia",foreground="red")
        self.lbl_receta_dia.grid(row=0,column=0,sticky=tk.EW,padx=10,pady=5)

        self.receta_dia = tk.StringVar()
        self.entry_receta_dia = tk.Entry(self.parent,width=25,textvariable=self.receta_dia)
        self.entry_receta_dia.grid(row=0,column=1,sticky=tk.EW,padx=10,pady=5)

        self.btn_receta_dia = tk.Button(self.parent,text="Ver",foreground="red",command=self.mostrar_receta_dia)
        self.btn_receta_dia.grid(row=0,column=2,sticky=tk.EW,padx=10,pady=5)

        self.frame_recetas = ttk.LabelFrame(self.parent,text="Recetas")
        self.frame_recetas.grid(row=2,column=0,columnspan=4)
        

        self.tabla_recetas = ttk.Treeview(self.frame_recetas,selectmode='browse',columns=tuple(['nombre', 'preparacion', 'coccion','etiqueta','id_r']))
        self.tabla_recetas.grid(row=1, column=0, columnspan=4,padx=10, pady=5)
        
        # asignamos tamño a las columnas
        self.tabla_recetas.column("#0", width=40, minwidth=10)
        self.tabla_recetas.column("nombre", width=200, minwidth=10)
        self.tabla_recetas.column("preparacion", width=100, minwidth=10)
        self.tabla_recetas.column("coccion", width=100, minwidth=10)
        self.tabla_recetas.column("etiqueta", width=100, minwidth=10)
        self.tabla_recetas.column("etiqueta", width=100, minwidth=10)
        self.tabla_recetas.column("id_r", width=0, minwidth=0)
        

        # colocamos nombres a la cabecera
        self.tabla_recetas.heading("#0", text="N°", anchor="center")
        self.tabla_recetas.heading("nombre", text="Nombre", anchor="center")
        self.tabla_recetas.heading("preparacion", text="Preparación", anchor="center")
        self.tabla_recetas.heading("coccion", text="Cocción", anchor="center")
        self.tabla_recetas.heading("etiqueta", text="Etiqueta", anchor="center")
        self.tabla_recetas.heading("id_r", text="Etiqueta", anchor="center")
        
        #botones crud
        self.btn_refrescar = tk.Button(self.frame_recetas,text="Refrescar tabla", command=self.llenar_tabla_recetas)
        self.btn_refrescar.grid(row=0,column=3)
        
        self.btn_mostrar = tk.Button(self.frame_recetas,text="Mostrar Receta",command=self.mostrar_receta)
        self.btn_mostrar.grid(row=2,column=0)

        self.btn_agregar = tk.Button(self.frame_recetas,text="Agregar Receta",command=self.agregar)
        self.btn_agregar.grid(row=2,column=1)

        self.btn_modificar = tk.Button(self.frame_recetas,text="Modificar Receta",command=self.modificar)
        self.btn_modificar.grid(row=2,column=2)

        self.btn_modificar = tk.Button(self.frame_recetas,text="Eliminar Receta",command=self.eliminar_receta)
        self.btn_modificar.grid(row=2,column=3)
    
    def cargar_receta_dia(self):
        '''Obtiene la receta del dia por medio de un
        metodo aleatorio y muestra en el entry de receta dia'''
        self.recetaAleatorio = log_recetario.get_aleatorio()
        if self.recetaAleatorio != None:
            self.receta_dia.set(self.recetaAleatorio.nombre)
            self.entry_receta_dia.config(state="readonly")

    def mostrar_receta_dia(self):
        '''muestra en un frame la receta del dia '''
        if self.recetaAleatorio != None:
            recetaDia = log_recetario.getReceta(self.recetaAleatorio.id)
            v_receta_dia = vr(self.parent,recetaDia)

    def llenar_tabla_recetas(self):
        self.tabla_recetas.delete(*self.tabla_recetas.get_children())
        self.buscado.set("")
        self.cbo_filtro.set("")
        num=0
        self.tabla_recetas.tag_configure('favorito', background='black', foreground='red')
        self.tabla_recetas.tag_configure('normal', background='white', foreground='red')
        if log_recetario.getRecetas() != []:
            #self.label_estado['text']=""
            
            for receta in log_recetario.getRecetas():
                num += 1
                valores = (receta.nombre,receta.tiempoPreparacion,receta.tiempoCocion,receta.etiqueta,receta.id) 
                my_tag='favorito' if num == 1 else 'normal' 
                self.tabla_recetas.insert("", tk.END, text=str(num),values=valores,tags = (my_tag))
                '''if num == 1:
                    self.tabla_recetas.insert("", tk.END, text=str(num),values=valores,tags = (''))
                else:
                    self.tabla_recetas.insert("", tk.END, text=str(num),values=valores)'''
                    
    
    def agregar(self):
        '''Abre una ventana top leve para agregar una receta'''
        ventana_agregar = Vista_Agregar(self.parent)
    
    def modificar(self):
        try:
            #nombre = self.tabla_recetas.item(self.tabla_recetas.selection())['values'][0]
            id_receta = self.tabla_recetas.item(self.tabla_recetas.selection())['values'][4]
            #print(id_receta)
            buscado = log_recetario.getReceta(id_receta)
            v_modificar = Vista_Agregar(self.parent,buscado)
        except Exception:
            messagebox.showwarning("Receta","Debe seleccionar una fila de la tabla")
         
    def mostrar_receta(self):
        try:
            #nombre = self.tabla_recetas.item(self.tabla_recetas.selection())['values'][0]
            id_receta = self.tabla_recetas.item(self.tabla_recetas.selection())['values'][4]
            buscado = log_recetario.getReceta(id_receta)
            v_mostrar = vr(self.parent,buscado)
            
        except Exception:
            messagebox.showwarning("Receta","Debe seleccionar una fila de la tabla")

    def eliminar_receta(self):
        try:
            
            id_receta = self.tabla_recetas.item(self.tabla_recetas.selection())['values'][4]
            res = messagebox.askyesno(title="Confirmar",message="¿Estas seguro que deseas eliminar este elemento del recetario?")
            if res:
                log_recetario.eliminarReceta(id_receta)
                self.llenar_tabla_recetas()

        except Exception:
            messagebox.showwarning("Receta","Debe seleccionar una fila de la tabla")

    def busqueda_receta(self):
        '''Realiza busqueda por nombre o etiqueta y refleja en la tabla el resultado'''
        num=0
        #print(lista_buscado)
        if self.cbo_filtro.get() == "Nombre":
            lista_buscado = list(filter(lambda r:  self.buscado.get().lower() in r.nombre.lower(),log_recetario.getRecetas()))
            if lista_buscado != []:
                self.tabla_recetas.delete(*self.tabla_recetas.get_children())
                for receta in lista_buscado:
                    num += 1
                    self.tabla_recetas.insert("", tk.END, text=str(num),values=(receta.nombre,receta.tiempoPreparacion,receta.tiempoCocion,receta.etiqueta,receta.id))
            else:
                messagebox.showinfo("Rcetario","No hay resultados para la busqueda.")
        elif self.cbo_filtro.get() == "Etiqueta":
            lista_buscado = list(filter(lambda r:  self.buscado.get().lower() in r.etiqueta.lower(),log_recetario.getRecetas()))
            if lista_buscado != []:
                self.tabla_recetas.delete(*self.tabla_recetas.get_children())
                for receta in lista_buscado:
                    num += 1
                    self.tabla_recetas.insert("", tk.END, text=str(num),values=(receta.nombre,receta.tiempoPreparacion,receta.tiempoCocion,receta.etiqueta,receta.id))
            else:
                messagebox.showinfo("Rcetario","No hay resultados para la busqueda.")
        else:
            messagebox.showinfo("Rcetario","Seleccione un filtro para buscar")
            
        
            


