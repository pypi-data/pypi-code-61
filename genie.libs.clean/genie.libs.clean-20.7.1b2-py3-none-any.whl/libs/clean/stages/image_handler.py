'''Common OS: Image Handler Class'''


class ImageHandler(object):


    def __init__(self, device, images, *args, **kwargs):
        self.device = device
        self.images = images

    def update_section(self, section_uid):
        ''' Initializes section dictionary and calls update method for
            respective method '''

        if (section_uid not in self.device.clean or
                not self.device.clean[section_uid]):
            self.device.clean[section_uid] = {}

        # call the ImageHandler update method
        if hasattr(self, 'update_' + section_uid):
            getattr(self, 'update_' + section_uid)()


