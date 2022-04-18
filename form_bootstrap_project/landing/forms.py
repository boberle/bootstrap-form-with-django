from django.forms.widgets import TextInput, HiddenInput
from django.core.validators import RegexValidator, MinValueValidator

from .models import Book
from .widgets import CustomTextInput
from django.forms.models import ModelFormMetaclass, ModelForm
from django.forms.fields import IntegerField

from .fields import BootstrapCustomTypedChoiceField, BootstrapCustomIntegerField, BootstrapCustomCharField, BootstrapCustomBooleanField


class BookForm(ModelForm):
    title = BootstrapCustomCharField(
        widget=TextInput(attrs={'class': 'form-control'}),
        label_attrs={'class': 'form-label'},
        wrapper_attrs={'class': 'mb-3'},
        template="include/form_elements/label_field.html",
        validators=[
            RegexValidator("^[A-Z]", "This field should starts with an upper case letter."),
            RegexValidator("[a-z]$", "This field should ends with a lower case letter."),
        ],
    )
    author = BootstrapCustomCharField(
        help_text="the author",
    )
    year = BootstrapCustomIntegerField(
        help_text="the year",
        validators=[MinValueValidator(2000)],
        initial=2000,
    )
    #year = IntegerField()
    is_available = BootstrapCustomBooleanField(
        label="is available for borrowing",
    )
    category = BootstrapCustomTypedChoiceField(
        label="category",
        choices=Book._meta.get_field('category').get_choices(),
    )
    class Meta:
        model = Book
        # you need to add the fields here, even if defined as class attribute,
        # in order for them to be bound to the form
        fields = ['title', 'author', 'year', 'is_available', 'category']
        label_attrs = dict(
            year={'class': 'more foo bar'},
        )
        #labels = dict(
        #    year="CHOSE"
        #)
    #    #labels = dict(title="THETITLE")
    #    #widgets = dict(title=Textarea(attrs=dict(cols=4, rows=3)))
    #    #widgets = dict(title=CustomTextInput(attrs={'class': 'cls1 cls2'}, label_attrs={'class': 'foo bar'}, label="The LABEL"))
