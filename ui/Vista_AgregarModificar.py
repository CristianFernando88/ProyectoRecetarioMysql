import tkinter as tk
from tkinter import ttk,messagebox
from Receta import Receta
from Ingrediente import Ingrediente
from Pasos import Pasos
from Recetario_Logica import RecetarioLogica as rl
from datetime import datetime as dt
from PIL import ImageTk, Image
from tkinter import filedialog
class Vista_Agregar:
    '''Crea una ventana para agregar o modificar una receta'''
    def __init__(self,parent,receta = None):
        self.parent = parent
        self.ventana = tk.Toplevel(self.parent)
        self.parent = parent
        self.ventana.width=675
        self.ventana.height=520
        self.screenwidth = self.ventana.winfo_screenwidth()
        self.screenheight = self.ventana.winfo_screenheight()
        self.alignstr = '%dx%d+%d+%d' % (self.ventana.width, self.ventana.height, (self.screenwidth - self.ventana.width) / 2, (self.screenheight - self.ventana.height) / 2)
        self.ventana.geometry(self.alignstr)
        
         #variables
        self.nombre = tk.StringVar()
        
        self.preparacion = tk.StringVar()
        self.coccion = tk.StringVar()
        self.etiqueta = tk.StringVar()
        self.favorito = tk.BooleanVar()
        self.fecha = tk.StringVar()
        self.crear_widgets()  
        self.bandera_modo = True
        if receta == None:
            self.ventana.title("Agregar Receta")  
            self.receta = Receta()
        else:
            self.ventana.title("Modificar Receta")  
            self.bandera_modo = False
            self.receta = receta
            self.btn_guardarAll.config(text="Modificar")
            self.cargar_receta_modificar()
            
        self.activar_control_paso(0)
        self.config_cajas_ingredientes(0)

        

    def crear_widgets(self):
         
        lbl_nombre = tk.Label(self.ventana,text="Nombre Receta")
        lbl_nombre.grid(row=0,column=0,padx=10,pady=5)
        input_nombre = tk.Entry(self.ventana,width=20,textvariable=self.nombre)
        input_nombre.grid(row=0,column=1,padx=5,pady=5)

        lbl_preparacion = tk.Label(self.ventana,text="Tiempo Preparacion (min): ")
        lbl_preparacion.grid(row=1,column=0,padx=10,pady=5)
        
        def validate_entry(text):
            return text.isdecimal()
        input_preparacion = tk.Entry(self.ventana,width=20,validate="key",validatecommand=(self.ventana.register(validate_entry),"%S"),textvariable=self.preparacion)
        input_preparacion.grid(row=1,column=1,padx=5,pady=5)

        lbl_cocccion = tk.Label(self.ventana,text="Tiempo Coccion (min): ")
        lbl_cocccion.grid(row=2,column=0,padx=10,pady=5)
        input_coccion = tk.Entry(self.ventana,width=20,validate="key",validatecommand=(self.ventana.register(validate_entry),"%S"),textvariable=self.coccion)
        input_coccion.grid(row=2,column=1,padx=5,pady=5)

        lbl_clave = tk.Label(self.ventana,text="Etiqueta: ")
        lbl_clave.grid(row=3,column=0,padx=10,pady=5)
        input_clave = tk.Entry(self.ventana,width=20,textvariable=self.etiqueta)
        input_clave.grid(row=3,column=1,padx=5,pady=5)
        
        chbtn_favorito = tk.Checkbutton(self.ventana,text="Es favorito",variable=self.favorito,command=lambda:print(self.favorito.get()))
        chbtn_favorito.grid(row=4,column=0,padx=5,pady=5)

        lbl_creacion = tk.Label(self.ventana,text="Fecha Creacion: ")
        lbl_creacion.grid(row=5,column=0,padx=10,pady=5)
        input_creacion = tk.Entry(self.ventana,width=20,textvariable=self.fecha,state="readonly")
        input_creacion.grid(row=5,column=1,padx=5,pady=5)

        #cuadro imagen
        frame_imagen = tk.LabelFrame(self.ventana,text="Foto")
        frame_imagen.grid(row=0,column=2,padx=5,pady=5,rowspan=5,columnspan=2)
        
        self.imagen = ImageTk.PhotoImage(Image.open("imagenes/agregar.png").resize((150,130)))
        
        label_imagen = tk.Label(frame_imagen,image = self.imagen)
        
        label_imagen.grid(row=0,column=0,columnspan=2)
        
        def abrirArchivo():
            archivo = filedialog.asksaveasfilename(title="Buscar Imagen",initialdir='imagenes',
            filetypes=(("Archivos jpg","*.jpg"),("Archivos png","*.png"),("Todos los archivos","*.*")))
            print(archivo)
            
        btn_agregar_img = tk.Button(self.ventana,text="Agregar",command=abrirArchivo)
        btn_agregar_img.grid(row=5,column=2,sticky=tk.E,padx=5)
        btn_quitar_img = tk.Button(self.ventana,text="Quitar",padx=5)
        btn_quitar_img.grid(row=5,column=3,sticky=tk.W)

        #cuadro ingredientes
        #variables ingredientes
        self.nom_ing = tk.StringVar()
        self.unidad = tk.StringVar()
        self.cant = tk.StringVar()
        self.estado_cajas_ingrediente = False
        
        def validate_entry_f(text):
            if text.isdecimal():
                return True
            return False

        frame_ingredientes = tk.LabelFrame(self.ventana,text="Ingredientes")
        frame_ingredientes.grid(row=6,column=0,columnspan=2,padx=5)
        
        lbl_non_ingr = tk.Label(frame_ingredientes,text="Nombre:")
        lbl_non_ingr.grid(row=0,column=0,padx=5,pady=5)
        self.entry_nom_ingr = tk.Entry(frame_ingredientes,textvariable=self.nom_ing,state=tk.DISABLED)
        self.entry_nom_ingr.grid(row=0,column=1,padx=5,pady=5)

        lbl_medida = tk.Label(frame_ingredientes,text="Unida de Medida:")
        lbl_medida.grid(row=1,column=0,padx=5,pady=5)
        
        valores_medida = ("","cc","lt","kg","grs.","unidades","docena","pizca")
        self.cbo_medida = ttk.Combobox(frame_ingredientes,values=valores_medida,textvariable=self.unidad,state=tk.DISABLED)
        self.cbo_medida.grid(row=1,column=1,pady=5)

        lbl_cantidad = tk.Label(frame_ingredientes,text="Cantidad:")
        lbl_cantidad.grid(row=2,column=0,padx=5,pady=5)
        self.entry_cantidad = tk.Entry(frame_ingredientes,textvariable=self.cant,validate="key",validatecommand=(self.ventana.register(validate_entry_f),"%S"),state=tk.DISABLED)
        self.entry_cantidad.grid(row=2,column=1,pady=5)
        
        self.list_ingredientes = tk.Listbox(frame_ingredientes,width=50)
        self.list_ingredientes.grid(row=4,column=0,columnspan=4,padx=5,pady=5,rowspan=4)
        self.btn_nuevo = tk.Button(frame_ingredientes,text="Nuevo",command=lambda:self.config_cajas_ingredientes(1))
        self.btn_nuevo.grid(row=0,column=3,sticky=tk.EW,padx=5)
        self.btn_guardar = tk.Button(frame_ingredientes,text="Guardar",command=self.guardar_ingrediente)
        self.btn_guardar.grid(row=1,column=3,sticky=tk.EW,padx=5)
        self.btn_quitar = tk.Button(frame_ingredientes,text="Quitar",command=self.eliminar_ingrediente)
        self.btn_quitar.grid(row=2,column=3,sticky=tk.EW,padx=5)

        
        
        #cuadro preparacion
        #variables preparacion
        
        self.paso = tk.StringVar()
        
        frame_preparacion = tk.LabelFrame(self.ventana,text="Preparacion")
        frame_preparacion.grid(row=6,column=2,columnspan=2,padx=5,sticky=tk.N)

        self.lbl_orden = tk.Label(frame_preparacion,text="Agregue de manera ordenada los pasos a seguir.",bg="grey",fg="cyan")
        self.lbl_orden.grid(row=0,column=0,columnspan=3,padx=5,pady=5)
        
        self.control_paso = False
        
        self.lbl_paso = tk.Label(frame_preparacion,text="Instruccion")
        self.lbl_paso.grid(row=1,column=0,padx=5,pady=5)
        self.entry_paso = tk.Entry(frame_preparacion,width=40,textvariable=self.paso,state=tk.DISABLED)
        self.entry_paso.grid(row=1,column=1,padx=5,pady=5,columnspan=2)

        self.btn_nuevo_paso = tk.Button(frame_preparacion,text="Nuevo",command=self.nuevo_paso)
        self.btn_nuevo_paso.grid(row=2,column=0,padx=5,sticky=tk.EW)
        self.btn_guardar_paso = tk.Button(frame_preparacion,text="Guardar",command=self.agregar_pasos,state=tk.DISABLED)
        self.btn_guardar_paso.grid(row=2,column=1,padx=5,sticky=tk.EW)
        self.btn_eliminar_paso = tk.Button(frame_preparacion,text="Quitar",command=self.eliminar_paso,state=tk.DISABLED)
        self.btn_eliminar_paso.grid(row=2,column=2,padx=5,sticky=tk.EW)

        self.list_pasos = tk.Listbox(frame_preparacion,width=50)
        self.list_pasos.grid(row=3,column=0,columnspan=3,padx=5,pady=5)

        self.btn_guardarAll = tk.Button(self.ventana,text="Guardar",command=self.guardar_general)
        self.btn_guardarAll.grid(row=7,column=1,sticky=tk.EW)
    
    def cargar_receta_modificar(self):
        self.nombre.set(self.receta.nombre)
        self.preparacion.set(self.receta.tiempoPreparacion)
        self.coccion.set(self.receta.tiempoCocion)
        self.etiqueta.set(self.receta.etiqueta)
        self.fecha.set(self.receta.creacion)
        self.favorito.set(self.receta.favorito)
        for ing in self.receta.ingredientes:
            #cadena = f'{ing.nombre}'
            self.list_ingredientes.insert(tk.END,ing)
        for p in self.receta.lista_pasos:
            #cadena = f'{ing.nombre}'
            self.list_pasos.insert(tk.END,p)
    #boton guardar todo
    def validar_cajas_gral(self):
        if self.nombre.get() != "" and self.preparacion.get()!="" and self.coccion.get()!="":
            return True
        else:
            return False
        
    def guardar_general(self):
        archivo_receta = rl("Recetario.json")
        if self.validar_cajas_gral():
            #print(self.receta.getDic())
            if self.bandera_modo:
                self.receta.nombre = self.nombre.get()
                self.receta.tiempoPreparacion = self.preparacion.get()
                self.receta.tiempoCocion = self.coccion.get()
                self.receta.etiqueta = self.etiqueta.get()
                self.receta.favorito = self.favorito.get()
                self.receta.creacion = dt.now()
                if archivo_receta.agregarReceta(self.receta):
                    messagebox.showinfo("Agregar Receta","La receta se ha guardado con exito!")
                    self.ventana.destroy()
                else:
                    messagebox.showwarning("Agregar Receta","Error al gurdar la receta")
            else:
                res = messagebox.askyesno(title="Confirmar",message="¿Esta seguro que desea guardar los cambios?")
                if res:
                    pos = archivo_receta.buscarRecetaNombre(self.receta.nombre)
                    self.receta.nombre = self.nombre.get()
                    self.receta.tiempoPreparacion = self.preparacion.get()
                    self.receta.tiempoCocion = self.coccion.get()
                    self.receta.etiqueta = self.etiqueta.get()
                    self.receta.favorito = self.favorito.get()
                    archivo_receta.modificaReceta(self.receta,pos)
                    messagebox.showinfo("Modificar","Cambios guardados exitosamente!")
                    self.ventana.destroy()
        else:
            messagebox.showwarning("Agregar Producto","Las cajas principales estan vacias")

    #funciones para caja de ingredientes
    def guardar_ingrediente(self):
        if self.nom_ing.get()!=0 and self.unidad.get!="" and self.cant.get()!="":
            ingrediente = Ingrediente(self.nom_ing.get(),self.unidad.get(),self.cant.get())
            self.limpar_ingrediente()
            
            self.list_ingredientes.insert(tk.END,ingrediente)
            self.receta.agregar_ingrediente(ingrediente)
            self.config_cajas_ingredientes(0)
        else:
            messagebox.showwarning("Receta ingrediente","Verifique que ningun campo este vacio")
    
    def eliminar_ingrediente(self):
        try:
            indice = self.list_ingredientes.curselection()[0]
            print(indice)
            ing = self.receta.ingredientes[indice]
            self.receta.eliminar_ingrediente(ing)
            self.list_ingredientes.delete(indice)
        except:
            messagebox.showwarning("Ingredientes","Debe seleccionar un elemento de la lista")
        

    def limpar_ingrediente(self):
        self.nom_ing.set("")
        self.unidad.set("")
        self.cant.set("")

    def config_cajas_ingredientes(self,op):
        #print(self.entry_nom_ingr.configure["state"])
        if op==0:
            self.entry_nom_ingr.configure(state=tk.DISABLED)
            self.cbo_medida.configure(state=tk.DISABLED)
            self.entry_cantidad.configure(state=tk.DISABLED)
            self.btn_nuevo.configure(state=tk.NORMAL)
            self.btn_guardar.configure(state=tk.DISABLED)
            if self.list_ingredientes.size()>0:
                self.btn_quitar.config(state=tk.NORMAL)
            else:
                self.btn_quitar.config(state=tk.DISABLED)
        elif op==1: 
            self.entry_nom_ingr.configure(state=tk.NORMAL)
            self.cbo_medida.configure(state=tk.NORMAL)
            self.entry_cantidad.configure(state=tk.NORMAL)
            self.btn_guardar.configure(state=tk.NORMAL)
            self.btn_nuevo.config(state=tk.DISABLED)
        elif op==2:
            if self.list_ingredientes.size()>0:
                self.btn_quitar.config(state=tk.NORMAL)
            else:
                self.btn_quitar.config(state=tk.DISABLED)

    #funciones para cajas de pasos
    def nuevo_paso(self):
        self.activar_control_paso(1)
        #self.btn_nuevo_paso.config(state=tk.DISABLED)
    
    def agregar_pasos(self):
        #paso = Pasos(self.orden.get(),self.paso.get())
        orden = len(self.receta.lista_pasos)+1
        paso = Pasos(orden,self.paso.get())
        self.receta.agregar_paso(paso)
        self.list_pasos.insert(tk.END,paso)
        self.paso.set("")
        self.activar_control_paso(0)

    def eliminar_paso(self):
        try:  
            indice = self.list_pasos.curselection()[0]
            #print(indice)
            paso = self.receta.lista_pasos[indice]
            #print(paso)
            self.receta.eliminar_paso(paso)
            #print(self.receta.diccionario_pasos())
            self.list_pasos.delete(0,tk.END)
            for p in self.receta.lista_pasos:
                self.list_pasos.insert(tk.END,p)
            self.activar_control_paso(2)
        except:
            messagebox.showwarning("Pasos","Debe seleccionar un elemento de la lista")
        
    
    def activar_control_paso(self,op):
        if op==0:
            self.entry_paso.config(state=tk.DISABLED)
            #self.btn_eliminar_paso.config(state=tk.DISABLED)
            self.btn_guardar_paso.config(state=tk.DISABLED)
            self.btn_nuevo_paso.config(state=tk.NORMAL)
            if self.list_pasos.size()>0:
                self.btn_eliminar_paso.config(state=tk.NORMAL)
            else:
                self.btn_eliminar_paso.config(state=tk.DISABLED)
                    
        elif op==1:
            self.entry_paso.config(state=tk.NORMAL)
            #self.btn_eliminar_paso.config(state=tk.NORMAL)
            self.btn_guardar_paso.config(state=tk.NORMAL)
            self.btn_nuevo_paso.config(state=tk.DISABLED)
        elif op==2:
            if self.list_pasos.size()>0:
                self.btn_eliminar_paso.config(state=tk.NORMAL)
            else:
                self.btn_eliminar_paso.config(state=tk.DISABLED)
            
                
               

    
        

if __name__ == "__main__":
    root = tk.Tk()
    ventana = Vista_Agregar(root)
    root.mainloop()
    