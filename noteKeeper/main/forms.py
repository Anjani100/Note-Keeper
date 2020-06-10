from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required = True)
	college = forms.CharField(max_length = 200, required = True)

	class Meta:
		model = User
		fields = ('username', 'email', 'college', 'password1', 'password2')

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		user.college = self.cleaned_data["college"]
		if commit:
			user.save()
		return user

class LoginForm(AuthenticationForm):
	email = forms.EmailField(required = False)

	class Meta:
		model = User
		fields = ('username', 'email', 'password')