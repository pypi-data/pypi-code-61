#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
from copy import copy
from inspect import signature
from typing import Callable, List, Optional

from ._in_contract import in_contract
from ._out_contract import out_contract
from .ycontract import DEFAULT_CONTRACT_STATE, ContractState


def pops_out_cond_f(cond_kw, f: Callable) -> List[Callable[..., bool]]:
    sig = signature(f)
    f_varnames = set(sig.parameters.keys())
    usable_varnames = {'returns', 'results', 'result', 'res'}
    for f_varname in f_varnames:
        usable_varnames.discard(f_varname)

    cond_fs = []
    for usable_varname in usable_varnames:
        cond = cond_kw.pop(usable_varname, None)
        if cond is not None:
            if callable(cond):
                cond_fs.append(cond)
            elif hasattr(cond, '__iter__'):
                cond_fs.extend(cond)
    return cond_fs


def contract(
        *conds,
        contract_tag: Optional[str] = None,
        contract_state: ContractState = DEFAULT_CONTRACT_STATE,
        **cond_opts_) -> Callable:

    def _in_contract(f: Callable) -> Callable:
        if contract_state.is_enable:
            cond_opts = copy(cond_opts_)
            cond_fs = pops_out_cond_f(cond_opts, f)
        else:
            cond_fs = []
            cond_opts = {}

        @out_contract(*cond_fs, contract_tag=contract_tag, contract_state=contract_state)
        @in_contract(*conds, contract_tag=contract_tag, contract_state=contract_state, **cond_opts)
        @functools.wraps(f)
        def wrapped(*args, **kw) -> Callable:
            return f(*args, **kw)

        return wrapped

    return _in_contract
