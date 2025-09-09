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


