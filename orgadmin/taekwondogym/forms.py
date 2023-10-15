from django import forms
from .models import Member,Staff,Classes,Course,MemberAttendance,StaffAttendance,Invoice,Payroll

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

class MemberAddForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['gym','profile_pic','name','address','parent_name','email_id','phone','line_id','member_status']
        
class MemberUpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['profile_pic','name','address','parent_name','email_id','phone','line_id','member_status','leave_at','point']
        
class StaffAddForm(forms.ModelForm):
    
    class Meta:
        model = Staff
        fields = ['gym','profile_pic','name','address','email_id','phone','line_id','member_status','leave_at']
        
class StaffUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Staff
        fields = ['profile_pic','name','address','email_id','phone','line_id','member_status','leave_at']
        
class ClassAddForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = ['gym','name','level_name','students']

class ClassUpdateForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = ['name','level_name','students','update_at']
        
class CourseAddForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['gym','course_name','course_type','course_fee','staff','open_course','close_course','classes']
        
class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name','course_type','course_fee','staff','open_course','close_course','classes']
        
class InvoiceAddForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['gym','invoice_number','students','invoice_status','courses','amount','discount','pay','remark','payment_type']
        
class InvoiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_number','students','invoice_status','courses','amount','discount','pay','remark','payment_type']

class PayrollAddForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = ['gym','staff','amount','bonus','pay','hour_amount','pay_at']
        
class PayrollUpdateForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = ['staff','amount','bonus','pay','hour_amount','pay_at']