# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 14:04:43 2020

This comes from MaterialsAutomated1, "MaterialsAutomated1-ElkDOSSumming" by Tyrel McQueen with slight variations
    https://github.com/materialsautomated/materialsautomated.github.io/blob/master/MaterialsAutomated1-ElkDOSSumming/MaterialsAutomated1.ipynb
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as spc
import re
from pathlib import Path
import os.path
from matplotlib.collections import LineCollection
def load_pdos(path):
    '''
    Read in all PDOS files
    This was derived from MaterialsAutomated1, "MaterialsAutomated1-ElkDOSSumming" by Tyrel McQueen
    https://github.com/materialsautomated/materialsautomated.github.io/blob/master/MaterialsAutomated1-ElkDOSSumming/MaterialsAutomated1.ipynb
    # Given the input directory, this function loads all PDOS files from an elk calculation, 
    # https://elk.sourceforge.net, and returns fulldos, a large multidimensional 
    # dict of dict of lists of lists of lists:
    #   fulldos[s][a][lms][row][col]
    # Where:
    # - s is the species number (typically 1,2,...)
    # - a is the atom number (typically 1,2,...)
    # - lms runs over all the input blocks within the file (how many and order depends on dosmsum and dossum settings)
    # - row goes from 0...len(single block)-1
    # - col is 0 (E-Efermi) or 1 (the PDOS for this s,a,lms,and E-Efermi)
    #
    #
    Parameters
    ----------
    path : TYPE
        DESCRIPTION.

    Returns
    -------
    fulldos : dict of dict of lists of lists of lists
		DESCRIPTION. fulldos[s][a][lms][row][col]
			 Where:
			 - s is the species number (typically 1,2,...)
			 - a is the atom number (typically 1,2,...)
			 - lms runs over all the input blocks within the file (how many and order depends on dosmsum and dossum settings)
			 - row goes from 0...len(single block)-1
			 - col is 0 (E-Efermi) or 1 (the PDOS for this s,a,lms,and E-Efermi)

    '''

    p=Path(path)
    fulldos={}
    for x in p.glob("PDOS*.OUT"):
        print(x)
        print(type(x))
        print(x.name)
        m=re.match("PDOS_S([0-9]+)_A([0-9]+).OUT", str(x.name))
        print(m)
        s = int(m.group(1))
        a = int(m.group(2))
        if not (s in fulldos):
            fulldos[s] = {}
        fulldos[s][a] = []
        with open(x, "r") as f:
            block = []
            for l in f.readlines():
                m = re.match("\s*([-0-9E\.]+)\s*([-0-9E\.]+)", l)
                if m is None:
                    # start of a new block
                    fulldos[s][a].append(block)
                    block = []
                else:
                    block.append([float(m.group(1))/spc.physical_constants['electron volt-hartree relationship'][0],float(m.group(2))*spc.physical_constants['electron volt-hartree relationship'][0]])
    return fulldos

def sum_atoms_np(fulldos):
	'''
    # sum over all atoms of a species, keeping the (lms) projections
    # implemented via numpy, faster, but less sanity checking.
	Parameters
    ----------
    fulldos : dict of dict of lists of lists of lists:
        DESCRIPTION. fulldos[s][a][lms][row][col]
		# Where:
		# - s is the species number (typically 1,2,...)
		# - a is the atom number (typically 1,2,...)
		# - lms runs over all the input blocks within the file (how many and order depends on dosmsum and dossum settings)
		# - row goes from 0...len(single block)-1
		# - col is 0 (E-Efermi) or 1 (the PDOS for this s,a,lms,and E-Efermi)

    Returns
    -------
    sdos : 4d numpy array
        DESCRIPTION. sum over all atoms of a species. sdos_np[s][lms] gives a 2-d array describing energy vs. DOS
	'''
	sdos = {}
	for s in fulldos:
		sdos[s] = np.array(list(fulldos[s].values()))
		nat = sdos[s].shape[0]
		sdos[s] = sdos[s].sum(axis=0)
		sdos[s][:,:,0] /= nat
	return sdos
def sum_atoms_lms_np(fulldos, single_spin=False):
	'''
    # sum over all atoms and lms of a species
    # implemented via numpy, faster, but less sanity checking.
		Parameters
    ----------
    fulldos : dict of dict of lists of lists of lists:
        DESCRIPTION. fulldos[s][a][lms][row][col]
		# Where:
		# - s is the species number (typically 1,2,...)
		# - a is the atom number (typically 1,2,...)
		# - lms runs over all the input blocks within the file (how many and order depends on dosmsum and dossum settings)
		# - row goes from 0...len(single block)-1
		# - col is 0 (E-Efermi) or 1 (the PDOS for this s,a,lms,and E-Efermi)

    Returns
    -------
    qdos : 3-d numpy array
        DESCRIPTION. PDOS summed over all atoms and lms of each species. qdos_np[s] gives a 2-d numpy array describing energy vs. DOS
	'''
	qdos = {}
	for s in fulldos:
		qdos[s] = np.array(list(fulldos[s].values()))
		natlms = qdos[s].shape[0]*qdos[s].shape[1]
		qdos[s] = qdos[s].sum(axis=0)
		if single_spin:
			qdos[s] = qdos[s].sum(axis=0)
		else:
			sa = np.split(qdos[s],2,axis=0)
			sa[1][:,:,0] *= -1.0
			qdos[s] = sa[0].sum(axis=0) - sa[1].sum(axis=0)
		qdos[s][:,0] /= natlms
	return qdos
def sum_species_atoms_np(fulldos):
	'''
    # sum over all species and atoms, leaving indexes by lms
    # implemented via np, faster, but less sanity checking.
		Parameters
    ----------
    fulldos : dict of dict of lists of lists of lists:
        DESCRIPTION. fulldos[s][a][lms][row][col]
		# Where:
		# - s is the species number (typically 1,2,...)
		# - a is the atom number (typically 1,2,...)
		# - lms runs over all the input blocks within the file (how many and order depends on dosmsum and dossum settings)
		# - row goes from 0...len(single block)-1
		# - col is 0 (E-Efermi) or 1 (the PDOS for this s,a,lms,and E-Efermi)

    Returns
    -------
    rdos : 3-d numpy array
        DESCRIPTION. PDOS summed over all atoms and species. rdos_np[lms] gives a 2-d numpy array describing energy vs. DOS. 
	'''
	sdos = sum_atoms_np(fulldos)
	rdos = np.zeros(sdos[1].shape)
	for s in sdos:
		rdos += sdos[s]
	rdos[:,:,0] /= len(sdos)
	return rdos


