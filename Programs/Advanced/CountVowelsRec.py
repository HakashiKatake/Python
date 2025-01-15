
def countVowels(s):
    if len(s) == 0:
        return 0
    else:
        if s[0].lower() in 'aeiou':
            return 1 + countVowels(s[1:])
        else:
            return countVowels(s[1:])
        
print(countVowels('Hello, World!')) 
