import time

def count_primes_efficient(limit):
    primes = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if (primes[p] == True):
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    return sum(1 for p in range(2, limit + 1) if primes[p])

if __name__ == "__main__":
    LIMIT = 2000000 
    ITERATIONS = 50
    print(f"Calculando primos hasta {LIMIT} ({ITERATIONS} veces)...")
    start = time.time()
    
    for _ in range(ITERATIONS):
        result = count_primes_efficient(LIMIT)
        
    end = time.time()
    print(f"Encontrados {result} primos.")
    print(f"Tiempo total para {ITERATIONS} iteraciones: {end - start:.2f} segundos.")