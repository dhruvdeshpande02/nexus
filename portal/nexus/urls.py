# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('create-coordinator/', views.create_coordinator_view, name='create_coordinator'),
    path('coordinator-list/', views.coordinator_list, name='listr'),
]
