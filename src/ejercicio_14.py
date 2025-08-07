def sistema_votacion():
    votos = set()

    while True:
        voto = input("Ingresa el nombre del candidato (o 'fin' para terminar): ").strip().lower()
        if voto == "fin":
            break
        votos.add(voto)

    if votos:
        print("\nCandidatos que recibieron votos:")
        for candidato in votos:
            print("-", candidato.capitalize())
    else:
        print("No se registraron votos.")

sistema_votacion()
