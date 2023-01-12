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
	roll_no = models.BigIntegerField()
	address = models.CharField(max_length=300, null=True, blank=True)
	mobile_no = models.BigIntegerField()
	dob = models.DateField()
	bloodgroup = models.CharField(max_length=10)
	gender = models.CharField(max_length=10)
	standard = models.CharField(choices=Standard,max_length=20,default="9th")
	division = models.CharField(max_length=10)
	photo = models.FileField(upload_to="userprofile/",default="default.png")
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.first_name