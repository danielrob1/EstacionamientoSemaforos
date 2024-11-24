import random
import threading
import time

semaforo = threading.Semaphore(3)

def acceder_estacionamiento(id_vehiculo):
    semaforo.acquire()
    print("Vehículo " + str(id_vehiculo) + " ha entrado al estacionamiento")
    time.sleep(random.uniform(1,3))
    print("Vehículo " + str(id_vehiculo) + " ha salido del estacionamiento")
    semaforo.release()


hilos=[]
for i in range(10):
    hilo= threading.Thread(target=acceder_estacionamiento, args=(i,))
    hilos.append(hilo)
    hilo.start()


for hilo in hilos:
    hilo.join()

print("Todos los vehículos han pasado por el estacionamiento")
