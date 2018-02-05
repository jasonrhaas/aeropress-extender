from django import forms
from .models import InterestedPerson


class EmailForm(forms.ModelForm):
    # email = forms.EmailField(label='Email', max_length=100)

    class Meta:
        model = InterestedPerson
        fields = ["email"]
