from coopstructs.vectors import IVector
from typing import Callable

class Segment:
    def __init__(self, end_pos: IVector, is_destination: bool, is_waypoint: bool, reservation_provider: Callable[[str, str], bool] = None, path_id:str= None, waypoint_id:str = None):
        self.end_pos = end_pos
        self.is_destination = is_destination
        self.is_waypoint = is_waypoint
        self.path_id = path_id
        self.waypoint_id = waypoint_id
        self.reservation_provider = reservation_provider

    def reserved(self, agent_name: str):
        return self.reservation_provider(self.waypoint_id, agent_name) if self.reservation_provider else True

    def __str__(self):
        return f"Seg -> wpid: {self.waypoint_id}, ending at: {self.end_pos}. dest: {self.is_destination}, waypoint: {self.is_waypoint}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Segment):
            return False

        if self.end_pos == other.end_pos:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.end_pos)

    def copy(self):
        return Segment(end_pos =self.end_pos, is_destination=self.is_destination, is_waypoint=self.is_waypoint, path_id=self.path_id, waypoint_id=self.waypoint_id, reservation_provider=self.reservation_provider)
