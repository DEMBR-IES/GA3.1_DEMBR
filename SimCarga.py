#Eje4_DEMBR

print('\n  PROGRMA 4: Simulador de Carga de Servidores ')

servidores = int(input("¿'Cuantos servidores deas simular?: "))

procesos = int(input("¿Cuantos procesos por servidor?: "))
for i in range(1, servidores + 1):
    print(f'\n Servidor #{i}: ')

    for j in range(1, procesos + 1):
        print(f' Cargando procesos {j}... ')