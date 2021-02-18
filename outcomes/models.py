from django.db import models


from admissions.models import Student_Profile

# Create your models here.
""" 
Model for Outcome Information
"""
class Student_Post_Moringa(models.Model):
    post_id = models.AutoField(auto_created=True, primary_key=True)
    student = models.ForeignKey(Student_Profile, on_delete=models.CASCADE)
    graduation_date = models.DateField()
    developer_profile = models.CharField(max_length=50)
    company_after_ms = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    fulltime_internship = models.CharField(max_length=50)
    salary_after_ms = models.IntegerField(null=True)
    sec_salary_after_ms = models.IntegerField(null=True)
    comments_post_call = models.IntegerField(null=True)

    class Meta:
        db_table = 'Student_Post_Moringa'
