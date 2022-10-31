from django.contrib.auth.forms import UserCreationForm
from signup_handler.models import User
from django import forms
from django.core import validators

class RegisterUserForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}), required=True, validators= [validators.EmailValidator()])
	first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}), required=True, validators= [validators.MaxLengthValidator(10)])
	last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}), required=True, validators= [validators.MaxLengthValidator(10)])
	

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'mobile', 'profile_pic')


	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'

