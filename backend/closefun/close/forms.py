from django import forms

class AddressForm(forms.Form):
    stree = forms.CharField(label='Street' , max_length=255)
    city = forms.CharField(label='City' , max_length=100)
    state = forms.CharField(label="State" , max_length=100)
    postal_code=forms.CharField(label="Postal Code" , max_length=20)
    contry=forms.CharField(label="Country" , max_length=100)