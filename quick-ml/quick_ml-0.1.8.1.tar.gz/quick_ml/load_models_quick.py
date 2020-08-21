def create_model(classes, model_name = 'VGG16', classification_model = 'default', freeze = False, input_shape = [512, 512,3], activation  = 'softmax', weights= "imagenet", optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = 'sparse_categorical_accuracy'):
	"""
	
	MODELS -> 'VGG16', 'VGG19',  
	'Xception',
	'DenseNet121', 'DenseNet169', 'DenseNet201', 
	'ResNet50', 'ResNet101', 'ResNet152', 'ResNet50V2', 'ResNet101V2', 'ResNet152V2', 
	'MobileNet', 'MobileNetV2',
	'InceptionV3', 'InceptionResNetV2', 
	'EfficientNetB0', 'EfficientNetB1', 'EfficientNetB2', 'EfficientNetB3', 'EfficientNetB4', 'EfficientNetB5', 'EfficientNetB6', 'EfficientNetB7'

	How to use ->
	
	1) For Effnet & Other than Effnet Models
	   a) with default classification model

	  from load_models_quick import create_model
	  model = create_model(classes = n_classes, model_name = "VGG19")
	   
	   
	   b) With Custom Classification Model
	   
	   from load_models_quick import create_model 
	   class_model = tf.keras.Sequential([
		  tf.keras.lkeras.layers.GlobalAveragePooling2D(),
		  tf.keras.layers.Dense(n_classes, activation = 'softmax') ])
	   model = create_model(classes = n_classes, model_name = 'VGG19', classification_model = 
		class_model)
		
		
	Load multiple models in a go. 
	
	model_names = ['VGG16', 'InceptionV3', 'DenseNet201', "EfficientNetB7"]
	models = []
	for model in model_names:
		models.append(create_model(classes = n_classes, model_name = model))
	
	
	"""
	
	if classification_model != 'default':
		print("""
		Make Sure that the classification model consists of layers of tf.keras.layers only else it won't work.
			
		""")
	
	import os
	if model_name.startswith("EfficientNet"):
		import os
		os.system("pip install git+https://github.com/qubvel/segmentation_models")
		#import keras
		import tensorflow as tf
	else:
		import tensorflow as tf
		from tensorflow.keras.applications import VGG16, VGG19,  Xception,DenseNet121, DenseNet169, DenseNet201, ResNet50, ResNet101, ResNet152, ResNet50V2, ResNet101V2, ResNet152V2, MobileNet, MobileNetV2, InceptionV3, InceptionResNetV2
		#import keras
	params = {"input_shape" : input_shape, "weights" : weights, "include_top" : False}
	
	
	if model_name == "VGG16":
		pretrained_model = VGG16(**params)
	elif model_name == "VGG19":
		pretrained_model = VGG19(**params)
	elif model_name == 'Xception':
		pretrained_model = Xception(**params)
	elif model_name == "DenseNet121":
		pretrained_model = DenseNet121(**params)
	elif model_name == "DenseNet169":
		pretrained_model = DenseNet169(**params)
	elif model_name == "DenseNet201":
		pretrained_model = DenseNet201(**params)
	elif model_name == 'EfficientNetB7':
		#import os 
		#os.system("pip install tensorflow==2.1")
		#os.system("pip install keras==2.3.1")
		#os.system("pip install git+https://github.com/qubvel/segmentation_models")
		import efficientnet.tfkeras as efn        
		pretrained_model = efn.EfficientNetB7(**params)
		
	elif model_name == 'EfficientNetB6':
		
		#os.system("!pip install -q efficientnet")
		#import efficientnet.tfkeras as efficientnet
		#pretrained_model = efficientnet.EfficientNetB6(**params)
		
		import efficientnet.tfkeras as efn        
		pretrained_model = efn.EfficientNetB6(**params)
		
	elif model_name == 'EfficientNetB5':
		#os.system("!pip install -q efficientnet")
		#import efficientnet.tfkeras as efficientnet
		#pretrained_model = efficientnet.EfficientNetB5(**params)
		
		import efficientnet.tfkeras as efn        
		pretrained_model = efn.EfficientNetB5(**params)
		
	elif model_name == 'EfficientNetB4':
		#os.system("!pip install -q efficientnet")
		#import efficientnet.tfkeras as efficientnet
		#pretrained_model = efficientnet.EfficientNetB4(**params)
		
		import efficientnet.tfkeras as efn        
		pretrained_model = efn.EfficientNetB4(**params)
		
	elif model_name == 'EfficientNetB3':
		#os.system("!pip install -q efficientnet")
		#import efficientnet.tfkeras as efficientnet
		#pretrained_model = efficientnet.EfficientNetB3(**params)
		
		import efficientnet.tfkeras as efn        
		pretrained_model = efn.EfficientNetB3(**params)
		
	elif model_name == 'EfficientNetB2':
		#os.system("!pip install -q efficientnet")
		#import efficientnet.tfkeras as efficientnet
		#pretrained_model = efficientnet.EfficientNetB2(**params)
		
		import efficientnet.tfkeras as efn        
		pretrained_model = efn.EfficientNetB2(**params)
		
	elif model_name == 'EfficientNetB1':
		#os.system("!pip install -q efficientnet")
		#import efficientnet.tfkeras as efficientnet
		#pretrained_model = efficientnet.EfficientNetB1(**params)
		
		import efficientnet.tfkeras as efn        
		pretrained_model = efn.EfficientNetB1(**params)
		
	elif model_name == 'EfficientNetB0':
		#os.system("!pip install -q efficientnet")
		#import efficientnet.tfkeras as efficientnet
		#pretrained_model = efficientnet.EfficientNetB0(**params)
		
		import efficientnet.tfkeras as efn        
		pretrained_model = efn.EfficientNetB0(**params)
		
	elif model_name == "InceptionV3":
		pretrained_model = InceptionV3(**params)
	elif model_name == "ResNet50":
		pretrained_model = ResNet50(**params)
	elif model_name == "ResNet101":
		pretrained_model = ResNet101(**params)
	elif model_name == "ResNet152":
		pretrained_model = ResNet152(**params)
	elif model_name == "ResNet50V2":
		pretrained_model = ResNet50V2(**params)
	elif model_name == "ResNet101V2":
		pretrained_model = ResNet101V2(**params)
	elif model_name == "ResNet152V2":
		pretrained_model = ResNet152V2(**params)
	elif model_name == 'MobileNet':
		pretrained_model = MobileNet(**params)    
	elif model_name == 'MobileNetV2':
		pretrained_model = MobileNetV2(**params)
	elif model_name == "InceptionResNetV2":
		pretrained_model = InceptionResNetV2(**params)
	else:
		print("model not among known models... exiting...")
		return
	
	if freeze:
		pretrained_model.trainable = False
	else:
		pretrained_model.trainable = True
	
	if model_name.startswith("EfficientNet"):
		
		if classification_model == 'default':
			model = tf.keras.Sequential([
			pretrained_model,
			tf.keras.layers.GlobalAveragePooling2D(),
			tf.keras.layers.Dense(classes, activation = activation)
			])
		else:
			new_model = tf.keras.Sequential()
			new_model.add(pretrained_model)
			for layer in classification_model.layers:
				new_model.add(layer)
			new_model.compile(optimizer = optimizer, loss = loss, metrics = [metrics])
			return new_model
	else:
		
		if classification_model == 'default':
			model = tf.keras.Sequential([
			pretrained_model,
			tf.keras.layers.GlobalAveragePooling2D(),
			tf.keras.layers.Dense(classes, activation =activation)
			])
		else:
			new_model = tf.keras.Sequential()
			new_model.add(pretrained_model)
			for layer in classification_model.layers:
				new_model.add(layer)
			new_model.compile(optimizer = optimizer, loss = loss, metrics = [metrics])
			return new_model
				
	
	model.compile(optimizer = optimizer, loss = loss, metrics = [metrics])
	
	return model     

if __name__ == "__main__":
	pass
else:
	#print("Please refer to help(create_model) to know about how to use.\n")
	#import os
	#print("Installing the reqd libraries...\n")
	#os.system("pip install tensorflow==2.2.0")
	#os.system("pip install keras==2.4.3")
	import tensorflow as tf
	if tf.__version__ == '2.2.0':
		pass
	else:
		print("Error! Tensorflow version mismatch...")
