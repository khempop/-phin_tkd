from django.db import models
from multiselectfield import MultiSelectField

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



class Member(models.Model):
    profile_pic = models.ImageField(upload_to="images/contact",blank=True,null=True)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=250,null=True, blank=True)
    parent_name = models.CharField(max_length=150,null=True, blank=True)
    email_id = models.EmailField(max_length=150,unique=True)
    phone = models.CharField(max_length=13,null=True, blank=True)
    line_id = models.CharField(max_length=150,null=True, blank=True)
    member_status = models.CharField(max_length=50,choices=MEMBER_STATUS,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    join_at = models.DateTimeField(auto_now_add=True)
    leave_at = models.DateTimeField()
    point = models.IntegerField()
    update_at = models.DateTimeField(null=True)

    def get_photo_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
        else:
            return "/static/images/users/user-dummy-img.jpg"

class Staff(models.Model):
    profile_pic = models.ImageField(upload_to="images/contact",blank=True,null=True)
    name = models.CharField(max_length=150,)
    address = models.CharField(max_length=25,null=True, blank=True)
    email_id = models.EmailField(max_length=150,unique=True)
    phone = models.CharField(max_length=13,null=True, blank=True)
    line_id = models.CharField(max_length=150,null=True, blank=True)
    member_status = models.CharField(max_length=50,choices=MEMBER_STATUS,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    join_at = models.DateTimeField(auto_now_add=True)
    leave_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(null=True)
    
    def get_photo_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
        else:
            return "/static/images/users/user-dummy-img.jpg"

class Classes(models.Model):
    name = models.CharField(max_length=150)
    level_name = models.CharField(max_length=200)
    students = models.ManyToManyField(Member)
    update_at = models.DateTimeField(null=True)

class Course(models.Model):
    course_name = models.CharField(max_length=150)
    course_type = models.CharField(max_length=50,choices=COURSE_TYPE)
    course_fee = models.IntegerField(null=True, blank=True)
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE, verbose_name="staff",null=True, blank=True)
    open_course = models.DateField(blank=True, null=True)
    close_course = models.DateField(blank=True, null=True)
    classes = models.ForeignKey(Classes,on_delete=models.CASCADE, verbose_name="member level",null=True, blank=True)
    update_at = models.DateTimeField(null=True)

class MemberAttendance(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE, verbose_name="member")
    active_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE, verbose_name="course",null=True, blank=True)
    update_at = models.DateTimeField(null=True)    
    
class StaffAttendance(models.Model):
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE, verbose_name="staff")
    active_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE, verbose_name="course",null=True, blank=True)
    update_at = models.DateTimeField(null=True)

class Invoice(models.Model):
    invoice_number = models.AutoField(auto_created = True,primary_key = True,serialize = True )
    students = models.ManyToManyField(Member)
    invoice_status = models.CharField(max_length=50,choices=INVOICE_STATUS)
    courses = models.ManyToManyField(Course)
    amount = models.FloatField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    pay = models.FloatField(null=True, blank=True)
    remark = models.TextField(null=True, blank=True)
    payment_type = models.CharField(max_length=50,choices=PAYMENT_TYPE)
    created_at =  models.DateTimeField(auto_now_add=True)
    pay_at =  models.DateTimeField(null=True, blank=True)
    update_at = models.DateTimeField(null=True)

class Payroll(models.Model):
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE, verbose_name="staff")
    amount = models.FloatField(null=True, blank=True)
    bonus = models.FloatField(null=True, blank=True)
    pay = models.FloatField(null=True, blank=True)
    hour_amount = models.FloatField(null=True, blank=True)
    pay_at = models.DateTimeField(null=True, blank=True)
    update_at = models.DateTimeField(null=True)