from typing import Callable, List, Tuple

from palett import Preset
from palett.presets import FRESH, PLANET
from texting import COLF, RTSP

from xbrief.deco.deco_entries.deco_entries import deco_entries
from texting.enum.brackets import BRC


def deco_dict(
        entries: dict,
        key_read: Callable = None,
        read: Callable = None,
        head: int = None,
        tail: int = None,
        presets: Tuple[Preset] = (FRESH, PLANET),
        effects: List[str] = None,
        delim: str = COLF,
        bracket: int = BRC,
        inner_bracket: int = None,
        ansi: bool = False,
        dash: str = RTSP
):
    return deco_entries(list(entries.items()),
                        key_read,
                        read,
                        head,
                        tail,
                        presets,
                        effects,
                        delim,
                        bracket,
                        inner_bracket,
                        ansi,
                        dash)
