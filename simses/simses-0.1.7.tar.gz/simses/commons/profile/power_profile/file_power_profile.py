from simses.commons.profile.file_profile import FileProfile
from simses.commons.profile.power_profile.power_profile import PowerProfile
from simses.config.simulation.general_config import GeneralSimulationConfig


class FilePowerProfile(PowerProfile):

    class Header:
        ANNUAL_CONSUMPTION: str = 'Annual load consumption in kWh'
        DATASET: str = 'Datasets'
        PEAK_POWER: str = 'Nominal power in kWp'
        SAMPLING: str = 'Sampling in s'

    def __init__(self, config: GeneralSimulationConfig, filename: str, delimiter: str = ',', scaling_factor: float = 1):
        super().__init__()
        self.__file: FileProfile = FileProfile(config, filename, delimiter, scaling_factor)

    def next(self, time: float) -> float:
        return self.__file.next(time)

    def profile_data_to_list(self, sign_factor=1) -> [float]:
        """
        Extracts the whole time series as a list and resets the pointer of the (internal) file afterwards

        Parameters
        ----------
        sign_factor :

        Returns
        -------
        list:
            profile values as a list

        """
        time, values = self.__file.profile_data_to_list(sign_factor)
        return values

    def close(self):
        self.__file.close()
