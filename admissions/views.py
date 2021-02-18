from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from admissions.models import Prep_Cohort, Core_Cohort, Student_Profile, Student_Education_Background
from outcomes.models import Student_Post_Moringa

# Create your views here.

""" 
View for Returning all Prep Cohorts
"""
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def prep_cohort(request):
    prep_cohorts = Prep_Cohort.objects.all()

    cohorts = []

    if prep_cohorts:
        for cohort in prep_cohorts:
            c = {"cohort name": cohort.prep_cohort}
            cohorts.append(c)

    else:
        pass

    return Response(cohorts)

""" 
View for Returning all Core Cohorts
"""
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def core_cohort(request):
    core_cohorts = Core_Cohort.objects.all()

    cohorts = []

    if core_cohorts:
        for cohort in core_cohorts:
            c = {"cohort name": cohort.core_cohort}
            cohorts.append(c)

    else:
        pass

    return Response(cohorts)

""" 
View for Returning Student Details --- Student Profile and Background
"""
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def student_profile(request):
    student_profile = Student_Profile.objects.all()

    profiles = []

    if student_profile:
        for profile in student_profile:
            prep = Prep_Cohort.objects.get(cohort_id=profile.prep_cohort_id)
            core = Core_Cohort.objects.get(cohort_id=profile.core_cohort_id)
            p = {"student_name": profile.name, "email": profile.email, "gender": profile.gender, "dob": profile.dob,
                 "phone": profile.phone, "prep_cohort": prep.prep_cohort, "core_cohort": core.core_cohort}
            profiles.append(p)

    else:
        pass

    return Response(profiles)

""" 
View for Returning Student Details --- Student Profile and Background
"""
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def student_background(request):
    student_background = Student_Education_Background.objects.all()

    backs = []

    if student_background:
        for back in student_background:
            student = Student_Profile.objects.get(student_id=back.student_id)
            # prep = Prep_Cohort.objects.get(cohort_id=profile.)
            b = {"student_name": student.name, "education_level": back.education_level, "university": back.university, "university_course": back.university_course, "employed_before": back.employed_before,
                 "employer": back.employer, "employed_net_salary": back.employed_net_salary, "gross_income_guardian": back.gross_income_guardian}
            backs.append(b)

    else:
        pass

    return Response(backs)