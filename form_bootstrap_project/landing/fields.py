from django import forms
from django.forms.widgets import (
    CheckboxInput,
    NumberInput,
    Select,
    TextInput,
    Textarea,
)
from django.forms.boundfield import BoundField


# custom bound field ###########################################################


class CustomBoundField(BoundField):
    def __init__(self, form, field, name):
        super().__init__(form, field, name)
        for attr in ('label_attrs', 'wrapper_attrs'):
            if (hasattr(self.field, attr)
                    and getattr(self.field, attr) is not None):
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


# custom form fields ###########################################################


class CustomFieldMixin:
    def __init__(
            self, *,
            label_attrs=None, wrapper_attrs=None, template=None, **kwargs):
        super().__init__(**kwargs)
        self.label_attrs = label_attrs
        self.wrapper_attrs = wrapper_attrs
        self.template = template

    def get_bound_field(self, form, field_name):
        return CustomBoundField(form, self, field_name)


class CustomCharField(CustomFieldMixin, forms.CharField):
    pass


class CustomIntegerField(CustomFieldMixin, forms.IntegerField):
    pass


class CustomBooleanField(CustomFieldMixin, forms.BooleanField):
    pass


class CustomTypedChoiceField(CustomFieldMixin, forms.TypedChoiceField):
    pass


## bootstrap custom form field #################################################


class BoostrapAttributesMixin:
    _default_widget = TextInput
    _default_label_attrs = dict()
    _default_wrapper_attrs = dict()
    _default_template = None
    _default_kwargs = dict()

    def __init__(self, **kwargs):
        widget = kwargs.pop('widget', self._default_widget)
        label_attrs = kwargs.pop(
            'label_attrs',
            self._default_label_attrs
        ).copy()
        wrapper_attrs = kwargs.pop(
            'wrapper_attrs',
            self._default_wrapper_attrs
        ).copy()
        template = kwargs.pop('template', self._default_template)

        options = dict(
            widget=widget,
            label_attrs=label_attrs,
            wrapper_attrs=wrapper_attrs,
            template=template,
        )
        options.update(self._default_kwargs)
        options.update(kwargs)
        super().__init__(**options)


class BootstrapInputAttributesMixin(BoostrapAttributesMixin):
    _default_widget = TextInput(attrs={'class': 'form-control'})
    _default_wrapper_attrs = {'class': 'mb-3'}
    _default_label_attrs = {'class': 'form-label'}
    _default_template = "include/form_elements/label_field.html"


class BootstrapCharField(BootstrapInputAttributesMixin, CustomCharField):
    pass


class BootstrapCharFieldWithTextarea(
        BootstrapInputAttributesMixin, CustomCharField):
    _default_widget = Textarea(attrs={'class': 'form-control'})


class BootstrapIntegerField(BootstrapInputAttributesMixin, CustomIntegerField):
    _default_widget = NumberInput(attrs={'class': 'form-control'})


class BootstrapCheckboxAttributesMixin(BoostrapAttributesMixin):
    _default_widget = CheckboxInput(attrs={'class': 'form-check-input'})
    _default_wrapper_attrs = {'class': 'mb-3'}
    _default_label_attrs = {'class': 'form-check-label'}
    _default_template = "include/form_elements/field_label.html"
    _default_kwargs = {'required': False}


class BootstrapBooleanField(
        BootstrapCheckboxAttributesMixin, CustomBooleanField):
    pass


class BootstrapTypedChoiceAttributesMixin(BoostrapAttributesMixin):
    _default_widget = Select(attrs={'class': 'form-select'})
    _default_wrapper_attrs = {'class': 'mb-3'}
    _default_label_attrs = {'class': 'form-label'}
    _default_template = "include/form_elements/label_field.html"


class BootstrapTypedChoiceField(
        BootstrapTypedChoiceAttributesMixin, CustomTypedChoiceField):
    pass
