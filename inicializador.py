from pyautocad import Autocad

class Inicializador():
    def __init__(self):
        try:    
            self.acad = Autocad()
            self.doc = self.acad.doc
            self.model = self.acad.model
            print("Autocad conectado")
        except:
            print("Autocad no se esta ejecutando correctamente")
