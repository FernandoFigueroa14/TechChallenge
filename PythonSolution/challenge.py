#Stori Tech Challenge
#Fernando Figueroa

file = input("Account file (.csv): ")
file = open(file)

def processFile(file):
    print(file.read())

processFile(file)