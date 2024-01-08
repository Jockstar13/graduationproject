from django import forms
from . import views




class LoginForm(forms.Form):
  
  username   = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
  # job_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
  password   = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': ''}))



class DashboardForm(forms.Form):

  start        = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type': 'date'}))
  end          = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type': 'date'}))
  team_mem_num = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))


class SetDoctorForm():
  
  pass