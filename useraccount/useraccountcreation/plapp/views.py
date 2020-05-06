from django.shortcuts import render
from django.http import HttpResponse
from plapp.models import studentdata
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def account(request):
	if request.method == 'POST':
		firstName = request.POST['firstName']
		lastName = request.POST['lastName']
		userName = request.POST['userName']
		mailId = request.POST['mailId']
		phone = request.POST['phone']
		age = request.POST['age']
		password = lastName+'@123'
		obj = studentdata(firstName=firstName,lastName=lastName,userName=userName,mailId=mailId,phone=phone,age=age,password=password)
		obj.save()
		sub  = 'hi'
		body = 'This is your secrete password  '+ password
		receiver = mailId
		sender  = settings.EMAIL_HOST_USER
		send_mail(sub,body,sender,[receiver])
		return HttpResponse('Mail send Successfully.....')
		# name = studentdata.objects.get(lastName)
		# print(name)
		#bio = {'firstName':firstName ,'userName':userName,'lastName':lastName}

		#return render(request,'plapp/password.html',{'bio':bio})

	return render(request, 'plapp/account.html',{})

def loginform(request):
	if request.method == 'POST':
		un = request.POST['UserName']
		pd = request.POST['Password']
		data = studentdata.objects.get(userName =un)
		if data :
		 	print('Welcome')
		 	print(data)
		 	return render(request,'plapp/showdetails.html',{'data':data})
		else:
			print("Invalid credintials")
			return HttpResponse("""<h2>Oops..! Invalid credintials</h2>""")
			
	return render(request,'plapp/loginform.html',{})
