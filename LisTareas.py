#Eje2_DEMBR

print('\n  Programa 2: Registro de Tareas ')

cantidad = int(input("¿Cuantas tareas deseas ingresar?: "))

tareas = []

for i in range(cantidad):
    tarea =input(f"Ingrese la tarea #{i + 1}: ")
    tareas.append(tarea)

print('\nTareas resgistradas: ')

for i in range(len(tareas)):
    print(f'Tareas {i + 1}: {tareas[i]}')