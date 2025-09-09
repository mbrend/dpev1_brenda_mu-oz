from Pais import Pais

class Empresa(Pais):

    codigoEmpresa=0
    nombreEmpresa=''
    telefonoEmpresa=0

    def verDatos(self):
        print('\n---Datos de la empresa---')
        print('Codigo de la empresa: ', self.codigoEmpresa)
        print('Nombre de la empresa: ', self.nombreEmpresa)
        print('Telefono de la empresa: ', self.telefonoEmpresa)

        super().verDatos()


