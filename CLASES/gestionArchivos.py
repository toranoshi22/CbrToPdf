# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:00:27 2019

pip install pyunpack
pip install patool

@author: Francisco Rodriguez Alfaro
@email: info@datamanagement.es
"""
import os
from pyunpack import Archive
from PIL import Image
import patoolib

class GestionArchivos():
    
    RUTA_ENTRADA = None
    RUTA_SALIDA_CSV = None
    RUTA_FICHEROS_PROCESADOS = None
    RUTA_BASE = ""
            
    
            
    def __init__( self):
        print("GestionarArchivos creado")
        self.RUTA_BASE = os.getcwd() 
        print(self.RUTA_BASE)
        
    def log(func):
        def trace(self, RUTA_CBR, RUTA_PDF):
            RUTA_CBR = self.RUTA_BASE + RUTA_CBR
            RUTA_PDF = self.RUTA_BASE + RUTA_PDF
            print (f"CBR File : {RUTA_CBR},", end="")
            print (f"PDF File : {RUTA_PDF},", end="")
            return func(self, RUTA_CBR, RUTA_PDF)
        return trace
    
    
      
    def listFiles( self, RUTA, extension, fullPath = True ):
        imagenes = list()
        RUTA =  self.RUTA_BASE + RUTA
        for root, dirs, files in os.walk( RUTA ):
            for file in files:
                if file.upper().endswith(extension.upper()):
                    if "__MACOSX" not in root :
                        if fullPath:    
                            if not root.endswith("/"):
                                root+= "/"
                            imagenes.append(root + file)
                        else:
                            imagenes.append(file)  
                    
        return imagenes
              

    def crear_ruta_salida_si_no_existe(self, RUTA):
        if ( not os.path.exists( RUTA ) ):
            os.makedirs( RUTA )


    def getCBRFileName(self, RUTA):
        RUTA =  self.RUTA_BASE + RUTA
        for root, dirs, files in os.walk( RUTA ):
            for file in files:
                if file.endswith(".cbr") | file.endswith(".CBR"):
                    self.NOMBRE_FICHERO_DESCARGADO = file


    def setCBRFileName(self, file):
        self.NOMBRE_FICHERO_DESCARGADO = file
        

    def unRarFileDownload(self, RUTA_ARCHIVO, RUTA_DESCARGA ):
            RUTA_ARCHIVO =  self.RUTA_BASE + RUTA_ARCHIVO
            RUTA_DESCARGA =  self.RUTA_BASE + RUTA_DESCARGA
            self.crear_ruta_salida_si_no_existe(RUTA_DESCARGA)
            
            Archive(RUTA_ARCHIVO + self.NOMBRE_FICHERO_DESCARGADO ).extractall( RUTA_DESCARGA )

    """
    def unRarFileDownload(self, RUTA_DOWNLOAD, RUTA_DESCARGA ):
        RUTA_DOWNLOAD =  self.RUTA_BASE + RUTA_DOWNLOAD
        RUTA_DESCARGA =  self.RUTA_BASE + RUTA_DESCARGA
        self.crear_ruta_salida_si_no_existe(RUTA_DESCARGA)
        
        Archive( RUTA_DOWNLOAD + self.NOMBRE_FICHERO_DESCARGADO ).extractall( RUTA_DESCARGA )
    """    
    
    def createPDF(self,RUTA, imagenes ):
       pdfFileName = self.RUTA_BASE + RUTA + os.path.splitext(self.NOMBRE_FICHERO_DESCARGADO)[0] + ".pdf"
       print(f"Pdf File Name: {pdfFileName} ")
       pil_images = []
       try:
        for image in imagenes:
            pil_images.append(Image.open(image))
            
            
        convert_pil_images = []

        for pil_image in pil_images:
            convert_pil_images.append(pil_image.convert('RGB'))
            

        image_list = convert_pil_images[1:] 

        convert_pil_images[0].save(pdfFileName, save_all = True, append_images = image_list)


        for image in imagenes:
            os.remove(image)

       except Exception as e:
        print('Error: {0}\nException message: {1}'.format(type(e).__name__, e))

"""
URL_PEDIDOS_DOWNLOAD = "http://datamanagement.es/Recursos/pedidos.rar"
RUTA_DOWNLOAD = "C:/Users/Fran/Desktop/datamanagement/Python/EJEMPLO/DOWNLOAD/"
RUTA_DESCARGA = "C:/Users/Fran/Desktop/datamanagement/Python/EJEMPLO/DATASOURCE/"
gestionArchivos = GestionArchivos()
gestionArchivos.downloadPedidosRarURL( URL_PEDIDOS_DOWNLOAD, RUTA_DOWNLOAD )
gestionArchivos.unRarFileDownload( RUTA_DOWNLOAD, RUTA_DESCARGA )

"""
                
"""   
Probar que el método devuelve una lista de ficheros 
gestionArchivos = GestionArchivos()
lista = gestionArchivos.getFilesXMLFromOrigin( "C:/Users/Fran/Desktop/datamanagement/Python/EJEMPLO/DATASOURCE/" )
    


"""












