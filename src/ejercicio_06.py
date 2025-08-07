import random
import math

def coordenadas_en_circulo():
    puntos = tuple((random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(10))
    dentro = []

    for x, y in puntos:
        distancia = math.sqrt(x**2 + y**2)
        if distancia <= 5:
            dentro.append((x, y))

    print("Puntos generados:", puntos)
    print("Puntos dentro del círculo:", tuple(dentro))

coordenadas_en_circulo()
