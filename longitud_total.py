from inicializador import Inicializador
from grupo_seleccion import Seleccion
import numpy as np
import pandas as pd
from math import pi

class LongitudTotal(Inicializador, Seleccion):
    def __init__(self):
        Inicializador.__init__(self)
        Seleccion.__init__(self)
        self.longitudes = []
        
    def tipos(self) -> list:
        self.lineas = [
           "AcDbLine",
           "AcDbPolyline",
           "AcDbCircle",
           "AcDbEllipse",
           "AcDbArc"
           ]
        return self.lineas
    
    def longitud(self):
        for i in self.grupo: 
            if i.EntityName in self.lineas[0:2] :
                self.longitudes.append(i.Length)
            elif i.EntityName == self.lineas[2]:
                self.longitudes.append(i.Circumference)
            elif i.Entityname == self.lineas[3]:
                self.longitudes.append(i.MajorRadius*i.MinorRadius*pi)    
            elif i.EntityName == self.lineas[4]:
                self.longitudes.append(i.ArcLength)
            else:
                print("No se admite el tipo seleccionado")
            self.longitudes_np = np.array(self.longitudes)
            
    def expotar_excel(self, ruta):
        self.nombres = [f"Objeto{i+1}" for i in range(len(self.longitudes_np))]
        self.nombres_np = np.array(self.nombres)
        
        self.tabla = pd.DataFrame({"Nombre" : self.nombres_np,
                                   "Longitud" : self.longitudes_np})
        self.tabla.to_excel(ruta, index=False)

if __name__ == "__main__":
    objeto1 = LongitudTotal()
    objeto1.tipos()
    objeto1.longitud()
    """Colocar la ruta para el archivo, indicando el nombre de este
    con su extensión .xlsx"""
    objeto1.expotar_excel("Z:/Longitud_Total/prueba01.xlsx")
    
    

