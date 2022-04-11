#%%
import shutil
import enum 
import json
import os
from typing import List
# %%

class TruckEnum(enum.Enum):
	diesel_fe74s_truck_name = "diesel_fe74s_truck"
	diesel_fe84HDL_truck_name = "diesel_fe84HDL_truck"
	diesel_fe74L_truck_name = "diesel_fe74L_truck"
	diesel_fe84BC_truck_name = "diesel_fe84BC_truck"

class WeightEnumStandard(enum.Enum):
	diesel_fe74s_truck_name = 40
	diesel_fe84HDL_truck_name = "diesel_fe84HDL_truck"
	diesel_fe74L_truck_name = "diesel_fe74L_truck"
	diesel_fe84BC_truck_name = "diesel_fe84BC_truck"

class WeightEnumFull(enum.Enum):
	diesel_fe74s_truck_name = 50
	diesel_fe84HDL_truck_name = "diesel_fe84HDL_truck"
	diesel_fe74L_truck_name = "diesel_fe74L_truck"
	diesel_fe84BC_truck_name = "diesel_fe84BC_truck"

def weight_repository(typeTruck : str):
	if(typeTruck == TruckEnum.diesel_fe74L_truck_name.value):
		min_cw = WeightEnumStandard.diesel_fe74L_truck_name.value
		max_cw = WeihgtEnumFull.diesel_fe74L_truck_name.value
		return min_cw, max_cw
	elif(typeTruck == TruckEnum.diesel_fe84HDL_truck_name.value):
		pass

def calculate_weight(type : str, min_cw : float, max_cw : float):
	truckType = TruckEnum[type].value
	if(truckType == TruckEnum.diesel_fe74s_truck_name.value):
		return weight_repository(typeTruck)

def getRandom():
	list_truck_types = [
	TruckEnum.diesel_fe74s_truck_name.value,
	TruckEnum.diesel_fe84HDL_truck_name.value, 
	TruckEnum.diesel_fe74L_truck_name.value, 
	TruckEnum.diesel_fe84BC_truck_name.value]

	list_truck_weights = [
		(TruckEnum.diesel_fe74L_truck_name.value,12,14),
		(TruckEnum.diesel_fe74s_truck_name.value,23,23),
		(TruckEnum.diesel_fe74s_truck_name.value,11,23),
		(TruckEnum.diesel_fe74s_truck_name.value,31,23),
	]
	return list_truck_types, list_truck_weights

def makeDict(list_truck_types, list_truck_weights):
	dict_truck = {}
	for truck, (name,mincw, maxcw) in zip(list_truck_types, list_truck_weights):
		dict_truck[truck] = {}
		dict_truck[truck]['name'] = name
		dict_truck[truck]['minimum'] = mincw
		dict_truck[truck]["maximum"] = maxcw
	return dict_truck

def saveTheOlderFile(json_file_path : str):
	if(os.path.isdir("legacy_json")):
		shutil.copy(json_file_path, "legacy_json")
	else:
		os.makedirs("legacy_json")
		shutil.copy(json_file_path, "legacy_json")	

def write_json(list_truck_types : List, list_truck_weights : List):
	dict_truck = makeDict(list_truck_types, list_truck_weights)
	with open('truck_weights.json', 'w') as outfile:
		json.dump(dict_truck, outfile)

if __name__ == "__main__":
	list_truck_types, list_truck_weights = getRandom()
	write_json(list_truck_types, list_truck_weights)
	saveTheOlderFile("truck_weights.json")

# %%
