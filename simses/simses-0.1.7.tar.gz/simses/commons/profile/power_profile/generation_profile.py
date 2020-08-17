from simses.commons.profile.power_profile.file_power_profile import FilePowerProfile
from simses.config.simulation.general_config import GeneralSimulationConfig
from simses.config.simulation.profile_config import ProfileConfig


class GenerationProfile(FilePowerProfile):

    def __init__(self, profile_config: ProfileConfig, general_config: GeneralSimulationConfig):
        super().__init__(general_config, profile_config.generation_profile_file,
                         scaling_factor=profile_config.generation_scaling_factor)
