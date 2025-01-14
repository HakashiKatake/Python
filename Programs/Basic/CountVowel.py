#Given a string, count how many vowels (a, e, i, o, u) it contains.

s = input("Enter a string: ")
count = 0
for i in s:
    if i in "aeiou" or "AEIOU":
        count += 1
print(f"Number of vowels: {count}")
