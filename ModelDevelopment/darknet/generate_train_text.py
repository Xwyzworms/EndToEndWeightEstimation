import os
from typing import List 


image_files : List  = []

ABS_PATH : str ="data/obj"
os.chdir(ABS_PATH) # data/obj ( Data Location )
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append(os.path.join(ABS_PATH,filename))
os.chdir("..") # go back to data create the Train txt. consist of path to images

with open("train.txt", "w") as fuf:
    for fileLoc in image_files:
		# For everysingle fileLocation, Create A single Line
		# loc1
		# loc2
		# loc3
        fuf.write(fileLoc)
        fuf.write("\n")  
    fuf.close()
os.chdir("..") # go back to the main folder
