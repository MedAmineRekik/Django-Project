from django import forms

from .models import User

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['email'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['number'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '1',
        }

    class Meta:
        model = User
        fields = ('name', 'email', 'number')