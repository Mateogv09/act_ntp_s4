import math

def distancia_total(puntos):
    total = 0
    for i in range(1, len(puntos)):
        x1, y1 = puntos[i - 1]
        x2, y2 = puntos[i]
        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        total += distancia
    return total

puntos = ((0, 0), (3, 4), (6, 8), (6, 10))
print("Distancia total recorrida:", distancia_total(puntos))
