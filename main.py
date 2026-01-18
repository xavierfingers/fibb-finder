
from functools import lru_cache
import os
import sys
import psutil
import struct
import mmap
@lru_cache(maxsize=None)
def setaff(cpus):
     p = psutil.Process()
     p.cpu_affinity(cpus)
def write_memorymap(f, x, size=8192):
 cache = os.open('cache.bin', os.O_RDWR)
 mem = mmap.mmap(cache, size)
 r = f(x)[0]
 offset = (8*2)+(8 * 8)
 if r < 10000:
  mem[offset:offset+8] =  struct.pack('Q', r)
  return struct.unpack('Q', mem[offset:offset+8])[0]
 return r
def fib(n):
   cpus = range(os.cpu_count())
   setaff(cpus)
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
 print(write_memorymap(fib, x))
if choice == "verify":
 x = int(input("Enter number: "))
 v = fib(x)[0] == fib(x - 1)[0] + fib(x-2)[0]
 v1 = fib(x+1)[0]*fib(x-1)[0] - (fib(x)[0])**2 == (-1)**x 
 v2 = sum([fib(s)[0] for s in range(0, x)]) == fib(x+1)[0] - 1
 print(f"{"="*50}") 
 print("Verification: sum([fib(s) for s in range(0, x)]) == fib(x+1) - 1", v2)
 print("Verification: fib(n) = fib(n - 1) + fib(n - 2): " + "✅ " + str(v))
 print("Verification: F(n+1)F(n-1) - F(n)^2 = (-1)^n: " + str(v1) + " ✅")