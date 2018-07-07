import os, shutil
from shutil import copyfile
from distutils.dir_util import copy_tree
dir_name = raw_input('Choose  installation 1 (12 Jun): ')
with open('old_RUs.txt','r') as f:
	for line in f:
		file_name=os.path.join(dir_name,line)
		file_name=file_name.strip()
		nb=raw_input( 'should '+file_name+ ' be removed ?')		
		if nb=='1' and not file_name.endswith("shared"):
			if os.path.exists(file_name):
				if file_name.endswith(".jar"):
					os.remove(file_name)
			
				else:	
					shutil.rmtree(file_name)
			print "old RU  "+line+" removed from 12 Jun installation \n"		
		else:
			print "not removing"
		
		

	
newdir= raw_input('Choose Installation 2 (3 Jul): ')
with open('new_RUs.txt','r') as f:
	for line in f:
		line=line.strip()
		src= newdir+"/"+line
		print "for "+src+" \n "
		if not os.path.exists(dir_name+"/"+line):
			os.mkdir(dir_name+"/"+line)
		for root, dirs, files in os.walk(dir_name+"/"+line):  
  			for momo in dirs:  
    				os.chown(os.path.join(root, momo), 502, 20)
  			for momo in files:
    				os.chown(os.path.join(root, momo), 502, 20)	
		os.chmod(dir_name+"/"+line,0o777)	
		if src.endswith(".jar"):
			print "copying jar"
			#dest_name=os.path.join()
			#print "copying "+src+" to "+
			
			shutil.copyfile(src,dir_name+"/"+line)
			print "RU "+line+ " copied over from Jul 3 to Jun 12 installation \n"
		else:
			try:
				
        			copy_tree(src, dir_name+"/"+line)
				print "RU "+line+ " copied over from Jul 3 to Jun 12 installation \n"	
    # Directories are the same
    			except shutil.Error as e:
        			print('Directory not copied. Error: %s' % e +" for "+src+" and "+(dir_name+"/"+line))
    # Any error saying that the directory doesn't exist
    			except OSError as e:
        			print("Directory not copied. Error  for "+src+" and "+(dir_name+"/"+line))
		


