from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Member,Staff,Classes,Course,MemberAttendance,StaffAttendance,Invoice,Payroll
from . forms import *
from django.contrib import messages
from django.shortcuts import render

# Create your views here.
class AppsView(LoginRequiredMixin,TemplateView):
    pass

member_add_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
member_update_view = AppsView.as_view(template_name="apps/job/apps-job-new.html")
member_list_view = AppsView.as_view(template_name="taekwondogym/courses/member-list.html")

staff_add_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
staff_update_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
staff_list_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")

class_add_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
class_update_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
class_list_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")

course_add_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
course_update_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
course_list_view = AppsView.as_view(template_name="taekwondogym/courses/course-list.html")

invoice_add_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
invoice_update_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
invoice_list_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")

payroll_add_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
payroll_update_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
payroll_list_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")

member_attendance_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
staff_attendance_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
