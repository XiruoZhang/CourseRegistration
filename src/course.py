class course:
    def __init__(self, id, name, maxNumber, professorID):
        self.id = id
        self.name = name
        self.maxNumber = maxNumber
        self.professorID = professorID

    def insert(self):
        return "insert into courses values (" + str(self.id) + ", '"+ self.name +"', "+ str(self.maxNumber) + " , " + str(self.professorID)+" )";