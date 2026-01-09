import time
import math
from mpmath import mp
import re
def pi(n, p=0):
 a = mp.mpf(1)
 b = 1 / mp.sqrt(2)
 t = mp.mpf(1) / 4
 p = mp.mpf(1)
 mp.dps = n
 for _ in range(n):
  an = (a+b) / 2
  b = mp.sqrt(a*b)
  t -= p * (a - an) ** 2
  a = an
  p *= 2
  result = (a+b)**2 / (4 * t)
  print("Result: " + str(result))
def e(n):
 e = mp.mpf(1)
 x = 1
 mp.dps = n
 for k in range(1,n):
  T = lambda: 1
  N = lambda k: mp.factorial(k)
  term1 = T() / N(k)
  e += term1
  x += 1
  print("Approximation: " + str(e))
print("Welcome to Pi-Power - Crunching hundreds of pi digits and others")
choice = input("Enter choice: ")
if choice == "e":
 n = int(input("Enter digits: "))
 e(n)
elif choice == "pi": 
 n = int(input("Enter digits to calculate: "))
 for i in range(n):
   pi(i)