import time as ti
from numpy.core._multiarray_umath import sign

from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp

from simses.commons.state.system_state import SystemState
from simses.config.simulation.general_config import GeneralSimulationConfig
from simses.config.simulation.storage_system_config import StorageSystemConfig
from simses.simulation.storage_system.auxiliary.auxiliary import Auxiliary
from simses.simulation.storage_system.auxiliary.heating_ventilation_air_conditioning.hvac import \
    HeatingVentilationAirConditioning
from simses.simulation.storage_system.housing.housing import Housing
from simses.simulation.storage_system.housing.twenty_ft_container import TwentyFtContainer
from simses.simulation.storage_system.power_electronics.acdc_converter.acdc_converter import AcDcConverter
from simses.simulation.storage_system.power_electronics.dcdc_converter.dcdc_converter import DcDcConverter
from simses.simulation.storage_system.storage_system_dc import StorageSystemDC
from simses.simulation.storage_system.technology.technology import StorageTechnology
from simses.simulation.storage_system.thermal_model.ambient_thermal_model.ambient_thermal_model import \
    AmbientThermalModel
from simses.simulation.storage_system.thermal_model.system_thermal_model.system_thermal_model import SystemThermalModel


class ZeroDDynamicSystemThermalModel(SystemThermalModel):
    """This is going to be Stefan's model."""

    def __init__(self, ambient_thermal_model: AmbientThermalModel, housing: Housing,
                 hvac: HeatingVentilationAirConditioning, general_config: GeneralSimulationConfig,
                 storage_system_config: StorageSystemConfig, dc_systems: [StorageSystemDC],
                 acdc_converter: AcDcConverter):
        # General parameters and config
        super().__init__()
        self.__system_config: StorageSystemConfig = storage_system_config
        #  getting the max power and capacity of the storage system for cooling power scaling
        self.__max_power_battery = int(self.__system_config.storage_systems_ac[0][1])
        self.__energy_capacity_battery = int(self.__system_config.storage_technologies['storage_1'][0])
        self.__acdc_converter = acdc_converter
        self.__hvac = hvac
        self.__dc_systems = dc_systems[0]
        self.__storage_technology: StorageTechnology = self.__dc_systems.get_storage_technology()
        self.__dc_dc_converter: DcDcConverter = self.__dc_systems.get_dc_dc_converter()
        self.__start_time: float = general_config.start
        self.__end_time: float = general_config.end
        self.__sample_time: float = general_config.timestep
        self.__loop: int = general_config.loop

        # Ambient temperature model
        self.__ambient_thermal_model: AmbientThermalModel = ambient_thermal_model

        # Solar irradiation model
        # TODO create and couple solar irradiation model
        # this is the internal air temperature within the container. Initialized with ambient temperature

        # Housing Model
        self.__housing: TwentyFtContainer = housing  # Link housing object
        # HVAC model
        self.__heating_cooling: HeatingVentilationAirConditioning = hvac
        self.__cooling_power = 0  # in W, -ve implies heating and vice versa
        self.__set_point_temperature: float = self.__heating_cooling.get_set_point_temperature()  # K

        # ---------- Settings ----------
        # It is possible to give optional parameters and settings for the thermal model in the simulation config
        # -HVAC section.

        # if plotting is wished, it is possible to set plotting active in the config
        try:
            self.__plot_yes_or_no: int = int(self.__system_config.hvac['constant_hvac'][7])
        except:
            self.__plot_yes_or_no = 0
        else:
            if self.__plot_yes_or_no != 1 and self.__plot_yes_or_no != 0 :
                raise Exception('Plotting, in the config, must be set to 0 (not wished) or 1 (wished) or shouldn´t be set at all.')

        try:
            self.__developer_mode: int = int(self.__system_config.hvac['constant_hvac'][8])
        except:
            self.__developer_mode = 0
        else:
            if self.__plot_yes_or_no != 1 and self.__plot_yes_or_no != 0 :
                raise Exception('Developer mode, in the config, must be set to 0 (not wished) or 1 (wished) or shouldn´t be set at all.')

        # ---------- Initializing Parameters ----------

        # Air parameters
        self.__individual_gas_constant = self.universal_gas_constant / self.molecular_weight_air  # J/kgK
        self.__air_density = self.air_pressure / (
                self.__individual_gas_constant * 298.15)  # kg/m3
        self.update_air_parameters()
        self.__air_specific_heat = 1006  # J/kgK, cp (at constant pressure)
        # Model with p & V constant, i.e. if T rises, mass must decrease.
        # Quantities with reference to ideal gas equation

        # Battery
        self.__surface_area_battery = self.__storage_technology.surface_area  # in m2
        self.__mass_battery = self.__storage_technology.mass  # in kg
        self.__specific_heat_capacity_battery = self.__storage_technology.specific_heat  # in J/kgK
        self.__convection_coefficient_cell_air = self.__storage_technology.convection_coefficient  # in W/m2K

        # DC-DC Converter
        self.__surface_area_converter_dc_dc = self.__dc_dc_converter.surface_area  # in m2
        self.__mass_converter_dc_dc = self.__dc_dc_converter.mass  # in kg
        self.__specific_heat_capacity_converter_dc_dc = self.__specific_heat_capacity_battery  # for Aluminium in J/kgK
        self.__convection_coefficient_converter_dc_dc = self.__convection_coefficient_cell_air  # in W/m2K

        # AC-DC Converter
        self.__surface_area_converter_ac_dc = self.__acdc_converter.surface_area  # in m2
        self.__mass_converter_ac_dc = self.__acdc_converter.mass   # in kg
        self.__specific_heat_capacity_converter_ac_dc = self.__specific_heat_capacity_battery  # for Aluminium in J/kgK
        self.__convection_coefficient_converter_ac_dc = self.__convection_coefficient_cell_air  # in W/m2K

        # calculation of thermal resistances
        self.calculate_thermal_resistances()
        # calculation of thermal capacities
        self.calculate_thermal_capacities()

        # ---------- input values for cooling_power calculation and control ----------
        # try to get coefficients out of the config, if none were given local ones are taken
        try:
            self.__kp_coefficient = float(self.__system_config.hvac['constant_hvac'][3])
        except:
            self.__kp_coefficient = 400

        try:
            self.__ki_coefficient = float(self.__system_config.hvac['constant_hvac'][4])
        except:
            self.__ki_coefficient = 0

        try:
            self.__kd_coefficient = float(self.__system_config.hvac['constant_hvac'][5])
        except:
            self.__kd_coefficient = 0

        self.__cooling_power_max = self.__heating_cooling.get_max_thermal_power()
        # cooling power scaling factor
        # TODO Logic for scaling factor

        self.__cooling_power_scaling_factor = (self.__max_power_battery / 100000) * \
                                              (self.__energy_capacity_battery / self.__max_power_battery) * 2
        # temperature difference after which the HVAC activates
        self.__temperature_delta_cooling_power_activate = 2
        # temperature difference after which the HVAC deactivates
        self.__temperature_delta_cooling_power_deactivate = 0.5
        # upper boundary for the integral part
        self.__i_temperature_difference_upper_boundary = 1000000
        # targeted temperature for battery

        try:
            self.__battery_temperature_target = float(self.__system_config.hvac['constant_hvac'][2])+273.15
        except:
            self.__battery_temperature_target = 298.15

        # ---------- initializing temperatures of components ----------
        self.__ia_temperature: float = self.__battery_temperature_target  # K internal air temp.
        self.__battery_temperature = self.__battery_temperature_target  # K battery temperature
        self.__converter_temperature_dc_dc = self.__battery_temperature_target  # K
        self.__converter_temperature_ac_dc = self.__battery_temperature_target  # K
        # self.__ia_temperature: float = self.__ambient_thermal_model.get_initial_temperature()  # K internal air temp.
        # self.__battery_temperature = self.__dc_systems.state.temperature  # K battery temperature
        # self.__converter_temperature_dc_dc = self.__ambient_thermal_model.get_initial_temperature()  # K
        # self.__converter_temperature_ac_dc = self.__ambient_thermal_model.get_initial_temperature()  # K
        self.__l1_temperature = self.__housing.surface_temperature_L1
        self.__l2_temperature = self.__housing.temperature_L2
        self.__l3_temperature = self.__housing.surface_temperature_L3

        # ---------- initializing variables and arrays ----------
        self.__cooling_power = 0
        self.__i_temperature_difference = 0

        self.__ac_dc__converter_losses = 0
        self.__battery_and_dc_dc_converter_losses = 0
        self.__hvac_losses = 0
        self.__hvac_losses_2 = 0

        self.__temperature_series = []
        # sum passed time keeps track of the time already simulated; used for x_axis for plotting
        self.__sum_passed_time = 0
        # arrays to store the temperatures and cooling power for multiple sample times
        self.__cooling_power_storage = [0]
        self.__zero_line_for_cooling_power_plot = [0]
        self.__zero_line_for_losses_plot = [0]
        self.__zero_line_for_temperature_difference_plot = [0]
        self.__target_line_for_temperature_plot = [self.__battery_temperature_target]
        self.__temperature_difference_storage = [self.__battery_temperature - self.__battery_temperature_target]
        self.__inner_air_temperature_storage = [self.__ia_temperature]
        self.__battery_temperature_storage = [self.__battery_temperature]
        self.__converter_temperature_storage = [self.__converter_temperature_dc_dc]
        self.__l1_temperature_storage = [self.__l1_temperature]
        self.__l2_temperature_storage = [self.__l2_temperature]
        self.__l3_temperature_storage = [self.__l3_temperature]
        self.__battery_and_dc_dc_converter_loss_storage = [0]
        self.__converter_loss = [0]
        # for intelligent control self.__hvac_active = 1 if HVAC is active and 0 if not
        self.__hvac_active = 0

        # ---------- values for the while loop ----------
        # self.__calculation_time_step is the time step after which the cooling power gets recalculated
        # self.__calculation_time_step : int = int(self.__sample_time)

        try:
            self.__calculation_time_step: int = int(self.__system_config.hvac['constant_hvac'][6])
        except:
            # if the simulated time span is larger then 1 day, the calculation time step increases to keep the runtime low
            if self.__end_time - self.__start_time >= 86400:
                self.__calculation_time_step = 300
            #     if self.__sample_time <= 900:
            #         self.__calculation_time_step = int(self.__sample_time)
            #     else:
            #         self.__calculation_time_step = 600
            else:
                self.__calculation_time_step = 60

        # securing that the sample time is an integer multiple of the calculation time step
        if self.__sample_time % self.__calculation_time_step != 0:
            raise Exception('calculate_temperature failed because calculation_time_step is not an integer multiple of '
                            'sample time, please change calculation_time_step or the sample time')
        # self.__t_eval_step is the time step after which the equation gets evaluated, it is only important if plotting
        # is wished because it results in the graphs getting more detailed ; has no impact on the calculation itself !!
        # set t_eval-step to self.__calculation_time_step if plots are not needed
        self.__t_eval_step: int = self.__calculation_time_step
        # securing that calculation_time is an integer multiple of t_eval_step
        if self.__calculation_time_step % self.__t_eval_step != 0:
            raise Exception('calculate_temperature failed because sample_time is not an integer multiple of '
                            't_eval_step, please change t_eval_step')

        self.__time_for_differential_equation = 0
        self.__time_for_calculate_temperature = 0
        self.__time_for_calculate_cooling_power = 0

    def calculate_thermal_resistances(self):
        # calculates thermal conduction resistance between the margin of Layer 3 (l3) and the mid of Layer 2 (l2)
        self.__l3_l2_thermal_resistance = self.__housing.thickness_L3 / \
                                          (self.__housing.thermal_conductivity_L3 * self.__housing.internal_surface_area) \
                                          + 0.5 * self.__housing.thickness_L2 / \
                                          (self.__housing.thermal_conductivity_L2 * self.__housing.mean_surface_area)
        # calculates thermal conduction resistance  between the mid of Layer 2 (l2) and the margin of Layer 1 (l1)
        self.__l2_l1_thermal_resistance = 0.5 * self.__housing.thickness_L2 / \
                                          (self.__housing.thermal_conductivity_L2 * self.__housing.mean_surface_area) \
                                          + self.__housing.thickness_L1 / \
                                          ( self.__housing.thermal_conductivity_L1 * self.__housing.external_surface_area)
        # calculates thermal convection resistance between the surrounding air (sa) and Layer 3 (l3) of the wall
        self.__sa_l3_thermal_resistance = 1 / (self.__housing.convection_coefficient_air_L1 *
                                               self.__housing.external_surface_area)
        # calculates thermal convection resistance  between Layer 1 (l1) of the wall and the inner air (ia)
        self.__l1_ia_thermal_resistance = 1 / (self.__housing.convection_coefficient_L3_air *
                                               self.__housing.internal_surface_area)
        # calculates thermal convection resistance  between the battery (bat) and the inner air (ia)
        self.__bat_ia_thermal_resistance = 1 / (self.__convection_coefficient_cell_air *
                                                (self.__surface_area_battery + self.__surface_area_converter_dc_dc))
        # calculates thermal convection resistance  between the converter (conv) and the inner air (ia)
        self.__conv_ia_thermal_resistance = 1 / (self.__convection_coefficient_converter_ac_dc *
                                                 self.__surface_area_converter_ac_dc)

        if self.__developer_mode == 1:
            print('Resistances')
            print('Battery-IA Resistance :', self.__bat_ia_thermal_resistance)
            print('Converter-IA Resistance :', self.__conv_ia_thermal_resistance)
            print('Wall TOTAL Thermal Resistance :', self.__l3_l2_thermal_resistance + self.__l2_l1_thermal_resistance +
                  self.__sa_l3_thermal_resistance + self.__l1_ia_thermal_resistance)
            print('     SA-l3 Resistance :', self.__sa_l3_thermal_resistance)
            print('     l3-l2 Resistance :', self.__l3_l2_thermal_resistance)
            print('     l2-l1 Resistance :', self.__l2_l1_thermal_resistance)
            print('     l1-IA Resistance :', self.__l1_ia_thermal_resistance)

    def calculate_thermal_capacities(self):
        self.__battery_thermal_capacity = (self.__mass_battery + self.__mass_converter_dc_dc) * \
                                          self.__specific_heat_capacity_battery
        self.__converter_thermal_capacity = self.__mass_converter_ac_dc * self.__specific_heat_capacity_converter_ac_dc
        self.__inner_air_thermal_capacity = self.__air_mass * self.__air_specific_heat
        self.__l3_thermal_capacity = self.__housing.mass_L3 * self.__housing.specific_heat_L3
        self.__l2_thermal_capacity = self.__housing.mass_L2 * self.__housing.specific_heat_L2
        self.__l1_thermal_capacity = self.__housing.mass_L1 * self.__housing.specific_heat_L1

        if self.__developer_mode == 1:
            print('Capacities')
            print('IA Thermal Capacity :', self.__inner_air_thermal_capacity)
            print('Battery Capacity :', self.__battery_thermal_capacity)
            print('Converter Capacity :', self.__converter_thermal_capacity)
            print('Wall Thermal Capacity: ',
                  self.__l3_thermal_capacity + self.__l2_thermal_capacity + self.__l1_thermal_capacity)

    def update_air_parameters(self):
        self.__air_volume = self.__housing.internal_air_volume  # in m3
        self.__air_mass = self.__air_volume * self.__air_density  # kg

    def calculate_temperature(self, time, state: SystemState) -> None:
        start_time_calculate_temperature = ti.time()
        ambient_air_temperature = self.__ambient_thermal_model.get_temperature(time)
        self.__air_density = self.air_pressure / (self.__individual_gas_constant * state.temperature)
        self.update_air_parameters()
        # selecting the first dc_system out of the dc_system array
        # dc_system_state = dc_system_states[0]
        calculated_time = 0
        # TODO solar radiation model
        radiation_power = 0  # for the non-shaded area in W - link this to a radiation model
        # radiation_power_per_unit_area = self.__solar_radiation_model.get_irradiance(time)
        # for the non-shaded area in W - link this to a radiation model
        # radiation_power = radiation_power_per_unit_area * area  # in W

        while calculated_time < self.__sample_time:
            calculated_time += self.__calculation_time_step
            self.__sum_passed_time += self.__calculation_time_step
            start_time_differential_equation = ti.time()

            def equation_rhs(t, variable_array):
                # variable_array = [inner_air_temperature, battery_temperature, converter_temperature,
                # l3_temperature, l2_temperature, l1_temperature]
                # Temperature variables: inner_air_temperature, battery_temperature, converter_temperature,
                # l3_temperature, l2_temperature, l1_temperature
                # independent variable: time

                # Differential equation for change in inner air temperature
                d_by_dt_inner_air_temperature = (((variable_array[5] - variable_array[0]) / self.__l1_ia_thermal_resistance) +
                                                 ((variable_array[1] - variable_array[0]) / self.__bat_ia_thermal_resistance) +
                                                 ((variable_array[2] - variable_array[0]) / self.__conv_ia_thermal_resistance) -
                                                 self.__cooling_power) / \
                                                self.__inner_air_thermal_capacity
                # Differential equation for change in battery temperature
                d_by_dt_battery_temperature = ((state.storage_power_loss + state.dc_power_loss) -
                                               (variable_array[1] - variable_array[0]) / self.__bat_ia_thermal_resistance) / \
                                              self.__battery_thermal_capacity
                # Differential equation for change in converter temperature
                d_by_dt_converter_temperature_ac_dc = (state.pe_losses - ((variable_array[2] - variable_array[0])
                                                                          / self.__conv_ia_thermal_resistance)) / \
                                                        self.__converter_thermal_capacity
                # Differential equation for change in L3 temperature
                d_by_dt_l3_temperature = (radiation_power +
                                          ((ambient_air_temperature - variable_array[3]) / self.__sa_l3_thermal_resistance)
                                          - ((variable_array[3] - variable_array[4]) / self.__l3_l2_thermal_resistance)) / \
                                         self.__l3_thermal_capacity
                # Differential equation for change in l2 temperature
                d_by_dt_l2_temperature = (((variable_array[3] - variable_array[4]) / self.__l3_l2_thermal_resistance) -
                                          ((variable_array[4] - variable_array[5]) / self.__l2_l1_thermal_resistance)) / \
                                         self.__l2_thermal_capacity
                # Differential equation for change in L1 temperature
                d_by_dt_l1_temperature = (((variable_array[4] - variable_array[5]) / self.__l2_l1_thermal_resistance) -
                                          ((variable_array[5] - variable_array[0]) / self.__l1_ia_thermal_resistance)) / \
                                         self.__l1_thermal_capacity

                equation_rhs_array = [d_by_dt_inner_air_temperature, d_by_dt_battery_temperature,
                                      d_by_dt_converter_temperature_ac_dc, d_by_dt_l3_temperature,
                                      d_by_dt_l2_temperature,
                                      d_by_dt_l1_temperature]
                return equation_rhs_array

            # time_interval is
            time_interval = [i for i in range(self.__t_eval_step, self.__calculation_time_step + self.__t_eval_step,
                                              self.__t_eval_step)]

            sol = solve_ivp(equation_rhs, (0, self.__calculation_time_step),
                            [self.__ia_temperature, self.__battery_temperature, self.__converter_temperature_ac_dc,
                             self.__l3_temperature, self.__l2_temperature, self.__l1_temperature],
                            method='BDF', t_eval=time_interval)

            end_time_differential_equation = ti.time()
            self.__time_for_differential_equation += end_time_differential_equation - start_time_differential_equation
            # print('Time needed :', end_time_differential_equation-start_time)
            self.__temperature_series = sol.y
            # setting current temperatures
            state.temperature = self.__temperature_series[0, -1]
            self.__ia_temperature = self.__temperature_series[0, -1]
            self.__battery_temperature = self.__temperature_series[1, -1]
            self.__converter_temperature_ac_dc = self.__temperature_series[2, -1]
            self.__l3_temperature = self.__temperature_series[3, -1]
            self.__l2_temperature = self.__temperature_series[4, -1]
            self.__l1_temperature = self.__temperature_series[5, -1]

            # store temperatures for plotting
            self.__inner_air_temperature_storage.extend(self.__temperature_series[0])
            self.__battery_temperature_storage.extend(self.__temperature_series[1])
            self.__converter_temperature_storage.extend(self.__temperature_series[2])
            self.__l3_temperature_storage.extend(self.__temperature_series[3])
            self.__l2_temperature_storage.extend(self.__temperature_series[4])
            self.__l1_temperature_storage.extend(self.__temperature_series[5])

            # ---------- calculate cooling power ----------
            self.calculate_cooling_power()

        #   end while   #######################################################################
        # the energy losses of the converter and hvac get calculated in kWh
        self.__ac_dc__converter_losses += state.pe_losses * ((self.__sample_time / 3600) / 1000)
        self.__battery_and_dc_dc_converter_losses += (state.storage_power_loss + state.dc_power_loss) \
                                                     * ((self.__sample_time / 3600) / 1000)
        self.__hvac_losses += self.__heating_cooling.get_electric_power() * ((self.__sample_time / 3600) / 1000)
        self.__hvac_losses_2 += state.aux_losses * ((self.__sample_time / 3600) / 1000)

        # Setting temperature for simses simulation and plotting
        self.__storage_technology.state.temperature = self.__battery_temperature

        self.__battery_and_dc_dc_converter_loss_storage.append(int(state.storage_power_loss + state.dc_power_loss))
        self.__converter_loss.append(int(state.pe_losses))
        self.__zero_line_for_losses_plot.append(0)

        end_time_calculate_temperature = ti.time()
        self.__time_for_calculate_temperature += end_time_calculate_temperature - start_time_calculate_temperature

        # ---------- Plotting the temperatures at the end of the simulated time ----------
        # plotting after the last complete sample time
        if self.__sum_passed_time > self.__loop * (self.__end_time - self.__start_time) - self.__sample_time:
            self.plot_temperatures(state)

    def calculate_cooling_power(self):
        start_time_calculate_cooling_power = ti.time()

        # temperature_difference_storage equals the difference between the actual and the targeted
        # battery temperature
        temperature_steps_for_integration = []

        for i in self.__temperature_series[1]:
            self.__temperature_difference_storage.append(i - self.__battery_temperature_target)
            self.__zero_line_for_temperature_difference_plot.append(0)
            self.__target_line_for_temperature_plot.append(self.__battery_temperature_target)
            temperature_steps_for_integration.append(i - self.__battery_temperature_target)

        p_temperature_difference = self.__temperature_difference_storage[-1]
        # i_temperature_difference gets calculated by simple "rectangle integration"
        for x in temperature_steps_for_integration:
            self.__i_temperature_difference += x * self.__t_eval_step

        # setting an upper boundary for the integral part
        if abs(self.__i_temperature_difference) > self.__i_temperature_difference_upper_boundary:
            self.__i_temperature_difference = self.__i_temperature_difference_upper_boundary * \
                                              sign(self.__i_temperature_difference)

        # there were Problems when self.__calculation_time_step equals self.__t_eval_step because
        #  len(self.__temperature_difference_storage) = 1 in the first cycle
        if len(self.__temperature_difference_storage) == 1:
            d_temperature_difference = self.__temperature_difference_storage[-1]
        else:
            d_temperature_difference = self.__temperature_difference_storage[-1] - \
                                       self.__temperature_difference_storage[-2]

        # cooling_power is +ve when cooling and -ve when heating
        # TODO scale cooling power and boundaries
        cooling_power_required = self.__cooling_power_scaling_factor * \
                                 (self.__kp_coefficient * p_temperature_difference +
                                  self.__ki_coefficient * self.__i_temperature_difference +
                                  self.__kd_coefficient * d_temperature_difference)

        # ---------- logic for cooling power ----------
        # Logic too stop the HVAC from running the whole time (reduce base power needed to run HVAC):
        # The HVAC activates if the temperature difference reaches self.__temperature_delta_cooling_power_activate
        # and deactivates after reaching self.__temperature_delta_cooling_power_deactivate.
        # if abs(p_temperature_difference) > self.__temperature_delta_cooling_power_activate:
        #     self.__hvac_active = 1
        # elif abs(p_temperature_difference) < self.__temperature_delta_cooling_power_deactivate:
        #     self.__hvac_active = 0
        self.__hvac_active = 1
        if self.__hvac_active == 1:
            if abs(cooling_power_required) < self.__cooling_power_max:
                self.__cooling_power = cooling_power_required

            else:
                self.__cooling_power = self.__cooling_power_max * sign(cooling_power_required)
        else:
            self.__cooling_power = 0
        # self.__cooling_power = 0
        # runs the hvac, the electrical energy needed gets logged and calculated into efficiency
        self.__heating_cooling.run_air_conditioning(self.__cooling_power)

        self.__cooling_power_storage.append(self.__cooling_power)
        self.__zero_line_for_cooling_power_plot.append(0)

        end_time_calculate_cooling_power = ti.time()
        self.__time_for_calculate_cooling_power += end_time_calculate_cooling_power - start_time_calculate_cooling_power

    def plot_temperatures(self, state: SystemState):
        # TODO printing the losses and capacity should be in the developer mode
        print()
        print('battery and dc_dc losses :', self.__battery_and_dc_dc_converter_losses)
        print('ac_dc losses :', self.__ac_dc__converter_losses)
        print('hvac losses  :', self.__hvac_losses)
        # print('hvac losses 2 :', self.__hvac_losses_2)
        print()
        print('Kp coefficient :', self.__kp_coefficient)
        print('Ki coefficient :', self.__ki_coefficient)
        print('Kd coefficient :', self.__kd_coefficient)
        print('capacity remaining :', state.capacity)
        print('capacity remaining in percent :', state.capacity / self.__energy_capacity_battery)
        print('sum losses', self.__ac_dc__converter_losses + self.__hvac_losses +
              self.__battery_and_dc_dc_converter_losses)
        print()
        control_difference_max = max(self.__temperature_difference_storage)
        control_difference_mean_calculation_help = 0
        for x in self.__temperature_difference_storage:
            control_difference_mean_calculation_help += x
        control_difference_mean = control_difference_mean_calculation_help / len(
            self.__temperature_difference_storage)
        # TODO prining control differences should be devloper mode too
        print('Max control difference:', control_difference_max)
        print('Mean control difference:', control_difference_mean)
        # ____until here_____________
        if self.__plot_yes_or_no == 1 or self.__developer_mode == 1:
            start_time_for_plot = ti.time()
        
            # generating the time array which contains the x-coordinates for the temperatures
            t_axis_for_temperature_plot = [0]+[i for i in range(self.__t_eval_step, self.__sum_passed_time +
                                                                self.__t_eval_step, self.__t_eval_step)]
            plt.figure(1)
            plt.subplot(411)
            print_coefficients = ('[Kp coefficient : ' + str(self.__kp_coefficient) + '  ;  Ki coefficient : ' +
                                  str(self.__ki_coefficient) + '  ;  Kd coefficient : ' + str(self.__kd_coefficient)
                                  + '  ;  Sample time : ' + str(self.__sample_time) + '  ;  Calculation time : ' +
                                  str(self.__calculation_time_step) + '  ;  Evaluation time : ' +
                                  str(self.__t_eval_step) + ']')
            axes = plt.gca()
            axes.text(0, 1.5, print_coefficients,
                      transform=axes.transAxes, fontsize=12, verticalalignment='top')
            plt.plot(t_axis_for_temperature_plot, self.__inner_air_temperature_storage, label='inner_air_temperature')
            plt.plot(t_axis_for_temperature_plot, self.__battery_temperature_storage, label='battery_temperature')
            plt.plot(t_axis_for_temperature_plot, self.__converter_temperature_storage,
                     label='converter_temperature_ac_dc')
            plt.plot(t_axis_for_temperature_plot, self.__l3_temperature_storage, label='L3_temperature')
            plt.plot(t_axis_for_temperature_plot, self.__l2_temperature_storage, label='L2_temperature')
            plt.plot(t_axis_for_temperature_plot, self.__l1_temperature_storage, label='L1_temperature')
            plt.plot(t_axis_for_temperature_plot, self.__target_line_for_temperature_plot, 'black', label='target')
            axes = plt.gca()
            axes.set_xlim([0, self.__end_time - self.__start_time])
            plt.title('Temperatures over Time')
            plt.ylabel('Temperature')
            plt.legend(loc=1)
        
            plt.subplot(412)
            plt.plot(t_axis_for_temperature_plot, self.__temperature_difference_storage, label='temperature difference')
            plt.plot(t_axis_for_temperature_plot, self.__zero_line_for_temperature_difference_plot, 'black',
                     label='zero')
            axes = plt.gca()
            axes.set_xlim([0, self.__end_time - self.__start_time])
            # axes.set_ylim([-15, 15])
            plt.ylabel('Temperature Difference')
            plt.legend(loc=1)
        
            plt.subplot(413)
            # cooling power needs its own x_axis scale, because it gets calculated after self.__calculation_time_step
            # and not after self.__t_eval_step like the temperatures
            t_axis_for_cooling_power_plot = [0]
            j = 0
            while j * self.__calculation_time_step < self.__sum_passed_time:
                t_axis_for_cooling_power_plot.append((j + 1) * self.__calculation_time_step)
                j += 1
            plt.plot(t_axis_for_cooling_power_plot, self.__cooling_power_storage, label='cooling power')
            plt.plot(t_axis_for_cooling_power_plot, self.__zero_line_for_cooling_power_plot, 'black', label='zero')
            axes = plt.gca()
            axes.set_xlim([0, self.__end_time - self.__start_time])
            axes.set_ylim([-self.__cooling_power_max-1000, self.__cooling_power_max+1000])
            plt.ylabel('Power')
            plt.legend(loc=1)
        
            plt.subplot(414)
            # battery_loss and converter_loss need their own x_axis scale, because they get calculated after each
            # sample time and not after self.__t_eval_step or self.__calculation_time_step like the temperatures
            t_axis_for_losses_plot = [0]
            n = 0
            while n * self.__sample_time < self.__sum_passed_time:
                t_axis_for_losses_plot.append((n + 1) * self.__sample_time)
                n += 1
            plt.plot(t_axis_for_losses_plot, self.__battery_and_dc_dc_converter_loss_storage, 'orange', label='DC-DC converter and battery loss')
            plt.plot(t_axis_for_losses_plot, self.__converter_loss, 'g', label='AC-DC converter loss')
            plt.plot(t_axis_for_losses_plot, self.__zero_line_for_losses_plot, 'black', label='zero')
            axes = plt.gca()
            axes.set_xlim([0, self.__end_time - self.__start_time])
            if self.__developer_mode == 1:
                print_control_difference = ('[Max control difference : ' + str(control_difference_max) +
                                            '  ;  Mean control difference : ' + str(control_difference_mean) + ']')
                axes.text(0, -0.4, print_control_difference,
                          transform=axes.transAxes, fontsize=12, verticalalignment='top')
            plt.xlabel('Time')
            plt.ylabel('Losses')
            plt.legend(loc=1)
        
            plt.show()
            end_time_for_plot = ti.time()
            if self.__developer_mode == 'True':
                print('Time needed for plotting', end_time_for_plot - start_time_for_plot)
                print('Time needed for calculate_temperature total', self.__time_for_calculate_temperature)
                print('Time needed for differential equations ', self.__time_for_differential_equation)
                print('Time needed for calculate_cooling power', self.__time_for_calculate_cooling_power)

    def get_auxiliaries(self) -> [Auxiliary]:
        return [self.__heating_cooling]

    def get_temperature(self) -> float:
        return self.__ia_temperature

    # def get_air_mass(self) -> float:
    #     return self.__air_mass
    #
    # def get_air_specific_heat(self) -> float:
    #     return self.__air_specific_heat

    def close(self):
        self.__housing.close()
