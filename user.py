from GoogleAPI import *

#read JSON file to objects
class User:
    def __init__(self):
        self.uid = "-1"
        self.type = "donor"
        self.name = "Llama"
        self.supplyType = "mask"
        self.supplyNumber = 1
        self.addr = "3411 Chestnut Street"
        self.tel = "6786467287"
        self.email = "pqy@seas.upenn.edu"
        self.info = "Hi"
    
    def setAll(self, type, name, supplyT, supplyN, addr, tel, email, info = "N/A"):
        self.type = type
        self.name = name
        self.supplyType = supplyT
        self.supplyNumber = int(supplyN)
        self.addr = addr
        self.tel = tel
        self.email = email
        self.info = info
    
    def intro(self):
        print("Hello! I'm " + self.name + " and I'm a " + self.type)

    def give(self, supplyType, n):
        num = int(self.supplyNumber)
        self.supplyNumber = str(num - n)
    
    def receive(self, supplyType, n):
        num = int(self.supplyNumber)
        self.supplyNumber = str(num + n)
    

def findClosest(myAddr, addrMap):
    minDist = float("inf")
    minuid = -1
    for uid in addrMap:
        dest = addrMap[uid]
        currDist = getDistance(myAddr, dest)
        if currDist < minDist:
            minDist = currDist
            minuid = uid
    return minuid

def testUser():
    user = User()
    user.intro()
    print("I have " + user.supplyNumber + " " + user.supplyType)
    user.give("mask", 2)
    print("Now I have " + user.supplyNumber + " " + user.supplyType)    

def testFindClosest():
    currLoc = "3401 Grays Ferry Ave, PA"
    Loc1 = "3411 Chestnut St, PA"
    Loc2 = "New York"
    addrMap = {1:Loc2, 2:Loc1}
    return findClosest(currLoc, addrMap)

print(testFindClosest())