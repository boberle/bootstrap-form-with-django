from django.forms.widgets import TextInput
from django.core.validators import RegexValidator, MinValueValidator
from django.forms.models import ModelForm

from .models import Book
from .fields import (
    BootstrapBooleanField,
    BootstrapCharField,
    BootstrapCharFieldWithTextarea,
    BootstrapIntegerField,
    BootstrapTypedChoiceField,
    CustomCharField,
)


class BookForm(ModelForm):

    # example of how it works with a simple custom form field
    title = CustomCharField(
        widget=TextInput(attrs={'class': 'form-control'}),
        label_attrs={'class': 'form-label'},
        wrapper_attrs={'class': 'mb-3'},
        template="include/form_elements/label_field.html",
        validators=[
            RegexValidator(
                "^[A-Z]",
                "This field should starts with an upper case letter."
            ),
            RegexValidator(
                "[a-z]$",
                "This field should ends with a lower case letter."
            ),
        ],
    )

    # using various bootstrap form fields
    author = BootstrapCharField(
        help_text="the author",
    )
    year = BootstrapIntegerField(
        help_text="the year",
        validators=[MinValueValidator(2000)],
        initial=2000,
    )
    is_available = BootstrapBooleanField(
        label="is available for borrowing",
    )
    category = BootstrapTypedChoiceField(
        label="category",
        choices=Book._meta.get_field('category').get_choices(),
        required=False,
    )
    description = BootstrapCharFieldWithTextarea(
        required=False,
    )

    class Meta:
        model = Book
        # you need to add the fields here, even if defined as class attribute,
        # in order for them to be bound to the form
        fields = [
            'title',
            'author',
            'year',
            'is_available',
            'category',
            'description',
        ]
        label_attrs = dict(
            year={'class': 'more foo bar'},
        )
