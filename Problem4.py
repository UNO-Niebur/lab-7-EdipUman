#NumberTests.py
#Name: Edip Uman
#Date: 3/12/26
#Assignment: Lab 7
#Problem  : A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009=91x99.
#Find the largest palindrome made from the product of two 3-digit numbers.

from NumberTests import Palindrome

def main():
  maxPal = 0 
  xMax = zMax=0
  for x in range(100, 1000):
    for z in range(100, 1000):
      prod = x * z 
      if prod > maxPal and Palindrome(prod):
        maxPal =  prod
        xMax, zMax = x,z
  print(f"{maxPal} = largest Palindrome from two 3digit numbers; {xMax}, {zMax}")

if __name__ == '__main__':
    main()
  
