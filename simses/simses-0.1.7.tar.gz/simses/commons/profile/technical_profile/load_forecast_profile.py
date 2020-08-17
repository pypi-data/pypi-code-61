from simses.commons.profile.file_profile import FileProfile
from simses.commons.profile.technical_profile.technical_profile import TechnicalProfile
from simses.config.simulation.general_config import GeneralSimulationConfig
from simses.config.simulation.profile_config import ProfileConfig


class LoadForecastProfile(TechnicalProfile):

    def __init__(self, config: GeneralSimulationConfig, profile_config: ProfileConfig, scaling_factor: float = 1):
        super().__init__()
        self.__file: FileProfile = FileProfile(config, profile_config.load_forecast_file, scaling_factor=scaling_factor)

    def next(self, time: float) -> float:
        return self.__file.next(time)

    def profile_data_to_list(self, sign_factor=1) -> [float]:
        time, values = self.__file.profile_data_to_list(sign_factor)
        return values

    def close(self):
        self.__file.close()
