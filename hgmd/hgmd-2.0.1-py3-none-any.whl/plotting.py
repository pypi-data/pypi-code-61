import os
import sys

import numpy as np
import pandas as pd
import scipy.interpolate as sci
import yaml
import palettable
import matplotlib.pyplot as plt

from pymatgen.io.vasp.outputs import Vasprun, BSVasprun
from pymatgen.electronic_structure.plotter import BSPlotter, DosPlotter, BSDOSPlotter
from pymatgen.electronic_structure.core import Spin, OrbitalType

def error(phrase):
	r = "\n\n"+"#"*40+"\n\n"
	print(r+parse+r)

def _load_yaml(paraname):
	pwd = os.getcwd()
	abspath = os.path.dirname(__file__)
	graph = "{}/graph.yaml".format(abspath)
	if os.path.isfile("{}/graph.yaml".format(pwd)):
		graph = "{}/graph.yaml".format(pwd)
	stream = open(graph,"r")
	loading = yaml.load(stream)
	if loading["name"] == "All":
		para = loading[paraname]
	elif loading["name"] == paraname:
		para = loading
	else :
		error("This is not {}\nPlease check last line in graph.yaml file".format(paraname))
		sys.exit(1)
	return para

class DOSPlotting :
	def __init__(self, vasprun="vasprun.xml",dos=None, zero_to_efermi=True, stack=True) :
		self.zero_to_efermi = zero_to_efermi 
		self.stack = stack
		self.efermi = Vasprun("vasprun.xml").efermi
		self.energies = [float(i.split()[0])-self.efermi if self.zero_to_efermi else float(i.split()[0]) for i in dos]
		self.densities = [float(i.split()[1]) for i in dos]
	
	def get_plot(self, figsize=(12,8), xlim=None, ylim=None, fontsize=30,color="r") :
		plt.rcParams['font.family']='Arial'
		plt.rcParams['figure.figsize']=figsize
		plt.rcParams['font.size']=fontsize
		plt.rcParams['lines.linewidth'] = 3
		plt.rcParams['axes.linewidth'] = 3

		allpts = []
		allpts.extend(list(zip(self.energies, self.densities)))

		if xlim :
			plt.xlim(xlim)
		if ylim :
			plt.ylim(ylim)
		else :
			xlim = plt.xlim()
			relevanty = [p[1] for p in allpts if xlim[0] < p[0] < xlim[1]]
		plt.ylim((min(relevanty),max(relevanty)))

		if self.stack :
			plt.fill_between(self.energies,0,self.densities,color='r',alpha=.1)
		if self.zero_to_efermi :
			ylim = plt.ylim()
			plt.plot([0,0], ylim, 'k--', linewidth=2)

		plt.xlabel("Energies(eV)")
		plt.ylabel("Density of States")

		plt.plot(self.energies, self.densities, color=color, label="Total DOS")
		plt.tight_layout()
		return plt

class BSPlotting :
	def __init__(self, vasprun="vasprun.xml"):
		self.vrun = Vasprun(vasprun,parse_dos=True)
		self.bsrun = BSVasprun(vasprun,parse_projected_eigen=True)
		self.bs = self.bsrun.get_band_structure("KPOINTS",efermi=self.vrun.efermi)
		self.bsp = BSPlotter(self.bs)
		self.data =self.bsp.bs_plot_data()

	def band_inform(self):
		ad = self.bsrun.as_dict()['output']

		bandgap = "%.3f(Indirect)"%(ad['bandgap'])
		if ad['is_gap_direct'] :
			bandgap = "%.3f(Direct)"%(ad['bandgap'])

		print("\nnumber of bands : {}".format(self.bs.nb_bands))
		print("fermi energy : %.3f"%(self.bs.efermi))
		print("band gap : {}\n".format(bandgap))

	def get_plot(self,figsize=(12,8),zero_to_efermi=True,fontsize=20,xlim=None,ylim=None,color='b',vbm_cbm_marker=True,linewidth=1):
		import scipy.interpolate as scint
		from pymatgen.util.plotting import pretty_plot

		ad = self.bsrun.as_dict()['output']
		bandgap = "%.3f(Indirect)"%(ad['bandgap'])
		if ad['is_gap_direct'] :
			bandgap = "%.3f(Direct)"%(ad['bandgap'])
		print("band gap : {}".format(bandgap))

		plt = pretty_plot(figsize[0],figsize[1])

		plt.rcParams['lines.linewidth'] = linewidth
		plt.rcParams['font.size'] = fontsize

		for d in range(len(self.data['distances'])):
			for i in range(self.bs.nb_bands):
				plt.plot(self.data['distances'][d],
					[self.data['energy'][d][str(Spin.up)][i][j] 
					for j in range(len(self.data['distances'][d]))],
					color=color, ls='-')
				if self.bsp._bs.is_spin_polarized :
					plt.plot(self.data['distances'[d],
						[self.data['energy'][d][str(Spin.up)][i][j] 
						for j in range(len(self.data['distances'][d]))]],
						color='r', ls='-')
		self.bsp._maketicks(plt)
		plt.xlabel(r'$\mathrm{Wave\ Vector}$', fontsize=30)
		ylabel = r'$\mathrm{E\ -\ E_f\ (eV)}$' if zero_to_efermi \
            else r'$\mathrm{Energy\ (eV)}$'
		plt.ylabel(ylabel)

		if xlim is None :
			plt.xlim(0, self.data['distances'][-1][-1])
		else :
			xlim_list = sorted(set(self.bsp.get_ticks()['distance']))
			if xlim_index[-1] > len(xlim_list):
				error("Out of the index\nPlease Chekc the KPOINTS file")
				sys.exit(1)
			plt.xlim(xlim_list[xlim[0]-1], xlim_list[xlim[0]-1])

		if ylim is None :
			emin = -10 ; emax=10
			if self.bsp._bs.is_metal():
				if zero_to_efermi:
					plt.ylim(emin, emax)
				else :
					plt.ylim(self.vrun.efermi+emin, self.vrun.efermi+emax)
			else :
				if vbm_cbm_marker :
					for cbm in self.data['cbm']:
						plt.scatter(cbm[0], cbm[1], color='r', marker='o', s=100)
					for vbm in self.data['vbm']:
						plt.scatter(vbm[0], vbm[1], color='g', marker='o', s=100)
				plt.ylim(self.data['vbm'][0][1] + emin, self.data['cbm'][0][1]+emax)
		else :
			plt.ylim(ylim)
			if not self.bsp._bs.is_metal() and vbm_cbm_marker:
				for cbm in self.data['cbm']:
					plt.scatter(cbm[0], cbm[1], color='r', marker='o',s=100)
				for vbm in self.data['vbm']:
					plt.scatter(vbm[0], vbm[1], color='g', marker='o',s=100)
			plt.tight_layout()

		if not zero_to_efermi :
			ef = self.vrun.efermi
			plt.axhline(ef, linewidth=linewidth, color='k', ls="--")
		else :
			ax = plt.gca()
			xlim = ax.get_xlim()
			ax.hlines(0, xlim[0], xlim[1], linestyles="dashed", color='k')

		if self.bsp._bs.is_spin_polarized :
			ax.plot((),(),color=color,ls='-',label="spin up")
			ax.plot((),(),color='r',ls='-',label="spin dwon")
			ax.legend(loc="upper left")
		return plt

def analyze_plot(args):
	plt=None;path=args.path
	
	if args.band or args.bandcheck :
		bsp = BSPlotting(vasprun=path) #line the path of vasprun.xml using the argument
		if args.bandcheck :
			bsp.band_inform()
		elif args.band :
			para = _load_yaml("B_Parameter")
			plt = bsp.get_plot(figsize=para["fig_size"],zero_to_efermi=para["zero_to_efermi"],
			fontsize=para["fontsize"],xlim=para["xlim"],ylim=para["ylim"],color=para["color"],
			vbm_cbm_marker=para["vbm_cbm_marker"],linewidth=para["linewidth"])

	elif args.dos or args.partial :
		para = _load_yaml("D_Parameter")
		if args.dos :
			f = open("dos","r")
			filelist = f.readlines()[1:]
			dp = DOSPlotting(vasrpun=path,dos=filelist, zero_to_efermi=para["zero_to_efermi"],stack=para["stack"]) 
			plt = dp.get_plot(figsize=para["fig_size"],xlim=para["xlim"],ylim=para["ylim"],
			fontsize=para["font_size"],color=para["color"])
		if args.partial :
			f = open("LIST.dos","r")
			filelist=f.readlines()[1:]
			dp = DOSPlotting(vasprun=path,dos=filelist)
			plt = dp.get_plot(figsize=para["fig_size"],xlim=para["xlim"],ylim=para["ylim"],
			fontsize=para["font_size"],color=para["color"])

	elif args.bdos :
		run = Vasprun(path,parse_dos=True)
		dos = run.complete_dos
		vrun = BSVasprun(path,parse_projected_eigen=True)
		bs =vrun.get_band_structure('KPOINTS',efermi=dos.efermi)

		bdpara=_load_yaml("BD_Parameter")
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

	if plt :
		if args.out_file :
			plt.savefig("%s.%s"%(args.out_file,args.format))
		else :
			plt.show()