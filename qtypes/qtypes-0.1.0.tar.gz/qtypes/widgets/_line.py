"""Class for a graphical line."""


import os

from qtpy import QtWidgets

from ..core.ini import INI


here = os.path.abspath(os.path.dirname(__file__))

colors = INI(os.path.join(here, "colors.ini")).dictionary["night"]


class Line(QtWidgets.QFrame):
    """
    direction: 'V' or 'H'
    """

    def __init__(self, direction):
        super().__init__()
        if direction == "V":
            self.setFrameShape(QtWidgets.QFrame.VLine)
        else:
            self.setFrameShape(QtWidgets.QFrame.HLine)
        StyleSheet = "QFrame{border: 2px solid custom_color; border-radius: 0px; padding: 0px;}".replace(
            "custom_color", colors["foreground"]
        )
        self.setStyleSheet(StyleSheet)
