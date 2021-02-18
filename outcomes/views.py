from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from outcomes.models import Student_Post_Moringa
from admissions.models import Student_Profile

# Create your views here.
""" 
View for Returning all Prep Cohorts
"""
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def student_post(request):
    student_posts = Student_Post_Moringa.objects.all()

    posts = []

    if student_posts:
        for post in student_posts:
            student = Student_Profile.objects.get(student_id=post.student_id)
            p = {"student_name": student.name, "graduation_date": post.graduation_date, "developer_profile": post.developer_profile,
                 "company_after_ms": post.company_after_ms, "job_title": post.job_title, "fulltime_internship": post.fulltime_internship,
                 "salary_after_ms": post.salary_after_ms, "sec_salary_after_ms": post.sec_salary_after_ms,
                 "comments_post_call": post.comments_post_call}
            posts.append(p)

    else:
        pass

    return Response(posts)
