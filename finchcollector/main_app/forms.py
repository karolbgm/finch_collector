from django.forms import ModelForm
from .models import Feeding
#we only want this form to handle feeding

class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']