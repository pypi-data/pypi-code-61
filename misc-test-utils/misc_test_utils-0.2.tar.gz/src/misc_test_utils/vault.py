# -*- coding: utf-8 -*-
"""Helper functions for dealing with a vault that manages secrets."""
from types import SimpleNamespace
from typing import Generator

import pytest
from secrets_manager import generate_resource_prefix_from_deployment_tier
from secrets_manager import Vault

_vault_namespace = SimpleNamespace()  # pylint: disable=invalid-name
_vault_namespace.vault = None


class VaultNotSetError(Exception):
    def __init__(self) -> None:
        super().__init__(
            "The vault has not been initialized. Use misc_test_utils.set_vault()."
        )


class VaultSetToProductionTierError(Exception):
    def __init__(self) -> None:
        super().__init__(
            "The provided Vault was set to operate in the production tier. This is not allowed in a non-production environment."
        )


def set_vault(vault: Vault) -> None:
    if vault.get_deployment_tier() == "prod":
        raise VaultSetToProductionTierError
    _vault_namespace.vault = vault


def get_vault() -> Vault:
    vault = _get_vault()
    if vault is None:
        raise VaultNotSetError()
    return vault


def _get_vault() -> Vault:
    return _vault_namespace.vault


def clear_vault() -> None:
    _vault_namespace.vault = None


@pytest.fixture(scope="session", name="session_resource_prefix")  # type: ignore
def fixture_session_resource_prefix() -> Generator[str, None, None]:
    vault = get_vault()
    prefix = generate_resource_prefix_from_deployment_tier(vault.get_deployment_tier())
    yield prefix


@pytest.fixture(scope="session", name="session_dns_resource_prefix")  # type: ignore
def fixture_session_dns_resource_prefix(
    session_resource_prefix: str,
) -> Generator[str, None, None]:
    dns_prefix = session_resource_prefix.replace("_", "-")
    yield dns_prefix
