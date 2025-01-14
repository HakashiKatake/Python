
n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_seq = [0, 1]
for i in range(2, n):
    fib_seq.append(fib_seq[-1] + fib_seq[-2])
print(f"First {n} Fibonacci numbers: {fib_seq[:n]}")