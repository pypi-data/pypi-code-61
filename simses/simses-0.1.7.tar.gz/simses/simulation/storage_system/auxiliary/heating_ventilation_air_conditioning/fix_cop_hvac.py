from numpy.core._multiarray_umath import sign

from simses.simulation.storage_system.auxiliary.heating_ventilation_air_conditioning.hvac import \
    HeatingVentilationAirConditioning


class FixCOPHeatingVentilationAirConditioning(HeatingVentilationAirConditioning):

    def __init__(self, max_thermal_power: float, set_point_temperature: float):
        super().__init__()
        self.__max_thermal_power: float = max_thermal_power
        self.__min_thermal_power: float = max_thermal_power * 0.0
        # source for scop and seer :
        # https://data.toshiba-klima.at/de/Multisplit%20R32%20-%2010,00%20kW%20-%20R32%20-%20Home%20RAS-5M34U2AVG-E%20de.pdf
        # seasonal coefficient of performance (for cooling)
        self.__scop: float = 4.08
        # seasonal energy efficiency ratio (for heating)
        self.__seer: float = 6.31
        self.__set_point_temperature = set_point_temperature + 273.15  # in K
        self.__electric_power: float = 0
        self.__thermal_power: float = 0

    def run_air_conditioning(self, thermal_power_required: float) -> None:
        if abs(thermal_power_required) < self.__min_thermal_power:
            self.__thermal_power = 0.0
        elif abs(thermal_power_required) > self.__max_thermal_power:
            self.__thermal_power = self.__max_thermal_power * sign(thermal_power_required)
        else:
            self.__thermal_power = thermal_power_required

        # thermal_power is +ve when cooling and -ve when heating
        if thermal_power_required > 0:
            self.__electric_power = abs(self.__thermal_power / self.__seer)
        else:
            self.__electric_power = abs(self.__thermal_power / self.__scop)
        # # idea to set basic power consumption if the hvac is active
        # if self.__thermal_power != 0:
        #     self.__electric_power = 1000+abs(self.__thermal_power / self.__scop)

    def get_max_thermal_power(self) -> float:
        return self.__max_thermal_power

    def get_thermal_power(self) -> float:
        return self.__thermal_power

    def get_electric_power(self) -> float:
        return self.__electric_power

    def get_set_point_temperature(self) -> float:
        return self.__set_point_temperature

    def get_cop(self) -> float:
        return self.__scop
