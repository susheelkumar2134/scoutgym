from django import forms 
from gymapp.models import User_Details

class User_Form(forms.ModelForm):
     class Meta:
        model = User_Details # This line means select model name .
        fields = "__all__" # This fields select all fields in models .
        # fields = ['First_name','Last_name','Email'] # If we want to create selected feilds .