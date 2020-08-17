from abc import ABC, abstractmethod
import math

from simses.commons.log import Logger
from simses.commons.state.technology.redox_flow_state import RedoxFlowState


class StackModule(ABC):
    """A StackModule describes a module of connected redox flow stacks"""

    __exact_size: bool = True  # True if serial / parallel connection of stacks can be floats

    def __init__(self, voltage: float, power: float, stack_voltage: float, stack_power: float):
        super().__init__()
        self.__log: Logger = Logger(self.__class__.__name__)
        serial, parallel = self.__stack_connection(voltage, power, stack_voltage, stack_power)
        self._SERIAL_SCALE: float = serial
        self._PARALLEL_SCALE: float = parallel
        self.__log.debug('serial: ' + str(serial) + ', parallel: ' + str(parallel))

    def __stack_connection(self, voltage: float, power: float, stack_voltage: float, stack_power: float):
        """
        calculates the number of serial and parallel connected stacks in a stack module to obtain the system voltage and
        power

        Parameters
        ----------
        voltage : float
            voltage of the system
        power : float
            power of the system
        stack_voltage : float
            nominal voltage of one stack
        stack_power : float
            nominal power of one stack

        Returns
        -------
            serial number of stacks connected in one stack module
            parallel number of stacks connected in one stack module

        """
        if self.__exact_size:
            serial: float = voltage / stack_voltage
            parallel: float = power / stack_power * stack_voltage / voltage
            return serial, parallel
        # integer serial and parallel stack numbers, highest number used
        serial: int = math.ceil(voltage / stack_voltage)
        parallel: int = math.ceil(power / stack_power * stack_voltage / voltage)
        return serial, parallel

    @abstractmethod
    def get_open_circuit_voltage(self, ocv_cell: float) -> float:
        """
        Determines the open circuit voltage based on the current RedoxFlowState.

        Parameters
        ----------
        ocv_cell : float
            Current ocv of a single cell of the electrolyte.

        Returns
        -------
        float:
            Open circuit voltage of the stack module in V

        """
        pass

    @abstractmethod
    def get_internal_resistance(self, redox_flow_state: RedoxFlowState) -> float:
        """
        Determines the internal resistance based on the current RedoxFlowState.

        Parameters
        ----------
        redox_flow_state : RedoxFlowState
            Current state of the redox flow battery.

        Returns
        -------
        float:
            Internal resistance of the stack module in Ohm.

        """
        pass

    @abstractmethod
    def get_cell_per_stack(self) -> int:
        """
        Determines the cells per stack for a specific stack type

        Returns
        -------
        int:
            number of cells per stack
        """
        pass

    @abstractmethod
    def get_min_voltage(self) -> float:
        """
        Determines the minimal voltage of a stack module.

        Returns
        -------
        float:
            minimal stack module voltage in V
        """
        pass

    @abstractmethod
    def get_max_voltage(self) -> float:
        """
        Determines the maximal voltage of a stack module.

        Returns
        -------
        float:
            maximal stack module voltage in V
        """
        pass

    @abstractmethod
    def get_min_current(self, redox_flow_state: RedoxFlowState) -> float:
        """
        Determines the minimal faraday current (maximal discharge current) based on the flow rate.

        Parameters
        ----------
        redox_flow_state : RedoxFlowState
            Current state of the redox flow battery.

        Returns
        -------
        float:
            minimal current (=discharge current) in A
        """
        pass

    @abstractmethod
    def get_max_current(self, redox_flow_state: RedoxFlowState) -> float:
        """
        Determines the mmaximal faraday current (maximal charge current) based on the flow rate.

        Parameters
        ----------
        redox_flow_state : RedoxFlowState
            Current state of the redox flow battery.

        Returns
        -------
        float:
            maximal current (=charge current) in A
        """
        pass

    @abstractmethod
    def get_self_discharge_current(self, redox_flow_state: RedoxFlowState) -> float:
        """
        Determines the self discharge current, which discharges the stack during standby for a stack module.

        Parameters
        ----------
        redox_flow_state : RedoxFlowState
            Current state of the redox flow battery.

        Returns
        -------
        float:
            self discharge current for a stack module in A
        """
        pass

    @abstractmethod
    def get_stacks_volume(self) -> float:
        """
        Returns the volume of electrolyte in the stack module electrodes in m^3.

        Returns
        -------
        float:
            electrolyte volume in the electrodes of the stack module in m^3
        """
        pass

    @abstractmethod
    def get_nominal_voltage_cell(self) -> float:
        """
        Returns the nominal voltage of a single cell of the stack module in V. The value is used to calculate the
        capacity in Ws from its value in As and vice versa.

        Returns
        -------
        float:
           nominal cell voltage in V
        """
        pass

    @abstractmethod
    def get_electrolyte_temperature(self) -> float:
        """
        Determines the electrolyte temperature in the stack.

        Returns
        -------
        float:
            electrolyte temperature in K

        """
        pass

    @abstractmethod
    def get_specif_cell_area(self) -> float:
        """
        Returns the specific electrode area in cm^2.

        Returns
        -------
        float:
            cell area in cm^2
        """
        pass

    def get_name(self) -> str:
        """
        Determines the class name of a stack typ  (e.g. StandardStack)

        Returns
        -------
        str:
            class name of a stack typ
        """
        return self.__class__.__name__

    def get_serial_scale(self) -> float:
        """
        Returns the serial scale of stacks in the stack module. The value can be float if exact_size is true.

        Returns
        -------
        float:
            number of serial stacks in the stack module
        """
        return self._SERIAL_SCALE

    def get_parallel_scale(self) -> float:
        """
        Returns the parallel scale of stacks in the stack module. The value can be float if exact_size is true.

        Returns
        -------
        float:
            number of parallel stacks in the stack module
        """
        return self._PARALLEL_SCALE

    def close(self):
        """Closing all resources in stack_module"""
        self.__log.close()
