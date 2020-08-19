import torch
import torch.nn as nn
from cnn.SegmentationModel import EESPNet_Seg

class EESPNetV2(nn.Module):
    def __init__(self, params):
        super(EESPNetV2, self).__init__()
        self.params = params
        self.in_chns   = self.params['in_chns']
        self.n_class   = self.params['class_num']
        self.output_stride = self.params['output_stride']
        self.network = EESPNet_Seg( classes = self.n_class,
                                    s = self.output_stride, 
                                    pretrained = None)
    def forward(self, x):
        x_shape = list(x.shape)
        if(len(x_shape) == 5):
            [N, C, D, H, W] = x_shape
            new_shape = [N*D, C, H, W]
            x = torch.transpose(x, 1, 2)
            x = torch.reshape(x, new_shape)
        output = self.network(x)
        if(isinstance(output, tuple)):
            output = output[0]

        if(len(x_shape) == 5):
            new_shape = [N, D] + list(output.shape)[1:]
            output = torch.reshape(output, new_shape)
            output = torch.transpose(output, 1, 2)
        return output
