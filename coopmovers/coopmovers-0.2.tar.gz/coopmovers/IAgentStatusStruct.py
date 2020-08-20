from abc import ABC
from coopstructs.vectors import IVector

class IAgentStatusStruct(ABC):
    def __init__(self, pos: IVector):
        self.pos = pos