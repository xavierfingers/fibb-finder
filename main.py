import sys
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
x = int(input("Enter number: "))
print(f"The {x}th Fibonacci number is {fib(x)[0]}")