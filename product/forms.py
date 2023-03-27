from django import forms 
from django.core import validators
class RecentProduct(forms.Form):
    mobile = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)
    laptop = forms.CharField(label='Enter Your Laptop Name')
    email = forms.EmailField(validators=[validators.MaxLengthValidator(30)])
    Details = forms.CharField(widget=forms.Textarea(attrs={'rows' : 4, 'cols':40}))
    ram = forms.IntegerField(min_value=4,max_value=16)
    youtube=forms.BooleanField()
    def clean(self):
        cleaned_data = super().clean() #confusion
        password_match = self.cleaned_data['password'] #confusion
        re_password_match = self.cleaned_data['re_password']
        if password_match!=re_password_match:
            raise forms.ValidationError("Password doesn't match")
    def clean_password(self):
        
        password_validation = self.cleaned_data['password'] 
        if len(password_validation)<4:
            raise forms.ValidationError("Enter Your Correct Password")
        return password_validation
    