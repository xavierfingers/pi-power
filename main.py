import time
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
         if t_1 - t_2 == 1:
          if t_1 == 0:
            return (1, 1)
         inverse_pi = factorial * summed 
         p = 1/inverse_pi
         print(f"Approximation: {p} digits: {len(str(p))}") 
def e(n):
 factorial = mp.mpf(1)
 mp.dps = n
 x = 1
 e = mp.mpf(1)
 t = time.perf_counter()
 for i in range(n):
  factorial *= x
  if x == 0:
   factorial **= x
  term = mp.mpf(1) / factorial
  if term == 0:
   term += mp.mpf(1) / factorial
  e += term
  x += 1
  if x - n == 1:
   term = mp.mpf(x) / factorial
  sc = time.perf_counter() - t 
  print("Approximation: " + str(e))
 print("Took: " + str(sc) + " seconds")
print("Welcome to Pi-Power - Crunching hundreds of pi digits and others")
choice = input("Enter choice: ")
if choice == "e":
 n = int(input("Enter digits: "))
 e(n)
elif choice == "pi": 
 n = int(input("Enter digits to calculate: "))
 for i in range(n):
   pi(i)