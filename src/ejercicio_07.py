def filtrar_estudiantes(estudiantes):
    seleccionados = []

    for estudiante in estudiantes:
        nombre, edad, promedio = estudiante
        if promedio > 8.0:
            seleccionados.append(estudiante)
    
    return tuple(seleccionados)

estudiantes = (
    ("Ana", 20, 9.2),
    ("Luis", 22, 7.5),
    ("Carlos", 19, 8.5),
    ("Lucía", 21, 6.8),
)
print("Estudiantes con promedio > 8.0:", filtrar_estudiantes(estudiantes))
