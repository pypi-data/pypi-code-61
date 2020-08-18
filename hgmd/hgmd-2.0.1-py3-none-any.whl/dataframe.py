# -*- coding: utf-8 -*
import os
import sys

import pandas as pd

from pymatgen.io.vasp.outputs import Vasprun, BSVasprun
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

class Dataframe :
	def structure_list(structure):
		list1=[]
		list1.append(structure.lattice.abc)
		list1.append(structure.lattice.angles)
		return list1

	def make_csv(vrun):
		csv_base_path = "%s/data/Perovskite_data.csv"%(os.path.split(os.path.dirname(__file__))[0])
		structure = vrun.final_structure
		kpoints = vrun.kpoints 
		incar = vrun.incar
		vrun_dic = vrun.as_dict()

		base_df = pd.read_csv(csv_base_path,index_col=False)
		df = pd.DataFrame({'ID':"GMD-%i"%(len(base_df)+1),
				'Perovskites':vrun_dic['pretty_formula']},
				index=[0],columns=['ID','Perovskites'])

		unitcell = vrun_dic['unit_cell_formula']
		unitstring = ''
		for i in unitcell :
			unitstring+=i
			unitstring+="%i"%(int(unitcell[i]))
		element=0;formula=0
		for j in unitcell.values() :
			element+= j
		for i in vrun_dic['reduced_cell_formula'].values(): 
			formula+=i

		formulaunit = int(element/formula)
		if 'H' and 'C' and 'N' in unitcell :
			a=1
			if int(unitcell['N']/unitcell['C']) == 2 :
				df['E%i'%(a)] = 'FA'
				df['N%i'%(a)] = unitcell['C']
				a+=1
			else :
				df['E%i'%(a)] = 'MA'
				df['N%i'%(a)] = unitcell['C']
				a+=1
			del unitcell['H']
			del unitcell['C']
			del unitcell['N']

			for j in unitcell.keys():
				df['E%i'%(a)] = j
				df['N%i'%(a)] = int(unitcell[j]/formulaunit)
				a+=1
			for i in range(a,5):
				df['E%i'%(i)]=''
				df['N%i'%(i)]=''
		else :
			a=1
			for j in unitcell.keys():
				df['E%i'%(a)] = j
				df['N%i'%(a)] = int(unitcell[j])
				a+=1
			for i in range(a,5):
				df['E%i'%(i)]=''
				df['N%i'%(i)]=''
		# Reference
		df['Refence'] = None 

		# SpaceGroup
		finder=SpacegroupAnalyzer(structure)
		space_group = '%s[%s]'%(finder.get_space_group_symbol(),finder.get_space_group_number())
		df['Space Group']= space_group
		df['Method']='Calc'

		#Structure_inform
		struc_list = Dataframe.structure_list(structure)
		df['Structure'] = 'a=%.4f\nb=%.4f\nc=%.4f\nal=%.4f\nbe=%.4f\nga=%.4f'%(struc_list[0][0],struc_list[0][1],struc_list[0][2],struc_list[1][0],struc_list[1][1],struc_list[1][2])

		#Primitive
		primitive = structure.get_primitive_structure()
		if structure == primitive : 
			df['Stucture_Prim']=''
		else :
			prim_list = Dataframe.structure_list(primitive)
			df['Structure_Prim'] = 'a=%.4f\nb=%.4f\nc=%.4f\nal=%.4f\nbe=%.4f\nga=%.4f'%(prim_list[0][0],prim_list[0][1],prim_list[0][2],prim_list[1][0],prim_list[1][1],prim_list[1][2])

		# Run type & Encut 
		if 'GGA' in vrun.incar.keys() :
			df['Run Type'] = 'PBESol' 
		elif 'IVDW' in vrun.incar.keys() :
			df['Run Type'] = 'VDW' 
		elif 'METAGGA' in vrun.incar.keys() :
			df['Run Type'] = 'SCAN' 
		else :
			df['Run Type'] = 'PBE'
		df['Cut off'] = int(incar['ENCUT'])

		# KPOINTS
		kpoints = kpoints.kpts[0]
		df['KPOINTS']='%i %i %i\n0 0 0'%(kpoints[0],kpoints[1],kpoints[2])

		# Pseudo Pot
		potcar = vrun_dic['input']['potcar']
		fi=''
		for i in potcar :
			fi+=i+'\n'	
		df['Pseudo Pot']=fi
		epera = vrun_dic['output']['final_energy_per_atom']

		df['E/Atom'] = '%.3f'%(epera)
		df['E/FU'] = '%.3f'%(vrun.final_energy/formulaunit)
		df['Total Energy'] = vrun.final_energy
		df['#Atom'] = int(element)
		df['#FU'] = formulaunit
		df['PATH'] = os.getcwd()

		for u,i,j in zip(base_df['ID'],base_df['Structure'],base_df['Total Energy']) :
			for e,k in zip(df['Structure'],df['Total Energy']) :
				if i == e and j == k :
					print("The same data exists in %s"%(u))
					sys.exit(1)

		df1 = pd.concat([base_df,df],ignore_index=True,sort=False)
		df1.to_csv(csv_base_path,index=False,index_label="Numbering")
		print(df)
		print(structure)

def analyze_argument(args):
	if args.save :
		vrun = Vasprun("vasprun.xml")
		Dataframe.make_csv(vrun)

