import threading
import time

event = threading.Event()

def corredor(id_sensor):
    print(f"Corredor {id_sensor} en posicion, esperando la señal de salida...")
    #Wait para hacer la salida de la carrera
    event.wait()
    print(f"Corredor {id_sensor} he llegado a la meta.")

def iniciar_carrera():
    #Iniciamos la carrera
    print("Señal de salida en 2 segundos...")
    time.sleep(2)
    event.set()
    print("¡Salida! Los corredores han comenzado")

corredores = []
for i in range(4):
    t = threading.Thread(target=corredor, args=(i,))
    corredores.append(t)
    t.start()

carrera = threading.Thread(target=iniciar_carrera)
carrera.start()

for t in corredores:
    t.join()
carrera.join()