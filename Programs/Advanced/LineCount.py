

def lineCount(file):
    with open(file, 'r') as f:
        print(len(f.readlines()))

lineCount('Python/Programs/Advanced/LineCount.py')