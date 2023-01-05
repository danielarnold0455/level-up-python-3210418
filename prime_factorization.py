class PrimeFactors:
    def __init__(self, number):
        print(number)
        self.__number = number
        #self.__devisors = self.calc_divisors(number)
        self.__primefactors = self.calc_primefactors(number)

    @staticmethod
    def calc_divisors(number):
        divider = number
        primes = []
        while divider > 1:
            divider -= 1
            if not number % divider:
                primes.append(divider)
        return primes

    @staticmethod
    def calc_primefactors(number):
        divisor = 2
        factors = []
        while divisor <= number:
            if number % divisor: # Div mit Rest
                divisor += 1
            else: # div ohne rest
                print(f'found divisor: {divisor}')
                factors.append(divisor)
                number = number / divisor
        return factors

    def __str__(self):
        return f'{self.__number}: {self.__primefactors}'