# forms.py 
from django import forms 
from . models import *
  
class HotelForm(forms.ModelForm): 
  
    class Meta: 
        model = contact
        fields = ['sno','name', 
            'phone','email','content','mimg'] 