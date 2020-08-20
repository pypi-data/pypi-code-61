# coding: utf8


__all__ = [
    "get_bond_analytics",
    "get_option_analytics",
    "get_swap_analytics",
    "get_cds_analytics",
    "get_cross_analytics",
    "get_repo_analytics",
    "get_capfloor_analytics",
    "get_swaption_analytics",
    "get_term_deposit_analytics",
    "get_surface",
    "get_curve"
]

from .contracts._financial_contracts import FinancialContracts
from .surface._surfaces_class import Surfaces
from .curve._curves_class import Curves


def get_instrument_analytics(
        universe,
        fields=None,
        calculation_params=None,
        outputs=None,
        on_response=None,
        closure=None,
        session=None
):
    from refinitiv.dataplatform.factory.content_factory import ContentFactory

    _fin = FinancialContracts(session=session, on_response=on_response)
    result = _fin.get_instrument_analytics(
        universe=universe,
        fields=fields,
        calculation_params=calculation_params,
        outputs=outputs,
        closure=closure
    )
    ContentFactory._last_result = result
    if result.is_success and result.data and result.data.df is not None:
        return result.data.df
    else:
        ContentFactory._last_error_status = result.status
        return None


def get_bond_analytics(
        universe,
        fields=None,
        calculation_params=None,
        outputs=None,
        on_response=None,
        closure=None,
        session=None
):
    result = FinancialContracts.get_bond_analytics(
        universe=universe,
        fields=fields,
        calculation_params=calculation_params,
        outputs=outputs,
        on_response=on_response,
        closure=closure,
        session=session
    )
    from refinitiv.dataplatform.factory.content_factory import ContentFactory
    ContentFactory._last_result = result
    if result.is_success and result.data and result.data.df is not None:
        return result.data.df
    else:
        ContentFactory._last_error_status = result.status
        return None


def get_option_analytics(
        universe,
        fields=None,
        calculation_params=None,
        outputs=None,
        on_response=None,
        closure=None,
        session=None
):
    from refinitiv.dataplatform.factory.content_factory import ContentFactory

    result = FinancialContracts.get_option_analytics(
        universe=universe,
        fields=fields,
        calculation_params=calculation_params,
        outputs=outputs,
        on_response=on_response,
        closure=closure,
        session=session
    )
    ContentFactory._last_result = result
    if result.is_success and result.data and result.data.df is not None:
        return result.data.df
    else:
        ContentFactory._last_error_status = result.status
        return None


def get_swap_analytics(
        universe,
        fields=None,
        calculation_params=None,
        outputs=None,
        on_response=None,
        closure=None,
        session=None
):
    from refinitiv.dataplatform.factory.content_factory import ContentFactory

    result = FinancialContracts.get_swap_analytics(
        universe=universe,
        fields=fields,
        calculation_params=calculation_params,
        outputs=outputs,
        on_response=on_response,
        closure=closure,
        session=session
    )

    if result.is_success and result.data and result.data.df is not None:
        retval = result.data.df
    else:
        ContentFactory._last_error_status = result.status
        retval = None

    ContentFactory._last_result = result

    return retval


def get_cds_analytics(
        universe,
        fields=None,
        calculation_params=None,
        outputs=None,
        on_response=None,
        closure=None,
        session=None
):
    from refinitiv.dataplatform.factory.content_factory import ContentFactory

    result = FinancialContracts.get_cds_analytics(
        universe=universe,
        fields=fields,
        calculation_params=calculation_params,
        outputs=outputs,
        on_response=on_response,
        closure=closure,
        session=session
    )

    if result.is_success and result.data and result.data.df is not None:
        retval = result.data.df
    else:
        ContentFactory._last_error_status = result.status
        retval = None

    ContentFactory._last_result = result

    return retval


def get_cross_analytics(
        universe,
        fields=None,
        calculation_params=None,
        outputs=None,
        on_response=None,
        closure=None,
        session=None
):
    from refinitiv.dataplatform.factory.content_factory import ContentFactory

    result = FinancialContracts.get_cross_analytics(
        universe=universe,
        fields=fields,
        calculation_params=calculation_params,
        outputs=outputs,
        on_response=on_response,
        closure=closure,
        session=session
    )

    if result.is_success and result.data and result.data.df is not None:
        retval = result.data.df
    else:
        ContentFactory._last_error_status = result.status
        retval = None

    ContentFactory._last_result = result

    return retval


def get_repo_analytics(
        universe,
        fields=None,
        calculation_params=None,
        outputs=None,
        on_response=None,
        closure=None,
        session=None
):
    from refinitiv.dataplatform.factory.content_factory import ContentFactory

    result = FinancialContracts.get_repo_analytics(
        universe=universe,
        fields=fields,
        calculation_params=calculation_params,
        outputs=outputs,
        on_response=on_response,
        closure=closure,
        session=session
    )

    if result.is_success and result.data and result.data.df is not None:
        retval = result.data.df
    else:
        ContentFactory._last_error_status = result.status
        retval = None

    ContentFactory._last_result = result

    return retval


def get_capfloor_analytics(
        universe,
        fields=None,
        calculation_params=None,
        outputs=None,
        on_response=None,
        closure=None,
        session=None
):
    result = FinancialContracts.get_capfloor_analytics(
        universe=universe,
        fields=fields,
        calculation_params=calculation_params,
        outputs=outputs,
        on_response=on_response,
        closure=closure,
        session=session
    )
    from refinitiv.dataplatform.factory.content_factory import ContentFactory
    if result.is_success and result.data and result.data.df is not None:
        retval = result.data.df
    else:
        ContentFactory._last_error_status = result.status
        retval = None

    ContentFactory._last_result = result

    return retval


def get_swaption_analytics(
        universe,
        fields=None,
        calculation_params=None,
        outputs=None,
        on_response=None,
        closure=None,
        session=None
):
    result = FinancialContracts.get_swaption_analytics(
        universe=universe,
        fields=fields,
        calculation_params=calculation_params,
        outputs=outputs,
        on_response=on_response,
        closure=closure,
        session=session
    )
    from refinitiv.dataplatform.factory.content_factory import ContentFactory
    if result.is_success and result.data and result.data.df is not None:
        retval = result.data.df
    else:
        ContentFactory._last_error_status = result.status
        retval = None

    ContentFactory._last_result = result

    return retval


def get_term_deposit_analytics(
        universe,
        fields=None,
        calculation_params=None,
        outputs=None,
        on_response=None,
        closure=None,
        session=None
):
    result = FinancialContracts.get_term_deposit_analytics(
        universe=universe,
        fields=fields,
        calculation_params=calculation_params,
        outputs=outputs,
        on_response=on_response,
        closure=closure,
        session=session
    )
    from refinitiv.dataplatform.factory.content_factory import ContentFactory
    if result.is_success and result.data and result.data.df is not None:
        retval = result.data.df
    else:
        ContentFactory._last_error_status = {"error_code": result.error_code, "error_message": result.error_message}
        retval = None

    ContentFactory._last_result = result

    return retval


def get_surface(
        universe,
        outputs=None,
        on_response=None,
        closure=None,
        session=None
):
    result = Surfaces.get_surface(
        universe=universe,
        outputs=outputs,
        on_response=on_response,
        closure=closure,
        session=session
    )
    from refinitiv.dataplatform.factory.content_factory import ContentFactory
    if result.is_success and result.data and result.data.df is not None:
        retval = result.data.df
    else:
        ContentFactory._last_error_status = result.status
        retval = None

    ContentFactory._last_result = result

    return retval


def get_curve(
        universe,
        outputs=None,
        on_response=None,
        closure=None,
        session=None
):
    result = Curves.get_curve(
        universe=universe,
        outputs=outputs,
        on_response=on_response,
        closure=closure,
        session=session
    )
    from refinitiv.dataplatform.factory.content_factory import ContentFactory
    if result.is_success and result.data and result.data.df is not None:
        retval = result.data.df
    else:
        ContentFactory._last_error_status = result.status
        retval = None

    ContentFactory._last_result = result

    return retval
