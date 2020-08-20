from .mobject import MObject


class Combo(MObject):
    def __init__(self, allowed_values=["None"], initial_value=None, *args, **kwargs):
        super().__init__()
        self.type = "combo"
        self.allowed_values = list(allowed_values)
        self.data_type = type(self.allowed_values[0])
        if initial_value is None:
            self.write(self.allowed_values[0])
        else:
            self.write(initial_value)

    def associate(self, display=None, pre_name=""):
        # display
        if display is None:
            display = self.display
        # name
        name = pre_name + self.name
        # new object
        new_obj = Combo(
            initial_value=self.read(),
            display=display,
            allowed_values=self.allowed_values,
            name=name,
        )
        return new_obj

    def read_index(self):
        return self.allowed_values.index(self.read())

    def save(self, value=None):
        if value is not None:
            self.value.write(value)
        if self.has_ini:
            self.ini.write(
                self.section, self.option, self.value.read(), with_apostrophe=True
            )

    def set_allowed_values(self, allowed_values):
        """
        Set the allowed values of the Combo object.

        Parameters
        ----------
        allowed_values : list
            the new allowed values

        Notes
        ----------
        The value of the object is written to the first allowed value if the
        current value is not in the allowed values.
        """
        if allowed_values == self.allowed_values:
            return
        self.allowed_values = list(allowed_values)
        # update widget
        if self.has_widget:
            self.widget.currentIndexChanged.disconnect(self.write_from_widget)
            self.widget.clear()
            allowed_values_strings = [str(value) for value in self.allowed_values]
            self.widget.addItems(allowed_values_strings)
            self.widget.currentIndexChanged.connect(self.write_from_widget)
        # write value again
        if self.read() not in self.allowed_values:
            print(self.allowed_values)
            self.write(list(self.allowed_values)[0])
        else:
            self.write(self.read())

    def set_widget(self):
        allowed_values_strings = [str(value) for value in self.allowed_values]
        index = allowed_values_strings.index(str(self.read()))
        self.widget.setCurrentIndex(index)

    def write(self, value):
        # value will be maintained as original data type
        value = self.data_type(value)
        super().write(value)

    def write_from_widget(self):
        # needs to be defined method so we can connect and disconnect
        self.write(self.widget.currentText())

    def give_control(self, control_widget):
        self.widget = control_widget
        # fill out items
        allowed_values_strings = [str(value) for value in self.allowed_values]
        self.widget.addItems(allowed_values_strings)
        if self.read() is not None:
            self.widget.setCurrentIndex(allowed_values_strings.index(str(self.read())))
        # connect signals and slots
        self.updated.connect(self.set_widget)
        self.widget.currentIndexChanged.connect(self.write_from_widget)
        self.widget.setToolTip(self.tool_tip)
        self.widget.setDisabled(self.disabled)
        self.has_widget = True
