#NumberTests.py
#Name: Edip Uman
#Date: 3/12/26
#Assignment: Lab 7
#Problem  : 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# code skips all numbers that are not multiples of 20 to be more efficient


from NumberTests import Divisible1to20

def main():
  num = 20
  while True:
    if Divisible1to20(num):
      print("Smallest (+) number evenly divisible by all num 1-20 is,", num)
      return
    else: 
      num += 20

if __name__== "__main__":
  main()


