import asyncio

from PySide2.QtCore import QTimer, Qt, QSettings
from PySide2.QtGui import QImage, QPixmap
from PySide2.QtWidgets import (QPushButton, QTableView, QLabel, QHeaderView,
                               QHBoxLayout, QVBoxLayout, QFrame, QGridLayout,
                               QSpinBox, QDoubleSpinBox, QWidget, QAction)
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolBar)
from matplotlib.figure import Figure
from patchbay import ureg
from patchbay.patch import BaseUiPatch
from patchbay.qt.pint_widgets import PQDoubleSpinBox


class Patch(BaseUiPatch):
    def __init__(self, parent):
        self._parent = parent
        self.widgets = {}

        self.ui = self.make_ui()

    def make_ui(self):
        """Create and lay out UI elements."""

        freq = PQDoubleSpinBox(ureg.kHz)
        freq.setDecimals(3)
        freq.setRange(10, 20)
        freq.setSingleStep(0.001)
        freq.setKeyboardTracking(False)
        self.widgets['frequency'] = freq

        amplitude = PQDoubleSpinBox(ureg.V)
        amplitude.setDecimals(3)
        amplitude.setRange(0, 3.3)
        amplitude.setSingleStep(0.005)
        amplitude.setKeyboardTracking(False)
        self.widgets['amplitude'] = amplitude

        btn_enable = QPushButton('&Enable')
        btn_enable.setCheckable(True)

        btn_start = QPushButton()
        btn_start.setText('Start Measurement')
        btn_start.clicked.connect(self.run)
        self.widgets['btn_start'] = btn_start

        side_panel = QGridLayout()
        side_panel.setColumnStretch(0, 0)
        side_panel.setColumnStretch(1, 1)
        side_panel.setColumnStretch(2, 1)
        side_panel.setRowStretch(6, 1)  # shove everything to the top

        side_panel.addWidget(QLabel('<h2>Generator</h2>'), 0, 0, 1, 2)
        side_panel.addWidget(QLabel('Freq:'), 1, 0)
        side_panel.addWidget(freq, 1, 1)
        side_panel.addWidget(QLabel('Amp:'), 2, 0)
        side_panel.addWidget(amplitude, 2, 1)
        side_panel.addWidget(btn_enable, 3, 0, 1, 2)

        side_panel.addWidget(QLabel('<h2>Controls</h2>'), 4, 0, 1, 2)
        side_panel.addWidget(btn_start, 5, 0, 1, 2)

        graph = FigureCanvas(Figure(tight_layout=True))
        graph_toolbar = NavigationToolBar(graph, None)
        graph_toolbar.setObjectName('GraphToolBar')
        self.widgets['graph'] = graph

        axis = graph.figure.subplots()
        axis.grid()
        self.widgets['axis'] = axis

        vbox = QVBoxLayout()
        vbox.addWidget(graph)
        vbox.addWidget(graph_toolbar)

        hbox = QHBoxLayout()
        hbox.addLayout(side_panel)
        hbox.addLayout(vbox, 1)

        main_widget = QFrame()
        main_widget.setLayout(hbox)

        return main_widget

    def run(self):
        axis = self.widgets['axis']
        axis.plot([0,1,2,3], [1,3,5,7], '.')
        axis.relim()
        axis.autoscale_view()
        self.widgets['graph'].draw()

        loop = asyncio.get_event_loop()
        loop.create_task(self.rampup_amplitude())

    async def rampup_amplitude(self):
        self.widgets['btn_start'].setEnabled(False)
        amplitude = self.widgets['amplitude']
        amplitude.setValue(0 * ureg.V)
        for i in range(101):
            amplitude.setValue(i * 0.01 * ureg.V)
            await asyncio.sleep(0.1)
        self.widgets['btn_start'].setEnabled(True)

    def stop(self):
        pass

    def close(self):
        self.stop()
