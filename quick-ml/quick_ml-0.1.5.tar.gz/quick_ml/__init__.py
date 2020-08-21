import os
os.system("pip install tensorflow==2.2.0")
import tensorflow as tf
if tf.__version__ == '2.2.0':
	print(f"Tensorflow imported successfully. Tensorflow version -> {tf.__version__}")
else:
	print("Tensorflow version mismatch!. Please check tensorflow isn't imported before installing quick_ml. Restart the session to fix the error.")

import .tfrecords_maker