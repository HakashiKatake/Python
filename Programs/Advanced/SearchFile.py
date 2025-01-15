
def searchFile(file, substring):
    with open(file, 'r') as f:
        for line in f:
            if substring in line:
                print(line)
            else:
                continue


searchFile('Python/Programs/Advanced/SearchFile.py', 'Write a program')