#%%^

import os 
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from validateData import *

## VARIABEL CONST

IMG_HEIGHT : int = 224
IMG_WIDTH : int = 224
IMG_CHANNELS : int = 3

MAX_DELTA : float = 0.3 ## A little darker for Brightness
UPPER_BOUND_CONTRAST : float = 1.8
LOWER_BOUND_CONTRAST : float = 1.2

ABS_PATH : str = "../model_data/rawData"
PATH_PNG : str ="../model_data/rawData_png"
AUGMENT_PATH : str = "../model_data/augmentedData"
try :
	if (os.path.isdir(AUGMENT_PATH) == False ):
		os.mkdir(AUGMENT_PATH)
except FileNotFoundError as e:
	print("Folder Not Exists")
	os.mkdir(AUGMENT_PATH)

# %%
def getPathListTruck(path:str) :
	list_path = []
	for file in os.listdir(path):
		list_path.append(os.path.join(path, file))
	return list_path

def decode_image(filename : str, reshaped_dims):
	image = tf.keras.preprocessing.image.load_img(filename)
	return image

def createAugment(filename : str, augment=False):
	"""
	Do Only 
	Flipping
	Brightness
	And Contrast
	Args:
		filename (str): _description_
		random_augment (bool, optional): _description_. Defaults to False.
	"""
	if augment:
		image = decode_image(filename, reshaped_dims=(IMG_HEIGHT, IMG_WIDTH,IMG_CHANNELS))
		image = tf.image.random_flip_left_right(image)
		image = tf.image.random_brightness(image, max_delta=MAX_DELTA)
		image = tf.image.random_contrast(image, lower=LOWER_BOUND_CONTRAST, upper=UPPER_BOUND_CONTRAST)
	return image 


def plot_image(image):
	plt.figure(figsize=(5,5))
	plt.imshow(image,cmap="gray")
	plt.xticks([])
	plt.yticks([])
	plt.grid(False)
	plt.show()

#%%
def do_augment(path : str,folder_save : str):
	list_path = getPathListTruck(path)
	if(os.path.isdir(folder_save) == True):
		for file in list_path:
			augmented_image = createAugment(filename=file, augment=True)
			filename = str(regex.search("truck[1-4]-\d+", file).group(0))
			filename= filename + "_augmented.png"
			save_path = os.path.join(folder_save, filename)
			tf.keras.utils.save_img(save_path, augmented_image)
	else:
		os.mkdir(os.path.join(folder_save))
	

#%%
if __name__=="__main__":
	list_of_augment_folders = [
		FolderName.default_truck_gandar2_augment_folder.value,
		FolderName.default_truck_gandar3_augment_folder.value,
		FolderName.default_truck_gandar4_augment_folder.value
	]

	list_of_raw_folders = [
		FolderName.default_truck_gandar2_folder_name.value,
		FolderName.default_truck_gandar3_folder_name.value,
		FolderName.default_truck_gandar4_folder_name.value
	]
	for folder_augment, folder_raw in zip(list_of_augment_folders,list_of_raw_folders):
		do_augment(path=os.path.join(PATH_PNG,folder_raw ), folder_save=os.path.join(AUGMENT_PATH, folder_augment))
# %%
