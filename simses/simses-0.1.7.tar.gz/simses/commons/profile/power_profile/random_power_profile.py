from random import Random

from simses.commons.profile.power_profile.power_profile import PowerProfile


class RandomPowerProfile(PowerProfile):

    def __init__(self, max_power: float = 1500.0, power_offset: float = 0.0, scaling_factor: float = 1.0):
        super().__init__()
        self.__power: float = 0.0  # W
        self.__max_power: float = max_power  # W
        self.__d_power: float = max_power / 10.0  # W
        self.__random: Random = Random(93823341)
        self.__scaling_factor: float = scaling_factor
        self.__power_offset: float = power_offset

    def next(self, time: float) -> float:
        self.__power += self.__random.uniform(-self.__d_power, self.__d_power)
        self.__power = max(-self.__max_power, min(self.__max_power, self.__power))
        return self.__power * self.__scaling_factor + self.__power_offset

    def close(self) -> None:
        pass
