import time
import math
from mpmath import mp
def pi(n, p=0):
        summed = mp.mpf(0)
        mp.dps = n
        p = mp.mpf(0)
        factorial = 2*mp.sqrt(2)/mp.mpf(9801)
        for k in range(0, n):
         t_1 = mp.mpf(mp.factorial(4*k)*mp.mpf(1103 + 26390*k))
         t_2 = mp.mpf(mp.factorial(k)**4 * mp.mpf(396)**mp.mpf((4*k)))
         summed += t_1 / t_2
         inverse_pi = factorial * summed
         p = 1/inverse_pi
         print(f"Approximation: {p} digits: {len(str(p))}") 
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