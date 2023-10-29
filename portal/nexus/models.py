from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    # Add any additional fields you need for the User model here.
    is_student = models.BooleanField(default=False)
    is_coordinator = models.BooleanField(default=False)
    is_tnpadmin = models.BooleanField(default=True)

class Student(models.Model):
    
    S_NAME = models.CharField(max_length=255)
    S_PRN = models.PositiveIntegerField(unique=True)
    S_DOB = models.DateField()
    S_GENDER = models.CharField(max_length=10)
    S_EMAIL = models.EmailField()
    S_AGE = models.PositiveIntegerField()
    S_MOBILE_NO = models.PositiveIntegerField()
    S_ALT_Mobile_NO = models.PositiveIntegerField()
    S_LOCAL_ADDRS = models.CharField(max_length=255)
    S_PERM_ADDRS = models.CharField(max_length=255)
    S_Native_Place = models.CharField(max_length=255)
    X_Percentage = models.DecimalField(max_digits=5, decimal_places=2)
    X_year_of_passing = models.PositiveIntegerField()
    X_board = models.CharField(max_length=255)
    XII_Percentage = models.DecimalField(max_digits=5, decimal_places=2,blank = True,null=True)
    XII_year_of_passing = models.PositiveIntegerField(blank = True,null=True)
    XII_board = models.CharField(max_length=255,blank = True,null=True)
    Diploma_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank = True, null=True)
    Diploma_year_of_passing = models.PositiveIntegerField(blank = True,null=True)
    Diploma_college = models.CharField(max_length=255,blank = True,null=True)
    Diploma_branch = models.CharField(max_length=255,blank = True,null=True)
    Admission_Type = models.CharField(max_length=255)
    Engg_year_of_passing = models.PositiveIntegerField()
    SEM_1_sgpa = models.DecimalField(max_digits=4, decimal_places=2)
    SEM_2_sgpa = models.DecimalField(max_digits=4, decimal_places=2)
    SEM_3_sgpa = models.DecimalField(max_digits=4, decimal_places=2)
    SEM_4_sgpa = models.DecimalField(max_digits=4, decimal_places=2)
    SEM_5_sgpa = models.DecimalField(max_digits=4, decimal_places=2)
    SEM_6_sgpa = models.DecimalField(max_digits=4, decimal_places=2)
    SEM_7_sgpa = models.DecimalField(max_digits=4, decimal_places=2,null=True)
    SEM_8_sgpa = models.DecimalField(max_digits=4, decimal_places=2,blank=True, null=True)
    AVG_TILL_SEM_cgpa = models.DecimalField(max_digits=5, decimal_places=2)
    AVG_TILL_SEM_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    Live_backlogs = models.PositiveIntegerField()
    Dead_backlogs = models.CharField(max_length=255)
    Year_gap = models.CharField(max_length=255)
    Co_Curricular = models.CharField(max_length=255)
    Extra_Curricular = models.CharField(max_length=255)
    Mini_project = models.CharField(max_length=255)
    Maj_project = models.CharField(max_length=255)
    Prog_lang_known = models.CharField(max_length=255)
    Preference_1 = models.CharField(max_length=255)
    Preference_2 = models.CharField(max_length=255)
    Preference_3 = models.CharField(max_length=255)
    Placement_status = models.CharField(max_length=255)
    s_password = models.CharField(max_length=128, default='Provide a strong password')
    




    
    AVG_TILL_SEM_cgpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    AVG_TILL_SEM_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def calculate_average_and_percentage(self):
        # Create a list of SGPA values for the semesters
        sem_sgpa_fields = [self.SEM_1_sgpa, self.SEM_2_sgpa, self.SEM_3_sgpa, self.SEM_4_sgpa, self.SEM_5_sgpa, self.SEM_6_sgpa, self.SEM_7_sgpa, self.SEM_8_sgpa]

        # Filter out None values and then calculate the average
        valid_sgpa_values = [sgpa for sgpa in sem_sgpa_fields if sgpa is not None]
        
        if valid_sgpa_values:
            avg_cgpa = sum(valid_sgpa_values) / len(valid_sgpa_values)
            self.AVG_TILL_SEM_cgpa = round(avg_cgpa, 2)
            
            # Calculate percentage (assuming 10 is the maximum SGPA)
            max_sgpa = 10
            percentage = (avg_cgpa / max_sgpa) * 100
            self.AVG_TILL_SEM_percentage = round(percentage, 2)

    def save(self, *args, **kwargs):
        self.calculate_average_and_percentage()  # Calculate before saving
        super(Student, self).save(*args, **kwargs)
    

class Coordinator(models.Model):
    
    F_NAME = models.CharField(max_length=255)
    F_PHONE_NO = models.PositiveIntegerField()
    F_EMAIL = models.EmailField()
    F_DEPARTMENT = models.CharField(max_length=255)
    F_Personal_Email = models.EmailField()
    F_ID = models.CharField(max_length=20,unique=True)
    F_INSTITUTE = models.CharField(max_length=255)
    f_password = models.CharField(max_length=128, default='Provide a strong password')
class TNPAdmin(models.Model):
   
    T_ID = models.CharField(max_length=20,unique=True)
    T_NAME = models.CharField(max_length=255)
    T_EMAIL = models.EmailField()
    T_PH_NO = models.PositiveIntegerField()
    t_password = models.CharField(max_length=128, default='Provide a strong password')
from django.db import models
from django.utils import timezone

class Notice(models.Model):
    NOTICE_TYPES = (
        ('CPD', 'CPD'),
        ('CPPA', 'CPPA'),
    )

    notice_type = models.CharField(max_length=4, choices=NOTICE_TYPES)
    title = models.CharField(max_length=100)
    notice_id = models.CharField(max_length=20,default="00")
    content = models.TextField()
    file = models.FileField(upload_to='notices/')
    notice_date = models.DateTimeField(default=timezone.now)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    applicants = models.ManyToManyField(User, related_name='applied_notices', blank=True)
    

    def __str__(self):
        return self.title

    def is_cpd(self):
        return self.notice_type == 'CPD'

    def is_cppa(self):
        return self.notice_type == 'CPPA'

from django.db import models

from .models import Notice  # Import your notice model

class Application(models.Model):
    notice_id = models.ForeignKey(Notice, on_delete=models.CASCADE,default='01')
    S_prn = models.ForeignKey(Student, on_delete=models.CASCADE,default='20200110')  # Assuming you have a Student model
    application_status = models.TextField(default='pending')  # Add fields as needed



