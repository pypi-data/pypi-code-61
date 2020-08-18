import os
import sys

import numpy as np
import random as rd
import subprocess
from collections import Counter
import yaml

from pymatgen import Element
from pymatgen.core import Structure
from pymatgen.io.vasp.outputs import Vasprun, BSVasprun
from pymatgen.io.vasp.inputs import Incar

def print_error(string):
	try : 
		atom = str(input(string)) 
		Element(atom)
	except :
		print("There isn't the element")
		sys.exit(1)
	return atom 

def Substitution(structure,atom1,atom2,ratio):
	'''
	Return Structure that Substituted other Elements

	Args : 
		atom1(str) : Elements in the structure 
		atom2(str) : Element to substitute
		ratio(float) : Ratio of Elements to be substituted

	Returns :
		Structure
	'''
	index=[]
	for i in range(structure.num_sites):
		if structure.species[i].symbol == Element(atom1).symbol :
			index.append(i)
	chagenum = round(ratio*len(index))
	random_ele = rd.sample(index,chagenum)
	for i in random_ele :
		structure.replace(i,atom2)
	return structure

def MakeIncarYaml(filename):
	incar = Incar.from_file(filename)
	incardic = incar.as_dict()
	del incardic["@module"]
	del incardic["@class"]
	return incardic

def vaspname(structure):
	result = Counter(structure.species)
	vaspname = ""
	for ele,number in result.items():
		if number == 1 :
			vaspname += ele.symbol
		else :
			vaspname += ele.symbol+str(number)
	return vaspname

def graphyaml():
	data = dict(
		name = "Test",
		BD_Parameter = dict(
			bs_projection = 'elements', 
			dos_projection =  'elements', 
			vb_energy_range= 4, 
			cb_energy_range= 4, 
			fixed_cb_energy= False, 
			egrid_interval= 2, 
			font= 'Arial', 
			axis_fontsize= 20, 
			tick_fontsize= 15, 
			legend_fontsize= 14, 
			bs_legend= 'best', 
			dos_legend= 'best', 
			rgb_legend= True, 
			fig_size= (11,8.5)
		),
		B_Parameter = dict(
			fig_size= (12,8), 
			zero_to_efermi= True, 
			fontsize= 20, 
			xlim= None,
			ylim= (-4,4), 
			color = 'b',
			vbm_cbm_marker= True, 
			linewidth= 1
		),
		D_Parameter = dict(
			zero_to_efermi=True,
			stack=True,
			fig_size= (12,8),
			xlim= (-4,4), 
			ylim= None, 
			font_size= 30,
			color="r"
		)
	)
	return data

def strain_lattice(structure,strain) :
	s = Structure.from_file(structure)
	s.apply_strain(strain)
	s_dic = s.as_dict()
	for i in s_dic['sites'] :
		if not 'oxidation_state' in i['species'][0].keys():
			s.to(filename="POSCAR_%.3f%%"%(strain*100))
			sys.exit(1)

	for i in range(len(s.species)):
		s.replace(i,s.species[i].element)
	return s
	s.to(filename="POSCAR_%.3f%%"%(strain*100))

def generate_inpcar(path,kpoints):
	abspath = os.path.abspath(path)
	os.chdir(abspath)

	vrun = Vasprun("vasprun.xml")
	lattice = vrun.final_structure.lattice
	aa =subprocess.check_output(['grep','NELECT','OUTCAR'])
	bandnumber = aa.split()[2].decode("utf-8")

	with open("INPCAR",'w') as fi :
		for i in kpoints :
			fi.write("%s "%(i))
		fi.write("\n")
		fi.write("0.01\n")
		for i in kpoints :
			fi.write("%.0f "%(float(i)))
		fi.write("\nV\n%s"%(str(lattice)))
	fi.close()

def analyze_files(args) :
	if args.graph :
		gy = graphyaml()
		if args.graph == "BD" :
			data = gy["BD_Parameter"]
			data["name"] = "BD_Parameter"
		elif args.graph == "B" :
			data = gy["B_Parameter"]
			data["name"] = "B_Parameter"
		elif args.graph == "D" :
			data = gy["D_Parameter"]
			data["name"] = "D_Parameter"
		elif args.graph == "All" :
			data = gy
			data["name"] = "All"
		with open('graph.yaml','w') as out:
			yaml.dump(data,out,default_flow_style=False)
		print("generate the graph.yaml file")

	elif args.strain :
		structure = os.path.abspath(args.strain[0])
		strain = float(args.strain[1])
		s = Structure.from_file(structure)
		s.apply_strain(strain)
		s.to(filename="POSCAR_%.2f%%"%(strain*100))
		print(s.volume)

	elif args.substitution :
		if len(args.substitution) != 2 :
			print("Please enter two option")
			sys.exit(1)
		pwd = os.path.abspath(args.substitution[0])
		name = os.path.split(os.path.abspath(args.substitution[0]))[-1]
		inputatom = print_error("Enter the atom to be substituted >> ")
		substitute = print_error("Enter the atom to substitute >> ")
		change = float(input("Enter the ratio >> "))
		if change > 1 :
			change = 1.0 
		directory = "%s_ratio_%.2f%%_to_%s_from_%s"%(name,(change*100),inputatom,substitute)
		if not os.path.exists(directory) :
			os.makedirs(directory)
			os.chdir("./%s"%(directory))

			for i in range(int(args.substitution[1])):
				struc = Structure.from_file(pwd)
				struc = Substitution(struc,atom1 = inputatom, atom2 =  substitute, ratio=change)
				struc.sort()
				struc.to(filename="POSCAR_%s_multiple_%i"%(name,i+1))
		else :
			print("Error : Creating directory. " + directory)
			
	elif args.incar:
		incar_method={"SYSTEM":"Structure Optimization","PREC":"Accurate","ISTART":0,"ISPIN":1,"LREAL":"A","ENCUT":520,"IBRION":2,"ISIF":3,"EDIFF":1E-4,"EDIFFG":-1E-2,"NSW":500,"ALGO":"Normal","LCHARG":False,"LWAVE":False,"SIGMA":0.05,'ISMEAR':0}
		if args.incar == "PBE" :
			user_incar_settings = incar_method
		elif args.incar == "SOL" :
			user_incar_settings = incar_method
			user_incar_settings['GGA']='PS'
		elif args.incar == "VDW":
			user_incar_settings = incar_method
			user_incar_settings['IVDW']=21
		elif args.incar == "SCAN":
			user_incar_settings = incar_method
			user_incar_settings['METAGGA']='SCAN'
		with open('incar.yaml','w') as out:
			yaml.dump(user_incar_settings,out,default_flow_style=False)
		print("generate the incar.yaml file")

	elif args.makeincar :
		incar = MakeIncarYaml(args.makeincar[0])
		with open("incar.yaml","w") as file :
			documnet = yaml.dump(incar, file)
		print("Successfully Generated %s/incar.yaml"%(os.path.abspath("."))) 	
	elif args.inpcar :
		print("prepare")
		#generate_inpcar(path,bn)
