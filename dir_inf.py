import os, imghdr

def get_size(path):
	total_size = 0
	for dirpath, dirnames, filenames in os.walk(path):
		for f in filenames:
			fp = os.path.join(dirpath, f)
			if not os.path.islink(fp):
				total_size += os.path.getsize(fp)
	
	return total_size


def count_img(path):
	count = 0
	for dirpath, dirnames, filenames in os.walk(path):
		for f in filenames:
			fp = os.path.join(dirpath, f)
			if imghdr.what(fp) != None:
				count += 1	
	return count
	
	
def sup_dir(path):
	count = -1
	for dirpath, dirnames, filenames in os.walk(path):
		if os.path.isdir(dirpath):
			count += 1
			
	return count


def sup_dir_names(path):
	dirs = ""
	for dirpath, dirnames, filenames in os.walk(path):
		if str(dirnames) != '[]':
			dirs += str(dirnames)
			
	return dirs


def get_inf(path):

	res = "dir name: " + os.path.basename(path) + "\n"    

	res += "size: " + str(get_size(path)) + " bytes\n"
	res += "there is " + str(count_img(path)) + " images\n"
	res += "there is " + str(sup_dir(path)) + " directory\n"
	if sup_dir_names(path) != '[]':
		res += "directory names is: " + sup_dir_names(path) + "\n"
	else:
		res += "there is no directorys"
	
	
	return res

def write_directory_inf_to_file(path):
	with open("directory_inf.txt", 'w') as f:
		f.write(get_inf(path))

	

if __name__ == "__main__":
	path = "/home/ibra/Desktop/python_exercises/python-self-learning-files-ibrahimidk"
	path1 = "/home/ibra/Desktop/python_exercises/python-directory-summarize-ibrahimidk/d"
	write_directory_inf_to_file(path1)
	
	

