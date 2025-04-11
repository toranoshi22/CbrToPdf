# -*- coding: utf-8 -*-
import os
from pyunpack import Archive
from PIL import Image


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
            
            Archive(f"{RUTA_ARCHIVO}\{self.NOMBRE_FICHERO_DESCARGADO}").extractall(RUTA_DESCARGA)

  
    
    def createPDF(self,RUTA, imagenes ):
       pdfFileName = f"{self.RUTA_BASE}{RUTA}\{os.path.splitext(self.NOMBRE_FICHERO_DESCARGADO)[0]}.pdf"
       print(f"Creating PDF File: {pdfFileName} ")
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

                













