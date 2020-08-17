from simses.simulation.storage_system.technology.hydrogen.electrolyzer.pressure_model.pressure_controller import \
    PressureController


class IdealVarCathodePressureController(PressureController):
    """ This pressure controller controls the cathode pressure at a disired level and keeps the anode pressure
    at ambient level"""
    def __init__(self):
        super().__init__()
        self.__max_pressure_variation_rate = 0.5  # bar/s
        self.__pressure_control_on: bool = False
        self.__no_h2_production_counter = 0
        self.__shut_down_time = 0.5  # h

    def calculate_n_h2_out(self, pressure_cathode, pressure_cathode_desire, n_h2_prod, max_n_h2_out, timestep, pressure_factor) -> float:
        pressure_variation_rate_desire = (pressure_cathode - pressure_cathode_desire) / timestep  # bar/s  >0 if pressure cathode > pressure cathode deisire
        self.__pressure_control_on = self.__check_pressure_control_on(n_h2_prod, timestep)
        if self.__pressure_control_on:
            if pressure_variation_rate_desire < self.__max_pressure_variation_rate:
                pressure_variation_rate = pressure_variation_rate_desire
            else:
                pressure_variation_rate = pressure_variation_rate_desire / abs(pressure_variation_rate_desire) * self.__max_pressure_variation_rate
            p_c_1 = pressure_cathode - pressure_variation_rate * timestep
            n_h2_out = n_h2_prod - (p_c_1 - pressure_cathode) * 10 ** 5 / pressure_factor
            return max(n_h2_out, 0)
        else:
            p_c_1 = max(pressure_cathode - self.__max_pressure_variation_rate * timestep, 0)
            return n_h2_prod - (p_c_1 - pressure_cathode) * 10 ** 5 / pressure_factor

    def calculate_n_o2_out(self, pressure_anode, pressure_anode_desire, n_o2_prod, timestep) -> float:
        if n_o2_prod >= 0:
            return n_o2_prod
        else:
            return 0  # no intake of atmosphere in case of negative oxygen production (-> only permeation)

    def __check_pressure_control_on(self, n_h2_prod, timestep) -> bool:
        if n_h2_prod <= 0:
            self.__no_h2_production_counter += 1
        else:
            self.__no_h2_production_counter = 0
        if self.__no_h2_production_counter <= self.__shut_down_time * 3600 / timestep:
            return True
        else:
            return False
