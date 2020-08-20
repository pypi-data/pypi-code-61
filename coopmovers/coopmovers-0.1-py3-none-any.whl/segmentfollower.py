from coopstructs.vectors import IVector
from coopmovers.movers import Mover
from coopmovers.segment import Segment
from typing import List
import logging

class SegmentFollower(Mover):
    def __init__(self, name: str, start_pos: IVector, max_speed_meters_per_sec: float, max_accel_meters_per_sec: float, initial_velocity: IVector = None):
        Mover.__init__(self, name, start_pos, max_speed_meters_per_sec, max_accel_meters_per_sec, initial_velocity)
        self.segments = []

    def add_waypoints(self, waypoints: List[Segment], index: int = -1):
        for point in waypoints:
            if not isinstance(point, Segment):
                raise TypeError(f"waypoints must be of type {type(Segment)}, but type {type(point)} was provided")

        if index < 0 or index > len(self.segments):
            self.segments += waypoints
            logging.debug(f"Appending waypoints to agent {self.name}: {waypoints}")
        else:
            self.segments[index:index] = waypoints
            logging.debug(f"Adding waypoints to agent {self.name} at index [{index}]: {waypoints}")

    def get_next_segment(self) -> Segment:
        if len(self.segments) > 1:
            segment = self.segments[1]
            return segment
        else:
            return None

    def get_next_destination(self) -> Segment:
        if len(self.segments) > 1:
            destination = next(x for x in self.segments if x.is_destination)
            return destination
        else:
            return None

    def get_segments_to_next_destination(self):
        segments = []
        if len(self.segments) > 0:
            for x in self.segments:
                segments.append(x)
                if x.is_destination:
                    break

            return segments
        else:
            return None

    def length_remaining_for_agent(self):
        current_segment = self.segments[1]
        length_of_remaining_segments = (current_segment.end_pos - self.pos).length()

        last = current_segment
        for ii in range(2, len(self.segments)):
            next = self.segments[ii]
            length = (next.end_pos - last.end_pos).length()
            length_of_remaining_segments += length

        return length_of_remaining_segments

    def agent_last_pos(self, agent_name: str):
        return self.segments[-1].end_pos if len(self.segments) > 0 else self.pos


