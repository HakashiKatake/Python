
def countWord(file):
    with open(file, 'r') as f:
        print(len(f.read().split()))

countWord('Python/Programs/Advanced/CountWord.py')