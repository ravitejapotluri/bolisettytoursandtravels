from django import  forms
from manager.models import enquiry,login


class enquiryform(forms.ModelForm):
    class Meta():
        model=enquiry
        exclude=["customer",
                 "name",
                 "email",
                 "mobile",
                 'destination',
                 'date']

class loginform(forms.ModelForm):
    class Meta():
        model=login
        exclude=['email',
                 'password']