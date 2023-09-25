import sys

def fibonacci(n):
    a=0
    b=1
    for x in range(n):
        a, b = b, a+b
    return a
    
#for x in range(50000):
#   print(f"{x}. number fibonacci is: {fibonacci(x)}")
sys.set_int_max_str_digits(500000000)
print(f"30000. number fibonacci is: {fibonacci(65000)}")