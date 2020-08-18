import datetime
import os

import numpy as np
import asyncio
import pandas as pd
from PySide2.QtCore import QTimer, Qt, QSettings
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtWidgets import (QPushButton, QTableView, QLabel, QHeaderView,
                               QHBoxLayout, QVBoxLayout, QFrame, QGridLayout,
                               QSpinBox, QDoubleSpinBox, QWidget, QAction)
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolBar)
from matplotlib.figure import Figure
import matplotlib.animation as animation
import sounddevice as sd
import math
import queue
import soundfile as sf

q = queue.Queue()


class Patch:
    def __init__(self, parent):
        self._parent = parent
        self.widgets = {}

        self.ui = self.make_ui()
        self.restore_settings()

        today = datetime.datetime.now().strftime('%Y-%m-%d')
        self.out_path = os.path.expanduser(
            os.path.join('~', 'EEPartners', f'{today}'))
        if not os.path.exists(self.out_path):
            os.mkdir(self.out_path)

        self.n_bins = 150
        self.s_width = 300
        self.i = 0
        self.im = np.zeros([self.n_bins, self.s_width])
        self.f_min = 100
        self.f_max = 6000
        self.start_devices()
        self.inputstream = None
        self.im_obj = self.widgets['axis'].imshow(self.im, cmap='gray_r', vmax=1, aspect='auto',
                                                  extent=[0, 1, self.f_max, self.f_min])

        self.widgets['axis'].invert_yaxis()
        # self.widgets['axis'].set_ylim([100, 6000])

        self.animator = animation.FuncAnimation(self.widgets['graph'].figure, self.update_image(),
                                                init_func=self.init_image(), interval=100)

        colors = 30, 34, 35, 91, 93, 97
        chars = ' :%#\t#%:'
        self.gradient = []
        for bg, fg in zip(colors, colors[1:]):
            for char in chars:
                if char == '\t':
                    bg, fg = fg, bg
                else:
                    self.gradient.append('\x1b[{};{}m{}'.format(fg, bg + 10, char))

    def init_image(self):
        def init_img():
            self.im_obj.set_data(np.zeros([self.n_bins, self.s_width]))
        return init_img

    def update_image(self):
        def update_img(i):
            self.im_obj.set_data(self.im)
            return self.im_obj
        return update_img

    def get_actions(self):
        return []

    def restore_settings(self):
        settings = QSettings()
        for key, default in {'sample_num': 0,
                             }.items():
            pass
            # self.widgets[key].setValue(float(settings.value(key, default)))

    def save_settings(self):
        settings = QSettings()
        for key in ['sample_num']:
            pass
            # settings.setValue(key, self.widgets[key].value())

    def start_devices(self):
        self.samplerate = sd.query_devices(None, 'input')['default_samplerate']
        self.df = (self.f_max - self.f_min) / (self.n_bins - 1)
        self.fftsize = math.ceil(self.samplerate / self.df)
        self.low_bin = math.floor(self.f_min / self.df)
        print(f'Sample rate: {self.samplerate} Hz\n'
              f'df: {self.df} Hz\n'
              f'FFT size: {self.fftsize}'
              f'{self.low_bin}')

    def get_callback(self):
        def callback(indata, outdata, frames, time, status):
            if status:
                text = ' ' + str(status) + ' '
                print('\x1b[34;40m', text.center(50, '#'), '\x1b[0m', sep='')
            if any(indata):
                q.put(indata.copy())
                outdata[:] = indata
                magnitude = np.abs(np.fft.rfft(indata[:, 0], n=self.fftsize))
                magnitude *= 100 / self.fftsize

                self.im[:, self.i] = magnitude[self.low_bin:self.low_bin + self.n_bins]
                self.i += 1
                if self.i == self.s_width:
                    self.i = 0
                self.im[:, self.i] = 0
                # self.widgets['axis'].imshow(self.im, animated=True, cmap='hot')
                # self.im_obj.set_data(self.im)
                # self.widgets['graph'].draw()

                line = (self.gradient[int(np.clip(x, 0, 1) * (len(self.gradient) - 1))]
                        for x in magnitude[self.low_bin:self.low_bin + 100])
                print(*line, sep='', end='\x1b[0m\n')
            else:
                print('no input')
        return callback

    def make_ui(self):
        """Create and lay out UI elements."""

        graph = FigureCanvas(Figure(tight_layout=True))
        graph_toolbar = NavigationToolBar(graph, None)
        graph_toolbar.setObjectName('GraphToolBar')
        self.widgets['graph'] = graph
        self.widgets['axis'] = graph.figure.subplots()
        # self.widgets['axis'].set_xlim(1.0, 1.6)
        # self.widgets['axis'].set_ylim(0, 4)
        self.widgets['axis'].grid()
        self.widgets['axis'].set_xlabel('Time [s]')
        self.widgets['axis'].set_ylabel('Frequency [Hz]')

        vbox = QVBoxLayout()
        vbox.addWidget(graph)
        vbox.addWidget(graph_toolbar)

        main_widget = QFrame()
        main_widget.setLayout(vbox)

        return main_widget

    def run(self):
        self.inputstream = sd.Stream(device=(None, None), channels=(1,2), callback=self.get_callback(),
                                     blocksize=int(self.samplerate * 50 / 1000),
                                     samplerate=self.samplerate)
        self.inputstream.start()
            # while True:
            #     response = input()
            #     if response in ('', 'q', 'Q'):
            #         break
            #     for ch in response:
            #         if ch == '+':
            #             args.gain *= 2
            #         elif ch == '-':
            #             args.gain /= 2
            #         else:
            #             print('\x1b[31;40m', usage_line.center(args.columns, '#'),
            #                   '\x1b[0m', sep='')
            #             break

        # np.random.seed(19680801)
        #
        # dt = 0.0005
        # t = np.arange(0.0, 20.0, dt)
        # s1 = np.sin(2 * np.pi * 100 * t)
        # s2 = 2 * np.sin(2 * np.pi * 400 * t)
        #
        # # create a transient "chirp"
        # s2[t <= 10] = s2[12 <= t] = 0
        #
        # # add some noise into the mix
        # nse = 0.01 * np.random.random(size=len(t))
        #
        # x = s1 + s2 + nse  # the signal
        # NFFT = 1024  # the length of the windowing segments
        # Fs = int(1.0 / dt)  # the sampling frequency

        # fig, (ax1, ax2) = plt.subplots(nrows=2)
        # axis = self.widgets['axis']
        # # axis.plot(t, x)
        # Pxx, freqs, bins, im = axis.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=900)
        # axis.relim()
        # self.widgets['graph'].draw()

        # The `specgram` method returns 4 objects. They are:
        # - Pxx: the periodogram
        # - freqs: the frequency vector
        # - bins: the centers of the time bins
        # - im: the matplotlib.image.AxesImage instance representing the data in the plot

    def stop(self):
        if self.inputstream is not None:
            self.inputstream.stop()
            self.inputstream.close()
            self.inputstream = None

            axis = self.widgets['axis']
            data = np.array([])
            while not q.empty():
                data = np.concatenate([data, q.get().flatten()])
            axis.specgram(data, NFFT=1024, Fs=self.samplerate, noverlap=512)
            axis.relim()
            axis.set_ylim(100, 6000)
            self.widgets['graph'].draw()

            filename = os.path.join(self.out_path, datetime.datetime.now().strftime('%H-%M-%S.wav'))
            with sf.SoundFile(filename, mode='x', samplerate=int(self.samplerate), channels=1) as file:
                file.write(data)

    def close(self):
        self.stop()
        self.save_settings()