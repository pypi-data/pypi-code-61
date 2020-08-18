import os
import sys
import time
import glob
import subprocess
from collections import Counter
from shutil import copyfile,move
import yaml
import numpy as np

from pymatgen import Structure
from pymatgen.io.vasp.sets import MPRelaxSet, DictSet
from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.io.vasp.inputs import VaspInput
from pymatgen.symmetry.bandstructure import HighSymmKpath

import autocalculation

cal_type = mpath[0]
mode = mpath[1][0]
path = mpath[1][1]

pwd = os.getcwd()

def running_mode(list1,list2) :
	pwd = os.getcwd()
	for j in list1 :
		os.chdir(os.path.join(pwd,j))
		if cal_type == "GGA" :
			try :
				autocalculation.read_vaspscript(list2[0][0],list2[0][1])
			except :
				autocalculation.read_vaspscript(list2[0][0],j)
		elif cal_type == "SOC" :
			try :
				autocalculation.SOC_vaspscript(list2[0][0],list2[0][1])
			except :
				autocalculation.SOC_vaspscript(list2[0][0],j)
		subprocess.check_call(['qsub','vasp.sh'])	

def running_time(folder1,string) :
	while True :
		checklist=[]
		for j in folder1 :
			os.chdir(os.path.join(pwd,j))
			try :
				finalstruc = Vasprun("vasprun.xml").final_structure
				aa = subprocess.check_output(['tail','-n','1','OSZICAR']).decode('utf-8')
				time.sleep(10)
				if int(aa.split()[0]) == Vasprun("vasprun.xml").as_dict()['input']['incar']['NSW'] :
					print("%s is Non-PASS"%(j))
					subprocess.call(['rm','vasprun.xml'])
					folder_list = [folder for folder in os.listdir(".") if folder.endswith("initial")]
					subprocess.call(['cp','POSCAR','POSCAR_%i_initial'%(len(folder_list))])
					subprocess.call(['cp','CONTCAR','POSCAR'])
					subprocess.check_call(['qsub','vasp.sh'])	
					time.sleep(10)
				else :
					print("PASS")
					checklist.append(finalstruc)
			except : 
				pass
		if len(folder1) == len(checklist) :
			break
	print("Finished %s"%(string))
	return checklist
	
struclist=[]
abspath = os.path.abspath(path)
if os.path.isfile(abspath):
	struclist.append(os.path.split(abspath)[0])
	struclist.append(autocalculation.delete_oxidation(abspath))
else :
	struclist.append(abspath)
	for j in os.listdir(abspath) :
		try :
			struclist.append(autocalculation.delete_oxidation(os.path.join(abspath,j)))
		except :

			pass
# relaxation
if mode == "r" :
	del(user_incar_settings["EDIFFG"]) 
	if cal_type == "GGA" :
		folder1 = autocalculation.vaspinfo(struclist,user_incar_settings,"R_mode")
		running_mode(folder1,running)
		checklist1 = running_time(folder1,"R_mode")
	if cal_type == "SOC" :
		user_incar_settings['MAGMOM']=None
		folder1 = autocalculation.vaspinfo(struclist,user_incar_settings,"R_SOCmode")
		running_mode(folder1,running)
		checklist1 = running_time(folder1,"R_SOCmode")

elif mode == "c" :
	user_incar_settings['NSW']=0
	user_incar_settings['LCHARG']=True
	user_incar_settings['EDIFF']=1E-6

	if cal_type == "GGA" :
		folder1 = autocalculation.vaspinfo(struclist,user_incar_settings,"C_mode")
		running_mode(folder1,running)
		checklist1 = running_time(folder1,"C_mode")
	elif cal_type == "SOC" :
		user_incar_settings['MAGMOM']=None
		folder1 = autocalculation.vaspinfo(struclist,user_incar_settings,"C_SOCmode")
		running_mode(folder1,running)
		checklist1 = running_time(folder1,"C_SOCmode")
elif mode == "b" :
	user_incar_settings['NSW']=0
	user_incar_settings['LCHARG']=False
	user_incar_settings['ICHARG']=11
	user_incar_settings['EDIFF']=1E-6
	if cal_type == "GGA" :
		folder = autocalculation.vaspinfo(struclist,user_incar_settings,"B_mode")
		chgcar_path = os.path.split(os.path.abspath(path))[0]

		if len(folder) != 1 :
			print("Please enter the structure path")
			sys.exit(1)

		structure = Structure.from_file("%s/POSCAR"%(os.path.abspath(folder[0])))
		copyfile("%s/CHGCAR"%(chgcar_path),'%s/CHGCAR'%(os.path.abspath(folder[0])))
		kpath_info = HighSymmKpath(structure).kpath['kpoints']
		kpath = HighSymmKpath(structure).kpath['path'][0]
		with open('%s/KPOINTS'%(os.path.abspath(folder[0])),'w') as fi :
			fi.write('kpoints\n21\nL\nR\n')
			for i in range(len(kpath)-1):
				fi.write('%.3f %.3f %.3f !%s\n'%(kpath_info[kpath[i]][0],kpath_info[kpath[i]][1],kpath_info[kpath[i]][2],kpath[i]))
				fi.write('%.3f %.3f %.3f !%s\n'%(kpath_info[kpath[i+1]][0],kpath_info[kpath[i+1]][1],kpath_info[kpath[i+1]][2],kpath[i+1]))
				fi.write('\n')
		running_mode(folder,running)
		checklist1 = running_time(folder,"B_mode")
	elif cal_type == "SOC" :
		folder = autocalculation.vaspinfo(struclist,user_incar_settings,"B_SOCmode")
		chgcar_path = os.path.split(os.path.abspath(path))[0]

		if len(folder) != 1 :
			print("Please enter the structure path")
			sys.exit(1)

		structure = Structure.from_file("%s/POSCAR"%(os.path.abspath(folder[0])))
		copyfile("%s/CHGCAR"%(chgcar_path),'%s/CHGCAR'%(os.path.abspath(folder[0])))
		kpath_info = HighSymmKpath(structure).kpath['kpoints']
		kpath = HighSymmKpath(structure).kpath['path'][0]
		with open('%s/KPOINTS'%(os.path.abspath(folder[0])),'w') as fi :
			fi.write('kpoints\n21\nL\nR\n')
			for i in range(len(kpath)-1):
				fi.write('%.3f %.3f %.3f !%s\n'%(kpath_info[kpath[i]][0],kpath_info[kpath[i]][1],kpath_info[kpath[i]][2],kpath[i]))
				fi.write('%.3f %.3f %.3f !%s\n'%(kpath_info[kpath[i+1]][0],kpath_info[kpath[i+1]][1],kpath_info[kpath[i+1]][2],kpath[i+1]))
				fi.write('\n')
		running_mode(folder,running)
		checklist1 = running_time(folder,"B_SOCmode")

elif mode == "rc" :
	#relaxation
	del(user_incar_settings["EDIFFG"])
	
	if cal_type == "GGA" :
		folder1 = autocalculation.vaspinfo(struclist,user_incar_settings,"R_mode")
		running_mode(folder1,running)
		checklist1 = running_time(folder1,"R_mode")
	elif cal_type == "SOC" :
		user_incar_settings['MAGMOM']=None
		folder1 = autocalculation.vaspinfo(struclist,user_incar_settings,"R_SOCmode")
		running_mode(folder1,running)
		checklist1 = running_time(folder1,"R_SOCmode")

	#chgcar
	checklist1.insert(0,pwd)
	os.chdir(pwd)

	user_incar_settings['NSW']=0
	user_incar_settings['LCHARG']=True
	user_incar_settings['EDIFF']=1E-6
	user_incar_settings['EDIFFG']=-1E-2

	if cal_type == "GGA" :
		folder2 = autocalculation.vaspinfo(struclist,user_incar_settings,"C_mode")
		running_mode(folder2,running)
		checklist2 = running_time(folder2,"C_mode")
	elif cal_type == "SOC" :
		folder2 = autocalculation.vaspinfo(struclist,user_incar_settings,"C_SOCmode")
		running_mode(folder2,running)
		checklist2 = running_time(folder1,"C_SOCmode")

elif mode == "cb":
	# chgcar
	user_incar_settings['NSW']=0
	user_incar_settings['LCHARG']=True
	user_incar_settings['EDIFF']=1E-6

	folder1 = autocalculation.vaspinfo(struclist,user_incar_settings,"C_mode")
	running_mode(folder1,running)
	checklist1 = running_time(folder1,"C_mode")

	#band
	checklist1.insert(0,pwd)
	os.chdir(pwd)

	user_incar_settings['LCHARG']=False
	user_incar_settings['ICHARG']=11

	folder2 = autocalculation.vaspinfo(checklist1,user_incar_settings,"BAND")
	del checklist1[0]
	for i in folder1 :
		com_struc = Vasprun("%s/vasprun.xml"%(os.path.abspath(i))).final_structure
		for f in folder2 :
			structure = Structure.from_file("%s/POSCAR"%(os.path.abspath(f)))
			if com_struc == structure :
				copyfile("%s/CHGCAR"%(os.path.abspath(i)),'%s/CHGCAR'%(os.path.abspath(f)))
				kpath_info = HighSymmKpath(structure).kpath['kpoints']
				kpath = HighSymmKpath(structure).kpath['path'][0]
				with open('%s/KPOINTS'%(os.path.abspath(f)),'w') as fi :
					fi.write('kpoints\n21\nL\nR\n')
					for i in range(len(kpath)-1):
						fi.write('%.3f %.3f %.3f !%s\n'%(kpath_info[kpath[i]][0],kpath_info[kpath[i]][1],kpath_info[kpath[i]][2],kpath[i]))
						fi.write('%.3f %.3f %.3f !%s\n'%(kpath_info[kpath[i+1]][0],kpath_info[kpath[i+1]][1],kpath_info[kpath[i+1]][2],kpath[i+1]))
						fi.write('\n')
				fi.close()
	running_mode(folder2,running)
	checklist2 = running_time(folder2,"band")

elif mode == "rcb" :
	#relaxation
	del(user_incar_settings["EDIFFG"]) 
	folder1 = autocalculation.vaspinfo(struclist,user_incar_settings,"R_mode")
	running_mode(folder1,running)
	checklist1 = running_time(folder1,"R_mode")

	#chgcar
	checklist1.insert(0,pwd)
	os.chdir(pwd)

	user_incar_settings['NSW']=0
	user_incar_settings['LCHARG']=True
	user_incar_settings['EDIFF']=1E-6
	user_incar_settings['EDIFFG']=-1E-2

	folder2 = autocalculation.vaspinfo(checklist1,user_incar_settings,"C_mode")
	running_mode(folder2,running)
	checklist2 = running_time(folder2,"C_mode")

	#band
	checklist2.insert(0,pwd)
	os.chdir(pwd)

	user_incar_settings['LCHARG']=False
	user_incar_settings['ICHARG']=11

	folder3 = autocalculation.vaspinfo(checklist2,user_incar_settings,"band")
	del checklist2[0]
	for i in folder2 :
		com_struc = Structure.from_file("%s/CONTCAR"%(os.path.abspath(i)))
		for f in folder3 :
			structure = Structure.from_file("%s/POSCAR"%(os.path.abspath(f)))
			if com_struc == structure :
				copyfile("%s/CHGCAR"%(os.path.abspath(i)),'%s/CHGCAR'%(os.path.abspath(f)))
				kpath_info = HighSymmKpath(structure).kpath['kpoints']
				kpath = HighSymmKpath(structure).kpath['path'][0]
				with open('%s/KPOINTS'%(os.path.abspath(f)),'w') as fi :
					fi.write('kpoints\n21\nL\nR\n')
					for i in range(len(kpath)-1):
						fi.write('%.3f %.3f %.3f !%s\n'%(kpath_info[kpath[i]][0],kpath_info[kpath[i]][1],kpath_info[kpath[i]][2],kpath[i]))
						fi.write('%.3f %.3f %.3f !%s\n'%(kpath_info[kpath[i+1]][0],kpath_info[kpath[i+1]][1],kpath_info[kpath[i+1]][2],kpath[i+1]))
						fi.write('\n')
				fi.close()
	running_mode(folder3,running)
	checklist3 = running_time(folder3,"band")
else :
	print("Ready for scripts")
