def define_tpu_strategy():
	try:
        tpu = tf.distribute.cluster_resolver.TPUClusterResolver()
        print('Running on TPU ', tpu.master())
    
    except ValueError:
    	print("TPU not activated. Please check the settings. Settings -> Accelerator -> TPU v3-8\n")
        tpu = None
    
    
    if tpu:
        tf.config.experimental_connect_to_cluster(tpu)
        tf.tpu.experimental.initialize_tpu_system(tpu)
        strategy = tf.distribute.experimental.TPUStrategy(tpu)
    else:
        strategy = tf.distribute.get_strategy()
    
    return strategy, tpu


############### DATASET SETUP  ###################


def decode_image(image_data, IMAGE_SIZE):
    
    image = tf.io.decode_raw(image_data, tf.uint8)
    
    image = tf.cast(image, tf.float32) / 255.0
    

    # how would I obtain Image_Size 
    image = tf.reshape(image, [*IMAGE_SIZE, 3])
    return image

def read_labeled_tfrecord(example):
    print("Enter the dictionary of Labeled_TFREC_FORMAT\n")
    dictionary = eval(input())
    print("Enter Image Size; Example Format ->  192,192  (w/o brackets)\n\n")
    IMAGE_SIZE = input()
    IMAGE_SIZE = [int(IMAGE_SIZE.split(',')[0]), int(IMAGE_SIZE.split(',')[1])]
    example = tf.io.parse_single_example(example, dictionary)
    image = decode_image(example[list(dictionary.keys())[0]], IMAGE_SIZE)
    label = tf.cast(example[list(dictionary.keys())[1]], tf.int32)
    return image, label

def read_unlabeled_tfrecord(example):
    print("Enter the dictionary of the UnLabeled_TFREC_FORMAT\n")
    dictionary = eval(input())
    print("Enter Image Size; Example Format ->  192,192  (w/o brackets)\n\n")
    IMAGE_SIZE = input()
    IMAGE_SIZE = [int(IMAGE_SIZE.split(',')[0]), int(IMAGE_SIZE.split(',')[1])]
    example = tf.io.parse_single_example(example, dictionary)
    image = decode_image(example[list(dictionary.keys())[0]], IMAGE_SIZE)
    idnum = example[list(dictionary.keys())[1]]
    return image, idnum


def load_dataset(filenames, labeled = True, ordered = False):
    ignore_order = tf.data.Options()
    if not ordered:
        ignore_order.experimental_deterministic = False
        
    dataset = tf.data.TFRecordDataset(filenames, num_parallel_reads = tf.data.experimental.AUTOTUNE) # can add AUTO if multiple files need to be read in a go.
    dataset = dataset.with_options(ignore_order)
    dataset = dataset.map(read_labeled_tfrecord if labeled else read_unlabeled_tfrecord)
    return dataset


def get_training_dataset(GCS_DS_PATH, train_tfrec_path, BATCH_SIZE):
    
    print(""" Make Sure to
	Define how to read LABELED tfrecord data as per the LABELED_TFRECORD_FORMAT
	Rest of the helper functions are implemented.
	""")
    dataset = load_dataset(tf.io.gfile.glob(GCS_DS_PATH  + train_tfrec_path), labeled = True)
    cnt = 0
	for data in dataset:
		cnt += 1
    print(f"Loaded {train_tfrec_path} with {cnt} examples")
    dataset = dataset.repeat()
    dataset = dataset.shuffle(2048)
    dataset = dataset.batch(BATCH_SIZE)
    return dataset


def get_validation_dataset(GCS_DS_PATH,val_tfrec_path, BATCH_SIZE ):
    
    print(""" Make Sure to
	Define how to read LABELED tfrecord data as per the LABELED_TFRECORD_FORMAT
	Rest of the helper functions are implemented.
	""")
    
    dataset = load_dataset(tf.io.gfile.glob(GCS_DS_PATH + val_tfrec_path), labeled = True, ordered = False)
    cnt = 0
	for data in dataset:
		cnt += 1
    print(f"Loaded {val_tfrec_path} with {cnt} examples")
    dataset = dataset.batch(BATCH_SIZE)
    dataset = dataset.cache()
    
    return dataset


def get_test_dataset(GCS_DS_PATH, test_tfrec_path, BATCH_SIZE):
    
	print(""" Make Sure to
	Define how to read UNLABELED tfrecord data as per the UNLABELED_TFRECORD_FORMAT
	Rest of the helper functions are implemented.
	""")

	dataset = load_dataset(tf.io.gfile.glob(GCS_DS_PATH + test_tfrec_path), labeled = False, ordered = False)
	cnt = 0
	for data in dataset:
		cnt += 1
    print(f"Loaded {test_tfrec_path} with {cnt} examples")
    dataset = dataset.batch(BATCH_SIZE)
    return dataset


def count_num_examples(tfrecordfile, labeled = True):
	
	tfdataset = load_dataset(tfrecordfile, labeled)
	cnt = 0
	for data in tfdataset:
		cnt += 1
	print(f"{tfrecordfile} contains {cnt} Examples")

if __name__ == "__main__":
	pass
else:
	import tensorflow as tf
	if tf.__version__ == '2.2.0':
		pass
	else:
		print("Error! Tensorflow version mismatch as per the docs")