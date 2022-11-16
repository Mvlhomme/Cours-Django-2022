from django import forms
from .models import Account, UserProfile

class RegistrationForm(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput(attrs={
		'placeholder': 'Mot de passe',
		'class': 'form-control',
	}))

	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
		'placeholder': 'Confimer le mot de passe'
	}))

	def clean(self):
		cleaned_data = super(RegistrationForm, self).clean()
		password = cleaned_data.get('password')
		confirm_password = cleaned_data.get('confirm_password')

		if password != confirm_password:
			raise forms.ValidationError(
				"Le mot de passe ne correspond pas."
			)

	class Meta:
		model = Account
		fields = ['nom', 'prenom', 'phone_number', 'email', 'password']

	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)

		self.fields['nom'].widget.attrs['placeholder'] = 'Entrer votre nom'
		self.fields['prenom'].widget.attrs['placeholder'] = 'Entrer votre prenom'
		self.fields['phone_number'].widget.attrs['placeholder'] = 'Numero de téléphone'
		self.fields['email'].widget.attrs['placeholder'] = 'Email Address'

		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'


class UserForm(forms.ModelForm):
	class Meta:
		model = Account 
		fields = ('nom', 'prenom', 'phone_number')

	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'

class UserProfileForm(forms.ModelForm):
	profile_picture = forms.ImageField(required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)
	class Meta:
		model = UserProfile 
		fields = ('address_line_1', 'address_line_2', 'city', 'state', 'country', 'profile_picture')

	def __init__(self, *args, **kwargs):
		super(UserProfileForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'