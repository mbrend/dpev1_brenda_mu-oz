from Continente import Continente

class Pais(Continente):

    codigoPais=0
    nombrePais=''

    def verDatos(self):
        print('\n---Datos del Pais---')
        print('Codigo del pais: ', self.codigoPais)
        print('Nombre del pais: ', self.nombrePais)

        super().verDatos()

