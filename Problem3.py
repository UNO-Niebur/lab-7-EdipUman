#NumberTests.py
#Name: Edip Uman
#Date: 3/12/26
#Assignment: Lab 7
#Problem  : The prime factors of 13195 are 13 and 29.
#What is the largest prime factor of the number 600851475143?

from NumberTests import isPrime
from NumberTests import getFactors

def main():
    number= 600851475143
    factors = getFactors(number)
    print(factors)

    for f in factors:
       if isPrime(f):
          print(f)
         
if __name__ == '__main__':
  main()
