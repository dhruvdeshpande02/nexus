# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CoordinatorCreationForm

@login_required
def create_coordinator_view(request):
    # Check if the user is a TNP admin
    if not request.user.is_authenticated or not request.user.is_tnpadmin:
        return redirect('login')  # Redirect unauthorized users to login page

    if request.method == 'POST':
        form = CoordinatorCreationForm(request.POST)
        if form.is_valid():
            # Save the coordinator account
            coordinator = form.save(commit=False)
            coordinator.user = request.user  # Assign the TNP admin user
            coordinator.save()
            return redirect('coordinator_list')  # Redirect to the list of coordinators
    else:
        form = CoordinatorCreationForm()

    return render(request, 'create_coordinator.html', {'form': form})

from .models import Coordinator

def coordinator_list(request):
    coordinators = Coordinator.objects.all()  # Query all coordinators from the database
    context = {'coordinators': coordinators}
    return render(request, 'coordinator_list.html', context)
