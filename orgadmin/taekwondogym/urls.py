from django.urls import path
from taekwondogym.views import(
    member_add_view,
    member_update_view,
    member_list_view,
    MemberAPI,

    staff_add_view,
    staff_update_view,
    staff_list_view,

    class_add_view,
    class_update_view,
    class_list_view,

    course_add_view,
    course_update_view,
    course_list_view,

    invoice_add_view,
    invoice_update_view,
    invoice_list_view,

    payroll_add_view,
    payroll_update_view,
    payroll_list_view,

    member_attendance_view,
    staff_attendance_view
)
app_name = "taekwondogym"

urlpatterns = [
    path("add-member", view=member_add_view, name="member.add"),
    path("update-member", view=member_update_view, name="member.update"),
    path("list-member", view=member_list_view, name="member.list"),
    path("api/add-member", MemberAPI.as_view()),
    path("api/update-member/<int:id>/", MemberAPI.as_view()),
    path("api/member/<int:id>/", MemberAPI.as_view()),
    path("api/member", MemberAPI.as_view()),

    path("add-staff", view=staff_add_view, name="staff.add"),
    path("update-staff", view=staff_update_view, name="staff.update"),
    path("list-staff", view=staff_update_view, name="staff.list"),

    path("add-class", view=class_add_view, name="class.add"),
    path("update-class", view=class_update_view, name="class.update"),
    path("list-class", view=class_update_view, name="class.list"),

    path("add-course", view=course_add_view, name="course.add"),
    path("update-course", view=course_update_view, name="course.update"),
    path("list-course", view=course_list_view, name="course.list"),

    path("add-invoice", view=invoice_add_view, name="invoice.add"),
    path("update-invoice", view=invoice_update_view, name="invoice.update"),
    path("list-invoice", view=invoice_update_view, name="invoice.list"),

    path("add-payroll", view=payroll_add_view, name="payroll.add"),
    path("update-payroll", view=payroll_update_view, name="payroll.update"),
    path("list-payroll", view=payroll_update_view, name="payroll.list"),

    path("member-attendance", view=member_attendance_view, name="member.attendance"),
    path("staff-attendance", view=staff_attendance_view, name="staff.attendance"),
]