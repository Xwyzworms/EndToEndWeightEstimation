import os 	
from typing import List

image_files : List = []

ABS_PATH : str = "data/test"

print(os.getcwd())
os.chdir(ABS_PATH)
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append(os.path.join(ABS_PATH, filename))
os.chdir("..")
with open("test.txt","w") as fuf:
    for fileLoc in image_files:
        fuf.write(fileLoc)
        fuf.write("\n")
    fuf.close()
os.chdir("..")    