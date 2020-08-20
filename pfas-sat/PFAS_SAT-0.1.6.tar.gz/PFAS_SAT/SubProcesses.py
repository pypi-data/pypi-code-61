# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 19:18:05 2020

@author: msmsa
"""
import pandas as pd
from .Flow import Flow


def mix(*args):
    mix = Flow()
    for F in args:
        mix.mass += F.mass
        mix.ts += F.ts
        mix.moist += F.moist
        mix.C += F.C
        mix.PFAS += F.PFAS

    if all(['vol' in F.__dict__ for F in args]):
        mix.vol = sum([F.vol for F in args])

    if all(['FlowType' in F.__dict__ for F in args]):
        if len(set([F.FlowType for F in args])) == 1:
            mix.FlowType = F.FlowType
        else:
            raise ValueError('Type of the mixed flow are not the same: {}'.format(set(['FlowType' in F.__dict__ for F in args])))
    return(mix)


def split(InputFlow, **kwargs):
    if sum(kwargs.values()) < 0.999 or sum(kwargs.values()) > 1.001:
        raise ValueError('Sum of fractions is not 1')

    output = {}
    for name, frac in kwargs.items():
        output[name] = Flow()
        output[name].mass = InputFlow.mass * frac
        output[name].ts = InputFlow.ts * frac
        output[name].moist = InputFlow.moist * frac
        output[name].C = InputFlow.C * frac
        output[name].PFAS = InputFlow.PFAS * frac

        if 'vol' in InputFlow.__dict__:
            output[name].vol = InputFlow.vol * frac

        if 'FlowType' in InputFlow.__dict__:
            output[name].FlowType = InputFlow.FlowType
    return(output)


def solid_water_partition(mixture, water_vol, LogPartCoef_data):
    solid_mass = mixture.ts

    C_Water = pd.Series(index=mixture._PFAS_Index)
    C_Solid = pd.Series(index=mixture._PFAS_Index)

    for i, j in enumerate(mixture._PFAS_Index):
        C_Water[i] = mixture.PFAS[j] / (water_vol+mixture.get_Ccont() * solid_mass * 10**LogPartCoef_data[j]['amount'])
        C_Solid[i] = C_Water[i] * 10**(LogPartCoef_data[j]['amount']) * mixture.get_Ccont()
    return(C_Solid, C_Water)


def soil_sorption(mixture, LogPartCoef_data, Leachate_vol, RunOff_vol):
    water_mass = mixture.moist
    water_vol = water_mass * 1

    C_Solid, C_Water = solid_water_partition(mixture, water_vol, LogPartCoef_data)

    Leachate = Flow()
    Leachate.vol = Leachate_vol + water_vol
    Leachate.PFAS = C_Water * (Leachate_vol + water_vol)
    RunOff = Flow()
    RunOff.vol = RunOff_vol
    RunOff.PFAS = C_Water * RunOff_vol
    Remaining = Flow()
    Remaining.PFAS = mixture.PFAS - Leachate.PFAS - RunOff.PFAS

    return(Remaining, Leachate, RunOff)


def aerobic_composting(mixture, ProcessData, LogPartCoef_data, PrecipitationData):
    water_vol = mixture.moist*1  # L/kg

    C_Solid, C_Water = solid_water_partition(mixture, water_vol, LogPartCoef_data)  # C_S: μg/kg and C_W:μg/L

    C_loss = mixture.C * ProcessData['frac_C_lost']['amount']  # KgC
    Solid_loss = C_loss * ProcessData['sol_loss_per_C_loss']['amount']  # Kg

    Remaining = Flow()
    Remaining.ts = mixture.ts - Solid_loss
    Remaining.C = mixture.C - C_loss
    Remaining.moist = Remaining.ts * (1 / ProcessData['ts_end']['amount'] - 1)
    Remaining.mass = Remaining.moist + Remaining.ts

    # Calculating the volume of percipitation (includes RunOff, Leachate and collected Contact Water)
    Area_windrow = mixture.mass / ProcessData['bulk_dens']['amount'] * 2 / ProcessData['wind_ht']['amount']  # m^2   area/volume=(L*W)/(H*W/2*L)=2/H
    Percip_Vol = Area_windrow * PrecipitationData['ann_precip']['amount'] * 1000  # L/yr

    if ProcessData['is_covered']['amount']:
        Leachate_Vol = 0
        RunOff_Vol = 0
        ContactW_vol = 0
    else:
        if ProcessData['is_cw_col']['amount']:
            Leachate_Vol = Percip_Vol * ProcessData['frac_leach']['amount'] * (1 - ProcessData['frac_cw_col']['amount'])  # L/yr
            RunOff_Vol = Percip_Vol * ProcessData['frac_runoff']['amount'] * (1 - ProcessData['frac_cw_col']['amount'])
            ContactW_vol = Percip_Vol * (ProcessData['frac_leach']['amount'] + ProcessData['frac_runoff']['amount']) * \
                ProcessData['frac_cw_col']['amount']
        else:
            Leachate_Vol = Percip_Vol * ProcessData['frac_leach']['amount']
            RunOff_Vol = Percip_Vol * ProcessData['frac_runoff']['amount']
            ContactW_vol = 0

    Leachate = Flow()
    Leachate.vol = Leachate_Vol
    RunOff = Flow()
    RunOff.vol = RunOff_Vol
    Contact_water = Flow()
    Contact_water.vol = ContactW_vol

    # PFAS Balance
    Leachate.PFAS = C_Water * Leachate_Vol
    RunOff.PFAS = C_Water * RunOff_Vol
    Contact_water.PFAS = C_Water * ContactW_vol
    Remaining.PFAS = mixture.PFAS - C_Water * Leachate_Vol - C_Water * RunOff_Vol - C_Water * ContactW_vol

    return(Remaining, Leachate, RunOff, Contact_water)


def landfil_sorption(mixture, LogPartCoef_data, LF_Leachate_Vol, Leachate_Vol):
    water_mass = mixture.moist
    water_vol = water_mass * 1

    C_Solid, C_Water = solid_water_partition(mixture, water_vol, LogPartCoef_data)

    LF_Leachate = Flow()
    LF_Leachate.vol = LF_Leachate_Vol
    LF_Leachate.PFAS = C_Water * LF_Leachate_Vol
    Leachate = Flow()
    Leachate.vol = Leachate_Vol
    Leachate.PFAS = C_Water * Leachate_Vol
    LF_storage = Flow()
    LF_storage.PFAS = mixture.PFAS - LF_Leachate.PFAS - Leachate.PFAS
    return(LF_storage, LF_Leachate, Leachate)


def dewatering(mixture, final_sol_cont, cont_PFAS_water, is_active=True):
    solids = Flow()
    rmvd_water = Flow()

    if is_active:
        # Calc Water removed
        if mixture.mass > 0:
            solids.ts = mixture.ts
            solids.moist = mixture.ts / final_sol_cont * (1 - final_sol_cont)
            solids.mass = solids.ts + solids.moist

            # Calc vol of lost water
            vol_flow = (mixture.moist - solids.moist) * 1

            # Calc PFAS in the lost water
            kwargs = {}
            kwargs['PFAS_cont'] = {}
            for key, data in cont_PFAS_water.items():
                kwargs['PFAS_cont'][key] = data['amount']

            # set the lost water flow
            rmvd_water.set_flow_liq(vol_flow, **kwargs)

            # PFAS Balance in Thickening
            solids.PFAS = mixture.PFAS - rmvd_water.PFAS
    else:
        solids = mixture
    return(solids, rmvd_water)
