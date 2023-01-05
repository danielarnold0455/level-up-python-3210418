import prime_factorization
import random

def calc_prime(number):
    primes = prime_factorization.PrimeFactors(number)
    print(primes)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calc_prime(random.randint(2,1e6))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
