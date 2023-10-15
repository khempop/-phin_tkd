from rest_framework import serializers
from . models import Member,Staff,Classes,Course,MemberAttendance,StaffAttendance,Invoice,Payroll

# Create your models here.
MEMBER_STATUS = (
    ('Active','Active'),
    ('Disabled','Disabled')
)

COURSE_TYPE = (
    ('SINGLE','SINGLE'),
    ('CONTINUE','CONTINUE')
)

INVOICE_STATUS = (
    ('PAID','PAID'),
    ('HOLD','HOLD'),
    ('FAILED','FAILED'),
    ('CANCEL','CANCEL')
)

PAYMENT_TYPE = (
    ('ONLINE','ONLINE'),
    ('PROMPTPAY','PROMPTPAY'),
    ('CASH','CASH')
)

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['gym','profile_pic','name','address','parent_name','email_id','phone','line_id','member_status','leave_at','point']

class Staff(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['gym','profile_pic','name','address','email_id','phone','line_id','member_status','leave_at']

class Classes(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ['gym','name','level_name','students','update_at']

class Course(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['gym','course_name','course_type','course_fee','staff','open_course','close_course','classes']

class MemberAttendance(serializers.ModelSerializer):
    class Meta:
        model = MemberAttendance
        fields = ['gym','member','active_at','course','update_at']
    
class StaffAttendance(serializers.ModelSerializer):
    class Meta:
        model = StaffAttendance
        fields = ['gym','staff','active_at','course','update_at']

class Invoice(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['gym','invoice_number','students','invoice_status','courses','amount','discount','pay','remark','payment_type']
class Payroll(serializers.ModelSerializer):
    class Meta:
        model = Payroll
        fields = ['gym','staff','amount','bonus','pay','hour_amount','pay_at']