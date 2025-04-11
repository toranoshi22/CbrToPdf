from CLASES.gestionArchivos import GestionArchivos
import tkinter as tk

gestionArchivos = GestionArchivos()

#GUI
root = tk.Tk()
root.title("CBR to PDF Converter")
root.geometry('640x480+300+300')
root.resizable(True,True)
label = tk.Label(root, text="Hello World")
label.pack()
submit_btn = tk.Button(root, text="Convertir")
submit_btn.configure(command=gestionArchivos.start_converting)
submit_btn.pack()
root.mainloop()




    











































