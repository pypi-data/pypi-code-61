from typing import Callable, List, Tuple

from ject import oneself
from palett import Preset, fluo_entries
from palett.presets import FRESH, PLANET
from texting import COLF, COSP, ELLIP, LF, liner, to_br
from texting.enum.brackets import BRK, PAR
from veho.entries import zipper
from veho.vector import mapper
from veho.vector.length import length

from xbrief.margin import EntriesMargin
from xbrief.padder.pad_entries import pad_entries


def deco_entries(
        entries: list,
        key_read: Callable = None,
        read: Callable = None,
        head: int = None,
        tail: int = None,
        presets: Tuple[Preset] = (FRESH, PLANET),
        effects: List[str] = None,
        delim: str = COLF,
        bracket: int = BRK,
        inner_bracket: int = PAR,
        ansi: bool = False,
        dash: str = COSP
):
    size = length(entries)
    if not size: return str(entries)
    vn = EntriesMargin.build(entries, head, tail)
    raw, text = vn.to_list(ELLIP), vn.stringify(key_read, read).to_list(ELLIP)
    dye = fluo_entries(raw, presets, effects, colorant=True, mutate=True) if presets else None
    entries = pad_entries(text, raw, dye, ansi=presets or ansi) \
        if delim.find(LF) >= 0 \
        else zipper(text, dye, lambda tx, dy: dy(tx)) if presets else text
    brk = to_br(inner_bracket) or oneself
    lines = mapper(entries, lambda entry: brk(entry[0] + dash + entry[1].rstrip()))
    return liner(lines, delim=delim, bracket=bracket)
