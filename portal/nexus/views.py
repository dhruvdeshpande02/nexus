# views.py

import pdb
from django.shortcuts import render, redirect
from .forms import CoordinatorCreationForm,StudentRegistrationForm,CoordinatorLoginForm,NoticeForm,TnpAdminLoginForm
from .models import Coordinator,Student,Notice
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from django.contrib.auth.decorators import user_passes_test



from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    if request.method == 'GET':
        # Your view logic for handling GET requests
        return render(request, 'home.html')

 

def create_coordinator_view(request):
    if request.method == 'POST':
        form = CoordinatorCreationForm(request.POST)
        if form.is_valid():
            coordinator = form.save(commit=True)
            
            return redirect('coordinator-list/')
        else:
            print(form.errors)
    else:
        form = CoordinatorCreationForm()  # Instantiate the form here

    return render(request, 'create_coordinator.html', {'form': form})

    
from django.contrib.auth.decorators import user_passes_test

# Custom test function to check if the user is a TNP Admin or Coordinator

def create_notice(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.uploaded_by = request.user
            notice.save()
            return redirect('cnotice_list')  # Redirect to the list of notices
    else:
        form = NoticeForm()
    return render(request, 'notice_form.html', {'form': form})

def coordinator_list(request):
    coordinators = Coordinator.objects.all()  # Query all coordinators from the database
    context = {'coordinators': coordinators}
    return render(request, 'coordinator_list.html', context)

def student_registration(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save(True)  # Save the form data to the database
            return redirect('student_login')
            # You can add a success message or redirect to a different page
        debug =True  
    else:
        form = StudentRegistrationForm()

    return render(request, 'student_registration.html', {'form': form})


def student_list(request):
    students = Student.objects.all() 
    context = {'students': students}
    return render(request, 'students_list.html', context)


# views.py



from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Student


def student_login(request):
    error_message = None

    if request.method == 'POST':
        S_PRN = request.POST.get('S_PRN')
        s_password = request.POST.get('s_password')

        # Authenticate the student
        student = authenticate(request, S_PRN=S_PRN, s_password=s_password)

        if student is not None:
            login(request, student)
            return redirect('home')  # Redirect to the 'home' page upon successful login
        else:
            error_message = 'Invalid PRN or password'
    return render(request, 'student_login.html', {'error_message': error_message})






from django.views.generic.edit import FormView
class CoordinatorLoginView(FormView):
    template_name = 'coordinator_login.html'
    form_class = CoordinatorLoginForm

    def form_valid(self, form):
        # Get form data
        F_ID = form.cleaned_data['F_ID']
        f_password = form.cleaned_data['f_password']

        # Authenticate the coordinator
        user = authenticate(request=self.request, F_ID=F_ID, f_password=f_password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Invalid F_ID or password')
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('home') 

class TNPAdminLoginView(LoginView):
    template_name = 'tnp_admin_login.html'  # Create this template
    form_class = TnpAdminLoginForm
    success_url = reverse_lazy('home')  # Redirect to the 'home' URL after successful login

def c_notice_list(request):
    notices = Notice.objects.all()  # Fetch all notices (you can add filtering logic if needed)
    return render(request, 'c_notice_list.html', {'notices': notices})

def s_notice_list(request):
    notices = Notice.objects.all()  # Fetch all notices (you can add filtering logic if needed)
    return render(request, 's_notice_list.html', {'notices': notices})

from django.shortcuts import render, get_object_or_404

def notice_detail(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    applications = Application.objects.all()

    return render(request, 'notice_detail.html', {'notice': notice, 'applications': applications})





from django.http import HttpResponse
from openpyxl import Workbook
from nexus.models import Student

def export_to_excel(request):
    # Query the data you want to export
    data = Student.objects.all()

    # Create a new Excel workbook and add a worksheet
    workbook = Workbook()
    worksheet = workbook.active

    # Define headers for your columns
    headers = ['PRN', 'NAME','DOB', 'GENDER','EMAIL','AGE','MOBILE_NO','ALT_MOBILE_NO','LOCAL_ADDRESS','PERM_ADDRESS','NATIVE_PLACE',
               'X_PRECENTAGE','X_YEAR_OF_PASSING','X_BOARD','XII_PERCENTAGE','XII_YEAR_OF_PASSING','XII_BOARD','DIPLOMA_PERCENTAGE'
               ,'DIPLOMA_YEAR_OF_PASSING','DIPLOMA_COLLEGE','DIPLOMA_BRANCH','ADMISSION_TYPE','ENGG_YEAR_OF_PASSING','SEM_1_SGPA','SEM_2_SGPA',
               'SEM_3_SGPA','SEM_4_SGPA','SEM_5_SGPA','SEM_6_SGPA','SEM_7_SGPA','SEM_8_SGPA','AVG_TILL_SEM_CGPA','AVG_TILL_SEM_PERCENTAGE',
               'LIVE_BACKLOG','DEAD_BACKLOG','YEAR_GAP','CO_CURRICULAR','EXTRA_CURRICULAR','MINI_PROJECT','MAJ_PROJECT','PROG_LANG_KNOWN',
               'PREFERENCE_1','PREFERENCE_2','PREFERENCE_3','PLACEMENT_STATUS']  # Replace with your column headers

    # Write headers to the worksheet
    worksheet.append(headers)

    # Iterate over the data and add rows
    for item in data:
        row = [item.S_PRN, item.S_NAME,item.S_DOB, item.S_GENDER, item.S_EMAIL,item.S_AGE,item.S_MOBILE_NO,item.S_ALT_Mobile_NO,item.S_LOCAL_ADDRS,
               item.S_PERM_ADDRS,item.S_Native_Place,item.X_Percentage,item.X_year_of_passing,item.X_board,item.XII_Percentage,item.XII_year_of_passing,
               item.XII_board,item.Diploma_percentage,item.Diploma_year_of_passing,item.Diploma_college,item.Diploma_branch,item.Admission_Type,
               item.Engg_year_of_passing,item.SEM_1_sgpa,item.SEM_2_sgpa,item.SEM_3_sgpa,item.SEM_4_sgpa,item.SEM_5_sgpa,item.SEM_6_sgpa,item.SEM_7_sgpa,
               item.SEM_8_sgpa,item.AVG_TILL_SEM_cgpa,item.AVG_TILL_SEM_percentage,item.Live_backlogs,item.Dead_backlogs,item.Year_gap,item.Co_Curricular,
               item.Extra_Curricular,item.Mini_project,item.Maj_project,item.Prog_lang_known,item.Preference_1,item.Preference_2,item.Preference_3,
               item.Placement_status]  # Replace with your model fields
        worksheet.append(row)

    # Create a response with the Excel content
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="exported_data.xlsx"'

    # Save the workbook content to the response
    workbook.save(response)

    return response

# views.py
from django.shortcuts import render, redirect
from .models import Application, Notice
from .forms import ApplicationForm

def apply_to_notice(request, notice_id):
    notice = Notice.objects.get(pk=notice_id)
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.notice = notice  # Associate the application with the notice
            application.student = request.user.student  # Assuming the student is logged in
            application.save()
            return redirect('s_notice_list')  # Replace with the URL to your notice list view
    
    # Handle errors or render a success message as needed
    return render(request, 'home.html', {'form': form, 'notice': notice})

from .models import Notice

def notice_delete(request, notice_id):
    # Get the notice object by its ID
    notice = get_object_or_404(Notice, id=notice_id)

    if request.method == 'POST':
        # Check if the request method is POST
        notice.delete()  # Delete the notice
        return redirect('cnotice_list')  # Redirect to the notice list page after deletion

    return render(request, 'notice_delete_confirm.html', {'notice': notice})