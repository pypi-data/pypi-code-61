from mayan.apps.smart_settings.classes import NamespaceMigration
from mayan.apps.smart_settings.utils import smart_yaml_load


class CommonSettingMigration(NamespaceMigration):
    """
    From version 0001 to 0002 backend arguments are no longer quoted
    but YAML valid too. Changed in version 3.3.
    """
    def common_shared_storage_arguments_0001(self, value):
        return smart_yaml_load(value=value)
