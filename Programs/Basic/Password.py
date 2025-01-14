

password = input("Enter a password: ")
if len(str(password)) > 6:
    print("*" * 6)
else:
    print("*" * len(str(password)))

    