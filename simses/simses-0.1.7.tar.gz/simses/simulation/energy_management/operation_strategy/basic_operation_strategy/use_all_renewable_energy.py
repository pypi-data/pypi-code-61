from simses.commons.profile.power_profile.generation_profile import GenerationProfile
from simses.commons.state.energy_management_state import EnergyManagementState
from simses.commons.state.system_state import SystemState
from simses.simulation.energy_management.operation_strategy.operation_priority import OperationPriority
from simses.simulation.energy_management.operation_strategy.operation_strategy import OperationStrategy


class UseAllRenewableEnergy(OperationStrategy):
    """
    Operation Strategy for a plant that uses the whole energy provided by an energy source
    made espacially for an electrolyzer which produces hydrogen with the energy out of solar oder wind energy plant
    """
    def __init__(self, pv_generation_profile: GenerationProfile):
        super().__init__(OperationPriority.MEDIUM)
        self.__pv_profile: GenerationProfile = pv_generation_profile
        self.__pv_power = 0
        self.__load_power = 0

    def next(self, time: float, system_state: SystemState, power: float = 0) -> float:
        self.__pv_power = self.__pv_profile.next(time)
        return self.__pv_power

    def update(self, energy_management_state: EnergyManagementState) -> None:
        energy_management_state.pv_power = self.__pv_power
        energy_management_state.load_power = self.__load_power

    def close(self) -> None:
        self.__pv_profile.close()