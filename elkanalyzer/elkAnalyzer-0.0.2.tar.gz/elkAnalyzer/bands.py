# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 14:04:43 2020

@author: epogue1
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as spc
import re
from pathlib import Path
import os.path
from matplotlib.collections import LineCollection


def getSpecialPoints(path):
    '''
    Extracts the x-coordinates of special points from BANDLINES.OUT for plotting
    Parameters
    ----------
    path : STRING ending in //
        DESCRIPTION. Full path to folder where BANDLINES.OUT is found

    Returns
    -------
    x : numpy array of floats
        DESCRIPTION. x-coordinates of special points

    '''
    x=[]
    lbl=[]
    with open(path+'BANDLINES.OUT') as file:
        L=file.readlines()
        n=len(L)
        for k in range(0, n, 3):
            line=L[k].split()
            x.append(line[0])
    x=np.array(x, float)
            
    return x
        

def readBandsFile(path):
    '''
    Read in BAND.OUT file as a vector (array) containing the x-coordinates and numpy array of band energies, where each column is a separate band.

    Parameters
    ----------
    path : STRING ending in //
        DESCRIPTION. Full path to folder where BAND.OUT is found

    Returns
    -------
    x : numpy array of floats, size=(n, )
        DESCRIPTION. numpy array of floats containing x-coordinates for plotting. Use getSpecialPoints() to extract special points for labeling
    y : numpy array of float
        DESCRIPTION. Array of band energies, where each column is a separate band


    '''
    fname=path+'BAND.OUT'
    x=[]
    y=[]
    L=[]
    with open(fname) as file:
        L=file.readlines()
        cnt=0
        while len(L[cnt].strip())>0:
            ln=L[cnt].split()
            x.append(np.float(ln[0]))
            y.append(np.float(ln[1])/spc.physical_constants['electron volt-hartree relationship'][0])
            cnt=cnt+1
        x=np.array(x)
        y=np.array(y)
        bndIndx=1
        cnt=cnt+1
        while cnt<len(L):
            blk=[]
            while len(L[cnt].strip())>0:
                ln=L[cnt].split()
                blk.append(np.float(ln[1])/spc.physical_constants['electron volt-hartree relationship'][0])
                cnt=cnt+1
            #stack block
            b=np.array(blk)
            y=np.vstack((y, b))
            cnt=cnt+1
    y=y.transpose()
        
            
    return x, y
def BANDSdecompose(fname):
    '''
    Import, for a given file the band structure, separated into s, p, d, and f, contributions

    Parameters
    ----------
    path : STRING ending in //
        DESCRIPTION. Full path to folder where BAND.OUT is found

    Returns
    -------
    x : numpy array of floats, size=(n, )
        DESCRIPTION. numpy array of floats containing x-coordinates for plotting. Use getSpecialPoints() to extract special points for labeling
    energy : numpy array of float
        DESCRIPTION. Array of band energies, where each column is a separate band
    s : numpy array of float
        DESCRIPTION. Array of s contributions of each band (same size as energy). This is not normalized.
	p : numpy array of float
        DESCRIPTION. Array of p contributions of each band (same size as energy). This is not normalized.
	d : numpy array of float
        DESCRIPTION. Array of d contributions of each band (same size as energy). This is not normalized.
	f : numpy array of float
        DESCRIPTION. Array of f contributions of each band (same size as energy). This is not normalized.
    '''
    x=[]
    s=[]
    p=[]
    d=[]
    f=[]
    tot=[]
    energy=[]
    with open(fname) as file:
        L=file.readlines()
        cnt=0
        while len(L[cnt].strip())>0:
            ln=L[cnt].split()
            x.append(np.float(ln[0]))
            energy.append(np.float(ln[1])/spc.physical_constants['electron volt-hartree relationship'][0])
            tot.append(np.float(ln[2]))
            s.append(np.float(ln[3]))
            p.append(np.float(ln[4]))
            d.append(np.float(ln[5]))
            f.append(np.float(ln[6]))
            cnt=cnt+1
        x=np.array(x)
        energy=np.array(energy)
        s=np.array(s)
        p=np.array(p)
        d=np.array(d)
        f=np.array(f)
        tot=np.array(tot)
        bndIndx=1
        cnt=cnt+1
        while cnt<len(L):
            blkE=[]
            blktot=[]
            blks=[]
            blkp=[]
            blkd=[]
            blkf=[]
            while len(L[cnt].strip())>0:
                ln=L[cnt].split()
                blkE.append(np.float(ln[1])/spc.physical_constants['electron volt-hartree relationship'][0])
                blktot.append(np.float(ln[2]))
                blks.append(np.float(ln[3]))
                blkp.append(np.float(ln[4]))
                blkd.append(np.float(ln[5]))
                blkf.append(np.float(ln[6]))
                cnt=cnt+1
            #stack block
            bE=np.array(blkE)
            btot=np.array(blktot)
            bs=np.array(blks)
            bp=np.array(blkp)
            bd=np.array(blkd)
            bf=np.array(blkf)
            energy=np.vstack((energy, bE))
            tot=np.vstack((tot, btot))
            s=np.vstack((s, bs))
            p=np.vstack((p, bp))
            d=np.vstack((d, bd))
            f=np.vstack((f, bf))
            cnt=cnt+1
    energy=energy.transpose()
    tot=tot.transpose()
    s=s.transpose()
    p=p.transpose()
    d=d.transpose()
    f=f.transpose()
    return x, energy, tot, s, p, d, f

def importSpeciesContributions(path):
    '''
    Imports species contributions for "BAND_S([0-9]+)_A([0-9]+).OUT" files in path

    Parameters
    ----------
    path : String
        DESCRIPTION. Path (ending in \) describing where the files are you want to import


    Returns
    -------
    x : numpy array of floats, size=(n, )
        DESCRIPTION. numpy array of floats containing x-coordinates for plotting. Use getSpecialPoints() to extract special points for labeling	
	energy : numpy array of float
        DESCRIPTION. Array of band energies, where each column is a separate band
    totSp : numpy array of float
        DESCRIPTION. total normalized contributions to the bands from s,p,d, and f orbitals
	sSp : numpy array of float
	    DESCRIPTION. total normalized s contributions to the bands 
	pSp : numpy array of float
	    DESCRIPTION. total normalized p contributions to the bands 
	dSp : numpy array of float
	    DESCRIPTION. total normalized d contributions to the bands 
	fSp : numpy array of float
	    DESCRIPTION. total normalized f contributions to the bands 
	uniqueAt: numpy array of integers
		DESCRIPTION. list of unique atoms
	norm: Number used to normalize contributions (leakage from atomic orbitals)
    maxWidth : TYPE, optional
        DESCRIPTION. The default is 4.x, energy, totSp, sSp, pSp, dSp, fSp, uniqueAt, norm

    '''

    p=Path(path)#Path(srcDir)
    x=[]
    energy=[]
    totSp=[]

    #pull out number of atom species
    sVect=[]
    aVect=[]
    for k in p.glob("BAND_*.OUT"):
        L=os.path.split(str(k))
        m=re.match("BAND_S([0-9]+)_A([0-9]+).OUT", L[1])
        sVect.append(int(m.group(1)))
        aVect.append(int(m.group(2)))
    uniqueAt=np.unique(np.array(sVect))
    totSp=[float]*len(uniqueAt)
    sSp=[float]*len(uniqueAt)
    pSp=[float]*len(uniqueAt)
    dSp=[float]*len(uniqueAt)
    fSp=[float]*len(uniqueAt)
    norm=[]
    for k in p.glob("BAND_*.OUT"):
        L=os.path.split(str(k))
        m=re.match("BAND_S([0-9]+)_A([0-9]+).OUT", L[1])
        sIdx=int(m.group(1))

        x, energy, tot, s, p, d, f=BANDSdecompose(str(k))
        if len(norm)==0:
            norm=tot
        else:
            norm=norm+tot
        idx=np.searchsorted(uniqueAt, sIdx)
        if type(totSp[idx])==type(float):

            totSp[idx]=tot
            sSp[idx]=s
            pSp[idx]=p
            dSp[idx]=d
            fSp[idx]=f
        else:
            
            totSp[idx]=totSp[idx]+tot
            sSp[idx]=sSp[idx]+s
            pSp[idx]=pSp[idx]+p
            dSp[idx]=dSp[idx]+d
            fSp[idx]=fSp[idx]+f
    for idx in range(len(sSp)):
        sSp[idx]=sSp[idx]/norm
        pSp[idx]=pSp[idx]/norm
        dSp[idx]=dSp[idx]/norm
        fSp[idx]=fSp[idx]/norm
        totSp[idx]=totSp[idx]/norm
        
        

    return x, energy, totSp, sSp, pSp, dSp, fSp, uniqueAt, norm
    
def plotWeightsWidth(x, energy, widths, lbl='', maxWidth=6, alpha=0.5, color='C0'):
    '''
    Plots energy vs. x with the linewidth given by widths, scaled such that the maximum width is maxWidth

    Parameters
    ----------
    x : numpy array of floats, size=(n, )
        DESCRIPTION. numpy array of floats containing x-coordinates for plotting. Use getSpecialPoints() to extract special points for labeling
    energy : numpy array of float
        DESCRIPTION. Array of band energies, where each column is a separate band
    widths : TYPE
        DESCRIPTION.
    maxWidth : TYPE, optional
        DESCRIPTION. The default is 4.

    Returns
    -------
    None.

    '''
    r,c=energy.shape
    lwidths=widths/np.amax(widths)*maxWidth
    ax=plt.gca()
    for k in range(c):
        y=energy[:,k]
        points=np.array([x,y]).T.reshape(-1,1,2)
        segments=np.concatenate([points[:-1], points[1:]], axis=1)
        if k==0:
            lc=LineCollection(segments, alpha=alpha, linewidths=lwidths[:,k], color=color, label=lbl)
        else:
            lc=LineCollection(segments, alpha=alpha, linewidths=lwidths[:,k], color=color)
        
        ax.add_collection(lc)
    ax.set_xlim(min(x), max(x))
    ax.set_xlabel('k')
    ax.set_ylabel('Energy (eV)')

        #plt.plot(x,y)
    
def plotWeightsColor(x, energy, weights, title='', cmap='plasma', linewidth=3):
	'''
    Plots energy vs. x with the linewidth given by widths, scaled such that the maximum width is maxWidth

    Parameters
    ----------
    x : numpy array of floats, size=(n, )
        DESCRIPTION. numpy array of floats containing x-coordinates for plotting. Use getSpecialPoints() to extract special points for labeling
    energy : numpy array of float
        DESCRIPTION. Array of band energies, where each column is a separate band
    weights : numpy array of float
        DESCRIPTION. describes the weighting of each value in energy (same size as energy)
	cmap: colormap, default 'plasma'
		DESCRIPTION. defaults to 'plasma', this is the colormap used in the plot


    Returns
    -------
    None.

    '''
	ax=plt.gca()
	ax.set_xlim(min(x), max(x))
	ax.set_xlabel('k')
	ax.set_ylabel('Energy (eV)')
	r,c=energy.shape
	ax.set_title(title)
	norm=plt.Normalize(0, 1)
	for k in range(c):
		y=energy[:,k]
		points=np.array([x,y]).T.reshape(-1,1,2)
		segments=np.concatenate([points[:-1], points[1:]], axis=1)
		if k==0:
			lc=LineCollection(segments, cmap=cmap, norm=norm)
		else:
			lc=LineCollection(segments, cmap=cmap, norm=norm)
		lc.set_array(weights[:, k])
		lc.set_linewidth(linewidth)
		line=ax.add_collection(lc)

	#fig.colorbar(line, ax)
	fig=plt.gcf()
	fig.colorbar(line, ax=ax)
	ax.set_xlim(min(x), max(x))
	ax.set_xlabel('k')
	ax.set_ylabel('Energy (eV)')
    
    
def plotFinish(path, lbl, energyRange=[-3, 3], figsize=(3, 2), xyLblSize=10, numSize=8):
	'''
    Edits the active range of the currently active plot, sets the figure size, adds k-point labels, adds axis labels

    Parameters
    ----------
    path : STRING ending in //
        DESCRIPTION. Full path to folder where BANDLINES.OUT is found
    lbl : list
        DESCRIPTION. labels for the special points, to appear on the x-axis
    energyRange : list of length 2
        DESCRIPTION. first value is y-min and second value is y-max

    Returns
    -------
    None.

	'''
	xSpec=getSpecialPoints(path)
	ax=plt.gca()
	lm=ax.get_xlim()
	ax.set_ylim(energyRange)
	fig=plt.gcf()
	fig.set_size_inches(figsize)
	plt.axhline(0, lm[0], lm[1], linestyle='--', color='k', linewidth=1)
	plt.rc('axes', labelsize=xyLblSize, titlesize=xyLblSize)
	plt.rc('xtick', labelsize=numSize)
	plt.rc('ytick', labelsize=numSize)
	plt.rc('legend', fontsize=numSize)
	ax.set_xticks(xSpec)
	ax.set_xticklabels(lbl)

    
	for k in range(len(xSpec)):
		plt.axvline(xSpec[k], lm[0], lm[1], linestyle='--', color='k', linewidth=1)
	leg=plt.legend()
	for legobj in leg.legendHandles:
		legobj.set_linewidth(2.0)
	ax.set_xlabel('k')
	ax.set_ylabel('Energy (eV)')
	plt.tight_layout(pad=0)
	fig.show()
    
def removeColorbar():
	'''
	remove the colorbar from the active plot
	'''
	
	fig=plt.gcf()
	ax_list=fig.axes
    
	ax=ax_list[-1]
	ax.remove()
	plt.tight_layout(pad=0)

def removeLegend():
	'''
	remove the legend from the active plot
	'''
	ax=plt.gca()
	ax.get_legend().remove()
    
def plotDispersion(path, lbl, title='', energyRange=[-3,3], figsize=(3,2), xyLblSize=10, numSize=8, color='C0', alpha=1):
	'''
    Edits the active range of the currently active plot, sets the figure size, adds k-point labels, adds axis labels

    Parameters
    ----------
    path : STRING ending in //
        DESCRIPTION. Full path to folder where BANDLINES.OUT is found
    lbl : list
        DESCRIPTION. labels for the special points, to appear on the x-axis
    energyRange : list of length 2
        DESCRIPTION. first value is y-min and second value is y-max

    Returns
    -------
    None.

    '''
	fig=plt.gcf()
	plt.title(title, fontsize=xyLblSize)
	x, energies=readBandsFile(path)
    
	plt.xlim(min(x), max(x))
	plt.plot(x, energies, color=color, alpha=alpha)
	plotFinish(path, lbl, energyRange, figsize=figsize, xyLblSize=10, numSize=8)
	removeLegend()
	fig.show()
	return x, energies
def plotDispersionWithLegend(path, lbl, title='', energyRange=[-3,3], figsize=(3,2), xyLblSize=10, numSize=8, color='C0', alpha=1, label="", loc='best'):
	'''
    Edits the active range of the currently active plot, sets the figure size, adds k-point labels, adds axis labels

    Parameters
    ----------
    path : STRING ending in //
        DESCRIPTION. Full path to folder where BANDLINES.OUT is found
    lbl : list
        DESCRIPTION. labels for the special points, to appear on the x-axis
    energyRange : list of length 2
        DESCRIPTION. first value is y-min and second value is y-max

    Returns
    -------
    x : numpy array of floats, size=(n, )
        DESCRIPTION. numpy array of floats containing x-coordinates for plotting. Use getSpecialPoints() to extract special points for labeling
    energies : numpy array of float
        DESCRIPTION. Array of band energies, where each column is a separate band

	'''
	fig=plt.gcf()
	plt.title(title, fontsize=xyLblSize)
	x, energies=readBandsFile(path)
    
	plt.xlim(min(x), max(x))
	plt.plot(x, energies, color=color, alpha=alpha, label=label)
	plotFinish(path, lbl, energyRange, figsize=figsize, xyLblSize=10, numSize=8)
    
	handles, labels = plt.gca().get_legend_handles_labels()
	by_label = dict(zip(labels, handles))
	plt.legend(by_label.values(), by_label.keys(), loc=loc)
	fig.show()
	return x, energies

    

def calcEg(energy, Ef=0):
	'''
    Calculates Eg given where the Fermi level lies (defaults to 0 eV) and the energies

    Parameters
    ----------
    energy : numpy array of float
        DESCRIPTION. Array of band energies, where each column is a separate band
    Ef : float, default is 0 eV
        DESCRIPTION. Fermi energy

    Returns
    -------
    Egvect : 1-d numpy array
        DESCRIPTION. 
    gap : float
        DESCRIPTION. the actual gap, the minimum of Egvect
	idxVBmax : int
        DESCRIPTION. the index of the valence band maximum
	idxCBmin : int
        DESCRIPTION. the index of the conduction band minimum
	vb+Ef : 1-d numpy array
        DESCRIPTION. the y-values of the valence band
	cb+Ef : 1-d numpy array
        DESCRIPTION. the y-values of the conduction band

    '''
	r, c=energy.shape
	energy=energy-Ef
	Egv=np.zeros(r)
	vb=np.zeros(r)
	cb=np.zeros(r)
	Egvect=np.zeros(r)
	for idx in range(r):
		es=energy[idx, :]
		idxVb=np.where(np.sign(es[:-1])!=np.sign(es[1:]))[0]
		vb[idx]=es[idxVb]
		cb[idx]=es[idxVb+1]
		Egvect[idx]=es[idxVb+1]-es[idxVb]
	idxVBmax=np.argmax(vb)
	idxCBmin=np.argmin(cb)
	gap=cb[idxCBmin]-vb[idxVBmax]
    
	return Egvect, gap, idxVBmax, idxCBmin, vb+Ef, cb+Ef

