#Eje5_DEMBR

print('\n PROGRAMA 5: Puestos por Departamento (anidado) ')

departamentos = int(input("¿Cuantos departamentos hay?: "))

nombres_departamentos = []

for i in range(departamentos):
    nombre = input(f"Nombre del departamento # {i + 1}: ")
    nombres_departamentos.append(nombre)
    puestos =int (input(f"¿Cuantos puestos tiene {nombre}?: "))
    print(f'\n Puestos en {nombres_departamentos[i]}: ')
    print(puestos)