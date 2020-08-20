import rhino3dm 
import Model
import uuid

class Reader:

    def __init__(self, filePath):
        pass

    def Load(self):
        return Model.Model(uuid.uuid4())