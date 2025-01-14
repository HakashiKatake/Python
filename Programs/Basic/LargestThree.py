a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("Enter third number: ")
if a > b and a > c:
    print(f"{a} is the largest")
elif b > a and b > c:
    print(f"{b} is the largest")
else:
    print(f"{c} is the largest")


#easy or my way is 
map(int, input().split())
print(max(a,b,c))
