#Write a Python script that reads a text file and prints its contents.

def readFile(file):
    with open(file, 'r') as f:
        print(f.read())

readFile('Python/Programs/Advanced/ReadFile.py')