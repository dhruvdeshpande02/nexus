# views.py

from django.shortcuts import render, redirect
from .forms import CoordinatorCreationForm,StudentRegistrationForm,CoordinatorLoginForm,NoticeForm,TnpAdminLoginForm,CombinedLoginForm
from .models import Coordinator,Student,Notice
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from django.contrib.auth.decorators import user_passes_test



class HomeView(TemplateView):
    template_name = 'home.html'  # Specify the template name for the 'home' page
    from django.shortcuts import render



from django.shortcuts import render, redirect

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
            return redirect('notice_list')  # Redirect to the list of notices
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
            
            # You can add a success message or redirect to a different page
        debug =True  
    else:
        form = StudentRegistrationForm()

    return render(request, 'student_registration.html', {'form': form})


def student_list(request):
    students = Student.objects.all() 
    context = {'students': students}
    return render(request, 'students_list.html', context)

from django.shortcuts import render, redirect



class CombinedLoginView(LoginView):
    form_class = CombinedLoginForm
    template_name = 'student_login.html'



class CoordinatorLoginView(LoginView):
    template_name = 'coordinator_login.html'  # Create this template
    form_class = CoordinatorLoginForm
    success_url = reverse_lazy('home')  # Redirect to the 'home' URL after successful login

class TNPAdminLoginView(LoginView):
    template_name = 'tnp_admin_login.html'  # Create this template
    form_class = TnpAdminLoginForm
    success_url = reverse_lazy('home')  # Redirect to the 'home' URL after successful login

def notice_list(request):
    notices = Notice.objects.all()  # Fetch all notices (you can add filtering logic if needed)
    return render(request, 'notice_list.html', {'notices': notices})

from django.shortcuts import render, get_object_or_404

def notice_detail(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    applicants = notice.applicants.all()

    return render(request, 'notice_detail.html', {'notice': notice, 'applicants': applicants})

from django.shortcuts import render, redirect
from .forms import ApplicationForm  # Import your Application form

def apply_to_notice(request, notice_id):
    notice = Notice.objects.get(pk=notice_id)  # Get the selected notice
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.student = request.user  # Set the student to the current user
            application.notice = notice  # Set the notice to which the student is applying
            application.save()
            return redirect('notice_list')  # Redirect to the notice list view or any other page
    else:
        form = ApplicationForm()

    return render(request, 'apply_to_notice.html', {'form': form, 'notice': notice})




import openpyxl
from openpyxl.utils import get_column_letter
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Your existing view for displaying student data goes here
# ...

def export_students_to_excel(request):
    # Load the HTML template that contains the student data table
    template = get_template('student_list.html')

    # Render the HTML template with the context data to get the table content
    context = {}  # You may need to pass any required context data here
    html_content = template.render(context)

    # Create a new Excel workbook
    wb = openpyxl.Workbook()
    ws = wb.active

    # Parse the HTML table content and populate the Excel sheet
    html_rows = pisa.pisaDocument(html_content)
    for row in html_rows:
        if hasattr(row, 'childNodes') and len(row.childNodes) > 0:
            excel_row = []
            for cell in row.childNodes:
                if hasattr(cell, 'attributes'):
                    if 'data-th' in cell.attributes:
                        excel_row.append(cell.attributes['data-th'])
                    else:
                        excel_row.append(cell.content)
            ws.append(excel_row)

    # Create an HttpResponse with the Excel content
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="student_data.xlsx"'

    # Save the workbook to the response
    wb.save(response)

    return response




