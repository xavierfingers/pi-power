# 100 lines of pure maths
# Pi-Power - Compute lots of constants
import time
import os
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
  an = (a + b) / 2
  b = sqrt(a * b)
  t -= p * (a - an)** 2
  a = an
  p = (int(p) << 1)
  T = lambda a, b: (a+b)**2 
  N = lambda t: 4  << int(t)-1
  def bs(a, b,c,d):
     if b == 0:
      return (1,1)
     else:
      Bao = b
      Qao = a
      Qao1 = c
      Bao1 = d
      return (Bao + Qao)**2 / (Bao1 * Qao1) 
  result = bs(b,a,t,4)
  end = time.perf_counter() - start
  def verify(x, place):
   if place < 1000:
    dn = math.floor(10**place * result) % 10
    print(f"{len(str(result))}th digit is {dn}")
  verify(str(result), len(str(result))-1) 
  print(str(result))
def e(digits):
 e = mp.mpf(1)
 n = digits // 2 + 1
 mp.dps = digits
 for k in range(n):
  def bs(b):
   Qao = (2 << (int(b) - 1))
   Bao = mp.mpf(1)
   return Bao / Qao 
  term1 = bs(n)
  result = 1 + term1
  for l in range(n):
   result *= result
  with open(f"e.txt", 'w') as f:
   f.write(str(result))
def s(x,digits):
 def fastsqrt(x):
  g = 1.0
  mp.dps = digits
  for i in range(0, digits):
   g = mp.mpf(g + x/g) / 2
  print("Using Newton's Method")
  print("Approximation: " + str(g))
  print(f"Saving to sqrt{x}.txt")
  os.system(f"type nul > sqrt{x}.txt")
  with open(f"sqrt{x}.txt", 'w') as f:
    f.write(str(g))
 fastsqrt(x)
def zeta3(digits):
 z3 = mp.mpf(0)
 mp.dps = digits
 for i in range(1, digits+1):
   def bs():
    Qao = mp.mpf((5/2)*((-1)**(i-1))/(i**3*mp.mpf(math.comb(2*i, i))))
    return Qao
   z3 += sum([bs()])
 with open("zeta.txt", 'w') as f:
    f.write(str(z3))
def phi(digits):
 x = mp.mpf("1.6")
 mp.dps = digits
 for _ in range(10):
    x = x - (x**2 - x - 1) / (2*x-1)
    os.system("type nul > phi.txt")
    with open("phi.txt", "w") as f:
     f.write(str(x)) 
print("Welcome to \033[5;1;4mPi-Power - Crunching hundreds of pi digits and others")
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
elif choice == "zeta3":
 n = int(input("Enter digits of zeta(3): "))
 zeta3(n)
elif choice == "phi":
 n = int(input("Enter number of digits: "))
 phi(n)
else:
 print("Unknown constant.")
 print("List: \nphi\nzeta3\nsqrt\npi\ne")
