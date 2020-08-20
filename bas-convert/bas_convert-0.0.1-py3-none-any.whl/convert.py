from oead.aamp import ParameterIO
from oead import S32

from . import paramlist, paramdict


def to_names(pio: ParameterIO) -> None:
    for _, element in pio.lists["Elements"].lists.items():
        element.objects["Parameters"].params["TypeIndex"] = paramlist[
            element.objects["Parameters"].params["TypeIndex"].v
        ]


def to_numbers(pio: ParameterIO) -> None:
    for _, element in pio.lists["Elements"].lists.items():
        element.objects["Parameters"].params["TypeIndex"] = S32(
            paramdict[element.objects["Parameters"].params["TypeIndex"].v]
        )
