from django import forms
from django.forms.widgets import TextInput, NumberInput, CheckboxInput, Select
from django.forms.boundfield import BoundField


class CustomBoundField(BoundField):
    def __init__(self, form, field, name):
        super().__init__(form, field, name)
        for attr in ('label_attrs', 'wrapper_attrs'):
            if hasattr(self.field, attr) and getattr(self.field, attr) is not None:
                setattr(self, attr, getattr(self.field, attr).copy())
            else:
                setattr(self, attr, dict())
        self.template = self.field.template

    def as_widget(self, widget=None, attrs=None, only_initial=False):
        widget = widget or self.field.widget
        classes = widget.attrs.get('class', "").split()
        if self.form.is_bound:
            if self.errors:
                validation_class = "is-invalid"
            else:
                validation_class = "is-valid"
            widget.attrs['class'] = " ".join(classes + [validation_class])
        return super().as_widget(widget, attrs, only_initial)



class CustomFieldInterface:
    def __init__(self, *, label_attrs=None, wrapper_attrs=None, template=None, **kwargs):
        super().__init__(**kwargs)
        #self.label_attrs = label_attrs.copy() if label_attrs is not None else dict()
        #self.wrapper_attrs = wrapper_attrs.copy() if wrapper_attrs is not None else dict()
        self.label_attrs = label_attrs
        self.wrapper_attrs = wrapper_attrs
        self.template = template

    def get_bound_field(self, form, field_name):
        return CustomBoundField(form, self, field_name)

#    @property
#    def widget(self):
#        return self._widget
#
#    @widget.setter
#    def widget(self, value):
#        if self.
#        self._widget = value


class CustomCharField(CustomFieldInterface, forms.CharField):
    pass


class CustomIntegerField(CustomFieldInterface, forms.IntegerField):
    pass


class CustomBooleanField(CustomFieldInterface, forms.BooleanField):
    pass


class CustomTypedChoiceField(CustomFieldInterface, forms.TypedChoiceField):
    pass


class BootstrapInputDefaultAttributes:
    _default_widget = None
    def __init__(self, **kwargs):
        options = dict(
            widget=kwargs.pop('widget') if 'widget' in kwargs else self._default_widget,
            label_attrs={'class': 'form-label'},
            wrapper_attrs={'class': 'mb-3'},
            template="include/form_elements/label_field.html",
        )
        options.update(kwargs)
        super().__init__(**options)


class BootstrapCustomCharField(BootstrapInputDefaultAttributes, CustomCharField):
    _default_widget = TextInput(attrs={'class': 'form-control'})


class BootstrapCustomIntegerField(BootstrapInputDefaultAttributes, CustomIntegerField):
    _default_widget = NumberInput(attrs={'class': 'form-control'})


class BootstrapCheckboxDefaultAttributes:
    _default_widget = None
    def __init__(self, **kwargs):
        options = dict(
            widget=kwargs.pop('widget') if 'widget' in kwargs else self._default_widget,
            label_attrs={'class': 'form-check-label'},
            wrapper_attrs={'class': 'mb-3'},
            template="include/form_elements/field_label.html",
            required=False,
        )
        options.update(kwargs)
        super().__init__(**options)


class BootstrapCustomBooleanField(BootstrapCheckboxDefaultAttributes, CustomBooleanField):
    _default_widget = CheckboxInput(attrs={'class': 'form-check-input'})


class BootstrapTypedChoiceDefaultAttributes:
    _default_widget = None
    def __init__(self, **kwargs):
        #choices = kwargs['choices'].copy() if 'choices' in kwargs else self._model._meta.get_field('category').get_choices()
        options = dict(
            widget=kwargs.pop('widget') if 'widget' in kwargs else self._default_widget,
            label_attrs={'class': 'form-label'},
            wrapper_attrs={'class': 'mb-3'},
            template="include/form_elements/label_field.html",
            required=False,
            #choices=choices,
        )
        options.update(kwargs)
        super().__init__(**options)


class BootstrapCustomTypedChoiceField(BootstrapTypedChoiceDefaultAttributes, CustomTypedChoiceField):
    _default_widget = Select(attrs={'class': 'form-select'})
    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    #choices = kwargs.pop('choices') if 'choices' in kwargs else self.field.get_choices()
    #    #Book._meta.get_field('category').get_choices()
    #    #print(self.get_bound_field())
