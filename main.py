import re

def writeFile(x):
    listLeft = []
    listRight = []

    synList = open("synonyms.txt", "r+")
    for info in synList:
        k, v = info.split("-")
        k = k.strip()
        v = v.strip()
        listLeft.append(k)
        if k.lower() == x:
            print(v)
            answer = input('Хотите ли вы добавить свой синоним? Y/N\n')
            answerLower = answer.lower()
            if answerLower == 'y':
                newSyn = str(input('Введите синоним:\n'))
                v = v + '; ' + newSyn

        listRight.append(v)

    synDict = dict(zip(listLeft, listRight))
    synString = str(synDict)

    synRegEx = re.sub('(, )', r'\n', synString, flags=re.M)
    synRegEx1 = re.sub(r"[{'}]", r'', synRegEx, flags=re.M)
    synRegEx2 = re.sub(r"[:]", r' -', synRegEx1, flags=re.M)

    synList.seek(0)
    synList.write(synRegEx2)
    synList.truncate()
    synList.close()


def checkWord(word):
    listLeft = []

    synList = open("synonyms.txt", "r")
    for info in synList:
        k, v = info.split("-")
        k = k.strip()
        v = v.strip()
        k = k.lower()
        listLeft.append(k)

    if word not in listLeft:
        print('Слово не найдено \nВведите цифру, чтобы выйти')
    else:
        writeFile(word)


def main():
    x = True

    while x == True:
        print('Введите цифру, чтобы выйти. \n')
        wordCheck = (input('Введите слово:\n'))

        if not wordCheck.isdigit():
            word = wordCheck.lower()
            checkWord(word)
        else:
            x = False



main()