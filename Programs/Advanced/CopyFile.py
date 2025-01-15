#Write a Python program to copy the contents of one file to another.

def copyFile(source, target):
    with open(source, 'r') as f:
        with open(target, 'w') as t:
            t.write(f.read())

copyFile('Python/Programs/Advanced/ReadFile.py', 'Python/Programs/Advanced/CopyFile.py')