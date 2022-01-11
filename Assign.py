from Read import read
import random

def omitFamily(family, personList):
    newList = []
    for x in personList:
        if x.getFamily() != family and x.getGifteeFamily() != family:
            newList.append(x)

    return newList

def changeList(name, personList, giftee):
    for x in personList:
        if x.getName() == name:
            x.setGiftee(giftee)
            break

def assign():
    personList = read()
    random.shuffle(personList)
    size = len(personList)-1
    usedNames = []

    for x in personList:
        loop = True
        while loop == True:
            giftee = random.choice(personList)

            if giftee != x and giftee.getFamily() != x.getFamily() and giftee.getName() not in usedNames:
                x.setGiftee(giftee)
                usedNames.append(giftee.getName())
                loop = False
            elif x == personList[size] and giftee.getFamily() == x.getFamily() and giftee.getName() not in usedNames:
                newList = omitFamily(x.getFamily(), personList)

                temp = random.choice(newList)
                x.setGiftee(temp.getGiftee())
                changeList(temp.getName(), personList, giftee)

                loop = False

    return personList