import os
import sys

from shutil import copyfile

class ShellPath :
	def __init__(self) :
		self.shellpath = "%s/shell"%(os.path.split(os.path.dirname(__file__))[0])
		self.files = [f for f in os.listdir(self.shellpath)]
	def shell_path(self,filename,savename):
		copyfile(filename,"%s/%s"%(self.shellpath,savename))
		print("%s Successfully Save "%(os.path.abspath(savename)))

	def check(self):
		shell=[f for f in self.files if f.split(".")[-1]== "sh"]
		if len(shell) != 1 :
			print("shell scripts are",shell)
		else:
			print("shell scirpt is",shell[0])
		print("If you add the shell script, Please enter the command, gmd config -s [directory][name]")

	def revise_shell(self,filename,nodes,maximum):
		shell=[f for f in self.files if i.split(".")[-1]== "sh"]
		if not filename in shell :
			print("The %s is not shell script, Please enter the command, gmd config -s [directory][name]"%(args.revise[0]))
			sys.exit(1)
		ff = open("%s/%s"%(shellpath,filename),"r")
		list1 = ff.readlines()
		for e,i in enumerate(list1) :
			if "MAX" in i :
				maximum = i,e 
			elif "nodes" in i :
				if "dirac" in i :
					pass
				else :
					nodes = i,e
		print(maximum)
		print(nodes)
		
def analyze_config(args):
	config = ShellPath()
	shellpath = config.shellpath 
	files = config.files

	if args.shell :
		shell_name = os.path.abspath(args.shell[0][0])
		add_shell = os.path.abspath("%s/%s"%(shellpath,args.shell[0][1]))
		if not os.path.isfile(shell_name) :
			print("%s isn't file"%shell_name)
		else :
			if os.path.isfile(add_shell):
				print("%s is already enrolled\n"%args.shell[0][1])
			else :
				copyfile(shell_name,add_shell)
				print("%s Successfully Save"%add_shell)
	elif args.check :
		print("shell script list :",files)
	elif args.revise :
		print("Prepare")
