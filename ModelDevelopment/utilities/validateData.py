#%% 
import os
import shutil
import imghdr
import enum 
import re as regex
from PIL import Image
from Augment import getPathListTruck 
ABS_PATH : str = "../model_data/rawData"
TOTAL : int = 200
PATH_PNG : str ="../model_data/rawData_png"
PATH_IMAGE_INTERNET : str ="../model_data/dataFromInternet"

class FolderName(enum.Enum):
	default_truck_gandar2_folder_name = "Truck2GandarSamping"
	default_truck_gandar3_folder_name = "Truck3GandarSamping"
	default_truck_gandar4_folder_name = "Truck4GandarSamping"

	default_truck_gandar2_augment_folder ="Truck2GandarSamping_augment"
	default_truck_gandar3_augment_folder ="Truck3GandarSamping_augment"
	default_truck_gandar4_augment_folder = "Truck4GandarSamping_augment"

	default_data_internet_colt2_gandar_folder = "Truk2GandarColt"

	
class TruckType(enum.Enum):
	# For Samping Dataset
	default_truk_gandar2_samping_name = "truk_2_gandar_samping_"
	default_truk_gandar3_samping_name = "truk_3_gandar_samping_"
	default_truk_gandar4_samping_name = "truk_4_gandar_samping_"

	# For Infront Data
	default_truk_gandar2_infront_name = "truk_2_gandar_infront_"
	default_truk_gandar3_infront_name ="truk_3_gandar_infront_"
	default_truk_gandar4_infront_name ="truk_4_gandar_infront_"

#%%

def check_image_quality(path : str,list_of_extensions=["jpg",'png']):
## For Dataset
	bad_images = []
	file_lists = os.listdir(path)

	for file in file_lists:
		file_path = os.path.join(path, file)
		extension = imghdr.what(file_path)
		if  extension not in list_of_extensions : #No Extension
			bad_images.append(file_path)
		if os.path.isfile(file_path) :
			try:
				img = Image.open(file_path)
				shape = img.shape
			except :
				#print("file", file_path, "is not an image")
				bad_images.append(file_path)
	
	return bad_images

def remove_jpeg(folder_path):
	for file in os.listdir(folder_path):
		file = os.path.join(folder_path, file)
		print(file)
		if(file.endswith(".jpg")):
			os.remove(file)
def rename_the_files(folder_path,baseName:str):
	counter : int = 0
	for file in os.listdir(folder_path):
		filename = os.path.join(folder_path, file)
		targetFilename = os.path.join(folder_path, baseName + "_" +str(counter))
		targetFilename = targetFilename + ".jpg"
		os.rename(filename, targetFilename)
		counter = counter + 1
	
def convert_to_png(file_list,path_to_make):
	try :
		os.mkdir(path_to_make)
		print("file for converting not exists, creating ...")
	except FileNotFoundError as e:
		os.mkdir(path_to_make)
	except FileExistsError as e:
		print("file Created")		
	finally :
		for file in file_list:
			image = Image.open(file)
			file_name_only = regex.search("truck[1-4]-\d+",file).group(0)
			image = image.convert("RGB")
			image.save(os.path.join(path_to_make, file_name_only+ ".png"))


#%%
if __name__ == "__main__":
	convert = False
	if(convert):
		list_of_truckFolder = [
		FolderName.default_truck_gandar2_folder_name.value,
		FolderName.default_truck_gandar3_folder_name.value,
		FolderName.default_truck_gandar4_folder_name.value,
		]

		for folder in list_of_truckFolder :
			list_bad_images = check_image_quality(os.path.join(ABS_PATH,folder))
			print("There's {} bad images".format(len(list_bad_images)))
			convert_to_png(list_bad_images, os.path.join(PATH_PNG, folder))
	else :
		list_of_custom_data_internet = [
		FolderName.default_data_internet_colt2_gandar_folder.value,

		]
		for folder in list_of_custom_data_internet:
			rename_the_files(os.path.join(PATH_IMAGE_INTERNET, folder),"truk_gandar2_colt")


# %%
