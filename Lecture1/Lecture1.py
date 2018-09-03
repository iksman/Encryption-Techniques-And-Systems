def alphabet(lower=True):
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if lower == True:
        return alph.lower()
    return alph

def getNumerical(char):
    try:
        return alphabet().index(char.lower())
    except:
        return -1

while True:
    print(getNumerical(input()))