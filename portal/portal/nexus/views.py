# views.py

from django.shortcuts import render, redirect
from .forms import CoordinatorCreationForm,StudentRegistrationForm,StudentLoginForm
from .models import Coordinator,Student
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
import logging






logger = logging.getLogger('nexus.views.StudentLoginView') 

class HomeView(TemplateView):
    template_name = 'home.html'  # Specify the template name for the 'home' page


def create_coordinator_view(request):
    form = CoordinatorCreationForm()  # Move the form instantiation here

    if request.method == 'POST':
        form = CoordinatorCreationForm(request.POST)
        if form.is_valid():
            coordinator = form.save(commit=True)
            coordinator.save()
            return redirect('coordinator_list')
    else:
        print(form.errors)
        return render(request, 'create_coordinator.html', {'form': form})




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


class StudentLoginView(LoginView):
    template_name = 'student_login.html'
    form_class = StudentLoginForm
    success_url = reverse_lazy('home') 
    

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        logger.debug("User %s successfully logged in.", user.username) 
        return super().form_valid(form)

def student_list(request):
    students = Student.objects.all() 
    context = {'students': students}
    return render(request, 'students_list.html', context)









