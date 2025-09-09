from Empresa import Empresa

class Representante(Empresa):
    codigoRepresentante=0
    nombreRepresentante=''
    

    def verDatos(self):
        print('\n---Datos del representante---')
        print('Codigo del representante: ', self.codigoRepresentante)
        print('Nombre del representante: ', self.nombreRepresentante)

        super().verDatos()