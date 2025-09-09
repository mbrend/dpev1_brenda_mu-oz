# Parcial 1 - Brenda Muñoz 202108211
Información de los problemas resueltos.

<b>Continente</b>

''
class Continente:
    codigoContinente=0
    nombreContinente=''

    def verDatos(self):
        print('\n---Datos del Continente---')
        print('Código del continente: ', self.codigoContinente)
        print('Nombre del continente: ', self.nombreContinente)
-----
from Continente import Continente

continente = Continente()

continente.codigoContinente = int(input('Ingrese el código del continente: '))
continente.nombreContinente = input('Ingrese el nombre del contienente: ')

continente.verDatos()

<b>País</b>

''
from Continente import Continente

class Pais(Continente):

    codigoPais=0
    nombrePais=''

    def verDatos(self):
        print('\n---Datos del Pais---')
        print('Codigo del pais: ', self.codigoPais)
        print('Nombre del pais: ', self.nombrePais)

        super().verDatos()


from Pais import Pais

pais = Pais()

#datos del continente
pais.codigoContinente = int(input('Ingrese el codigo del continente: '))
pais.nombreContinente = input('Ingrese el nombre del continente: ')

#datos del pais
pais.codigoPais = int(input('Ingrese el codigo del pais: '))
pais.nombrePais = input('Ingrese el nombre del pais: ')

pais.verDatos()


--------

<b>Empresa</b>

''
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

from Empresa import Empresa

empresa = Empresa()

#datos de continente
empresa.codigoContinente = int(input('Ingrese el codigo del continente: '))
empresa.nombreContinente = input('Ingrese el nombre del continente: ')  

#datos del pais
empresa.codigoPais = int(input('Ingrese el codigo del pais: '))
empresa.nombrePais = input('Ingrese el nombre del pais: ')

#datos de la empresa
empresa.codigoEmpresa = int(input('Ingrese el codigo de la empresa: ')) 
empresa.nombreEmpresa = input('Ingrese el nombre de la empresa: ')
empresa.telefonoEmpresa = int(input('Ingrese el telefono de la empresa: ')) 

empresa.verDatos()

-------

<b>Representante</b>

''
from Empresa import Empresa

class Representante(Empresa):
    codigoRepresentante=0
    nombreRepresentante=''
    

    def verDatos(self):
        print('\n---Datos del representante---')
        print('Codigo del representante: ', self.codigoRepresentante)
        print('Nombre del representante: ', self.nombreRepresentante)

        super().verDatos()


from Representante import Representante

representantes = []

try:
    n= int(input('¿Cuántos representantes desea ingresar? '))
except ValueError:
    n= 1    

for i in range(n):
    print('\n--Registro #', i+1, '--')
    representante=Representante()

   #datos del continente
    representante.codigoContinente = int(input('Ingrese el codigo del continente: '))
    representante.nombreContinente = input('Ingrese el nombre del continente: ')

    #datos del pais
    representante.codigoPais = int(input('Ingrese el codigo del pais: '))
    representante.nombrePais = input('Ingrese el nombre del pais: ')

    #datos de la empresa
    representante.codigoEmpresa = int(input('Ingrese el codigo de la empresa: ')) 
    representante.nombreEmpresa = input('Ingrese el nombre de la empresa: ')
    representante.telefonoEmpresa = int(input('Ingrese el telefono de la empresa: ')) 

    #datos del representante
    representante.codigoRepresentante = int(input('Ingrese el codigo del representante: '))
    representante.nombreRepresentante = input('Ingrese el nombre del representante: ')

    representantes.append(representante)

print('\n--- Datos de los ',n, 'representantes ingresados ---')
for idx, x in enumerate(representantes, start=1):
    print('\nRegistro #',idx)
    x.verDatos()
    print('----------------------------------------')


------


