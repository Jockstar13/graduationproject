import pandas as pd
from .forms import CompanyForm, CourseForm, LoginForm, WeeklyForm, GPForm, TimelineForm, RecommendedForm
from .models import CompanyInternship, CourseInternship, Student, WeeklyFollowing, GraduationProject, Timeline, StudentNotification, TimlineFiles, GraduationDetails, RecommendedProject, StudentRating
from datetime import datetime
from django.http import FileResponse
from doctor.models import Doctor, DoctorNotification
from django.shortcuts import render, redirect, get_object_or_404
from department.models import Department, DepartmentNotification
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.





############# Check If Student #############
def is_student(request):
  try:
    stu = Student.objects.get(stu=request.user)
    return stu
  except:
    logout(request)
    return redirect('login')
  



############# Send Notification to Department ###############
def notify_department(department, subject, message, url_name, query_pk=''):
  try:
    DepartmentNotification(department=department, subject=subject, message=message, url_name=url_name, query_pk=query_pk).save()
  except:
    DepartmentNotification(department=department, subject=subject, message=message, url_name=url_name).save()




############### Send Notification to Doctor #################
def notify_doctor(doctor, subject, message, url_name, query_pk=''):
  try:
    DoctorNotification(doctor=doctor, subject=subject, message=message, url_name=url_name, query_pk=query_pk).save()
  except:
    DoctorNotification(doctor=doctor, subject=subject, message=message, url_name=url_name).save()



##################### Get Notification ####################
def get_notification(request):
  student_rec = is_student(request)
  all_notifications = StudentNotification.objects.filter(student=student_rec.stu).order_by('-id')

  there_is = False
  for n in all_notifications:
    if not n.is_read:
      there_is = True
      break

  return {'all_notifications': all_notifications, 'there_is': there_is}







################### Redirect Notification ##################
def redirect_notifi(request, pk):
  try:
    n = StudentNotification.objects.get(id=pk)
    n.is_read = True
    n.save()

    if n.query_pk:
      query = n.query_pk
      return redirect(n.url_name, query)
    else:
      return redirect(n.url_name)
  except ObjectDoesNotExist:
    pass






################### Read All Notification ##################
def read_all_notifi(request):
  all_n = StudentNotification.objects.all()
  
  for n in all_n:
    n.is_read = True
    n.save()
  else:
    return redirect(request.META.get('HTTP_REFERER'))








###########################################################
######################### LOGIN ###########################
###########################################################
def index(request):


  if request.user.is_authenticated:
    return redirect('stu-home')

  context = {
    'title': 'Login',
    'flag': True,
    'form': LoginForm(),
  }


  if request.method == 'POST':


    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(request, username=username, password=password)

      if user is not None:
        try:
          stu = User.objects.get(username=username)
          stu_data = Student.objects.get(stu=stu)
          if not stu_data.in_internship and not stu_data.in_gp or not stu_data.hours >= 90:
            context.setdefault('allow_error', "You haven't permission to enter website.")
            return render(request, 'student/pages/index.html', context)
          
          less_than_start = Department.objects.get(dept_name=stu_data.major).is_less_than_start()
          if less_than_start:
            context.setdefault('date_error', f'The registration interval for Graduation Project and Internship doesn\'t start yet.')
            return render(request, 'student/pages/index.html', context)

          login(request, user)
          return redirect('stu-home')
        except:
          context.setdefault('allow_error', "You haven't permission to enter website.")

      else:
        context.setdefault('auth_error', 'Your username or passsword is incorrect.')


    else:
      context.setdefault('valid_error', 'Enter valid Data.')




  

  
  return render(request, 'student/pages/index.html', context)




###########################################################
######################### LOGOUT ##########################
###########################################################
def log_out(request):

  logout(request)
  return redirect('login')





###########################################################
########################## HOME ###########################
###########################################################
@login_required(login_url='login')
def home(request):
  student_rec = is_student(request)

  if type(student_rec) != Student:
    return redirect('login')






  context = {
    'title': 'Home',
    'flag': True,
    'user': request.user,
    'notifications': get_notification(request),
  }



  return render(request, 'student/pages/home.html', context)
####################################################################################################
####################################################################################################





####################### Get Stored Data ######################
def GP_data(request):
  try:
    student_rec = is_student(request)



    recordes = GraduationProject.objects.all()
    for rec in recordes:
      stus = rec.members.all()
      if student_rec.stu in stus:
        
        student_info = []
        for i in stus:
          student_info.append(Student.objects.get(stu=i))
        


        for i in range(1,3):
          doc1 = User.objects.get(email=rec.email_1)
          try:
            doc2 = User.objects.get(email=rec.email_2)
            doc2_name = f'{doc2.first_name} {doc2.last_name}'
          except:
            doc2_name = ' '



        correct = {
          'department'  : rec.department,
          'semester'    : rec.semester,
          'superviser_1': f'{doc1.first_name} {doc1.last_name}',
          'email_1'     : rec.email_1,
          'superviser_2': doc2_name,
          'email_2'     : rec.email_2,
          'project_type': rec.project_type,
          'project_name': rec.project_name,
          'project_idea': rec.project_idea,
          'project_goal': rec.project_goal,
          'technologies': rec.technologies,
        }

        return [correct, student_info]
  except:
    pass



##############################################################
################### GRADUTATION PROJECT ######################
##############################################################
@login_required(login_url='login')
def gp(request):
  # Get Student Record
  student_rec = is_student(request)

  if type(student_rec) != Student:
    return redirect('login')



  # Check If Student Register in Internship University Course
  if student_rec.in_gp != True:
    return redirect(request.META.get('HTTP_REFERER'))


  # Get Number of team's member
  dept = Department.objects.get(dept_name=student_rec.major)
  no   = dept.num_team_member




  # Context
  context = {
    'title': 'Graduation Project',
    'stu_team_num': range(dept.num_team_member),
    'notifications': get_notification(request),
  }



  # When the form submited
  if request.method == 'POST':
    form = GPForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data

      # Check if doctors emails are correct.
      for i in range(1,3):
        try:
          if 'email_' + str(i) in data.keys():
            docs = Doctor.objects.all()
            for doc in docs:
              if doc.doc.email == data['email_' + str(i)]:
                break
            else:
              context.setdefault('email_error', 'The email isn\'t correct.')
              break
        except:
          pass


      # If doctors emails are incorrect, then reject the form.
      if not 'email_error' in context.keys():
        # Try to Update The Record From Database
        try:
          student_rec = is_student(request)
          recordes = GraduationProject.objects.all()
          for rec in recordes:
            stus = rec.members.all()
            if student_rec.stu in stus:
              rec.department   = data['department']
              rec.semester     = data['semester']
              rec.superviser_1 = data['superviser_1']
              rec.superviser_2 = data['superviser_2']
              rec.email_1      = data['email_1']
              rec.email_2      = data['email_2']
              rec.project_type = request.POST['project_type']
              rec.project_name = data['project_name']
              rec.project_idea = data['project_idea']
              rec.project_goal = data['project_goal']
              rec.technologies = data['technologies']
              rec.save()
              rec.members.clear()
              rec.members.add(student_rec.stu)
              team_record = rec
              update = True


              # Push notification to the doctor and Department
              message   = f'{student_rec.stu.first_name} {student_rec.stu.last_name} update Graduation Project Info'
              for i in range(2):
                try:
                  doc = User.objects.get(email=data[f'email_{i+1}'])
                  notify_doctor(doc, subject='Update Graduation Project', message=message, url_name='team-details', query_pk=rec.pk)
                except:
                  pass
              else:
                dept_name = Department.objects.get(dept_name=student_rec.major)
                notify_department(dept_name, subject='Update Graduation Project', message=message, url_name='team_details', query_pk=rec.pk)

              break
          else:
            update = False
            context.setdefault('test', "update ERROR")
        except:
          return redirect('stu-home')




        try:
          # Store Student Info Into txt File.
          rejected = 0
          rejected_stus = []
          for i in range(dept.num_team_member):
            # Check if the data are spaces
            if request.POST['name' + str(i+1)].isspace() or request.POST['id' + str(i+1)].isspace() or request.POST['major' + str(i+1)].isspace():
              rejected += 1
              continue
            else:
              # Check if the data are empty
              if not request.POST['name' + str(i+1)] or not request.POST['id' + str(i+1)] or not request.POST['major' + str(i+1)]:
                rejected += 1
                continue
              else:

                # Get Student record and check if him/her in another team or not
                try:
                  s = Student.objects.get(student_id=request.POST['id' + str(i+1)])
                  recordes = GraduationProject.objects.all()
                  for rec in recordes:
                    stus = rec.members.all()
                    if s.stu in stus:
                      if s.stu != student_rec.stu:
                        rejected_stus.append(s.stu)
                  else:
                    context.setdefault('rejected_student', rejected_stus)

                    if not s.stu in rejected_stus:
                      if team_record.members.count() != dept.num_team_member:
                        team_record.members.add(s.stu)
                except:
                  continue
          else:
            if rejected == dept.num_team_member:
              context.setdefault('valid_error', 'Enter at least one student.')
            else:
              if update:
                context.setdefault('update', 'The form updated successfully.')
              else:
                context.setdefault('insert', 'The form inserted successfully.')
        except:
          pass

        # Try to Insert New Record in The Database
        try:
          if not update and not 'valid_error' in context.keys():
            pro = GraduationProject(
            department=data['department'], semester=data['semester'],
            superviser_1=data['superviser_1'], superviser_2=data['superviser_2'],
            email_1=data['email_1'], email_2=data['email_2'],
            project_type=request.POST['project_type'], project_name=data['project_name'], project_idea=data['project_idea'],
            project_goal=data['project_goal'], technologies=data['technologies'])
            pro.save()
            pro.members.add(student_rec.stu)
            team_record = pro


            # Push notification to the doctor and doctor
            message   = f'{student_rec.stu.first_name} {student_rec.stu.last_name} Insert Graduation Project Info'
            for i in range(2):
              try:
                doc = User.objects.get(email=data[f'email_{i+1}'])
                notify_doctor(doc, subject='Insert Graduation Project', message=message, url_name='team-details', query_pk=pro.pk)
              except:
                pass
            else:
              notify_department(student_rec.major, subject='Insert Graduation Project', message=message, url_name='team_details', query_pk=pro.pk)
        except:
          pass


    # else for
    else:
      context.setdefault('form_validation', 'The Form isn\'t Valid')



  try:
    stored_data = GP_data(request)
    context.setdefault('student_info', stored_data[1])
  except:
    pass

  try:
    context.setdefault('form', GPForm(stored_data[0]))
  except:
    context.setdefault('form', GPForm())




  return render(request, 'student/pages/Graduation-Project/reg-gp.html', context)
####################################################################################################
####################################################################################################





###################### Get Stored Post #######################
def get_posts(rec):

  try:
    return Timeline.objects.filter(team=rec).order_by('-id')
  except:
    pass



##############################################################
######################### TIMELINE ###########################
##############################################################
@login_required(login_url='login')
def timeline(request):
  student_rec = is_student(request)

  if type(student_rec) != Student:
    return redirect('login')



  # Check If Student Register in Internship University Course
  if student_rec.in_gp != True:
    return redirect(request.META.get('HTTP_REFERER'))



  context = {
    'title': 'Timeline',
    'user': request.user,
    'form': TimelineForm(),
    'notifications': get_notification(request),
  }


  if request.method == 'POST':
    form = TimelineForm(request.POST, request.FILES)
    if form.is_valid():
      data = form.cleaned_data

      important = False
      if 'important' in data.keys():
        important = data['important']

      doc = False
      if 'doc' in data.keys():
        doc = data['doc']

      new_release = False
      if 'new_release' in data.keys():
        new_release = data['new_release']

      final_release = False
      if 'final_release' in data.keys():
        final_release = data['final_release']

      programming = False
      if 'programming' in data.keys():
        programming = data['programming']

      research = False
      if 'research' in data.keys():
        research = data['research']

      update = False
      if 'update' in data.keys():
        update = data['update']

      web = False
      if 'web' in data.keys():
        web = data['web']

      mobile = False
      if 'mobile' in data.keys():
        mobile = data['mobile']

      network = False
      if 'network' in data.keys():
        network = data['network']

      cyber_security = False
      if 'cyber_security' in data.keys():
        cyber_security = data['cyber_security']

      ai = False
      if 'ai' in data.keys():
        ai = data['ai']

      machine_learning = False
      if 'machine_learning' in data.keys():
        machine_learning = data['machine_learning']

      problem = False
      if 'problem' in data.keys():
        problem = data['problem']


      p = Timeline(important=important, doc=doc, update=update, final_release=final_release, new_release=new_release, 
                  research=research, programming=programming, problem=problem, 
                  web=web, mobile=mobile, network=network, cyber_security=cyber_security,
                  ai=ai, machine_learning=machine_learning, post=data['post'],
                  date=datetime.now(), publisher=student_rec)
      p.save()


      files = None
      if 'files' in data.keys():
        files = request.FILES.getlist('files')
        for file in files:
          f = TimlineFiles(file=file)
          f.save()
          p.files.add(f)
          p.save()



      # Add All Members to the record
      try:
        recordes = GraduationProject.objects.all()
        for rec in recordes:
          stus = rec.members.all()
          if student_rec.stu in stus:
            p.team = rec
            p.save()
            for i in stus:
              p.members.add(i)
        else:
          # Push notification to the doctor
          message   = f'{student_rec.stu.first_name} {student_rec.stu.last_name} add new post in the team timeline.'
          notify_doctor(student_rec.doc_superviser.doc, subject='Timeline Post', message=message, url_name='team-details', query_pk=rec.pk)

      except:
        pass



  # If the student in a GP team get all post to this team,
  # otherwise, redirect to GP Form
  recordes = GraduationProject.objects.all()
  for rec in recordes:
    stus = rec.members.all()
    if student_rec.stu in stus:
      posts = get_posts(rec)

      full_posts = []
      for post in posts:
        files_full = []
        for item in post.files.all():
          files_full.append((str(item.file.name).split('.')[-1], item))

        else:
          full_posts.append((post,files_full))

      context.setdefault('posts', full_posts)
      break
  else:
    return redirect('gp')



  return render(request, 'student/pages/Graduation-Project/timeline.html', context)
####################################################################################################
####################################################################################################









#################################################################
########################## DELETE POST ##########################
#################################################################
@login_required(login_url='login')
def delete_timeline(request, post_id):
  student_rec = is_student(request)

  if type(student_rec) != Student:
    return redirect('login')
  
  try:
    post = Timeline.objects.get(id=post_id)
    post.delete()
  except ObjectDoesNotExist:
    pass

  return redirect('timeline')
####################################################################################################
####################################################################################################





################################################################
###################### RECOMMENED PROJECT ######################
################################################################
@login_required(login_url='login')
def rec_project(request):
  student_rec = is_student(request)

  if type(student_rec) != Student:
    return redirect('login')

  context = {
    'title': 'Recommended Project',
    'user': request.user,
    'notifications': get_notification(request),
  }


  # # Add sample student data for testing
  # student_data = {
  #     # 'username': 'test_user',
  #     # 'course_subject': 'Web Development',  # Replace with the actual course subject
  #     'web_dev_rating': 4.0,
  #     'network_rating': 3.5,
  #     'security_rating': 4.5,
  #     'data_science_rating': 3.0,
  # }






  # try:
  #   StudentRating.objects.get(stu_username=student_rec).delete()
  # except ObjectDoesNotExist:
  #   pass



  
  # Receive Form Submission
  if request.method == 'POST':

    student_data = {
        'username': student_rec,
        # 'course_subject': 'Web Development',  # Replace with the actual course subject
        'web_dev_rating': request.POST['web'],
        'network_rating': request.POST['network'],
        'security_rating': request.POST['security'],
        'data_science_rating': request.POST['data_science'],
    }

    try:
      student = StudentRating(stu_username=student_rec, web_dev_rating=request.POST['web'],
                        network_rating=request.POST['network'], security_rating=request.POST['security'],
                        data_science_rating=request.POST['data_science'])
      student.save()
    except:
      student = StudentRating.objects.get(stu_username=student_rec)
      student.web_dev_rating      = request.POST['web']
      student.network_rating      = request.POST['network']
      student.security_rating     = request.POST['security']
      student.data_science_rating = request.POST['data_science']
      student.save()



    # Try to retrieve the student or create if it doesn't exist
    student, created = StudentRating.objects.get_or_create(stu_username=student_data['username'], defaults=student_data)








    student_data_df = pd.DataFrame({
    'web_dev': [student.web_dev_rating],
    'network': [student.network_rating],
    'security': [student.security_rating],
    'data_science': [student.data_science_rating],
    })

    context.setdefault('student', student)
    # return render(request, 'student/pages/Graduation-Project/rec-project.html', context)

    # Fetch graduation projects from the database
    recommended_projects = RecommendedProject.objects.all()

    # Create a DataFrame for projects from the database
    projects_data_df = pd.DataFrame(list(recommended_projects.values()))

    # Calculate the similarity between the student and projects
    student_ratings = student_data_df.values.flatten()
    projects_ratings = projects_data_df[['web_dev', 'network', 'security', 'data_science']].values
    projects_data_df['similarity'] = projects_ratings.dot(student_ratings)


    # Filter projects based on similarity and sort them
    top_5 = projects_data_df.sort_values(by='similarity', ascending=False).head(5)

    # Filter projects that are recommended
    recommended_project_titles = top_5['title'].tolist()
    other_projects = projects_data_df[~projects_data_df['title'].isin(recommended_project_titles)]
    other_projects2 = projects_data_df[projects_data_df['title'].isin(recommended_project_titles)]



    top_5_projects = {}
    for project in list(other_projects2.to_dict('records')):
      p = RecommendedProject.objects.get(title=project['title'])
      # top_5_projects.setdefault(p, p.details)

      top_5_projects.setdefault(project['title'], (p.details, project['similarity']))






    context.setdefault('recommended_projects', top_5_projects)
    context.setdefault('other_projects', other_projects.to_dict('records'))


  context.setdefault('form', RecommendedForm(request.POST))









  return render(request, 'student/pages/Graduation-Project/rec-project.html', context)
####################################################################################################
####################################################################################################
####################################################################################################





##########################@######################################
######################## PROJECT DETAILS ########################
###########################@#####################################
@login_required(login_url='login')
def project_details(request, project_id):
  student_rec = is_student(request)

  if type(student_rec) != Student:
    return redirect('login')


  context = {
    'title': 'Recommended Project',
    'user': request.user,
    'notifications': get_notification(request),
    'page_name'    : request.resolver_match.url_name,
  }




  try:
    project = GraduationDetails.objects.get(id=project_id)
    project_title = RecommendedProject.objects.get(details=project)
    context.setdefault('project', project)
    context.setdefault('project_title', project_title)
  except ObjectDoesNotExist:
    return redirect('rec-project')






  return render(request, 'student/pages/Graduation-Project/project-details.html', context)
####################################################################################################
####################################################################################################











##############################################################
######################### COMPANY FORM #######################
##############################################################
@login_required(login_url='login')
def company(request):
  student_rec = is_student(request)


  if type(student_rec) != Student:
    return redirect('login')




  context = {
    'title': 'Internship - Company',
    'user': request.user,
    'notifications': get_notification(request),
  }


  # Check If Student Register in Internship University Course
  if student_rec.in_internship != True:
    return redirect(request.META.get('HTTP_REFERER'))


  if request.method == 'POST':

    form = CompanyForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data

      try:
        # Insert New Record
        CompanyInternship(student=request.user,
                  company=data['company'], address=data['address'], start=data['start'], end=data['end'],
                  name=data['name'], email=data['email'],
                  description_of_tasks=data['description_of_tasks'], technologies=data['technologies']).save()
        context.setdefault('success', 'The form has been filled out successfully.')


        try:
          # Push notification to the doctor
          message   = f'{student_rec.stu.first_name} {student_rec.stu.last_name} fill the company internship form.'
          notify_doctor(student_rec.doc_superviser.doc, subject='Insert Company - Internship', message=message, url_name='report', query_pk=student_rec.pk)
        except:
          pass


        # Push notification to the department
        dept_name = Department.objects.get(dept_name=student_rec.major)
        notify_department(dept_name, subject='Insert Company - Internship', message=message, url_name='student-report', query_pk=student_rec.pk)




      except:
        rec = CompanyInternship.objects.get(student=request.user)
        rec.company              = data['company']
        rec.address              = data['address']
        rec.start                = data['start']
        rec.end                  = data['end']
        rec.name                 = data['name']
        rec.email                = data['email']
        rec.description_of_tasks = data['description_of_tasks']
        rec.technologies         = data['technologies']
        rec.save()
        context.setdefault('update', 'The form was updated successfully.')


        try:
          # Push notification to the doctor
          message   = f'{student_rec.stu.first_name} {student_rec.stu.last_name} update company internship form.'
          notify_doctor(student_rec.doc_superviser.doc, subject='Update Company - Internship', message=message, url_name='report', query_pk=student_rec.pk)
        except:
          pass

        # Push notification to the department
        dept_name = Department.objects.get(dept_name=student_rec.major)
        notify_department(dept_name, subject='Update Company - Internship', message=message, url_name='student-report', query_pk=student_rec.pk)



    else:
      context.setdefault('valid_error', 'ERROR: Enter Valid Data.')


  else:
    pass

  # try .. except, to avoid exception when record.
  try:
    rec = CompanyInternship.objects.get(student=request.user)
    returned_data = {
      'company'             : rec.company,
      'address'             : rec.address,
      'start'               : rec.start,
      'end'                 : rec.end,
      'name'                : rec.name,
      'email'               : rec.email,
      'description_of_tasks': rec.description_of_tasks,
      'technologies'        : rec.technologies,
      'doc_note'            : rec.doc_note,
    }
    context.setdefault('form', CompanyForm(returned_data))
    context.setdefault('doc_note', CompanyInternship.objects.get(student=request.user).doc_note)

  except ObjectDoesNotExist:
    context.setdefault('form', CompanyForm())



  return render(request, 'student/pages/Internship/company.html', context)
####################################################################################################
####################################################################################################






##################################################################
########################## DELETE Company ########################
##################################################################
@login_required(login_url='login')
def delete_company(request):
  student_rec = is_student(request)

  if type(student_rec) != Student:
    return redirect('login')



  try:
    company = CompanyInternship.objects.get(student=request.user)
    company.delete()


    # Push notification to the doctor
    message   = f'{student_rec.stu.first_name} {student_rec.stu.last_name} delete company internship form.'
    notify_doctor(student_rec.doc_superviser.doc, subject='Delete Company - Internship', message=message, url_name='report', query_pk=student_rec.pk)
    dept_name = Department.objects.get(dept_name=student_rec.major)
    notify_department(dept_name, subject='Delete Company - Internship', message=message, url_name='student-report', query_pk=student_rec.pk)
  except:
    pass


  return redirect('company')
####################################################################################################
####################################################################################################








#################################################################
######################### COURSE FORM ###########################
#################################################################
@login_required(login_url='login')
def courses(request):
  # Get Student Record
  student_rec = is_student(request)

  if type(student_rec) != Student:
    return redirect('login')

  # Check If Student Register in Internship University Course
  if student_rec.in_internship != True:
    return redirect(request.META.get('HTTP_REFERER'))

  context = {
    'title': 'Internship - Courses',
    'user': request.user,
    'notifications': get_notification(request),
  }



  if request.method == 'POST':

    form = CourseForm(request.POST, request.FILES)
    if form.is_valid():

      certificate=None
      data = form.cleaned_data
      if 'certificate' in request.FILES.keys():
        extensions = ['jpg', 'jpeg', 'jpg', 'png', 'gif', 'pdf', 'docx']
        if not str(request.FILES['certificate']).split('.')[-1] in extensions:
          context.setdefault('file_extensions_error', extensions)
          file_extensions_error = True
        else:
          file_extensions_error = False
          certificate=request.FILES['certificate']
      else:
        file_extensions_error = False

      if not file_extensions_error:
        CourseInternship(stu=request.user, course=data['course'], hour=data['hour'],
                  provider=data['provider'], certificate=certificate).save()
        context.setdefault('success', 'The form has been filled out successfully.')
          
        
        # Push notification to the doctor
        message   = f'{student_rec.stu.first_name} {student_rec.stu.last_name} add new course for the internship.'
        notify_doctor(student_rec.doc_superviser.doc, subject='Insert Courses - Internship', message=message, url_name='report', query_pk=student_rec.pk)

        dept_name = Department.objects.get(dept_name=student_rec.major)
        notify_department(dept_name, subject='Insert Courses - Internship', message=message, url_name='student-report', query_pk=student_rec.pk)
    
    else:
      context.setdefault('error', 'ERROR: Enter Valid Data.')


  # Return added courses
  try :
    records = CourseInternship.objects.filter(stu=request.user)
    for rec in records:
      rec.certificate = str(rec.certificate).split('/')[-1]
    else:
      context.setdefault('records', records)
  except:
    pass




  context.setdefault('form', CourseForm())
  return render(request, 'student/pages/Internship/courses.html', context)
####################################################################################################
####################################################################################################









##################################################################
########################## UPDATE COURSES ########################
##################################################################
@login_required(login_url='login')
def update_courses(request, pk):
  student_rec = is_student(request)

  if type(student_rec) != Student:
    return redirect('login')



  if request.method == 'POST':

    if not request.POST['course'].isspace() or  request.POST['hour'].isspace() or  request.POST['provider'].isspace():

      if 'certificate' in request.FILES.keys():
        extensions = ['jpg', 'jpeg', 'jpg', 'png', 'gif', 'pdf', 'docx']
        if not str(request.FILES['certificate']).split('.')[-1] in extensions:
          file_extensions_error = True
        else:
          file_extensions_error = False
          certificate=request.FILES['certificate']
      else:
        certificate = None
        file_extensions_error = False

      if not file_extensions_error:

        course = CourseInternship.objects.get(id=pk)
        course.course = request.POST['course']
        course.hour = request.POST['hour']
        course.provider = request.POST['provider']
        if certificate != None:
          course.certificate = certificate
        course.save()
    else:
      return redirect('courses')






    # Push notification to the doctor
    message   = f'{student_rec.stu.first_name} {student_rec.stu.last_name} update course for the internship.'
    notify_doctor(student_rec.doc_superviser.doc, subject='Update Courses - Internship', message=message, url_name='report', query_pk=student_rec.pk)
      
  return redirect('courses')
####################################################################################################
####################################################################################################










##################################################################
########################## DELETE COURSES ########################
##################################################################
@login_required(login_url='login')
def delete_courses(request, pk):
  
  if request.method == 'POST':
    course = CourseInternship.objects.get(id=pk)
    course.delete()
  return redirect('courses')
####################################################################################################
####################################################################################################









#################################################################
######################### WEEKLY FORM ###########################
#################################################################
def weekly_form(request, student):
  try:
    u = User.objects.get(username=student)
    result = CompanyInternship.objects.get(student=u).student

    s    = Student.objects.get(stu=u).major
    week = Department.objects.get(dept_name=s).week

    weeks = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth']
    week = weeks[week-2]
  except:
    return redirect('close')


  if request.method == 'POST':
    form = WeeklyForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      u = User.objects.get(username=request.POST['student'])
      WeeklyFollowing(stu_user=u, task=data['task'], hour=data['hour'], sw_hw=data['sw_hw'], week=request.POST['week']).save()



  context = {
    'flag': True,
    'title': 'Weekly Following Form',
    'form': WeeklyForm(),
    'student': result,
    'week': week,
  }



  return render(request, 'student/pages/Internship/weekly_form.html', context)
####################################################################################################
####################################################################################################







###############################################################
####################### DOWNLOAD FILE #########################
###############################################################
def download_file(request, file_id):

  try:
    stored_file = CourseInternship.objects.get(id=file_id)

    response = FileResponse(stored_file.certificate, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{stored_file.certificate.name}"'
    return response

  except ObjectDoesNotExist:
    stored_file = TimlineFiles.objects.get(id=file_id)

    response = FileResponse(stored_file.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{stored_file.file.name}"'
    return response
  except:
    s = get_object_or_404(CourseInternship, pk=id)
####################################################################################################
####################################################################################################






################################################################
##################### NOT FOUND PAGE 404 #######################
################################################################
def handling_404(request, exception):
  return render(request, '404.html', {'flag', True},status=404)
####################################################################################################
####################################################################################################



################################################################
########################### Close ##############################
################################################################
def close(request):
  return render(request, 'close.html', {})
####################################################################################################
####################################################################################################