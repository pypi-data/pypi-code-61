# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 10:44:45 2020

@author: msmsa
"""
import pandas as pd
from .Flow import Flow
from .SubProcesses import split, mix, dewatering
from .WWTInput import WWTInput
from .ProcessModel import ProcessModel


class WWT(ProcessModel):
    """
    Assumptions:
        1. No volatilization or degradation of PFAS.
        2. Steady state.
        3. Concentration in water remains constant.
        4. Annual time horizon.
    """
    ProductsType = []

    def __init__(self, input_data_path=None, CommonDataObjct=None, InventoryObject=None):
        super().__init__(CommonDataObjct, InventoryObject)
        self.InputData = WWTInput(input_data_path)

    def calc(self, Inc_flow=None):
        # Initialize the Incoming flow
        if Inc_flow:
            self.Inc_flow = Inc_flow
        else:
            self.Inc_flow = Flow()
            kwargs = {}
            for key, data in self.InputData.IncProp.items():
                kwargs[key] = data['amount']
            kwargs['PFAS_cont'] = {}
            for key, data in self.InputData.IncPFAS.items():
                kwargs['PFAS_cont'][key] = data['amount']
            self.Inc_flow.set_flow_liq(**kwargs)

        # Screen and Grit Removal
        rmvd_frac = self.InputData.Screen['frac_sr-grit']['amount']
        self.screen = split(self.Inc_flow, **{'effluent': 1-rmvd_frac, 'rmvd': rmvd_frac})

        # Primary Settling
        rmvd_frac = self.InputData.PrimSet['is_prim_set']['amount'] * self.InputData.PrimSet['frac_prim_solids']['amount']
        self.prim_set = split(self.screen['effluent'], **{'effluent': 1-rmvd_frac, 'rmvd': rmvd_frac})

        # Set the mass flow for rmvd solids in Primary Settling
        self.prim_set['rmvd'].mass = self.prim_set['rmvd'].vol * 1 / (1 - self.InputData.PrimSet['sol_cont_prim_solids']['amount'])
        self.prim_set['rmvd'].ts = self.prim_set['rmvd'].mass * self.InputData.PrimSet['sol_cont_prim_solids']['amount']
        self.prim_set['rmvd'].moist = self.prim_set['rmvd'].mass - self.prim_set['rmvd'].ts

        # Secondary Settling
        rmvd_frac = self.InputData.SecSet['is_sec_set']['amount'] * self.InputData.SecSet['frac_sec_solids']['amount']
        self.sec_set = split(self.prim_set['effluent'], **{'effluent': 1-rmvd_frac, 'rmvd': rmvd_frac})

        # Set the mass flow for rmvd solids in Secondary Settling
        self.sec_set['rmvd'].mass = self.sec_set['rmvd'].vol * 1 / (1 - self.InputData.SecSet['sol_cont_sec_solids']['amount'])
        self.sec_set['rmvd'].ts = self.sec_set['rmvd'].mass * self.InputData.SecSet['sol_cont_sec_solids']['amount']
        self.sec_set['rmvd'].moist = self.sec_set['rmvd'].mass - self.sec_set['rmvd'].ts

        # Calc mass to Thickening
        if self.InputData.Thick['is_prim_thick']['amount'] and self.InputData.Thick['is_sec_thick']['amount']:
            flow_to_thick = mix(self.prim_set['rmvd'], self.sec_set['rmvd'])
        elif self.InputData.Thick['is_prim_thick']['amount']:
            flow_to_thick = self.prim_set['rmvd']
        elif self.InputData.Thick['is_sec_thick']['amount']:
            flow_to_thick = self.sec_set['rmvd']
        else:
            flow_to_thick = Flow()

        # Thickening: assumed that the removed water has the same PFAS concentration as input flow
        self.thick = {}
        self.thick['solids'], self.thick['rmvd_water'] = dewatering(mixture=flow_to_thick,
                                                                    final_sol_cont=self.InputData.Thick['sol_cont_thick']['amount'],
                                                                    cont_PFAS_water=self.InputData.IncPFAS,
                                                                    is_active=True)

        # Dewatering: assumed that the removed water has the same PFAS concentration as input flow
        self.Dew = {}
        self.Dew['solids'], self.Dew['rmvd_water'] = dewatering(mixture=self.thick['solids'],
                                                                final_sol_cont=self.InputData.Dew['sol_cont_dewat']['amount'],
                                                                cont_PFAS_water=self.InputData.IncPFAS,
                                                                is_active=self.InputData.Dew['is_sol_dew']['amount'])

        # Drying: assumed that the removed water has the same PFAS concentration as input flow
        self.Dry = {}
        self.Dry['solids'], self.Dry['rmvd_water'] = dewatering(mixture=self.Dew['solids'],
                                                                final_sol_cont=self.InputData.Dry['sol_cont_dry']['amount'],
                                                                cont_PFAS_water=self.InputData.IncPFAS,
                                                                is_active=self.InputData.Dry['is_sol_dry']['amount'])

# =============================================================================
#         # add to Inventory
#         self.Inventory.add('Leachate', 'Landfill', 'Water', self.Leachate)
#         self.Inventory.add('Storage', 'Landfill', 'Storage', self.LF_storage)
# =============================================================================

    def products(self):
        Products = {}
        return(Products)

    def setup_MC(self, seed=None):
        self.InputData.setup_MC(seed)

    def MC_Next(self):
        input_list = self.InputData.gen_MC()
        return(input_list)

    def report(self):
        report = pd.DataFrame(index=self.Inc_flow._PFAS_Index)
        report['effluent'] = self.sec_set['effluent'].PFAS
        report['solids'] = self.Dry['solids'].PFAS
        report['dewatered'] = self.Dry['rmvd_water'].PFAS + self.Dew['rmvd_water'].PFAS + self.thick['rmvd_water'].PFAS
        report['res'] = self.screen['rmvd'].PFAS
        return(report)
