from django import forms


class LoginForm(forms.Form):
  
  username   = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
  # job_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
  password   = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': ''}))



class AppCompForm(forms.Form):
  app_company = forms.CharField(max_length=650, required=False, widget=forms.Textarea(attrs={'class': 'form-control border border-1 border-dark', 
  'style': 'height: 5rem;'}))


class DisappCompForm(forms.Form):
  dis_company = forms.CharField(max_length=650, widget=forms.Textarea(attrs={'class': 'form-control border border-1 border-dark', 'style': 'height: 5rem;'}))


class AppCorForm(forms.Form):
    app_courses = forms.CharField(max_length=650, required=False, widget=forms.Textarea(attrs={'class': 'form-control border border-1 border-dark', 
    'style': 'height: 5rem;'}))


class DisappCorForm(forms.Form):
  dis_courses = forms.CharField(max_length=650, widget=forms.Textarea(attrs={'class': 'form-control border border-1 border-dark', 'style': 'height: 5rem;'}))

