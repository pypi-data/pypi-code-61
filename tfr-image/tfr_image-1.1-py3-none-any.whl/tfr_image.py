import random
import math
import os
import sys
from PIL import Image
import tensorflow as tf
from tfr_image.utils import (
    get_filenames_and_classes,
    write_label_file,
    bytes_feature,
    int64_feature,
)


class TFRimage(object):
    def create_tfrecords(
        self,
        dataset_dir,
        tfrecord_filename,
        validation_size=0,
        num_shards=2,
        random_seed=42,
    ):
        
        arguments = {"dataset_dir": dataset_dir, "tfrecord_filename": tfrecord_filename}

        for name, argu in arguments.items():
            if not argu:
                raise ValueError(
                    "{} is empty. Please state a tfrecord_filename argument.".format(
                        name
                    )
                )

        # Get a list of photo_filenames
        photo_filenames, class_names = get_filenames_and_classes(dataset_dir)

        # Refer each of the class name to a specific integer number for predictions later
        class_names_to_ids = dict(zip(class_names, range(len(class_names))))

        # Find the number of validation examples
        num_validation = int(validation_size * len(photo_filenames))

        # Divide the training datasets into train and validation
        random.seed(random_seed)
        random.shuffle(photo_filenames)
        training_filenames = photo_filenames[num_validation:]
        validation_filenames = photo_filenames[:num_validation]

        filenames_split = {
            "train": training_filenames,
            "validation": validation_filenames,
        }

        for split, filenames in filenames_split.items():
            if filenames:
                self._convert_dataset(
                    split,
                    filenames,
                    class_names_to_ids,
                    dataset_dir=dataset_dir,
                    tfrecord_filename=tfrecord_filename,
                    num_chards=num_shards,
                )

        # Write the labels file:
        labels_to_class_names = dict(zip(range(len(class_names)), class_names))
        write_label_file(labels_to_class_names, dataset_dir)
        print("\nFinished converting the %s dataset!" % (tfrecord_filename))

    def _convert_dataset(
        self,
        split_name,
        filenames,
        class_names_to_ids,
        dataset_dir,
        tfrecord_filename,
        num_chards,
    ):
        """Converts the given filenames to a TFRecord dataset.

        Args:
        split_name: The name of the dataset, either 'train' or 'validation'.
        filenames: A list of absolute paths to png or jpg images.
        class_names_to_ids: A dictionary from class names (strings) to ids
          (integers).
        dataset_dir: The directory where the converted datasets are stored.
        """
        assert split_name in ["train", "validation"]

        num_per_shard = int(math.ceil(len(filenames) / float(num_chards)))

        for shard_id in range(num_chards):
            output_filename = self._get_dataset_filename(
                dataset_dir,
                split_name,
                shard_id,
                tfrecord_filename=tfrecord_filename,
                num_chards=num_chards,
            )

            with tf.io.TFRecordWriter(output_filename) as tfrecord_writer:
                start_ndx = shard_id * num_per_shard
                end_ndx = min((shard_id + 1) * num_per_shard, len(filenames))
                for i in range(start_ndx, end_ndx):
                    sys.stdout.write(
                        "\r>> Converting image %d/%d shard %d"
                        % (i + 1, len(filenames), shard_id)
                    )
                    sys.stdout.flush()

                    # Read the filename:
                    image_data = tf.io.gfile.GFile(filenames[i], "rb").read()
                    with tf.io.gfile.GFile(filenames[i], "rb") as f:
                        image = Image.open(f)

                    height, width = image.size
                    class_name = os.path.basename(os.path.dirname(filenames[i]))
                    class_id = class_names_to_ids[class_name]

                    example = self._image_to_tfexample(
                        image_data, b"jpg", height, width, class_id
                    )
                    tfrecord_writer.write(example.SerializeToString())

        sys.stdout.write("\n")
        sys.stdout.flush()

    def _get_dataset_filename(
        self, dataset_dir, split_name, shard_id, tfrecord_filename, num_chards
    ):
        output_filename = "%s_%s_%05d-of-%05d.tfrecord" % (
            tfrecord_filename,
            split_name,
            shard_id,
            num_chards,
        )
        return os.path.join(dataset_dir, output_filename)

    def _image_to_tfexample(self, image_data, image_format, height, width, class_id):
        return tf.train.Example(
            features=tf.train.Features(
                feature={
                    "image": bytes_feature(image_data),
                    "format": bytes_feature(image_format),
                    "label": int64_feature(class_id),
                    "height": int64_feature(height),
                    "width": int64_feature(width),
                }
            )
        )
