from abc import ABC, abstractmethod
from coopstructs.vectors import Vector2
from typing import Dict
from coopmovers.IAgentStatusStruct import IAgentStatusStruct
from coopmovers.segment import Segment

class IAgentTracker(ABC):
    def __init__(self):
        self.agents = {}
        self.total_time = 0
        self.last_update = {}
        self.agent_status = {}

    @abstractmethod
    def add_agent(self, name: str, pos: Vector2, max_speed: int = 5, max_accel: int = 10):
        pass

    @abstractmethod
    def add_waypoints(self, agent:str, waypoints: Dict[str, Vector2], index: int = -1, path_id:str = None, as_destination: bool = True):
        pass

    @abstractmethod
    def get_agent_positions(self) -> Dict[str, IAgentStatusStruct]:
        pass

    @abstractmethod
    def clear_waypoints(self, agent_name: str, last_keep_index: int = None):
        pass

    @abstractmethod
    def get_next_destination(self, agent_name: str) -> Segment:
        pass