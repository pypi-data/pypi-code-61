'''NXOS N7K: Image Handler Class'''

# Python
import os

# Genie
from genie.libs.clean.stages.image_handler import ImageHandler as CommonImageHandler


class ImageHandler(CommonImageHandler):


    def __init__(self, device, images, *args, **kwargs):
        super().__init__(device, images, *args, **kwargs)

        # Set 'kickstart' and 'system' images
        if self.images:
            if isinstance(self.images, dict):
                for key, value in self.images.items():
                    try:
                        assert key in ['kickstart', 'system']
                    except AssertionError:
                        raise Exception("Invalid key '{}' provided for N7K images"
                                        "\nValid keys are 'kickstart' and 'system'")

                    # incase the file key is used
                    if isinstance(value, dict):
                        image_list = value['file']
                    else:
                        image_list = value

                    if len(image_list) > 1:
                        raise Exception("Found more than 1 image for '{}' image".\
                                        format(key))

                    setattr(self, key, image_list)
            elif isinstance(self.images, list) and len(self.images)==2:
                # Set 'kickstart'
                setattr(self, 'kickstart', [self.images[0]])
                # Set 'system'
                setattr(self, 'system', [self.images[1]])
            else:
                raise Exception("Expecting 'kickstart' and 'system' images for "
                                "NXOS N7K platform provided under 'images' "
                                "key as a list or dictionary")
        else:
            raise Exception("'images' list or dictionary not provided and is "
                            "expected for 'nxos'")

    def update_image_references(self, section):
        # section.parameters['image_mapping'] shall be saved in any
        # stage that modifies the image name/path
        if 'image_mapping' in section.parameters:

            for index,image in enumerate(self.system):
                # change the saved image to the new image name/path
                self.system[index] = section.parameters['image_mapping'].get(image, self.system[index])

            for index,image in enumerate(self.kickstart):
                # change the saved image to the new image name/path
                self.kickstart[index] = section.parameters['image_mapping'].get(image, self.kickstart[index])

    def update_tftp_boot(self):
        '''Update clean section 'tftp_boot' with image information'''

        tftp_boot = self.device.clean.setdefault('tftp_boot', {})
        tftp_boot.update({'image': self.kickstart + self.system})

    def update_copy_to_linux(self):
        '''Update clean section 'copy_to_linux' with image information'''

        # Init 'copy_to_linux' defaults
        origin = self.device.clean.setdefault('copy_to_linux', {}).\
                                          setdefault('origin', {})
        origin.update({'files': self.kickstart + self.system})

    def update_copy_to_device(self):
        '''Update clean stage 'copy_to_device' with image information'''

        origin = self.device.clean.setdefault('copy_to_device', {}).\
                                   setdefault('origin', {})
        origin.update({'files': self.kickstart + self.system})


    def update_change_boot_variable(self):
        '''Update clean stage 'change_boot_variable' with image information'''

        images = self.device.clean.setdefault('change_boot_variable', {}).\
                          setdefault('images', {})
        images.update({'kickstart': self.kickstart})
        images.update({'system': self.system})

    def update_verify_running_image(self):
        '''Update clean stage 'verify_running_image' with image information'''

        verify_running_image = self.device.clean.setdefault('verify_running_image', {})
        verify_running_image.update({'images': self.kickstart + self.system})

