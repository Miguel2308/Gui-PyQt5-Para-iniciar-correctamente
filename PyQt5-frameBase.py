#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 18:23:23 2021

@author: Miguel Miranda
"""

''' 
Iniciando en PyQt5, estas son algunas cuestiones basicas que se han ido
presentando en documentos encontrados en internet, convenciones, 
siempre intentando construir el codigo de la manera mas correcta posible
'''


'''Para no abrumar de entrada, estaremos creando la clase donde podremos ir agregando
los widgets o componente visuales que queramos en nuestra Gui, Una funcion main()
donde se instanciara todo lo necesario para que corra el codigo, y la comprobacion,
la cual solo ejecutara la funcion main() si es ejecutada desde si misma (convencion muy recomendable).
'''

'''Puede ser obvio para entendidos, pero ante el error "no module named PyQt5",
simplemente bajo el error, en la consola, hacemos "pip install PyQt5"
'''

from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

#Creo la clase, heredando de QMainWindow. Sera el marco base en el cual
#se iran agregando los widgets.
class BaseWindow(QMainWindow):
    def __init__(self,*args,**kwargs):                    # *args,**kwargs, permite una cantidad variable de argumentos.
        super(BaseWindow,self).__init__(*args,**kwargs)   # Indicamos que hereda las funciones de su clase padre.
        
        
        self.setWindowTitle('Interface Grafica De Prueba')#Titulo que aparece en la app (Nombre).
        self.setFixedSize(800,600)                        #Fija el tamaño con el que se inicia.
        
        # Aqui debajo iran todos los widgets que queramos agregar en el marco.
        
        
        
        
        
        
#Funcion principal, donde instanciar clases, y donde se produce la ejecucion del programa.
def main():
    app = QApplication([])
    window = BaseWindow()
    window.show()
    sys.exit(app.exec_())
    

# Comprobacion, suficiente con buscar breve definicion en google para comprender.
if __name__ == '__main__':
    main() # Le indicamos que ejecute nuestra fucion principal
    
    