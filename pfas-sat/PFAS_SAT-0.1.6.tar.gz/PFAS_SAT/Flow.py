# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:29:42 2020

@author: Mojtaba Sardarmehni
"""
import pandas as pd


class Flow:
    def __init__(self, **kwargs):
        self._PFAS_Index = ['PFAS', 'PFOA', 'PFNA', 'PFDA', 'PFUnA', 'PFOS', 'PFDS', 'N_MeFOSAA', 'N_EtFOSAA']
        self.mass = 0        # kg
        self.ts = 0          # kg
        self.moist = 0       # kg
        self.C = 0           # kg
        self.bulk_dens = None   # kg/m3
        self.PFAS = pd.Series(data=[0 for i in self._PFAS_Index], index=self._PFAS_Index)  # μg

        for key, value in kwargs.items():
            setattr(self, key, value)

    def set_flow(self, mass_flow, ts_cont, C_cont, PFAS_cont=None, bulk_dens=None, **kwargs):
        self.mass = mass_flow
        self.ts = mass_flow * ts_cont
        self.moist = mass_flow * (1 - ts_cont)
        self.C = self.ts * C_cont
        self.bulk_dens = bulk_dens if bulk_dens else None

        if PFAS_cont:
            self.PFAS = pd.Series([PFAS_cont[i] * self.mass for i in self._PFAS_Index], index=self._PFAS_Index)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def set_flow_liq(self, vol_flow, PFAS_cont=None, **kwargs):
        self.vol = vol_flow
        if PFAS_cont:
            self.PFAS = pd.Series([PFAS_cont[i] * self.vol for i in self._PFAS_Index], index=self._PFAS_Index)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_Ccont(self):
        return (self.C/self.ts)

    def get_TScont(self):
        return (self.ts/self.mass)

    def get_Moistcont(self):
        return (self.moist/self.mass)

    def get_PFAScont(self):
        return (self.PFAS/self.mass)

    def set_FlowType(self, FlowType):
        self.FlowType = FlowType
