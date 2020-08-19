import torch
import torch.nn as nn
from doc.deeplab_resnet import DeepLabv3_plus

class DeepLabv3plus(nn.Module):
    def __init__(self, params):
        super(DeepLabv3plus, self).__init__()
        self.params = params
        self.in_chns   = self.params['in_chns']
        self.n_class   = self.params['class_num']
        self.output_stride = self.params['output_stride']
        self.network = DeepLabv3_plus(nInputChannels = self.in_chns,
                                    n_classes = self.n_class,
                                    os = self.output_stride, 
                                    pretrained = False, _print=True)
    def forward(self, x):
        x_shape = list(x.shape)
        if(len(x_shape) == 5):
            [N, C, D, H, W] = x_shape
            new_shape = [N*D, C, H, W]
            x = torch.transpose(x, 1, 2)
            x = torch.reshape(x, new_shape)
        output = self.network(x)
        if(len(x_shape) == 5):
            new_shape = [N, D] + list(output.shape)[1:]
            output = torch.reshape(output, new_shape)
            output = torch.transpose(output, 1, 2)
        return output
