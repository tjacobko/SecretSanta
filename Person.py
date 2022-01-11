class Person:
    def __init__(self, name, family, gifts, phone, giftee):
        self.name = name
        self.family = family
        self.gifts = gifts
        self.phone = phone
        self.giftee = None

    def getName(self):
        return self.name

    def getFamily(self):
        return self.family

    def getGifts(self):
        return self.gifts

    def getPhone(self):
        return self.phone

    def getGifteeName(self):
        if self.giftee == None:
            return None
        else:
            return self.giftee.getName()

    def getGifteeFamily(self):
        if self.giftee == None:
            return None
        else:
            return self.giftee.getFamily()

    def getGiftee(self):
        if self.giftee == None:
            return None
        else:
            return self.giftee

    def setGiftee(self, giftee):
        self.giftee = giftee