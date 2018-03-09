from numpy import shape,ones
class ELMDataStruct:
    def __init__(self, dataSet):
        self.X = dataSet[:,1:]
        self.y = dataSet[:,0]
        self.dataClassStatus = {}
        self.numOfData = list(shape(self.X))[0]
        self.numOfFeature = list(shape(self.X))[1]
        self.numOfClass = self.calcnumOfClass()
        self.labelsMatrix = self.labelsTrans()

    def calcnumOfClass(self):

        for k in range(self.numOfData):
            if self.y[k, 0] not in self.dataClassStatus:
                self.dataClassStatus[self.y[k, 0]] = 1
            else:
                self.dataClassStatus[self.y[k, 0]] += 1
        self.numOfClass = len(self.dataClassStatus)
        return self.numOfClass

    def labelsTrans(self):
        self.labelsMatrix = ones((self.numOfClass, self.numOfData)) * -1
        for k in range(self.numOfData):
            i = int(self.y[k, 0] - 1)
            self.labelsMatrix[i, k] = 1
        return self.labelsMatrix