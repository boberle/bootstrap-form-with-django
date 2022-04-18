from django.forms.widgets import TextInput


class CustomTextInput(TextInput):
    template_name = "landing/custom_widget.html"

    def __init__(self, attrs=None, *, label=None, label_attrs=None):
        super().__init__(attrs=attrs)
        self.label_attrs = dict() if label_attrs is None else label_attrs.copy()
        self.label = label or ""
