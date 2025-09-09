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
