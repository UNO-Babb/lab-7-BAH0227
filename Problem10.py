

from NumberTests import isPrime

def main():
  
    def SumOfPrimesbelow(maximum):
        sum_primes = 0
        for number in range(2, maximum):
            if isPrime(number):
                sum_primes = number + sum_primes
        return sum_primes
  
    maximum  = 2000000
    result = SumOfPrimesbelow(maximum)
    print(result)

if __name__ == '__main__':
  main()
