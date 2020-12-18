from django import forms
from .models import EventUser, Event, Address, event_photo

'''access all Event user field into form'''
class event_user_form(forms.ModelForm):
    class Meta:
        model = EventUser
        fields = '__all__'
      
    '''Mobile number validation'''  
    def clean_mobile(self):
        mobile_passed = str(self.cleaned_data.get("mobile"))
        if len(mobile_passed) != 10:
            raise forms.ValidationError("Not a vailid number..! Please enter again")
        return mobile_passed

'''access some Event field into form'''
class event_form(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['event_user', 'publisher', 'payment_status']
        #in the exculde there is some fields mentioned will not visible in form  

'''access some address field into form'''
class address_form(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ["event"]
        #exclude hide the event field from form

'''access event photo field into form '''
class event_photo_form(forms.ModelForm):
    class Meta:
        model = event_photo
        exclude = ["event"]
        #exclude hide the event field from the form