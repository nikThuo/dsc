from django.db import models

# Create your models here.
""" 
Model for Prep Cohort
"""
class Prep_Cohort(models.Model):
    cohort_id = models.IntegerField(auto_created=True, primary_key=True)
    prep_cohort = models.CharField(max_length=50)

    class Meta:
        db_table = 'prep_cohort'

""" 
Model for Core Cohort
"""
class Core_Cohort(models.Model):
    cohort_id = models.IntegerField(auto_created=True, primary_key=True)
    core_cohort = models.CharField(max_length=50)

    class Meta:
        db_table = 'core_cohort'

""" 
Model for Student Profile
"""
class Student_Profile(models.Model):
    student_id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    dob = models.DateField()
    phone = models.IntegerField(null=True)
    prep_cohort = models.ForeignKey(Prep_Cohort, on_delete=models.CASCADE, null=True)
    core_cohort = models.ForeignKey(Core_Cohort, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'Student_Profile'

""" 
Model for Education Background
"""
class Student_Education_Background(models.Model):
    edu_id = models.AutoField(auto_created=True, primary_key=True)
    student = models.ForeignKey(Student_Profile, on_delete=models.CASCADE)
    education_level = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    university_course = models.CharField(max_length=50)
    employed_before = models.CharField(max_length=50)
    employer = models.CharField(max_length=50)
    employed_net_salary = models.CharField(max_length=50)
    gross_income_guardian = models.CharField(max_length=50)

    class Meta:
        db_table = 'Student_Education_Background'