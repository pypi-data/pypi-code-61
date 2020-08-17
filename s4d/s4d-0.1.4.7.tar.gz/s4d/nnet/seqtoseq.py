# -*- coding: utf-8 -*-
#
# This file is part of s4d.
#
# s4d is a python package for speaker diarization.
# Home page: http://www-lium.univ-lemans.fr/s4d/
#
# s4d is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# s4d is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with s4d.  If not, see <http://www.gnu.org/licenses/>.


"""
Copyright 2014-2020 Anthony Larcher
"""

import os
import sys
import numpy
import random
import h5py
import shutil
import torch
import torch.nn as nn
from torch import optim
from torch.utils.data import Dataset
import logging

from sidekit.nnet.vad_rnn import BLSTM
from torch.utils.data import DataLoader

__license__ = "LGPL"
__author__ = "Anthony Larcher"
__copyright__ = "Copyright 2015-2020 Anthony Larcher"
__maintainer__ = "Anthony Larcher"
__email__ = "anthony.larcher@univ-lemans.fr"
__status__ = "Production"
__docformat__ = 'reS'


def save_checkpoint(state, is_best, filename='checkpoint.pth.tar', best_filename='model_best.pth.tar'):
    """

    :param state:
    :param is_best:
    :param filename:
    :param best_filename:
    :return:
    """
    torch.save(state, filename)
    if is_best:
        shutil.copyfile(filename, best_filename)

class PreNet(nn.Module):
    def __init__(self,
               sample_rate=16000,
               windows_duration=0.2,
               frame_shift=0.01):
        super(PreNet, self).__init__()

        windows_length = int(sample_rate * windows_duration)
        if windows_length % 2:
            windows_length += 1
        stride_0 = int(sample_rate * frame_shift)

        self.conv0 = torch.nn.Conv1d(1, 64, windows_length, stride=stride_0, dilation=1)
        self.conv1 = torch.nn.Conv1d(64, 64, 3, dilation=1)
        self.conv2 = torch.nn.Conv1d(64, 64, 3, dilation=1)

        self.norm0 = torch.nn.BatchNorm1d(64)
        self.norm1 = torch.nn.BatchNorm1d(64)
        self.norm2 = torch.nn.BatchNorm1d(64)

        self.activation = torch.nn.LeakyReLU(0.2)


    def forward(self, input):

        x = self.norm0(self.activation(self.conv0(input)))
        x = self.norm1(self.activation(self.conv1(x)))
        output = self.norm2(self.activation(self.conv2(x)))

        return output




class BLSTM(nn.Module):
    """
    Bi LSTM model used for voice activity detection or speaker turn detection
    """
    def __init__(self,
                 input_size,
                 lstm_1,
                 lstm_2,
                 linear_1,
                 linear_2,
                 output_size=1):
        """

        :param input_size:
        :param lstm_1:
        :param lstm_2:
        :param linear_1:
        :param linear_2:
        :param output_size:
        """
        super(BLSTM, self).__init__()

        self.lstm_1 = nn.LSTM(input_size, lstm_1 // 2, bidirectional=True, batch_first=True)
        self.lstm_2 = nn.LSTM(lstm_1, lstm_2 // 2, bidirectional=True, batch_first=True)
        self.linear_1 = nn.Linear(lstm_2, linear_1)
        self.linear_2 = nn.Linear(linear_1, linear_2)
        self.output = nn.Linear(linear_2, output_size)
        self.hidden = None

    def forward(self, inputs):
        """

        :param inputs:
        :return:
        """
        if self.hidden is None:
            hidden_1, hidden_2 = None, None
        else:
            hidden_1, hidden_2 = self.hidden
        tmp, hidden_1 = self.lstm_1(inputs, hidden_1)
        x, hidden_2 = self.lstm_2(tmp, hidden_2)
        self.hidden = (hidden_1, hidden_2)
        x = torch.tanh(self.linear_1(x))
        x = torch.tanh(self.linear_2(x))
        x = torch.sigmoid(self.output(x))
        return x


class SeqToSeq(nn.Module):
    """
    Bi LSTM model used for voice activity detection or speaker turn detection
    """
    def __init__(self,
                 input_size,
                 lstm_1,
                 lstm_2,
                 linear_1,
                 linear_2,
                 output_size=1):

        super(SeqToSeq, self).__init__()
        self.preprocessor = PreNet(sample_rate=16000,
                                   windows_duration=0.2,
                                   frame_shift=0.01)

        self.lstm_1 = nn.LSTM(input_size, lstm_1 // 2, bidirectional=True, batch_first=True)
        self.lstm_2 = nn.LSTM(lstm_1, lstm_2 // 2, bidirectional=True, batch_first=True)
        self.linear_1 = nn.Linear(lstm_2, linear_1)
        self.linear_2 = nn.Linear(linear_1, linear_2)
        self.output = nn.Linear(linear_2, output_size)
        self.hidden = None

    def forward(self, inputs):
        """

        :param inputs:
        :return:
        """
        if self.hidden is None:
            hidden_1, hidden_2 = None, None
        else:
            hidden_1, hidden_2 = self.hidden
        tmp, hidden_1 = self.lstm_1(inputs, hidden_1)
        x, hidden_2 = self.lstm_2(tmp, hidden_2)
        self.hidden = (hidden_1, hidden_2)
        x = torch.tanh(self.linear_1(x))
        x = torch.tanh(self.linear_2(x))
        x = torch.sigmoid(self.output(x))
        return x


def seqTrain(data_dir,
             mode,
             duration=2.,
             seg_shift=0.25,
             filter_type="gate",
             collar_duration=0.1,
             framerate=16000,
             epochs=100,
             batch_size=32,
             lr=0.0001,
             loss="cross_validation",
             patience=10,
             tmp_model_name=None,
             best_model_name=None,
             multi_gpu=True,
             opt='sgd',
             num_thread=10
             ):
    """

    :param data_dir:
    :param mode:
    :param duration:
    :param seg_shift:
    :param filter_type:
    :param collar_duration:
    :param framerate:
    :param epochs:
    :param lr:
    :param loss:
    :param patience:
    :param tmp_model_name:
    :param best_model_name:
    :param multi_gpu:
    :param opt:
    :return:
    """
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    # Start from scratch
    model = SeqToSeq()
    # TODO implement a model adaptation

    if torch.cuda.device_count() > 1 and multi_gpu:
        print("Let's use", torch.cuda.device_count(), "GPUs!")
        model = torch.nn.DataParallel(model)
    else:
        print("Train on a single GPU")
    model.to(device)

    """
    Create two dataloaders for training and evaluation
    """
    training_set, validation_set = None, None
    training_loader = DataLoader(training_set,
                                 batch_size=batch_size,
                                 shuffle=True,
                                 drop_last=True,
                                 num_workers=num_thread)

    validation_loader = DataLoader(validation_set,
                                   batch_size=batch_size,
                                   drop_last=True,
                                   num_workers=num_thread)

    """
    Set the training options
    """
    if opt == 'sgd':
        _optimizer = torch.optim.SGD
        _options = {'lr': lr, 'momentum': 0.9}
    elif opt == 'adam':
        _optimizer = torch.optim.Adam
        _options = {'lr': lr}
    elif opt == 'rmsprop':
        _optimizer = torch.optim.RMSprop
        _options = {'lr': lr}

    params = [
        {
            'params': [
                param for name, param in model.named_parameters() if 'bn' not in name
            ]
        },
        {
            'params': [
                param for name, param in model.named_parameters() if 'bn' in name
            ],
            'weight_decay': 0
        },
    ]

    if type(model) is SeqToSeq:
        optimizer = _optimizer([
            {'params': model.parameters(),
             'weight_decay': model.weight_decay},],
            **_options
        )
    else:
        optimizer = _optimizer([
            {'params': model.module.sequence_network.parameters(),
             'weight_decay': model.module.sequence_network_weight_decay},],
            **_options
        )

    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, 'min', verbose=True)

    best_accuracy = 0.0
    best_accuracy_epoch = 1
    curr_patience = patience
    for epoch in range(1, epochs + 1):
        # Process one epoch and return the current model
        if curr_patience == 0:
            print(f"Stopping at epoch {epoch} for cause of patience")
            break
        model = train_epoch(model,
                            epoch,
                            training_loader,
                            optimizer,
                            log_interval,
                            device=device)

        # Add the cross validation here
        accuracy, val_loss = cross_validation(model, validation_loader, device=device)
        logging.critical("*** Cross validation accuracy = {} %".format(accuracy))

        # Decrease learning rate according to the scheduler policy
        scheduler.step(val_loss)
        print(f"Learning rate is {optimizer.param_groups[0]['lr']}")

        # remember best accuracy and save checkpoint
        is_best = accuracy > best_accuracy
        best_accuracy = max(accuracy, best_accuracy)

        if type(model) is SeqToSeq:
            save_checkpoint({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'accuracy': best_accuracy,
                'scheduler': scheduler
            }, is_best, filename=tmp_model_name + ".pt", best_filename=best_model_name + '.pt')
        else:
            save_checkpoint({
                'epoch': epoch,
                'model_state_dict': model.module.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'accuracy': best_accuracy,
                'scheduler': scheduler
            }, is_best, filename=tmp_model_name + ".pt", best_filename=best_model_name + '.pt')

        if is_best:
            best_accuracy_epoch = epoch
            curr_patience = patience
        else:
            curr_patience -= 1

    logging.critical(f"Best accuracy {best_accuracy * 100.} obtained at epoch {best_accuracy_epoch}")


def train_epoch(model, epoch, training_loader, optimizer, log_interval, device):
    """

    :param model:
    :param epoch:
    :param training_loader:
    :param optimizer:
    :param log_interval:
    :param device:
    :param clipping:
    :return:
    """
    model.train()
    criterion = torch.nn.CrossEntropyLoss(reduction='mean')

    accuracy = 0.0
    for batch_idx, (data, target) in enumerate(training_loader):
        target = target.squeeze()
        optimizer.zero_grad()
        output = model(data.to(device),target=target.to(device))
        loss = criterion(output, target.to(device))
        loss.backward()
        optimizer.step()
        accuracy += (torch.argmax(output.data, 1) == target.to(device)).sum()

        if batch_idx % log_interval == 0:
            batch_size = target.shape[0]
            logging.critical('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}\tAccuracy: {:.3f}'.format(
                epoch, batch_idx + 1, training_loader.__len__(),
                100. * batch_idx / training_loader.__len__(), loss.item(),
                100.0 * accuracy.item() / ((batch_idx + 1) * batch_size)))
    return model


def cross_validation(model, validation_loader, device):
    """

    :param model:
    :param validation_loader:
    :param device:
    :return:
    """
    model.eval()

    accuracy = 0.0
    loss = 0.0
    criterion = torch.nn.CrossEntropyLoss()
    with torch.no_grad():
        for batch_idx, (data, target) in enumerate(validation_loader):
            batch_size = target.shape[0]
            target = target.squeeze()
            output = model(data.to(device),target=target.to(device),is_eval=True)
            print(output.shape)
            accuracy += (torch.argmax(output.data, 1) == target.to(device)).sum()

            loss += criterion(output, target.to(device))
    return 100. * accuracy.cpu().numpy() / ((batch_idx + 1) * batch_size), \
           loss.cpu().numpy() / ((batch_idx + 1) * batch_size)

