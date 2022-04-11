#%% 

import os

def getTheFileTxt(path):
	allTxtFiles = []
	for file in os.listdir(path):
		if (file == "classes.txt"):
			continue
		elif(file.endswith(".txt")):
			allTxtFiles.append(os.path.join(path,file))
	return allTxtFiles
			
def convertid(filename):
    print(f"Converting ${filename}")
    with open(filename, "r+") as fuf:
        old_line = fuf.readline()
        old_line = old_line.split()
        print(old_line)
        if old_line[0] == "15":
            old_line[0] = "0"
        elif old_line[0] == "16":
            old_line[0]  = "1"
        print(old_line)
        old_line = " ".join(old_line)
        print(old_line)
        fuf.writelines(old_line)
    fuf.close()
		


# %%
def deleteFirst_line(filename):
    with open(filename, 'r') as fuf:
        data = fuf.read().splitlines(True)
    with open(filename,"w") as fuf:
        fuf.writelines(data[1:])
filetexts = getTheFileTxt("obj/blm")

for file in filetexts:
    convertid(file)
    
"""
filetexts = getTheFileTxt("obj/blm")
for file in filetexts:
    deleteFirst_line(file)
"""
# %%
#filetexts = getTheFileTxt("test")

#for file in filetexts:
#    convertid(file)
filetexts = getTheFileTxt("test")
for file in filetexts:
    deleteFirst_line(file)
# %%
