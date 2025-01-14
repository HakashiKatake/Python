num = int(input("Enter number"))
prime = True
for i in range(2,num):
    if (num*i == 0):
        prime = False 

if (prime):
    print("Prime number")
else:
    print("Not prime")
