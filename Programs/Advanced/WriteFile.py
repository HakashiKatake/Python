#Write a program that prompts the user for a line of text and writes that line to a file.

def writeFile(file):
    with open(file, 'w') as f:
        f.write(input("Enter a line of text: "))

writeFile('Python/Programs/Advanced/WriteFile.txt')
