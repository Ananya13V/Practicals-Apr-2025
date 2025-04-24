import threading

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n% i == 0:
            return False
    return True

def generate_primes(num):
    for i in range(2, num+1):
        if is_prime(i):
            print(f"Prime: {i}", end="\n")

def fib(num):
    a = 0
    b = 1
    if num >=1:
        print("Fib 1 : ", a, end = "\n")
    if num >=2:
        print("Fib 2 : ", b, end = "\n")
    for i in range(2, num):
        c = a + b
        print("Fibo {}: ".format(i+1), c, end = "\n")
        a = b
        b = c

prime_thread = threading.Thread(target = generate_primes, args = (20,))
fib_thread = threading.Thread(target=fib, args=(10,))
prime_thread.start()
fib_thread.start()

prime_thread.join()
fib_thread.join()