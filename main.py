
from functools import lru_cache
import threading
import time
import sys
@lru_cache(maxsize=None)
def fib(n):
   if n == 0:
            return (0, 1)
   a, b = fib(n >> 1)
   c = a * ((b << 1) - a)
   d = a * a + b * b
   if n & 1:
     return (d, c + d)
   else:
     return (c, d)
sys.set_int_max_str_digits(10000000)
print("Welcome to FibbFinder!")
choice  = input("Enter choice: ")
if choice == "fib":
 x = int(input("Enter number: "))
 print(fib(x)[0])
if choice == "verify":
 x = int(input("Enter number: "))
 v = fib(x)[0] == fib(x - 1)[0] + fib(x-2)[0]
 print(f"{"="*50}") 
 print("Verification: fib(n) = fib(n - 1) + fib(n - 2): ", v)