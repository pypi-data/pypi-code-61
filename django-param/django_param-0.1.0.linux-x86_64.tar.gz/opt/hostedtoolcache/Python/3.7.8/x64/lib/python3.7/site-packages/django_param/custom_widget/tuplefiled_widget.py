from django import forms
import pickle


class TupleFieldWidget(forms.widgets.MultiWidget):
    def __init__(self, attrs=None):
        widgets = [forms.TextInput()]
        super(TupleFieldWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if not isinstance(value, tuple):
            if value:
                return pickle.loads(value)
            else:
                return ['', '']
        else:
            return value

    def custom_get_context(self, name, value, attrs, context, **kwargs):
        xy = kwargs.get('xy', False)
        range_option = kwargs.get('range_option', False)
        if self.is_localized:
            for widget in self.widgets:
                widget.is_localized = self.is_localized
        # value is a list of values, each corresponding to a widget
        # in self.widgets.
        if not isinstance(value, list):
            value = self.decompress(value)

        final_attrs = context['widget']['attrs']
        input_type = final_attrs.pop('type', None)
        id_ = final_attrs.get('id')
        subwidgets = []
        for i, widget in enumerate(self.widgets):
            if input_type is not None:
                widget.input_type = input_type
            widget_name = name
            try:
                widget_value = value[i]
            except IndexError:
                widget_value = None
            if id_:
                widget_attrs = final_attrs.copy()
                widget_attrs['id'] = '%s_%s' % (id_, i)
            else:
                widget_attrs = final_attrs

            # Set step to any
            widget_attrs['step'] = "any"

            # Add label for xy coordinates
            widget_handler = widget.get_context(widget_name, widget_value, widget_attrs)['widget']
            if i == 0:
                if xy:
                    widget_handler['label'] = "X"
                if range_option:
                    widget_handler['label'] = "Min"
            else:
                if xy:
                    widget_handler['label'] = "Y"
                if range_option:
                    widget_handler['label'] = "Max"
            subwidgets.append(widget_handler)
        context['widget']['subwidgets'] = subwidgets
        return context

    def get_context(self, name, value, attrs):
        context = forms.Widget.get_context(self, name, value, attrs)
        self.widgets = []
        # Update number of widgets
        for i in range(len(value)):
            if isinstance(value[i], (float, int)):
                # Since bool inherits from int
                if isinstance(value[i], bool):
                    self.widgets.append(forms.CheckboxInput())
                else:
                    self.widgets.append(forms.NumberInput())
            else:
                if value[i] == "on":
                    self.widgets.append(forms.CheckboxInput())
                else:
                    self.widgets.append(forms.TextInput())

        context = self.custom_get_context(name, value, attrs, context)
        return context

    def value_from_datadict(self, data, files, name):
        # Override this method since we use one name for all the widgets.
        values = data.getlist(name)
        return values


class NumericTupleFieldWidget(TupleFieldWidget):
    def get_context(self, name, value, attrs):
        context = forms.Widget.get_context(self, name, value, attrs)
        self.widgets = []
        # Update number of widgets
        for i in range(len(value)):
            self.widgets.append(forms.NumberInput())

        context = self.custom_get_context(self, name, value, attrs, context)
        return context


class XYTupleFieldWidget(TupleFieldWidget):
    def get_context(self, name, value, attrs):
        context = forms.Widget.get_context(self, name, value, attrs)
        self.widgets = []
        # Update number of widgets
        for i in range(2):
            self.widgets.append(XYNumberInput())

        context = self.custom_get_context(name, value, attrs, context, xy=True)
        return context


class RangeTupleFieldWidget(TupleFieldWidget):
    def get_context(self, name, value, attrs):
        context = forms.Widget.get_context(self, name, value, attrs)
        self.widgets = []
        # Update number of widgets
        for i in range(2):
            self.widgets.append(XYNumberInput())

        context = self.custom_get_context(name, value, attrs, context, range_option=True)
        return context


class XYNumberInput(forms.NumberInput):
    # Template works for both range and xy coordinates
    template_name = 'django_param/tuplefield/xytuplefield.html'
