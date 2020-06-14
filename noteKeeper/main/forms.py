from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
	username = forms.CharField(label = 'Username', max_length = 150)
	email = forms.EmailField(label = 'Email', required = True)
	college = forms.CharField(label = 'College', max_length = 200)
	password1 = forms.CharField(label = 'Password', max_length = 32, widget = forms.PasswordInput)
	password2 = forms.CharField(label = 'Confirm Password', max_length = 32, widget = forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'college', 'email', 'password1', 'password2')

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		if commit:
			user.save()
		return user

class LoginForm(AuthenticationForm):
	# email = forms.EmailField(required = False)

	class Meta:
		model = User
		fields = ('username', 'password')
