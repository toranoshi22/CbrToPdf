"""
Created on Mon Oct  7 15:19:15 2019

@author: Francisco Rodriguez Alfaro
@email: info@datamanagement.es
"""

from CLASES.gestionArchivos import GestionArchivos
import json
import patoolib

"""
- Iniciar el proceso de parsear la lista de ficheros XML que se encuentra en la lista: ficheros_xml
- Se conecta a la BBDD y va insertando en la tabla de logs todo lo que va sucendiendoy calculando tiempos etc...
"""
#DEFINIR EL ENTORNO PARA QUE COJA LOS VALORES QUE SE ENCUENTRAN EN EL config.json
ENTORNO = "PRODUCCION"      #PRODUCCION | DESARROLLO | TOR | LOCAL



    

# Obtener las variables de acceso
with open('./config.json', 'r') as file:
    config = json.load(file)


gestionArchivos = GestionArchivos()

""" lista de Archivos cbr"""
comics = gestionArchivos.listFiles( RUTA = config[ENTORNO]['RUTA_CBR'], extension=".cbr", fullPath = False  )

print(comics)


for comic in comics:
    print (f"Comic: {comic}")
    
    gestionArchivos.setCBRFileName(comic)

    gestionArchivos.unRarFileDownload(RUTA_ARCHIVO = config[ENTORNO]['RUTA_CBR'], RUTA_DESCARGA = config[ENTORNO]['RUTA_JPG'] )
    
    #obtener una lista de todos los ficheros XML que hay dentro de la RUTA que se le envía por parámetro
    imagenes = gestionArchivos.listFiles( RUTA = config[ENTORNO]['RUTA_JPG'], extension=".jpg", fullPath= True)
    
    """print(imagenes)"""
    
    gestionArchivos.createPDF(RUTA = config[ENTORNO]['RUTA_PDF'], imagenes= imagenes)
    











































