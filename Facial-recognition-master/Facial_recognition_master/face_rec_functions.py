
import json
import numpy as np

def createFile():
	data = {}
	with open('data.txt', 'w') as outfile:  
		json.dump(data, outfile)


def dumpData(name):
	idd=1
	with open('data.txt') as json_file:  
		data = json.load(json_file)
		
	# print(data)
	if (bool(data)==False):
		data.update({1:name})

	else:
		id=max(data.keys())
		# print("ID",id)
		id=int(id)
		data.update({id+1:name})
		idd=id+1
	with open('data.txt', 'w') as f:
		json.dump(data, f)

	print(data)	
	return idd
 

# createFile()
# name=input("enter name ")
# print(dumpData(name))
