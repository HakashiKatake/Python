
def findLongestWord(file):
    with open(file, 'r') as f:
        words = f.read().split()
        longest = max(words, key=len)
        print(longest)

findLongestWord('Python/Programs/Advanced/FindLongestWord.py')