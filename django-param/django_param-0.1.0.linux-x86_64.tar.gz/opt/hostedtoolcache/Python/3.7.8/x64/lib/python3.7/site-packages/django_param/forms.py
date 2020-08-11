from django import forms
import param
from .widget_map import widget_map
from pandas import DataFrame
from datetime import datetime, date


class ParamForm(forms.Form):
    _param = None
    read_only = None
    _error_key_list = []
    cleaned_data = ""
    widget_map = widget_map

    def __init__(self, *args, **kwargs):
        param_class = kwargs.pop('param', None)
        if param_class is None:
            raise KeyError('Keyword argument param is required.')
        if not isinstance(param_class, param.Parameterized):
            raise ValueError(f'{param_class} must be an instance of param.Parameterized.')
        self._param = param_class

        read_only = kwargs.pop('read_only', None)
        if read_only:
            self.read_only = read_only

        custom_widget_map = kwargs.pop('widget_map', None)
        if custom_widget_map:
            self.widget_map = custom_widget_map
        super().__init__(*args, **kwargs)
        self._generate_form_fields()

    @property
    def param(self):
        return self._param

    @property
    def widget(self):
        return self.widget_map

    def _add_error(self, key, message):
        # Only add error once for each parameter to avoid duplicate
        if key not in self._error_key_list:
            self._error_key_list.append(key)
            self.add_error(key, str(message))

    def _set_and_validate_data(self, data):
        # To handle dataframe case
        dataframe_key_list = []

        for key, value in data.items():
            if key != 'csrfmiddlewaretoken':
                if get_dataframe_name(key):
                    variable_name, dataframe_name = get_dataframe_name(key)
                    dataframe_key_list.append(variable_name)
                else:
                    self._set_and_validate_data_name(data, key)
        if dataframe_key_list:
            self._set_and_validate_dataframe(data, dataframe_key_list, dataframe_name)

    def _set_and_validate_dataframe(self, data, data_list, dataframe_name):
        # Handle Dataframe case
        data_dict = {}
        for key in data_list:
            data_dict[key] = data.getlist(key + "___" + dataframe_name + "__")
        value = DataFrame.from_dict(data_dict)
        # Update param
        self.param.set_param(dataframe_name, value)

    def _set_and_validate_data_name(self, data, name):
        # Find out if it is dataframe
        is_dict = False
        if isinstance(self.param.params()[name], (param.List, param.ListSelector, param.ObjectSelector)):
            is_dict = True
        value_temp = data.getlist(name)

        # Clean up data
        if len(value_temp) > 1:
            value = clean_data(value_temp, is_dict=is_dict)
        else:
            value = clean_data(data.get(name), is_dict=is_dict)

        # Selector only take one value, not list.
        if isinstance(self.param.params()[name], (param.Selector, param.FileSelector)):
            if isinstance(value, list) and len(value) > 0:
                value = value[0]

        # Convert to datetime object if neccessary
        if isinstance(self.param.inspect_value(name), (date, datetime)):
            date_time_str = data[name]
            if ":" in date_time_str:
                date_time_format = '%m-%d-%Y %H:%M'
                value = datetime.strptime(date_time_str, date_time_format)
            else:
                date_time_format = '%m-%d-%Y'
                value = datetime.strptime(date_time_str, date_time_format).date()
        try:
            # Update param
            self.param.set_param(name, value)
        except ValueError as e:
            self._add_error(name, e)

    def _generate_form_fields(self):
        """
        Create a Django form from a Parameterized object.

        Returns:
            Form: a Django form with fields matching the parameters of the given parameterized object.
        """
        params = list(filter(lambda x: (x.precedence is None or x.precedence >= 0) and not x.constant,
                             self.param.params().values()))
        for p in sorted(params, key=lambda p: p.precedence or 9999):
            # TODO: Pass p.__dict__ as second argument instead of arbitrary
            p_name = p.name

            # Preserve param tuple type.
            if self.data:
                if isinstance(getattr(self.param, p.name), tuple):
                    p.default = tuple(self.data.getlist(p.name))

            # Preserve initial options for Selector
            if isinstance(self.param.params()[p_name],
                          (param.Selector, param.ListSelector, param.ObjectSelector, param.FileSelector,
                           param.MultiFileSelector)):
                p.default = self.param.params()[p_name].objects
            self.fields[p_name] = self.widget[type(p)](self.param, p, p.name)
            self.fields[p_name].label = p.name.replace("_", " ").title()
            if self.read_only is None:
                widget_attribute = {'class': 'form-control'}
            else:
                # TODO: Should this be readonly instead of disable?
                widget_attribute = {'class': 'form-control', 'disabled': self.read_only}
            self.fields[p_name].widget.attrs.update(widget_attribute)
        # self.fields = self.base_fields

    def as_param(self):
        self._clean()
        return self.param

    def _clean(self):
        self.cleaned_data = super().clean()
        # Use bound data to set the value if we both have bound and initial data.
        if self.is_bound and self.initial:
            self._set_and_validate_data(self.data)
            return
        else:
            # Set values according to bound data
            if self.is_bound:
                self._set_and_validate_data(self.data)
                return
            # Set values according to initial data
            if self.initial:
                self._set_and_validate_data(self.initial)
                return


def clean_data(in_data, is_dict=False):
    if isinstance(in_data, (list, tuple)):
        out_data = []
        for data in in_data:
            out_data.append(convert_string(data))
        if not is_dict:
            out_data = tuple(out_data)
    else:
        out_data = convert_string(in_data)
        if is_dict:
            temp_data = list()
            temp_data.append(out_data)
            out_data = temp_data
    return out_data


def convert_string(data):
    if is_number(data):
        if "." in data:
            data = float(data)
        else:
            data = int(data)
    if data == 'True' or data == 'on':
        data = True
    if data == 'False':
        data = False
    return data


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def get_dataframe_name(s):
    # Return list with variable_name, and dataframe_name if the type is dataframe.
    if s[-2:] == "__":
        s = s[:-2]
        dataframe_name = s.split("___")[-1]
        variable_name = s.split("___")[0]
        return variable_name, dataframe_name
    else:
        return False
