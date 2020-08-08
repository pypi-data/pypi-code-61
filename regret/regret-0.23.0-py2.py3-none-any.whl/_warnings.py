"""
Integration with the standard library's ``warnings`` module.
"""
import warnings


_STACKLEVELS_UNTIL_EMIT_IS_CALLED = 4


def emit(deprecation):
    warnings.warn(
        deprecation.message(),
        DeprecationWarning,
        stacklevel=_STACKLEVELS_UNTIL_EMIT_IS_CALLED,
    )
