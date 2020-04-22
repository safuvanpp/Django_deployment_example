from django import forms
from appthree.models import User

class NewUserForm(forms.ModelForm):
    """docstring for ."""

    class Meta():
        """docstring for ."""
        model = User
        fields = '__all__'
