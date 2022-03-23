import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import time
import tensorflow as tf

physical_devices = tf.config.experimental.list_physical_devices('GPU')
if (len(physical_devices) > 0) :
    tf.config.experimental.set_memory_growth(physical_devices[0], True)

from abs1 import app, flags, logging
from abs1.flags import FLAGS

import core.utils as utils
from core.yolov4 import filter_boxes
from tensorflow.python.saved_model import tag_constants

from core.config import cfg
from PIL import Image

import cv2
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

# IouImports

# Deep sort Imports
from deep_sort import preprocessing, nn_matching
from deep_sort.detection import Detection
from deep_sort.tracker import Tracker