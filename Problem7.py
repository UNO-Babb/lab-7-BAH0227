from NumberTests import isPrime

def main():
  NumberCount = 0
  number = 1
  while NumberCount < 10001:
    number = number + 1
    if isPrime(number):
      NumberCount = NumberCount + 1
  
  print(number)

if __name__ == '__main__':
  main()
