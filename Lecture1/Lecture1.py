def alphabet():
    return "abcdefghijklmnopqrstuvwxyz"

def getNumerical(char):
    try:
        return alphabet().index(char.lower())
    except:
        return -1

def calculateNumerical(number):
    number = number % 26
    return alphabet()[number]

#Ceasar Brute Forcing
def BrutusCaesar(text, keyword=None):
    print("Brute Force of string: " + text)
    if keyword != None: 
        print("Keyword: " + keyword)
    for i in range(1,26):
        ceasarResult = Caesar(text, i)
        if keyword != None:
            if keyword in ceasarResult:
                print("Key " + str(i) + ": " + Caesar(text, i))
        else:
            print("Key " + str(i) + ": " + Caesar(text, i))

def singularCaesar(text, key, decrypt=False):
    print("Input: " + text)
    print("Key: " + str(key))
    print("Output: " + Caesar(text, key, decrypt))

#Ceasar Cipher
def Caesar(text, key, decrypt=False):
    resultText = ""
    for letter in text:
        if (decrypt == False):
            if (letter in alphabet()):
                resultText += calculateNumerical(getNumerical(letter) + key)
            elif (letter.lower() in alphabet()):
                resultText += calculateNumerical(getNumerical(letter) + key).upper()
            else:
                resultText += letter
        else:
            if (letter in alphabet()):
                resultText += calculateNumerical(getNumerical(letter) - key)
            elif (letter.lower() in alphabet()):
                resultText += calculateNumerical(getNumerical(letter) - key).upper()
            else:
                resultText += letter
    return resultText




#Generate Playfair Matrix
def generateMatrix(key):
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    matrix = []
    for letter in key:
        if letter not in matrix:
            if letter == "i" and "j" in matrix:
                pass
            if letter == "j" and "i" in matrix:
                pass
            else:
                matrix.append(letter.lower())

    for letter in alphabet:
        if letter not in matrix:
            if letter == "i" and "j" in matrix:
                pass
            if letter == "j" and "i" in matrix:
                pass
            else:
                matrix.append(letter)

    matrix2d = ["","","","",""]

    matrix2d[0]=matrix[0:5]
    matrix2d[1]=matrix[5:10]
    matrix2d[2]=matrix[10:15]
    matrix2d[3]=matrix[15:20]
    matrix2d[4]=matrix[20:25]

    print(matrix2d)
    return matrix2d






    

print("Example1: ")
singularCaesar("Get me a vanilla ice cream!", 6)
print("-------------------------------")
print("Example2: ")
singularCaesar("Fdhvdu qhhgv wr orvh zhljkw", 3, True)
print("-------------------------------")
print("Example3: ")
BrutusCaesar("Gryy gurz gb tb gb nzoebfr puncry", "chapel")
print("-------------------------------")
print("Example4: ")
BrutusCaesar("Gryy gurz gb tb gb nzoebfr puncry")
#generateMatrix("largest")
#generateMatrix("occurrence")

