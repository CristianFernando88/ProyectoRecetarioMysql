import tkinter as tk
from ServiciosRecetario import Servicios
from ui.Vista_Recetario import Recetario
Servicios.create_if_not_exists()
root = tk.Tk()
recetario = Recetario(root)
root.mainloop()