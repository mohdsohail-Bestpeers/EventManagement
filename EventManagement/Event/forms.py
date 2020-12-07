from django import forms
from .models import EventUser, Event, Address, event_photo


class event_user_form(forms.ModelForm):
    class Meta:
        model = EventUser
        fields = ["fname", "lname", "email", "mobile"]
      
    '''Mobile number validation'''  
    def clean_mobile(self):
        mobile_passed = str(self.cleaned_data.get("mobile"))
        if len(mobile_passed) != 10:
            raise forms.ValidationError("Not a vailid number..! Please enter again")
        return mobile_passed


class event_form(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"


class address_form(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ["event"]


class event_photo_form(forms.ModelForm):
    class Meta:
        model = event_photo
        exclude = ["event"]
