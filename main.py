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
  def bs(a, b,c,d):
    Bao = b
    Qao = a
    Qao1 = c
    Bao1 = d
    return (Bao + Qao)**2 / (Bao1 * Qao1) 
  result = bs(a,b,4,t)
  end = time.perf_counter() - start
  print("Approximation of Pi: ", str(result))
  with open("pi.txt", "w") as f:
    f.write(str(result))
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
print("Welcome to Pi-Power - Crunching hundreds of pi digits and others")
choice = input("Enter choice: ")
if choice == "e":
 n = int(input("Enter digits: "))
 e(n)
elif choice == "pi": 
 n = int(input("Enter digits to calculate: "))
 result = mp.mpf(0)
 pi(n)