from django.db import models

# Create your models here.

class Admin(models.Model):
	first_name = models.CharField(max_length=300)
	middle_name = models.CharField(max_length=300)
	last_name = models.CharField(max_length=300)
	email = models.EmailField()
	mo_number = models.BigIntegerField()
	dob = models.DateField()

	def __str__(self):
		return self.first_name

class UserType(models.Model):
	user_type = models.CharField(max_length=30)

	def __str__(self):
		return self.user_type

Standard = (
        ("9th",'9th'),
        ("10th",'10th'),
		("11th",'11th'),
        ("12th",'12th'),
    )

class User(models.Model):
	usertype = models.ForeignKey(UserType,on_delete=models.CASCADE)
	first_name = models.CharField(max_length=20)
	middle_name = models.CharField(max_length=20,null=True, blank=True)
	last_name = models.CharField(max_length=20)
	email = models.EmailField()
	roll_no = models.BigIntegerField(null=True, blank=True)
	address = models.CharField(max_length=300, null=True, blank=True)
	mobile_no = models.BigIntegerField()
	dob = models.DateField(null=True, blank=True)
	bloodgroup = models.CharField(max_length=10,null=True, blank=True)
	gender = models.CharField(max_length=10)
	standard = models.CharField(choices=Standard,max_length=20,default="9th")
	division = models.CharField(max_length=10)
	photo = models.FileField(upload_to="userprofile/",default="default.png")
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.first_name

class Assignment(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	assignment_file = models.FileField(upload_to="assignment/",default="default.png")
	subject_name = models.CharField(max_length=30)

	def __str__(self):
		return self.subject_name

class Result(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	total = models.BigIntegerField()
	percentage = models.BigIntegerField()

	def __str__(self):
		return self.user

class Leave(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	reason = models.CharField(max_length=300)
	start_date = models.DateField()
	end_date = models.DateField()
	status = models.CharField(max_length=20)

	def __str__(self):
		return self.reason + " | " + self.user.first_name + " " +self.user.last_name 