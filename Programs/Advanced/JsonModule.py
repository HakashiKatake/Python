
import json

def readJsonFile(fileName):
    with open(fileName, 'r') as file:
        data = json.load(file)
    return data

def writeJsonFile(fileName, data):
    with open(fileName, 'w') as file:
        json.dump(data, file, indent=4)


data = readJsonFile('/Users/saurabhyadav/Desktop/Python/Python/Programs/Advanced/data.json')
data['name'] = 'John'
writeJsonFile('data.json', data)
print("Done")