def fibonacci_impares():
    fib = []
    a, b = 0, 1
    while len(fib) < 20:
        fib.append(a)
        a, b = b, a + b

    fib_tupla = tuple(fib)
    impares = [n for n in fib_tupla if n % 2 != 0]

    print("Fibonacci (20 primeros):", fib_tupla)
    print("Fibonacci impares:", tuple(impares))

fibonacci_impares()
