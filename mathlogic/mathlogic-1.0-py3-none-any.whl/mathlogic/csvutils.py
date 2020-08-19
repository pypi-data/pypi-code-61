def saveToCSV(df,file,tmp_filepath="/tmp"):
	import string, random, subprocess
	rand_dir="".join([random.choice(string.ascii_letters) for t in range(1,11)])
	filename=tmp_filepath+"/"+rand_dir+"/"+file
	header=",".join(df.columns)
	df.write.csv(filename,header=False)
	a=subprocess.check_call("cat "+filename+"/"+"part*"+" > "+file,shell=True)
	a=subprocess.check_call("sed -i '1i"+header+"' "+file,shell=True)
	if a ==0:
		print("Success. Writing "+file)

