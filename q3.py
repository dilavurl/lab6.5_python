def sieve_of_eratosthenes(num_list):

    primes = [True] * len(num_list)
    primes[0] = primes[1] = False

    for i in range(2, int(max(num_list) ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max(num_list) + 1, i):
                primes[j] = False

    return [num_list[i] for i in range(len(num_list)) if primes[i]]