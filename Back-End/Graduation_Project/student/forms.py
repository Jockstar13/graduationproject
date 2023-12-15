from django import forms
from .models import CompanyInternship

class LoginForm(forms.Form):
  
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': ''}))







################################################################
######################### Internship ###########################
################################################################

class CompanyForm(forms.Form):
  
  # Company Info
  company = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class':'form-control'}))
  address = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class':'form-control'}))
  start   = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type': 'date'}))
  end     = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type': 'date'}))

  # Superviser Info
  name      = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class':'form-control'}))
  email     = forms.EmailField(max_length=80, widget=forms.EmailInput(attrs={'class':'form-control'}))

  # Technical Info
  description_of_tasks = forms.CharField(max_length=450, widget=forms.Textarea(attrs={'class':'form-control', 'style': 'height: 5rem'}))
  technologies          = forms.CharField(max_length=450, widget=forms.Textarea(attrs={'class':'form-control', 'style': 'height: 5rem'}))



class CourseForm(forms.Form):
  
  # Course Info
  course      = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))
  hour        = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
  provider    = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))
  certificate = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control border border-1 border-dark'}), required=False)


class WeeklyForm(forms.Form):
  
  def gen_student():
    student_list = ()
    data = CompanyInternship.objects.values_list('name', 'email')


    return student_list

  # Student
  student = forms.ChoiceField()



  # Task Info
