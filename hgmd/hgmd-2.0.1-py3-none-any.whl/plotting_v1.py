import os
import sys

from pymatgen.io.vasp.outputs import Vasprun, BSVasprun
from pymatgen.electronic_structure.plotter import BSDOSPlotter
from plotting import BSDOSPlotter, DOSPlotting, BSPlotting

import matplotlib.pyplot as plt
import plotting as pl

name = sys.argv[1]
# band
bsp = BSPlotting(vasprun="vasprun.xml")
para = pl._load_yaml("B_Parameter")
plt = bsp.get_plot(figsize=para["fig_size"],zero_to_efermi=para["zero_to_efermi"],
fontsize=para["fontsize"],xlim=para["xlim"],ylim=para["ylim"],color=para["color"],
vbm_cbm_marker=para["vbm_cbm_marker"],linewidth=para["linewidth"])
plt.savefig("{}_B.pdf".format(name))

plt.figure(figsize=(12,8))
# DOS
para = pl._load_yaml("D_Parameter")
f = open("dos","r")
filelist = f.readlines()[1:]
dp = DOSPlotting(vasprun="vasprun.xml",dos=filelist, zero_to_efermi=para["zero_to_efermi"],stack=para["stack"]) 
plt = dp.get_plot(figsize=para["fig_size"],xlim=para["xlim"],ylim=para["ylim"],fontsize=para["font_size"],color=para["color"])
plt.savefig("{}_D.pdf".format(name))
plt.figure(figsize=(11,8.5))
plt.rcParams["lines.linewidth"]=2
#BD
run = Vasprun("vasprun.xml",parse_dos=True)
dos = run.complete_dos
vrun = BSVasprun("vasprun.xml",parse_projected_eigen=True)
bs =vrun.get_band_structure('KPOINTS',efermi=dos.efermi)
bdpara=pl._load_yaml("BD_Parameter")
bsdosplot = BSDOSPlotter(bs_projection=bdpara['bs_projection'],
	dos_projection=bdpara['dos_projection'],
	vb_energy_range=bdpara['vb_energy_range'],
	cb_energy_range=bdpara['cb_energy_range'],
	fixed_cb_energy=bdpara['fixed_cb_energy'],
	egrid_interval=bdpara['egrid_interval'], 
	font=bdpara['font'], 
	axis_fontsize=bdpara['axis_fontsize'],
	tick_fontsize=bdpara['tick_fontsize'], 
	legend_fontsize=bdpara['legend_fontsize'],
	bs_legend=bdpara['bs_legend'],
	dos_legend=bdpara['dos_legend'],
	rgb_legend=bdpara['rgb_legend'], 
	fig_size=bdpara['fig_size'])
plt = bsdosplot.get_plot(bs, dos=dos)
plt.savefig("{}_BD.pdf".format(name))
