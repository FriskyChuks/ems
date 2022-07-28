from django.forms import ModelForm
from django.forms.widgets import DateInput

from .models import *


class CreateApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        exclude=['date_created']