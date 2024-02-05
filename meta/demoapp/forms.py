from django import forms
#for modelform
# from django.forms import ModelForm
from .models import MenuChart, Reservation


SHIFTS=(
    (0,"--select--"),
    (1,"morning"),
    (2,"afternoon"),
    (3,"evening"),
)

class InputForm(forms.Form):
    fname=forms.CharField(max_length=200) 
    lname=forms.CharField(max_length=200, required=False)# required =False allows user to submit the form without filling that entry
    shift=forms.ChoiceField(choices=SHIFTS)
    time_log=forms.TimeField(help_text="write the exact time , eg : 9:30") # help_text helps user to know what they need to fill the form entry with
    
class loginFormEx(forms.Form):
    name=forms.CharField(max_length=200)
    email_id=forms.EmailField(max_length=200)
    
#for modelform
# ModelForm class renders the Model attributes as HTML form elements.
class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuChart
        fields='__all__' # it will automatically enter all of the feilds inside that model in this as list 
        
class ReservationForm(forms.ModelForm):
    class Meta:
        model=Reservation
        fields='__all__'