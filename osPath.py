import os
def search(path):
	for x in os.listdir(path):
		f = os.path.join(path,x)
		if os.path.isdir(f):
			search(f)
		else:
			print f


search("D:\\learning")