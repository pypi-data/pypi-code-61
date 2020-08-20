import inspect

from intype import is_numeric
from palett import fluo_entries, fluo_vector
from veho.entries import mutate_values
from veho.vector import mutate

from texting import brace, bracket, parenth
from xbrief.deco.deco_node.helpers.mutate_key_pad import mutate_key_pad
from xbrief.deco.deco_node.preset import DecoPreset
from xbrief.deco.deco_node.render import render_entries, render_vector


def deco(ob): return deco_node(DecoPreset(), ob, 0)


def deco_node(self, node, level, indent=0):
    if node is None: return str(node)
    if isinstance(node, str): return node if is_numeric(node) else str(node)
    if isinstance(node, (int, float)): return node
    if isinstance(node, bool): return node
    if isinstance(node, complex): return str(node)
    if isinstance(node, list): return '[list]' if level >= self.depth else bracket(de_ve(self, node[:], level))
    if isinstance(node, dict): return '[dict]' if level >= self.depth else brace(de_en(self, list(node.items()), level))
    if isinstance(node, tuple): return '[tuple]' if level >= self.depth else parenth(de_ve(self, list(node[:]), level))
    if inspect.isfunction(node): return str(node)
    if inspect.isclass(ty := type(node)):
        return f'[{ty.__name__}] {node.__dict__ if hasattr(node, "__dict__") else str(node)}'
    return str(node)


def de_ve(self, vector, lv):
    mutate(vector, lambda v: str(deco_node(self, v, lv + 1)))
    if self.presets: fluo_vector(vector, self.presets, mutate=True)
    return render_vector(self, vector, lv)


def de_en(self, entries, lv):
    pad = mutate_key_pad(entries)
    mutate_values(entries, lambda v: str(deco_node(self, v, lv + 1, pad)))
    if self.presets: fluo_entries(entries, self.presets, mutate=True)
    return render_entries(self, entries, lv)
