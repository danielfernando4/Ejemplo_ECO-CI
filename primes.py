import time

def count_primes_inefficient(limit):
    count = 0
    for num in range(2, limit):
        is_prime = True
        for i in range(2, num): 
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count

if __name__ == "__main__":
    LIMIT = 100000 
    print(f"--- baseline: Calculando hasta {LIMIT} ---")
    start = time.time()
    result = count_primes_inefficient(LIMIT)
    end = time.time()
    print(f"Resultado: {result} primos encontrados en {end - start:.2f} segundos.")