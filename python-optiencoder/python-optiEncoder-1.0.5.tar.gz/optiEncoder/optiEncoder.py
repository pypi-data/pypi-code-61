import copy
import math

class Encoder:
    def __init__(self, lst):
        self.lst = list(lst)
        self.categories = set(self.lst)
        self.categCount = len(self.categories)
        self.bits = math.ceil(math.log(self.categCount)/math.log(2))
        self.bitstrings = []
        self.counter = self.categCount
        self.generateBitStrings(self.bits, [])
        self.generateDictionary()

    def generateBitStrings(self, bitlen, payload):
        if self.counter<=0:
            return
        if bitlen== 0:
            self.bitstrings.append(payload)
            self.counter = self.counter-1
        else:
            case1 = copy.deepcopy(payload)
            case2 = copy.deepcopy(payload)
            case1.append(0)
            case2.append(1)
            self.generateBitStrings(bitlen-1, case1)
            self.generateBitStrings(bitlen-1, case2)
    def generateDictionary(self):
        self.mappings = {}
        for i,j in enumerate(list(self.categories)):
            self.mappings[j] = self.bitstrings[i] 
    def getMappings(self):
        return self.mappings
    def getEncodedList(self):
        self.encodedList = []
        for i in self.lst:
            self.encodedList.append(self.mappings[i])
        return self.encodedList