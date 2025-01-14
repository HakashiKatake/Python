a, b = map(int, input("Enter two numbers: ").split())
gcd = a
while b:
    gcd, b = b, gcd % b
lcm = abs(a * b) // gcd
print(f"LCM: {lcm}")