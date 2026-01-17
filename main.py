import threading
import time
import sys
def fib(n):
   s = time.perf_counter()
   if n == 0:
            return (0, 1)
   a, b = fib(n >> 1)
   c = a * ((b << 1) - a)
   d = a * a + b * b
   if n & 1:
     return (d, c + d)
   else:
    return (c, d)
def show(x):
 x = threading.Thread(target=print(fib(x)[0]))
 x.start()
sys.set_int_max_str_digits(10000000)
print("Welcome to FibbFinder!")
x = int(input("Enter number: "))
s = time.perf_counter()
show(x)
print("Took: ", time.perf_counter() - s)