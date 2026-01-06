from mpmath import mp
def pi(n, p=0):
        summed = mp.mpf(0)
        mp.dps = n
        factorial = 2*mp.sqrt(2)/mp.mpf(9801)
        for k in range(0, n):
         t_1 = mp.mpf(mp.factorial(4*k)*mp.mpf(1103 + 26390*k))
         t_2 = mp.mpf(mp.factorial(k)**4 * mp.mpf(396)**mp.mpf((4*k)))
         summed += t_1 / t_2
         inverse_pi = mp.mpf(factorial * summed)
         p = mp.mpf(1/inverse_pi)
         print(f"Approximation: {p} digits: {len(str(p))}")
print("Welcome to Pi-Power")
n = int(input("Enter digits to calculate: "))
for i in range(n):
 pi(i)