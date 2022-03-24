# Making sure we Know Everything we do

import os
import time
import tensorflow as tf
import cv2 
import numpy as np
import matplotlib.pyplot as plt
import importlib
importlib.reload("object_trackersFin.py")

from abs1 import app, flags, logging
from abs1.flags import FLAGS
from core.yolov4 import filter_boxes
from tensorflow.python.saved_model import tag_constants
from PIL import Image
from tensorflow.compat.v1 import ConfigProto # Configure The Yolo
from tensorflow.compat.v1 import InteractiveSession

# DeepsorImport
from deep_sort import preprocessing, nn_matching
from deep_sort.detection import Detection
from deep_sort.tracker import Tracker
from tools import generate_detections as gdet

# Define The Flags For CMD

# Default value every 2 Columns 
flags.DEFINE_string("framework", "tf","(tf, tflite, trt")
flags.DEFINE_string("weights", "./checkpoints/yolov4-416", "path to weights file") # TODO Define The Default yolo weights
flags.DEFINE_integer("size", 416, "resize images to")
flags.DEFINE_boolean("tiny", False, "yolo or yolo-tiny" )
flags.DEFINE_string("model","yolov4", "yolov3 or yolov4")
flags.DEFINE_string("video", "./data/video/test.mp4", "path to input video") # TODO Define the default path 
flags.DEFINE_string("output", None, "path to output video")
flags.DEFINE_string("output_format", "XVID", "codec used in VideoWriter When Saving video to a file ")

flags.DEFINE_float("iou", 0.45, "iou threshold")
flags.DEFINE_float("score", 0.25, "score threshold")
flags.DEFINE_boolean("dont_show", False, "dont show the tracking results")
flags.DEFINE_boolean("info", False, "Show Detailed info Of Tracked Objects")
flags.DEFINE_boolean("count", False, "Count Objects Being Tracked on Screen")


def main(_argv):
    
    # Define The Params
    max_cosine_distance : float = 0.4 # Jarak Antar Objek
    nn_budget = None
    nms_max_overlap = 1.0
    
    # init Deep sort
    model_filename = "model_data/mars-small128.pb"
    encoder = gdet.create_box_encoder(model_filename, batch_size=1)
    
    # Hitung Cosine Distance
    metric = nn_matching.NearestNeighborDistanceMetric("cosine", max_cosine_distance, nn_budget)
    
    # init Tracker
    tracker = Tracker(metric)
    
    # Load Configuration for Object Detector
    config = ConfigProto()
    config.gpu_options.allow_growth = True
    session = InteractiveSession(config=config)
    STRIDES, ANCHORS, NUM_CLASS, XYSCALE = utils.load_config(FLAGS)
    input_size = FLAGS.size
    video_path = FLAGS.video
    
    # Lpoad the Model Types ( if  you want to use it)
    # Tf lite Need to have their configuration
    if FLAGS.framework == "tflite":
        # Pada kasus tf lite emang butuh interpreter dlu sebelum bisa dieksekusi
        # sama halnya kalau di mobile juga gitu
        interpreter = tf.lite.Interpreter(model_path=FLAGS.weights)
        interpreter.allocate_tensors()
        
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        
        print(input_details)
        print(output_details)
    else 
    
    
