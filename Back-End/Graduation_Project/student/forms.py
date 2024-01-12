from django import forms


class LoginForm(forms.Form):
  
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': ''}))




################################################################
##################### Graduation Project #######################
################################################################

class GPForm(forms.Form):

  depts = (
    ('', 'Choose...'),
    ('Computer Science'               , 'Computer Science'),
    ('Computer Information Systems'   , 'Computer Information Systems'),
    ('Business Information Technology', 'Business Information Technology'),
    ('Data Science'                   , 'Data Science'),
    ('Cyber Security'                 , 'Cyber Security'),
    ('Artificial Intelligence'        , 'Artificial Intelligence'),
    ('Mixed'                          , 'Mixed'),
  )

  sems =(
    ('', 'Choose...'),
    ('First' , 'First'),
    ('Second', 'Second'),
    ('Summer', 'Summer'),
  )


  # Main
  department = forms.ChoiceField(choices=depts, widget=forms.Select(attrs={'class': 'form-select'}))
  semester   = forms.ChoiceField(choices=sems,  widget=forms.Select(attrs={'class': 'form-select'}))

  # Doctors Info
  superviser_1 = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class': 'form-control'}))
  email_1      = forms.CharField(max_length=32, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Make sure you write it correctly'}))
  superviser_2 = forms.CharField(max_length=32, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(optional)'}))
  email_2      = forms.CharField(max_length=32, required=False, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '(optional), Make sure you write it correctly'}))

  # Project Info
  project_name = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
  project_idea = forms.CharField(max_length=720, widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 7rem;'}))
  project_goal = forms.CharField(max_length=400, widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 7rem;'}))
  technologies = forms.CharField(max_length=400, widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 7rem;'}))



################################################################
##################### Graduation Project #######################
################################################################
class RecommendedForm(forms.Form):
  
  web          = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '5', 'step': '0.5'}))
  network      = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '5', 'step': '0.5'}))
  security     = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '5', 'step': '0.5'}))
  data_science = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '5', 'step': '0.5'}))









################################################################
########################## TIMELINE ############################
################################################################
class TimelineForm(forms.Form):

  important        = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'important'}))
  doc              = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'doc'}))
  update           = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'update'}))
  final_release    = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'final_release'}))
  new_release      = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'new_release'}))
  research         = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'research'}))
  programming      = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'programming'}))
  problem          = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'problem'}))
  web              = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'web'}))
  mobile           = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'mobile'}))
  network          = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'network'}))
  cyber_security   = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'cyber_security'}))
  ai               = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'ai'}))
  machine_learning = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'machine_learning'}))


  post  = forms.CharField(max_length=2500 ,widget=forms.Textarea(attrs={'class':'form-control border-1 border-dark post', 'placeholder':'Post', 'style':'height: 7rem;'}))
  files = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control border-1 border-dark', 'multiple': ''}), required=False)












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
  technologies         = forms.CharField(max_length=450, widget=forms.Textarea(attrs={'class':'form-control', 'style': 'height: 5rem'}))



class CourseForm(forms.Form):
  
  # Course Info
  course      = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))
  hour        = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
  provider    = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))
  certificate = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control border border-1 border-dark'}), required=False)


class WeeklyForm(forms.Form):

  task  = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
  hour  = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'max': 90, 'min': 1, 'placeholder': 'At least 15 hours in a week'}))
  sw_hw = forms.CharField(max_length=450, widget=forms.Textarea(attrs={'class':'form-control', 'style': 'height: 5rem'}))