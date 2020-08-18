import os
import sys
import time
import subprocess
import glob
from shutil import copyfile

import yaml
import numpy as np
import pandas as pd

from pymatgen import Structure, Element 
from pymatgen.io.vasp.sets import MPRelaxSet, batch_write_input
from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.symmetry.bandstructure import HighSymmKpath

class shell :
    def __init__(self, shell, name):
        self.shell_path = "{}/shell".format(os.path.split(os.path.dirname(__file__))[0])
        try :
            vaspsh = open("{}/{}".format(self.shell_path,shell),"r")
        except :
            print("There isn't {} file".format(shell))
            sys.exit(1)
        self.vaspsh_list = vaspsh.readlines()
        for i in self.vaspsh_list :
            if "-N" in i :
                nameline = i.split()
                name_index = self.vaspsh_list.index(i)
                del self.vaspsh_list[name_index]
                del nameline[-1]
        lines2=''
        for i in nameline :
            lines2 += i+""
        lines2 += name + '\n'
        self.vaspsh_list.insert(name_index,lines2)

    def write_vaspsh(self):
        with open("vasp.sh","w") as fi :
            for i in self.vaspsh_list :
                fi.write(i)
        fi.close()
    def SOC_read_vaspsh(self):
        for i in range(len(self.vaspsh_list)):
            if 'std' in self.vaspsh_list[i] :
                std_line = self.vaspsh_list[i].split("#")
                if len(std_line) == 1 :
                    a = list(std_line[0])
                    a.insert(0,"#")
                    aa=""
                    for j in a :
                        aa += j
                    self.vaspsh_list[i] = aa
                else :
                    pass
            elif 'ncl' in self.vaspsh_list[i] :
                ncl_line = self.vaspsh_list[i].split("#")
                if len(ncl_line) == 1 :
                    a = list(std_line[0])
                    a.insert(0,"#")
                    aa=""
                    for j in a :
                        aa += j
                    self.vaspsh_list[i] = aa
                else :
                    self.vaspsh_list[i] = ncl_line[-1]
            if 'gam' in self.vaspsh_list[i] :
                std_line = self.vaspsh_list[i].split("#")
                if len(std_line) == 1 :
                    a = list(std_line[0])
                    a.insert(0,"#")
                    aa=""
                    for j in a :
                        aa += j
                    self.vaspsh_list[i] = aa
                else :
                    pass
        with open("vasp.sh","w") as fi :
            for i in self.vaspsh_list :
                fi.write(i)
        fi.close()

class Input_POSCAR :
    def __init__(self, structure, delete_charge=True, delete_selective_dynamics=True) :
        self.structure = structure
        self.delete_charge = delete_charge
        self.delete_sd = delete_selective_dynamics
        for i in range(self.structure.num_sites):
            if self.delete_charge :
                try :
                    self.structure.replace(i, self.structure.species[i].element)
                except :
                    pass
            if self.delete_sd :
                try :
                    self.structure.replace(i,self.structure.species[i].element, properties=None)
                except :
                    self.structure.replace(i,self.structure.species[i],properties=None)

        from collections import Counter
        from pymatgen import Element
        self.vaspname=""
        c,h,n = [Element(sym) for sym in ["C","H","N"]]
        sn = Counter(self.structure.species)
        if c and h and n in sn :
            sdic={}
            if sn[c] == sn[n]:
                sdic["MA"] = sn[c]
            else :
                sdic["FA"] = sn[c]

            for i in [c,h,n] :
                del sn[i]
            sdic.update(sn)
        else :
            sdic = sn
        for i in sdic :
            try :
                if sdic[i] == 1 :
                    self.vaspname += i.symbol
                else :
                    self.vaspname += "{}{}".format(i.symbol,sdic[i])
            except :
                if sdic[i] == 1 :
                    self.vaspname += i
                else :
                    self.vaspname += "{}{}".format(i,sdic[i])

    def _number_folder(self,cal_mode):
        folder_list=[folder for folder in os.listdir(".") if "{}_mode".format(cal_mode) in folder]
        return len(folder_list)

    def revise_input(self, uis, number=40):
        mpr = MPRelaxSet(self.structure, user_incar_settings=uis)
        vi = mpr.get_vasp_input()
        lattice = [self.structure.as_dict()['lattice'][l] for l in ['a','b','c']]
        a,b,c = [i if i < number else number for i in lattice]
        vi["KPOINTS"].kpts[0] = [round(number/a),round(number/b),round(number/c)]
        return vi

def Input_INCAR(method1=None, method2=None):
    user_incar_settings={"SYSTEM":"Structure Optimization","PREC":"Accurate","ISTART":0,"ISPIN":1,"LREAL":"A","ENCUT":520,"IBRION":2,"ISIF":3,"EDIFF":1E-4,"EDIFFG":-1E-2,"NSW":500,"ALGO":"Normal","LCHARG":False,"LWAVE":False,"SIGMA":0.05,'ISMEAR':0}

    if os.path.isfile("incar.yaml"):
        stream = open("incar.yaml","r")
        loading = yaml.load(stream)
        for i in loading :
            user_incar_settings[i] = loading[i]
    
    if method1 == "PBE":
        pass
    elif method1 == "PBESol":
        user_incar_settings["GGA"] = "PS"
    elif method1 == "VDW":
        user_incar_settings["IVDW"] = 21
    elif method1 == "SCAN":
        user_incar_settings["METAGGA"] = "SCAN"

    if method2 == "R":
        del user_incar_settings["EDIFFG"]
    elif method2 == "C":
        user_incar_settings["NSW"] = 0
        user_incar_settings["LCHARG"] = True
        user_incar_settings["EDIFF"] = 1E-6
    elif method2 == "B" or method2 == "E":
        user_incar_settings["EDIFF"]=1E-6
        user_incar_settings["NSW"]=0
        user_incar_settings["LCHARG"] = False
        user_incar_settings["ICHARG"] = 11

    return user_incar_settings   

def load_structure(path):
    struclist=[]
    for p in path :
        path1 = os.path.abspath(p)
        if os.path.isfile(path1):
            try :
                struclist.append(Structure.from_file(path1))
            except :
                pass
        else :
            for j in os.listdir(path1):
                try :
                    struclist.append(Structure.from_file(j))
                except :
                    pass
    return struclist

def running_mode(path, ss, soc=False, run=True):
    pwd = os.getcwd()
    for j in range(len(path)):
        os.chdir(os.path.join(pwd,path[j]))
        if soc :
            shell(ss,path[j]).SOC_read_vaspsh()
        else :
            shell(ss,path[j]).write_vaspsh()
        if run :
            print("{} Running".format(path[j]))
            subprocess.check_call(['qsub','vasp.sh'])
        
def MakeKpointsBand(KPOINTS,kpath_info,kpath):
    with open(KPOINTS, 'w') as fi :
        fi.write("kpoints\n21\nL\nR\n")
        for i in range(len(kpath)-1):
            fi.write("%.3f %.3f %.3f !%s\n"%(kpath_info[kpath[i]][0],kpath_info[kpath[i]][1],kpath_info[kpath[i]][2],kpath[i]))
            fi.write("%.3f %.3f %.3f !%s\n"%(kpath_info[kpath[i+1]][0],kpath_info[kpath[i+1]][1],kpath_info[kpath[i+1]][2],kpath[i+1]))
            fi.write("\n")

def CheckCal(pwd, path, method1, struc, cs, ds=False, orbit=False,running="vasp.sh"):
    for s in cs:
        os.chdir(pwd)
        incar = Input_INCAR(method1=method1,method2=s)
        folder = [] ; kpath_list=[]
        if s == "B" or s == "E" :
            for b in path :
                b = os.path.abspath(b)
                if os.path.isfile(b):
                    chg_path = os.path.split(b)[0]
                else :
                    chg_path = b
                if "CHGCAR" in os.listdir(chg_path):
                    kpath_list.append("{}/CHGCAR".format(chg_path))
        for e,i in enumerate(struc):
            if ds :
                ifs = Input_POSCAR(i,delete_selective_dynamics=True)
            else :
                ifs = Input_POSCAR(i,delete_selective_dynamics=False) 
            naming = "%s_%i_%s_mode"%(ifs.vaspname,ifs._number_folder(cal_mode=s),s)
            folder.append(naming)
            ifs.revise_input(uis=incar,number=40).write_input(output_dir=naming)
            if s == "B" or s == "E":
                kpath_info = HighSymmKpath(i).kpath['kpoints']
                kpath = HighSymmKpath(i).kpath['path'][0]
                MakeKpointsBand("{}/{}/KPOINTS".format(pwd,naming),kpath_info,kpath)
                copyfile(kpath_list[e],"{}/{}/CHGCAR".format(pwd,naming))
        running_mode(folder,running,soc=orbit)
        while True :
            time.sleep(10)
            path = [] ; checklist= []
            for j in folder :
                os.chdir(os.path.join(pwd,j))
                try :
                    vrun = Vasprun("vasprun.xml")
                    finalstruc = vrun.final_structure
                    aa = subprocess.check_output(['tail','-n','1','OSZICAR']).decode('utf-8')
                    if int(aa.split()[0]) == vrun.as_dict()['input']['incar']['NSW']:
                        print("{} is Non-Pass".format(j))
                        subprocess.call(['rm','vasprun.xml'])
                        forlder_list=[folder for folder in os.listdir(".") if folder.endswith("initial")]
                        subprocessl.call(['cp','POSCAR','POSCAR_{}_initial'.format(len(folder_list))])
                        subprocess.call(['cp','CONTCAR','POSCAR'])
                        subrpocess.check_call(['qsub','vasp.sh'])
                        time.sleep(10)
                    else :
                        print("%s PASS"%(j))
                        checklist.append(finalstruc)
                        path.append(os.path.join(pwd,j))
                except :
                    pass
            if len(folder) == len(checklist) :
                break
        struclist = checklist
        print("Finished Time")
        print(time.strftime("%c",time.localtime(time.time())))

def analyze_calculation(args):
    # INCAR METHOD
    if args.PBE :
        method = "PBE"
    elif args.PBESOL :
        method = "PBESol"
    elif args.VDW :
        method = "VDW"
    elif args.SCAN :
        method = "SCAN"
    elif args.MP :
        method = "MP"

    if type(args.path) == str :
        path = [args.path]
    else :
        path = args.path

    struc = load_structure(path)
    cs = [s.upper() for s in args.mode]
    if args.run :
        f = open("{}/calnohup.py".format(os.path.dirname(__file__)),"r")
        ff = f.readlines()
        ff.insert(0,"method='{}'\n".format(method))
        ff.insert(1,"mode={}\n".format(str(cs)))
        ff.insert(2,"path={}\n".format(str(path)))
        if args.ds :
            ff.insert(3,"ds=True\n")
        else :
            ff.insert(3,"ds=False\n")
        if args.orbit :
            ff.insert(4,"orbit=True\n")
        else :
            ff.insert(4,"orbit=False\n")
        ff.insert(5,"running={}\n\n".format(str(args.run)))
        with open("{}/running_calnohup.py".format(os.path.dirname(__file__)),"w") as fi :
            for i in ff :
                fi.write(i)
        fi.close()
        #os.system("python {}/running_calnohup.py".format(os.path.dirname(__file__)))
        os.system("nohup python {}/running_calnohup.py &".format(os.path.dirname(__file__)))
    else :
        pwd = os.getcwd()
        for s in cs:
            os.chdir(pwd)
            incar = Input_INCAR(method1=method,method2=s)
            folder = []
            for e,i in enumerate(struc):
                if args.ds :
                    ifs = Input_POSCAR(i,delete_selective_dynamics=True)
                else :
                    ifs = Input_POSCAR(i,delete_selective_dynamics=False) 
                naming = "%s_%i_%s_mode"%(ifs.vaspname,ifs._number_folder(cal_mode=s),s)
                ifs.revise_input(uis=incar,number=40).write_input(output_dir=naming)