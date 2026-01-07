import main
import time
t = time.perf_counter()
n = int(input("Enter benchmark limit: "))
l = time.perf_counter() - t
main.pi(n)
print(f"Took {l/100} seconds to calculate Pi.")