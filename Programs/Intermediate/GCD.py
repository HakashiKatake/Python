a, b = map(int, input("Enter two numbers: ").split())
while b:
    a, b = b, a % b
print(f"GCD: {a}")