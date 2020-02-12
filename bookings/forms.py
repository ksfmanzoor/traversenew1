from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import TripBooking

class TripBookingCreateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = TripBooking
        fields = ['guest_number', 'phone_number', 'email_id']

    def __init__(self, *args, **kwargs):
        super(BookingCreateForm, self).__init__(*args, **kwargs)

        

# class TripBookingUpdateForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = TripBooking
#         fields = ['username', 'email']



# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']

#        