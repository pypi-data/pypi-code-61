from coopmovers.segment import Segment
from coopstructs.vectors import Vector2, IVector
from coopmovers.segmentfollower import SegmentFollower
from typing import List, Dict, Callable
import logging
from coopmovers.IAgentStatusStruct import IAgentStatusStruct
from coopmovers.IAgentTracker import IAgentTracker

class SegmentFollowerStatusStruct(IAgentStatusStruct):
    def __init__(self, pos: IVector, reached_waypoint: bool, reached_destination: bool, remaining_waypoints: List[Segment], active_path: str = None):
        super().__init__(pos)
        self.reached_waypoint = reached_waypoint
        self.reached_destination = reached_destination
        self.remaining_waypoints = remaining_waypoints
        self.active_path = active_path

    def __str__(self):
        ret = f"{self.pos}, reached_waypoint: {self.reached_waypoint}, reached destination: {self.reached_destination}" \
              f"\nRemaining Waypoints:"
        for segment in self.remaining_waypoints:
            ret += f"\n\t{segment}"

        return ret

    def __repr__(self):
        return self.__str__()


class SegmentFollowerHub(IAgentTracker):
    def __init__(self, reservation_provider: Callable[[str], bool]=None):
        super().__init__()
        self._waypoint_to_segment_map = {}
        self._reservation_provider = reservation_provider

    def add_agent(self, name: str, pos: IVector, max_speed: int = 5, max_accel: int = 10, initial_velocity: IVector = None):
        agent = SegmentFollower(name, start_pos=pos, max_speed_meters_per_sec=max_speed, max_accel_meters_per_sec=max_accel, initial_velocity=initial_velocity)
        self.agents[name] = agent
        self.agents[name].segments = [Segment(end_pos=pos, is_destination=False, is_waypoint=True, waypoint_id="INIT", reservation_provider=self._reservation_provider)]
        self.agent_status[name] = SegmentFollowerStatusStruct(pos=pos, reached_waypoint=True, reached_destination=False, remaining_waypoints=[])

    def _reset_agent_status(self, agent_name: str, reached_destination: bool = None, reached_waypoint: bool = None):
        current_segment = self.agents[agent_name].segments[0]
        if reached_destination is None:
            reached_destination = current_segment.is_destination
        if reached_waypoint is None:
            reached_waypoint = current_segment.is_waypoint

        remaining_waypoints = self.agents[agent_name].segments #[x.end_pos for x in self.agent_segments[agent_name] if x.is_waypoint is True]

        self.agent_status[agent_name] = SegmentFollowerStatusStruct(self.agents[agent_name].pos
                                                          , reached_waypoint=reached_waypoint
                                                          , reached_destination=reached_destination
                                                          , remaining_waypoints=remaining_waypoints
                                                          , active_path=current_segment.path_id)

    def add_waypoints(self, agent_name:str, waypoints: Dict[str, Vector2], index: int = -1, path_id: str = None, as_destination: bool = True):
        new_segments = []

        ''' Get Last Position before index'''
        # self.agent_segments.setdefault(agent_name, [])

        ''' 1. Case when index is out of bounds
            2. Case when index is zero (beginning of list)
            3. All other cases'''
        if index < 0 or index > len(self.agents[agent_name].segments):
            last_pos = self.agent_last_pos(agent_name)
        elif index == 0:
            last_pos = self.agent_status.get(agent_name, SegmentFollowerStatusStruct(Vector2(0, 0), reached_destination=False, reached_waypoint=False, remaining_waypoints=[], active_path=path_id)).pos
        else:
            last_pos = self.agents.get(agent_name).segments[index - 1]

        ''' for each point, Look for a mapping of the waypoint to segments'''
        for edge_id, point in waypoints.items():
            if not (isinstance(point, IVector) or issubclass(IVector, type(point))):
                raise TypeError(f"waypoints must be a derivative of type {IVector}, but type {type(point)} was provided")

            mapping = self.check_waypoint_mapping(last_pos, point)
            last_pos = point
            if mapping is None:
                new_segments.append(Segment(point, is_destination=False, is_waypoint=True, path_id=path_id, waypoint_id=edge_id, reservation_provider=self._reservation_provider))
            else:
                for seg in mapping:
                    new = seg.copy()
                    new.path_id = path_id
                    new.waypoint_id = edge_id
                    new_segments.append(new)

                new_segments[-1].is_waypoint = True

        ''' Update the last segment of segment list to be a new destination'''
        if as_destination:
            new_segments[-1].is_destination = True

        if index < 0:
            self.agents[agent_name].segments += new_segments
            logging.debug(f"Appending waypoints to agent {agent_name}: {new_segments}")
        else:
            self.agents[agent_name].segments[index:index] = new_segments
            logging.debug(f"Adding waypoints to agent {agent_name} at index [{index}]: {new_segments}")

        self._reset_agent_status(agent_name)

    def clear_waypoints(self, agent_name: str, last_keep_index: int = None):
        if agent_name in self.agents.keys():
            self.agents[agent_name].segments = self.agents[agent_name].segments[:last_keep_index + 1]

        self._reset_agent_status(agent_name)

    def get_agent_positions(self) -> Dict[str, tuple]:
        return self.agent_status

    def update_agents(self, time_delta_ms: int, time_scale: int = 1, debug:bool=False):
        self.total_time += time_delta_ms

        for agent_name in self.agents.keys():
            ''' Initialize Booleans'''
            reached_destination = False
            reached_waypoint = False
            completed_segment = False
            next_segment = None
            goal_unit_vector = None

            '''Get current segment for agent'''
            current_segment = self.get_next_segment(agent_name)
            logging.debug(f"Current Segment: {current_segment}")

            ''' Update agent towards goal if there is a current segment'''
            if current_segment and current_segment.reserved(agent_name):
                if debug:
                    self._deb_validate_agent_isnt_heading_toward_occupied_pos(agent_name, current_segment.end_pos)
                remaining_waypoint_length = self.length_remaining_for_agent(agent_name=agent_name, stop_at_next_destination=True)
                deccelerate = False if len(self.agents[agent_name].segments) > 1 and remaining_waypoint_length > self.agents[agent_name].distance_to_stop() else True

                '''Update Agent'''
                completed_segment = self.agents[agent_name].update(delta_time_ms=time_delta_ms, goal_pos=current_segment.end_pos, time_scale_seconds_per_second=time_scale, decelerate_to_goal=deccelerate, remaining_waypoint_length=remaining_waypoint_length)

                if debug:
                    self._deb_validate_agents_dont_share_occupied_pos()
            elif current_segment is None:
                ''' Continue to next agent if there is no current segment for agent'''
                self._reset_agent_status(agent_name, reached_destination=True,
                                         reached_waypoint=True)
                continue
            else:
                continue

            ''' Set booleans and get next segment if the current segment was reached'''
            if completed_segment:
                logging.debug(f"Agent {agent_name} arrived at segment: {current_segment}")
                reached_waypoint = current_segment.is_waypoint
                reached_destination = current_segment.is_destination

                self.complete_segment(agent_name)

                next_segment = self.get_next_segment(agent_name)

            if reached_destination:
                current_segment.is_destination = False

            '''Set new velocity on agent to last velocity of agent in the new goal direction if there is a new goal and it didnt deccelerate'''
            if next_segment and not deccelerate and not reached_destination:
                goal_unit_vector = (next_segment.end_pos - self.agents[agent_name].pos).unit()

            if goal_unit_vector is not None:
                new_velocity = goal_unit_vector * self.agents[agent_name].last_velo.length()
                self._set_agent_velocity(agent_name=agent_name, velocity=new_velocity)

            ''' Set return value for current agent'''
            self._reset_agent_status(agent_name, reached_destination=reached_destination, reached_waypoint=reached_waypoint)


        if debug:
            self._deb_validate_agents_dont_share_occupied_pos()

        return self.agent_status

    def get_next_segment(self, agent_name: str) -> Segment:
        if self.agents.get(agent_name, None) and len(self.agents[agent_name].segments) > 1:
            segment = self.agents[agent_name].segments[1]
            return segment
        else:
            return None

    def length_remaining_for_agent(self, agent_name: str, stop_at_next_destination: bool = False):
        current_segment = self.agents.get(agent_name, None).segments[1]
        # length_of_remaining_segments = (current_segment.end_pos - self.agents[agent_name].pos).length()

        # last = current_segment
        length_of_remaining_segments = 0
        last = self.agents[agent_name].pos

        for ii in range(1, len(self.agents[agent_name].segments)):
            next = self.agents[agent_name].segments[ii]
            length = (next.end_pos - last).length()
            length_of_remaining_segments += length

            '''return early if at destination and dont want to go past'''
            if next.is_destination and stop_at_next_destination:
                break

            ''' Update last'''
            last = next.end_pos

        return length_of_remaining_segments

    def complete_segment(self, agent_name: str):
        completed_segment = self.agents[agent_name].segments[1]

        ''' Remove from beginning of agent segments list until the 0-ith element is the agents current position and 
        the 1st element is not equal to the zero-ith'''
        while len(self.agents[agent_name].segments) > 1 and self.agents[agent_name].segments[1] == completed_segment:
            self.agents[agent_name].segments.pop(0)

    def _set_agent_velocity(self, agent_name:str, velocity: Vector2):
        if velocity:
            self.agents[agent_name].set_velocity(velocity)

    def set_waypoint_to_segment_map(self, map: Dict[Vector2, Dict[Vector2, List[Segment]]]):
        self._waypoint_to_segment_map = map

    def agent_last_pos(self, agent_name: str):
        return self.agents[agent_name].segments[-1].end_pos if len(self.agents[agent_name].segments) > 0 else self.agents[agent_name].pos

    def check_waypoint_mapping(self, start_pos: Vector2, end_pos: Vector2) -> List[Segment]:
       return self._waypoint_to_segment_map.get(start_pos, {}).get(end_pos, None)


    def get_next_destination(self, agent_name: str) -> Segment:
        if self.agents.get(agent_name, None) and len(self.agents[agent_name].segments) > 1:
            destination = next(x for x in self.agents[agent_name].segments if x.is_destination)
            return destination
        else:
            return None

    def _deb_validate_agent_isnt_heading_toward_occupied_pos(self, agent_name: str, destination_pos: Vector2):
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG
        agents_pos = [(agent, paths[0].end_pos) for agent, paths in [(agent, self.agents[agent].segments.items()) for agent in self.agents.keys()]]

        for ii in range(0, len(agents_pos)):
            for jj in range(ii + 1, len(agents_pos)):
                if agents_pos[ii][0] != agent_name and agents_pos[ii][1] == destination_pos != Vector2(0, 0):
                    print("error: agent moving to occupied position")
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG

    def _deb_validate_agents_dont_share_occupied_pos(self):
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG
        agent_pos = [paths[0].end_pos for agent, paths in [(agent, self.agents[agent].segments.items()) for agent in self.agents.keys()]]

        for ii in range(0, len(agent_pos)):
            for jj in range(ii + 1, len(agent_pos)):
                if agent_pos[ii] == agent_pos[jj] != Vector2(0, 0):
                    print("error: agents share position")
        # DEBUGDEBUGDEBUGDEBUGDEBUGDEBUGDEBUG

