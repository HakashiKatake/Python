
def countWord(file):
    try:
        with open(file, 'r') as f:
            print(len(f.read().split()))
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(e)

countWord('Python/Programs/Advanced/CountWord.py')
