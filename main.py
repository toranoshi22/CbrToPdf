from CLASES.gestionArchivos import GestionArchivos



gestionArchivos = GestionArchivos()

""" lista de Archivos cbr"""
comics = gestionArchivos.listFiles( RUTA = "/cbr", extension=".cbr", fullPath = False  )

print(comics)


for comic in comics:
    print (f"Comic: {comic}")
    
    gestionArchivos.setCBRFileName(comic)

    gestionArchivos.unRarFileDownload(RUTA_ARCHIVO = "\cbr", RUTA_DESCARGA = "\jpg")
    
    #obtener una lista de todos los ficheros XML que hay dentro de la RUTA que se le envía por parámetro
    imagenes = gestionArchivos.listFiles( RUTA = "\jpg", extension=".jpg", fullPath= True)
    
    """print(imagenes)"""
    
    gestionArchivos.createPDF(RUTA = "\pdf", imagenes= imagenes)
    











































