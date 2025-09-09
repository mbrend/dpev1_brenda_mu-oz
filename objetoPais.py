from Pais import Pais

pais = Pais()

#datos del continente
pais.codigoContinente = int(input('Ingrese el codigo del continente: '))
pais.nombreContinente = input('Ingrese el nombre del continente: ')

#datos del pais
pais.codigoPais = int(input('Ingrese el codigo del pais: '))
pais.nombrePais = input('Ingrese el nombre del pais: ')

pais.verDatos()


