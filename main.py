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
submit_btn.configure(command=gestionArchivos.on_submit)
submit_btn.pack()
root.mainloop()






for comic in comics:
    print (f"Comic: {comic}")
    
    gestionArchivos.setCBRFileName(comic)

    gestionArchivos.unRarFileDownload(RUTA_ARCHIVO = "\cbr", RUTA_DESCARGA = "\jpg")
    
    #obtener una lista de todos los ficheros XML que hay dentro de la RUTA que se le envía por parámetro
    imagenes = gestionArchivos.listFiles( RUTA = "\jpg", extension=".jpg", fullPath= True)
    
    """print(imagenes)"""
    
    gestionArchivos.createPDF(RUTA = "\pdf", imagenes= imagenes)
    











































