from time import sleep
class Seleccion():
    def __init__(self):
        try:
            self.doc.SelectionSets.Item("Grupo 1").Delete()
        except:
            print("No existe el Grupo 1, creando Grupo 1")
        self.grupo = self.doc.SelectionSets.Add("Grupo 1")
        self.grupo.SelectOnScreen()
        sleep(0.2)
        
        