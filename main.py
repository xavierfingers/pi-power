import time
import math
from mpmath import mp
import re
def pi(n, result=mp.mpf(0)):
 if n > 10:
  mp.dps = n
 else: 
  mp.dps = n
 end = 0
 a = mp.mpf(1)
 b = mp.mpf(1) / mp.sqrt(2)
 t = mp.mpf(1/4)
 p = mp.mpf(1)
 start = time.perf_counter() 
 for k in range(n):
  an = (a+b) / 2
  b = mp.sqrt(a*b)
  t -= p * (a - an) ** 2
  a = an
  p = 2 * p
  T = lambda a, b: (a+b)**2 
  N = lambda t: (4 * t)
 result = T(a, b) / N(t)
 end = time.perf_counter() - start
 print(end)
 print("---- Verification ------\n" + str(result))
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
 result = mp.mpf(0)
 pi(n)