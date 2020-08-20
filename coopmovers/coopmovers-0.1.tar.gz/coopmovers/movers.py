from coopstructs.vectors import Vector2, IVector

class Mover():
    def __init__(self, name: str, start_pos: IVector, max_speed_meters_per_sec: float, max_accel_meters_per_sec: float, initial_velocity: IVector = None):
        self.name = name
        self.pos = start_pos
        self.max_speed_meters_per_sec = max_speed_meters_per_sec
        self.max_accel_meters_per_sec = max_accel_meters_per_sec
        self.current_velocity = Vector2(0, 0)
        self.current_accel = Vector2(0, 0)

        if initial_velocity:
            self.current_velocity = initial_velocity
            self.last_velo = initial_velocity
        else:
            self.current_accel = Vector2(0, 0)
            self.last_velo = None

    def __eq__(self, other):
        if isinstance(other, Mover) and other.name == self.name:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name} at pos {self.pos}"

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(self.name)

    def set_pos(self, new_pos: IVector):
        self.pos = new_pos

    def set_velocity(self, velocity: Vector2):
        self.current_velocity = velocity

    def update(self, delta_time_ms: int, goal_pos: Vector2=None, time_scale_seconds_per_second: int = 1,
               decelerate_to_goal: bool = True, remaining_waypoint_length: float = -1, allow_overshoot=False) -> bool:

        if delta_time_ms is None or delta_time_ms <= 0:
            return False

        if goal_pos is None:
            goal_pos = self.pos

        ''' Calculate the amount of accrued velocity in delta time and apply to position'''
        delta_velocity = self.current_velocity * delta_time_ms / 1000.0 * time_scale_seconds_per_second

        old_pos = self.pos
        self.pos += delta_velocity

        ''' Calculate Vector to goal'''
        vector_to_goal = goal_pos - self.pos

        ''' Return early once "close enough"'''
        close = vector_to_goal.length() <= 0.1
        just_overshot = goal_pos.bounded_by(old_pos, self.pos)
        slow = self.current_velocity.length() <= .5
        far_from_final_dest = remaining_waypoint_length > 1

        if (close or just_overshot) \
                and (
                slow  # not moving fast means that we have successfully deccelerated to close enough to be considered a stop
                or far_from_final_dest  # we wont be deccelerating at this waypoint potentially even if deccel is true
                or decelerate_to_goal is False  # if not deccelerating at all, getting within range regardless of speed counts
                or not allow_overshoot
        ):
            self.pos = goal_pos
            self.last_velo = self.current_velocity
            self.current_velocity = Vector2(0, 0)
            self.current_accel = Vector2(0, 0)
            return True

        ''' Calculate the amount of accrued acceleration in delta time and apply to velocity up to max velocity'''
        delta_accel = self.current_accel * delta_time_ms / 1000.0 * time_scale_seconds_per_second

        if vector_to_goal == Vector2(0, 0):
            new_proposed_velocity = Vector2(0, 0)
        else:
            new_proposed_velocity = self.current_velocity.length() * vector_to_goal.unit() + delta_accel

        if new_proposed_velocity.length() <= self.max_speed_meters_per_sec:
            self.current_velocity = new_proposed_velocity
        else:
            self.current_velocity = new_proposed_velocity.unit() * self.max_speed_meters_per_sec

        '''Calculate the acceleration to apply that moves agent towards goal
           **Working dont alter, but periodically slows to stop in prior segment**
        '''
        if decelerate_to_goal and remaining_waypoint_length > 0 and self.distance_to_stop() > remaining_waypoint_length:
            self.current_accel = (vector_to_goal).unit() * self.max_accel_meters_per_sec * -1
        elif vector_to_goal.length() < 1:
            self.current_accel = vector_to_goal
        else:
            self.current_accel = (vector_to_goal).unit() * self.max_accel_meters_per_sec

        return False

    def calculate_acceleration(self, x_current: Vector2, x_desired: Vector2, v_current: Vector2, v_desired: Vector2):
        vector_to_goal = x_desired - x_current

        x = (v_desired.x - v_current.x)(v_desired.x + v_current.x) / (2 * vector_to_goal.x)
        y = (v_desired.y - v_current.y)(v_desired.y + v_current.y) / (2 * vector_to_goal.y)
        return Vector2(x, y)

    def distance_to_stop(self):
        sec_to_stop = self.sec_to_stop()
        return self.current_velocity.length() * sec_to_stop + self.max_accel_meters_per_sec * sec_to_stop ** 2 / 2.0

    def sec_to_stop(self):
        tts = self.current_velocity.length() / self.max_accel_meters_per_sec
        # print(tts)
        return tts


if __name__ =="__main__":
    name = "Coop"
    agent = Mover(name, start_pos=Vector2(5, 6), max_speed_meters_per_sec=5, max_accel_meters_per_sec=10)

    '''Test TimeScale'''
    v = Vector2(0, 10)
    goal = Vector2(0, 100)
    agent.set_velocity(v)

    while True:
        reached_dest = agent.update(delta_time_ms=1000, goal_pos=goal)
        print(agent.pos)
        if reached_dest:
            break

    assert agent.pos == goal