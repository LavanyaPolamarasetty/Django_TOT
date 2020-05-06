from django.db import models
# Create your models here.
class studentdata(models.Model):
	firstName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=40)
	userName = models.CharField(max_length=40)
	password = models.CharField(max_length=40)
	mailId = models.CharField(max_length=40)
	phone = models.IntegerField(max_length=40)
	age = models.IntegerField(max_length=40)

	def __str__(self):
		return self.userName+' '