import time
from mpmath import mp
def pi(n, p=0):
        summed = mp.mpf(0)
        mp.dps = n
        end = 0
        factorial = 2*mp.sqrt(2)/mp.mpf(9801)
        for k in range(0, n):
         r = time.perf_counter()
         t_1 = mp.mpf(mp.factorial(4*k)*mp.mpf(1103 + 26390*k))
         t_2 = mp.mpf(mp.factorial(k)**4 * mp.mpf(396)**mp.mpf((4*k)))
         if t_1 - t_2 == 1:
          summed += t_1 - t_2
         summed += t_1 / t_2
         if t_1 == t_2 or t_2 == t_1:
                summed += t_1
         inverse_pi = factorial * summed
         p = mp.mpf(1/inverse_pi)
         if len(str(p)) == n:
          break
         end = (time.perf_counter() - r) * 1000
         print(f"Approximation: {p} digits: {len(str(p))}")
        print(f"Took {end:.6f} ms to calculate") 
print("Welcome to Pi-Power")
n = int(input("Enter digits to calculate"))
for i in range(n):
  pi(i)