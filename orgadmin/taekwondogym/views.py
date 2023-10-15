from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Member,Staff,Classes,Course,MemberAttendance,StaffAttendance,Invoice,Payroll
from . forms import *
from django.contrib import messages
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from taekwondogym.serializers import MemberSerializer


# Create your views here.
class AppsView(LoginRequiredMixin,TemplateView):
    pass

member_add_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
member_update_view = AppsView.as_view(template_name="apps/job/apps-job-new.html")
#member_list_view = AppsView.as_view(template_name="taekwondogym/members/member-list.html")

staff_add_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
staff_update_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
staff_list_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")

class_add_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
class_update_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
class_list_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")

course_add_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
course_update_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
course_list_view = AppsView.as_view(template_name="taekwondogym/members/member-list.html")

invoice_add_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
invoice_update_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
invoice_list_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")

payroll_add_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
payroll_update_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
payroll_list_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")

member_attendance_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")
staff_attendance_view = AppsView.as_view(template_name="taekwondogym/courses/course-create.html")

def member_list_view(request):
    context = {}
    context["gym"] = request.user.id
    template = "taekwondogym/members/member-list.html"

    templates = [template]
    return render(request, templates, context)


class MemberAPI(APIView):
    # add permission to check if user is authenticated
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        members = Member.objects.filter(gym=str(request.user.id))
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)