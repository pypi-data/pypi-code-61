#!/usr/local/anaconda3-2019.10/bin/python
# coding : utf-8
# Pymtagen Citation

import os
import sys
import time

import subprocess
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yaml
from shutil import copyfile

from pymatgen import Structure, Element
from pymatgen.symmetry.bandstructure import HighSymmKpath
from pymatgen.io.vasp.outputs import Vasprun

from autocalculation import Incar, shell, InputFile
from config import ShellPath
import plotting
from molecule import Molecule
import files

def division_number(list1):
	while True:
		try :
			if type(list1[0]) == int :
				options = int(input("Please Enter the option number >> "))
			elif type(list1[0]) == str :	
				options = str(input("Please Enter from %s >> "%(list1)))

			if options in list1:
				break
			else:
				print("It is not a number in option")
				print("Please try again")
		except :
			print("Please enter the correct number")
	return options

def print_option_result(method,number1,dictionary):
	string1 = "\n"+("="*number1)+" %s OPTIONS "%(method)+("="*number1)+"\n"
	print(string1)
	di = dictionary.items()
	string = ""
	for number,explain in di :
		if len(string) >= 50 :
			print(string+"\n")
			string = ""

		if type(number) == int :
			string +="%i) %s\t"%(number,explain)
		else :
			string +="%s - %s\t\t"%(number,explain)
	print(string+"\n")

def Split_structural_file(path) :	
	struclist=[];abs_path = os.path.abspath(path)
	if os.path.isfile(abs_path) :
		try :
			structure = Structure.from_file(abs_path)
			struclist.append(abs_path)
		except : 
			pass
	else :
		for j in os.listdir(abs_path):
			try : 
				structure = Structure.from_file("%s/%s"%(abs_path,j))
				struclist.append("%s/%s"%(abs_path,j))
			except : 
				pass

	if len(struclist) == 0 :
		print("There isn't file in This PATH %s"%(path))
		sys.exit(0)
	return struclist

pwd = os.getcwd()

print("+"+("-"*63)+"+")
print("|\t\tGMDKIT Version: 2.0.1 (07 Jul, 2020)\t\t|")
print("|\t\t %s \t\t\t|"%(time.strftime("%c", time.localtime(time.time()))))
print("+"+("-"*63)+"+")

print_option_result("FILE",26,
		{
		1:"Create graph.yaml"
		,2:"Create incar.yaml"
		,3:"Strain of structural file"
		,4:"Substituted"
		,5:"Convert INCAR to incar.yaml"
		})
print_option_result("MOLE",26,
		{
		11:"Random Position & Random Degree - MA"
		,12:"Random Position & Fixed Degree - MA"
		,13:"Fixed Position & Random Degree - MA (MOLE FILE)"
		,14:"Fixed Position & Fixed Degree - MA (MOLE FILE)"
		,15:"Random Positition & Random Degree - FA"
		,16:"Random Position & Fixed Degree - FA"
		,17:"Fixed Position & Random Degree - FA (MOLE FILE)"
		,18:"Fixed Position & Fixed Degree - FA (MOLE FILE)"
		})
print_option_result("CONFIG",24,
		{
		21:"Assign a shell script"
		,22:"Check the shell script"
		,23:"revise the shell"
		})
print_option_result("PLOT",26,
		{
		31:"Band Structure & DOS"
		,32:"Band Structure"
		,33:"DOS(Total)"
		,34:"Partial DOS(p-DOS)"
		,35:"Band Gap Check"
		})
print_option_result("AUTO CALCULATING",20,
		{
		41:"PBE-GGA"
		,42:"PBESol-GGA"
		,43:"SCAN-GGA"
		,44:"VDW-GGA"
		,45:"PBE-SOC"
		,46:"PBESol-SOC"
		,47:"SCAN-SOC"
		,48:"VDW-SOC"})
print("\n0) OUT\n")

## Check the Options
option_list=[0,1,2,3,4,5,
	11,12,13,14,15,16,17,18,
	21,22,23,
	31,32,33,34,35,
	41,42,43,44,45,46,47,48]
option1 = division_number(option_list)
print()

if option1 == 0 :
	sys.exit(0)

############ FILES OPTION
elif option1 == 1 :
	graph_list=["BD","B","D","All"]
	graph = division_number(graph_list)
	gy = files.graphyaml()
	if graph == "BD":
		data = gy["BD_Parameter"]
	elif graph == "B" :
		data = gy["B_Parameter"]
	elif graph == "D" :
		data = gy["D_Parameter"]
	elif graph == "All" :
		data = gy

	with open('graph.yaml','w') as out:
		yaml.dump(data,out,default_flow_style=False)
	print("Generate %s/graph.yaml file"%(os.getcwd()))

elif option1 == 2:	
	user_incar_settings={"SYSTEM":"Structure Optimization","PREC":"Accurate","ISTART":0,"ISPIN":1,"LREAL":"A","ENCUT":520,"IBRION":2,"ISIF":3,"EDIFF":1E-4,"EDIFFG":-1E-2,"NSW":500,"ALGO":"Normal","LCHARG":False,"LWAVE":False,"SIGMA":0.0}
	incar = division_number(["PBE","SOL","VDW","SCAN"])
	if incar == "PBE" :
		pass
	elif incar == "SOL" :
		user_incar_settings['GGA']='PS'
	elif incar == "VDW":
		user_incar_settings['IVDW']=21
	elif incar == "SCAN":
		user_incar_settings['METAGGA']='SCAN'

	with open('incar.yaml','w') as out:
		yaml.dump(user_incar_settings,out,default_flow_style=False)
	print("Generate the %s/incar.yaml file"%(os.getcwd()))

elif option1 == 3 or option1 == 4 :
	name = str(input("Please Enter the Structural File Name >> "))
	try :
		structure = Structure.from_file(os.path.abspath(name))
	except :
		print("Please Enter the Structural Filename")
		sys.exit(0)

	if option1 == 3 :
		strain = float(input("Please Enter the Strain Rate ex) 1%=0.01 >> "))
		structure.apply_strain(strain)
		structure.to(filename="POSCAR_%s_strain"%(structure.composition.reduced_formula))
		print("Generate the POSCAR file strained")
	elif option1 == 4:
		inputatom = files.print_error("Enter the atom to be substituted >> ")
		substitute = files.print_error("Enter the atom to substitute >> ")
		change = float(input("Enter the ratio >> "))
		if change > 1 :
			change = 1.0
		multiples = int(input("Enter the Number of repetitions >> ")) 
		directory = "FILES_OPTION_4_ratio_%.2f%%_to_%s_from_%s"%((change*100),inputatom,substitute)

		if not os.path.exists(directory) :
			os.makedirs(directory)
			os.chdir(directory)
			for i in range(multiples):
				structure = Structure.from_file(os.path.abspath(name))
				struc = files.Substitution(structure=structure,atom1 = inputatom, atom2 = substitute, ratio = change)
				struc.to(filename="POSCAR_%s_multiple_%i"%(structure.composition.reduced_formula,i+1))
		else :
			print("Error : Creating directory. " + directory)
		print("Generate %s/%s"%(os.getcwd(),directory))

elif option1 == 5 :
	filename = str(input("Please enter the INCAR filename >> "))
	abs_file = os.path.abspath(filename)
	dic = files.MakeIncarYaml(abs_file)
	with open("incar.yaml","w") as file :
		documnet = yaml.dump(dic, file)
	print("Sucessfully Generated %s/incar.yaml"%(os.path.abspath(".")))

########## MOLECULE OPTION
elif option1 == 11 or option1 == 12 or option1 == 13 or option1 == 14 or option1 == 15 or option1 == 16 or option1 == 17 or option1 == 18 :
	if option1 == 11 or option1 == 15  :
		mole = Molecule(random_coord = True, random_degree= True)
	elif option1 == 12 or option1 == 16:
		mole = Molecule(random_coord = True, random_degree= False)
	if option1 == 13 or option1 == 17:
		mole = Molecule(random_coord = False, random_degree= True)
	elif option1 == 14 or option1 == 18:
		mole = Molecule(random_coord = False, random_degree= False)

	if option1 == 11 or option1 == 12 or option1 == 13 or option1 == 14 :
		mafa == "MA" 
	else :
		mafa == "FA" 
	ms = Molecule._loadmolecule(mafa)
	struc_name = str(input("Please Enter the Structural File Name or PATH >> "))
	while True :
		inputcsv = str(input("If you want to save the csv file? (Y or N) >> "))
		if inputcsv == "Y" or inputcsv == "N" :
			break
		else :
			print("Please enter the Y or N\n")

	pwd = os.getcwd()
	cur = pwd.split(os.path.sep)[-1]
	file_ = os.path.abspath(struc_name)
	filename = os.path.basename(file_)

	inputatom, changenum, fixcalc, multiple = mole._inputinform()

	if fixcalc == None :
		cur1 = "%s_ration%.2f%%_multiple%i_from_%s_%s"%(cur,changenum*100,multiple,filename,mafa)
	else :
		cur1 = "%s_ration%.2f%%_multiple%i_selective%i_from_%s_%s"%(cur,(changenum*100),multiple,fixcalc,filename,mafa)

	from files import vaspname

	if os.path.isfile(file_):
		s = Structure.from_file(file_)
		vaspname_ = vaspname(s)
		for i in range(multiple):
			m = mole.tiltingmolecule(s, ms, inputatom=inputatom, changenum=changenum,fixcalc = fixcalc)
			m[0].to(filename="POSCAR_%s_multiple%i"%(vaspname_,i+1))
			if inputcsv == "Y" :
				m[1].to_csv("%s_%i.csv"%(vaspname_,i+1))
	else :
		filesum=0
		for j in os.listdir(file_):
			try :
				s = Structure.from_file("%s/%s"%(file_,j))
				vaspname_ = vaspname(s)
				for i in range(multiple):
					m = mole.tiltingmolecule(s, ms, inputatom=inputatom, changenum=changenum,fixcalc = fixcalc)
					m[0].to(filename="POSCAR_%s_multiple%i"%(vaspname_,filesum+1))
					if inputcsv == "Y" :
						m[1].to_csv("%s_%i.csv"%(vaspname_,filesum+1))
			except :
				pass
	os.makedirs(os.path.join(cur1),exist_ok=True)
	os.system("mv %s/POSCAR_*_multiple* %s/%s"%(pwd,pwd,cur1))
	if inputcsv == "Y" :
		os.system("mv %s/*.csv %s/%s"%(pwd,pwd,cur1))
	print("Generate %s/%s"%(pwd,cur1))

#### CONFIG
elif option1 == 21 or option1 == 22 :
	config = ShellPath()
	shellpath = config.shellpath
	files = config.files
	if option1 == 21 :
		shell_name,add_shell = map(str,input("Please enter the shell name to be added and the sehll to be saved >> "))
		copyfile(shell_name, "%s/%s"%(shellpath,add_shell))
		print("%s/%s Successfully Save "%(shellpath,add_shell))
	elif option1 == 22 :
		shell = [sh for sh in files if sh.split(".") == "sh"]
		if len(shell) != 1 :
			print("shell script are",shell)
		else :
			print("shell script is",shell[0])

#### PLOTTING 
elif option1 == 31 or option1 == 32 or option1 == 33 or option1 == 34 or option1 == 35 :
	if option1 == 31 or option1 == 32 or option1 == 33 or option1 == 34 :
		plt = None
		out_file = str(input("If you want to save the Plotting File,Please Enter the filename (If you doesn't it, Please enter the N) >> "))
		if out_file == "N" :
			out_file = None
	else :
		pass

	if option1 == 31 or option1 == 32 or option1 == 35 :
		bsp = plotting.BSPlotting(vasprun = "vasprun.xml")
		if option1 == 35 :
			bsp.Band_Inform()
			sys.exit(0)
		elif option1 == 31 :
			if plotting.read_yaml()["name"] == "All" :
				dpara = plotting.read_yaml()["BD_Parameter"]
			elif plotting.read_yaml()["name"] == "BD_Parameter":
				dpara = plotting.read_yaml()
			else :
				sys.exit(0)
			plt = bsp.PlotBDosplotting(dpara)
		elif option1 == 32:
			if plotting.read_yaml()["name"] == "All" :
				bpara = plotting.read_yaml()["B_Parameter"]
			elif plotting.read_yaml()["name"] == "B_Parameter" :
				bpara = plotting.read_yaml()
			else :
				sys.exit(0)
			plt = bsp.PlotBandStructure(zero_to_efermi=bpara['zero_to_efermi'],
				ylim = bpara['ylim'], 
				smooth = bpara['smooth'],
				smooth_tol=bpara['smooth_tol'],
				vbm_cbm_marker=bpara['vbm_cbm_marker'],
				fig_size=bpara['fig_size'],
				color=bpara['color'],
				shape=bpara['shape'],
				fontsize=bpara['fontsize'],
				band_linewidth=bpara['band_linewidth'],
				xlim_index=bpara['xlim_index'])

	elif option1 == 33 or option1 == 34 :
		if plotting.read_yaml()["name"] == "All":
			dpara = plotting.read_yaml()["D_Parameter"]
		elif plotting.read_yaml()["name"] == "D_Parameter" :
			dpara = plotting.read_yaml()
		else :
			sys.exit(0)
		width = dpara["width"];interval = dpara["interval"]
		zero_to_efermi = dpara["zero_to_efermi"];stack = dpara["stack"]
		xlim = dpara["xlim"];ylim = dpara["ylim"]
		figsize = dpara["fig_size"];fontsize = dpara["font_size"]
		path = os.path.normpath("%s/pdos/pdos"%(os.path.split(__file__)[0]))
		if option1 == 33 :
			os.system("%s dos width=%f interval=%f"%(path,width,interval))
			f = open("dos",'r')
			filelist = f.readlines()[1:]
			dp = plotting.DOSPlotting("vasprun.xml",width = width, interval = interval, zero_to_efermi = zero_to_efermi, stack = stack,dos_list=filelist)
			plt = dp.gmd_plotting(fig_size=figsize, xlim=xlim, ylim=ylim, fontsize=fontsize)
			plt.plot(dp.energies,dp.densities,color='r',label="Total DOS")
			plt.legend()

		elif option1 == 34 :
			for f in os.listdir(os.getcwd()):
				if f == "LIST":
					ff = open("LIST","r")
					name = ff.readlines()[0].split()[0]
			os.system("%s pdos width=%f interval=%f"%(path,width,interval))
			f1 = open("%s.dos"%(name),"r")
			filelist = f1.readlines()[1:]	
			dp = plotting.DOSPlotting("vasprun.xml",width = width, interval = interval, zero_to_efermi = zero_to_efermi, stack = stack,dos_list=filelist)
			plt = dp.gmd_plotting(fig_size=figsize, xlim=xlim, ylim=ylim, fontsize=fontsize)
			plt.plot(dp.energies,dp.densities,color='r',label=name)
			plt.legend()
		else :
			print("Prepare")

	if plt :
		if out_file :
			plt.savefig("%s.pdf"%(out_file))
			print("Generate %s/%s.pdf"%(os.getcwd(),out_file))
		else :
			plt.show()
	else :
		print("It can't be being plotted")
		sys.exit(0)

#### AUTOCALCULATION
elif option1 == 41 or option1 == 42 or option1 == 43 or option1 == 44 or option1 == 45 or option1 == 46 or option1 == 47 or option1 == 48 :

	if option1 == 41 or option1 == 45 :
		method1 = "PBE"
	elif option1 == 42 or option1 == 46 :
		method1 = "PBESol"
	elif option1 == 43 or option1 == 47 :
		method1 = "SCAN"
	elif option1 == 44 or option1 == 48 :
		method1 = "VDW"
	else :
		print("prepare")

	newlist=[];direc={}
	print_option_result("MODE SELECT",25,{"R" : "RELAXATION" , "C" : "MAKE_CHGCAR", "B" : "BAND CALCAULTION",
				"RC" : "RELAXATION & MAKE_CHGCAR" , "CB" : "CHGCAR & BAND CALCAULTION" ,
				"RCB" : "RELAXATION & MAKE_CHGCAR & BAND CALCULATION"})
	auto_option_list = ["R","C","B","RC","CB","RCB"]
	cal = list(division_number(auto_option_list))
	struc_name = str(input("Please Enter the Structural File Name or PATH >> "))
	struclist = Split_structural_file(os.path.abspath(struc_name))
	newlist.append(cal)
	newlist.append(struclist)
	if option1 == 41 or option1 == 42 or option1 == 43 or option1 == 44 :
		direc["GGA"] = newlist
	else :
		direc["SOC"] = newlist

	shell = [sh for sh in ShellPath().files if sh.split(".")[1] == "sh"]
	running = division_number(shell)

	f = open("%s/calnohup.py"%(os.path.dirname(__file__)),'r')
	ff = f.readlines()		
	ff.insert(0,'method1="%s"\n'%(method))
	ff.insert(1,'direct='+str(direc)+'\n')
	ff.insert(2,'running='+str(args.run)+'\n')
	ff.insert(3,"ds='N'\n")
	with open("%s/running_test_nohup.py"%(os.path.dirname(__file__)),"w") as fi :
		for i in ff :
			fi.write(i)
	fi.close()
	os.system('nohup python -u %s/running_test_nohup.py &'%(os.path.dirname(__file__)))

else :
	print("Preparing")
