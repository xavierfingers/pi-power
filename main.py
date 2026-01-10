import time
import numba
import math
from mpmath import mp, sqrt
def pi(n, result=mp.mpf(0)):
 end = 0
 mp.dps = n
 a = mp.mpf(1)
 b = mp.mpf(1)  / sqrt(2)
 t = mp.mpf(1)/4
 p = mp.mpf(1)
 start = time.perf_counter() 
 for k in range(n):
  an = (a+b) / 2
  b = sqrt(a*b)
  t -= p * (a - an) ** 2
  a = an
  p = 2 * p
  T = lambda a, b: (a+b)**2 
  N = lambda t: (4 * t)
  def bs(a, b,c,d):
     Bao = b
     Qao = a
     Qao1 = c
     Bao1 = d
     return (Bao + Qao)**2 / (Bao1 * Qao1) 
  result = bs(b,a,t,4)
  end = time.perf_counter() - start
  print("Pi: " + str(result))
def e(digits):
 e = mp.mpf(1)
 n = digits // 2 + 1
 mp.dps = digits
 for k in range(n):
  def bs(b):
   Qao = (2**b)
   Bao = mp.mpf(1)
   return Bao / Qao 
  term1 = bs(n)
  result = 1 + term1
  for l in range(n):
   result *= result
  print("Approximation: " + str(result))
def s(x, digits):
 def fastsqrt(x):
  g = 1.0
  mp.dps = digits
  for i in range(0, digits):
   g = mp.mpf(g + x/g) / 2
   print("Approximation: " + str(g))
 fastsqrt(x)
print("Welcome to Pi-Power - Crunching hundreds of pi digits and others")
choice = input("Enter choice: ")
if choice == "e":
 n = int(input("Enter digits: "))
 e(n)
elif choice == "pi": 
 n = int(input("Enter digits to calculate: "))
 result = mp.mpf(0)
 pi(n)
elif choice == "sqrt":
 n = int(input("Enter sqrt of what? "))
 d = int(input(f"Enter digits of sqrt({n}): "))
 s(n, d)