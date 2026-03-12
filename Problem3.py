#NumberTests.py
#Name: Edip Uman
#Date: 3/12/26
#Assignment: Lab 7
#Problem  : The prime factors of 13195 are 13 and 29.
#What is the largest prime factor of the number 600851475143?

def largestPrimeFactor(num):
  factor = 2

  while factor * factor <= num:
    if num % factor == 0:
      num = num // factor
    else:
      factor += 1

  return num


def main():
  number = 600851475143
  print(largestPrimeFactor(number))

if __name__ == '__main__':
  main()


