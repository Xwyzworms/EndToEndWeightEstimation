#%%
import pyrebase

config = {
	"apiKey": "AIzaSyAUl67xIMwVPc3ll7HNAW6cSMzyX3LPM3U",
	"authDomain": "tugasakhirprim.firebaseapp.com",
    "databaseURL": "https://tugasakhirprim-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "projectId": "tugasakhirprim",
    "storageBucket": "tugasakhirprim.appspot.com",
    "messagingSenderId": "765795992354",
    "appId": "1:765795992354:web:882a1ea4fb09329cd95b7b",
    "measurementId": "G-WTN5XTS2VB"
}


firebase = pyrebase.initialize_app(config)
path_to_cloud = "data/raw.json"
path_data = "raw.json"


storage = firebase.storage()
storage.child(path_to_cloud).put(path_data)
print("Data Uploaded")
# %%
