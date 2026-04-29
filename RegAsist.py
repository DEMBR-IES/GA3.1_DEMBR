#Eje1_DEMBR

print('\n  PROGRMA 1: Registro de Asistencia ')

total_empleados = int(input("ingrese el numero de empleados a registrar "))
contador = 0
asistentes = []

while contador < total_empleados:
    nombre = input(f"Ingrese el nombre del empleado #{contador +1}:")
    asistentes.append(nombre)

    print(f'{nombre} ha sido registrado ')

    contador += 1

print('\nListado completo: ')

for persona in asistentes:
    print('- ' + persona)
    