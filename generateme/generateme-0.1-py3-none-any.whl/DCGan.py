"""Simplified code which can be used for production purposes. Once the generator 
is trained we don't need the Discriminator so we can discard it."""
import torch
import torchvision
from torchvision import transforms, datasets
import matplotlib.pyplot as plt
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import os
from torchvision.utils import save_image
import torchvision.utils as vutils

if torch.cuda.is_available():
    device = torch.device("cuda:0")
else:
    device = torch.device("cpu")
        
class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.convTr1 = nn.ConvTranspose2d(100, 64 * 8, 4, 1, 0, bias = False)
        self.batchNorm1 = nn.BatchNorm2d(64 * 8)
        self.convTr2 = nn.ConvTranspose2d(64 * 8, 64 * 4, 4, 2, 1, bias = False)
        self.batchNorm2 = nn.BatchNorm2d(64 * 4)
        self.convTr3 = nn.ConvTranspose2d(64 * 4, 64 * 2, 4, 2, 1, bias = False)
        self.batchNorm3 = nn.BatchNorm2d(64 * 2)
        self.convTr4 = nn.ConvTranspose2d(64 * 2, 64, 4, 2, 1, bias = False)
        self.batchNorm4 = nn.BatchNorm2d(64)
        self.convTr5 = nn.ConvTranspose2d(64, 3, 4, 2, 1, bias = False)

    def forward(self, x):
        x = F.relu_(self.batchNorm1(self.convTr1(x)))
        x = F.relu_(self.batchNorm2(self.convTr2(x)))
        x = F.relu_(self.batchNorm3(self.convTr3(x)))
        x = F.relu_(self.batchNorm4(self.convTr4(x)))
        x = self.convTr5(x)
        
        return torch.tanh(x)

#create the generator and moving it to the gpu if available
netG = Generator().to(device)

#loading the pretrained model
folder = os.path.dirname(os.path.abspath(__file__))
file = my_file = os.path.join(folder, "static/Models/dcGanGeneratorModel.pt")
netG.load_state_dict(torch.load(file, map_location=torch.device("cpu")))

#You can call this method from an api for example and it will return the numpy
#corresponding to the image.
def getConvImage():
  with torch.no_grad():
    test = torch.randn(128, 100, 1, 1, device=device)
    generated = netG(test)
    numpy = np.transpose(vutils.make_grid(generated[0].to(device), padding=5, normalize=True).cpu(),(1,2,0)).numpy()
    file = my_file = os.path.join(folder, "static/Photos/image.png")
    save_image(generated[0].view(3, 64, 64), file, normalize = True)
    return numpy