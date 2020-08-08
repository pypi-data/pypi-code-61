"""scrapli_community.huawei.vrp.huawei_vrp"""
from scrapli.driver.base_network_driver import PrivilegeLevel

from scrapli_community.huawei.vrp._async import default_async_on_close, default_async_on_open
from scrapli_community.huawei.vrp.sync import default_sync_on_close, default_sync_on_open

DEFAULT_PRIVILEGE_LEVELS = {
    "privilege_exec": (
        PrivilegeLevel(
            pattern=r"^[<a-z0-9.\-@()/:]{1,48}[#>$]\s*$",
            name="privilege_exec",
            previous_priv="",
            deescalate="",
            escalate="",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
    "configuration": (
        PrivilegeLevel(
            pattern=r"^\[[a-z0-9.\-@/:]{1,32}\]$",
            name="configuration",
            previous_priv="privilege_exec",
            deescalate="quit",
            escalate="system-view",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
}

SCRAPLI_PLATFORM = {
    "driver_type": "network",  # generic|network
    "defaults": {
        "privilege_levels": DEFAULT_PRIVILEGE_LEVELS,
        "default_desired_privilege_level": "privilege_exec",
        "sync_on_open": default_sync_on_open,
        "async_on_open": default_async_on_open,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
        "failed_when_contains": [],
        "textfsm_platform": "huawei_vrp",
        "genie_platform": "",
    },
}
