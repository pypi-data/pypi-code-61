__all__ = ["ScrollArea"]


from qtpy import QtCore, QtWidgets


class ScrollArea(QtWidgets.QScrollArea):
    def __init__(self, show_bar=True):
        super().__init__()
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setWidgetResizable(True)
        self.setFixedWidth(320)
        if show_bar:
            self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.child = QtWidgets.QWidget()
        self.child.setFixedWidth(300)
        self.child.setLayout(QtWidgets.QVBoxLayout())
        # TODO: self.child.layout().setMargin(5)
        self.child.layout().addStretch(1)
        self.setWidget(self.child)

    def add_widget(self, widget):
        self.child.layout().insertWidget(self.child.layout().count() - 1, widget)
