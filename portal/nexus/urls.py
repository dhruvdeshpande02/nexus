# urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # ... other URL patterns ...
    path('home/', views.home, name='home'),  
    path('coordinator_home/', views.coordinator_home, name='coordinator_home'), 
    path('tnp_home/', views.tnp_home, name='tnp_home'), 
    path('create-coordinator/', views.create_coordinator_view, name='create_coordinator'),
    path('coordinator-list/', views.coordinator_list, name='coordinator_list'),
    path('student/register/', views.student_registration, name='student_registration'),
    path('student/login/', views.student_login, name='student_login'),
    path('student-list/', views.student_list, name='studentlist'),
    path('create-notice/', views.create_notice, name='createnotice'),
    path('tnp_login/', views.tnp_login, name='tnp_login'),
    path('coordinatorhome/', views.coordinator_home, name='coordinator_home'),
    path('snotice-list/', views.s_notice_list, name='snotice_list'),
    path('notice/<int:notice_id>/', views.notice_detail, name='notice_detail'),
    path('export_to_excel/', views.export_to_excel, name='export_to_excel'),
    path('coordinator_login/', views.coordinator_login, name='coordinator_login'),
    path('undertaking/', views.undertaking_submit, name='undertaking_submit'),

    
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)