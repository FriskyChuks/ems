from django.contrib.auth import authenticate, login, get_user_model, logout
from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# @unauthenticated_user
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import LoginForm, SignUpForm
from .models import User

def login_view(request):
	msg=None
	if request.method == "POST":
		email_var = request.POST.get('email')
		password_var = request.POST.get('password')
		user = authenticate(request,username=email_var, password=password_var)

		qs = User.objects.filter(email=email_var)
		if len(qs) < 1:
			msg = 'This user does not EXIST!'
		try:
			user = User.objects.get(email=email_var)
		except:
			user = None
		if user is not None and not user.check_password(password_var):
			msg = 'Wrong Password'
		
		else: 
			if user is not None:   
				login(request, user)
				if "next" in request.POST:
					return redirect(request.POST.get('next'))
				else:
					return redirect('home')

	return render(request, "accounts/login.html", {"msg": msg})


def register_user(request):
	msg = None
	success = False
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get("email")
			first_name = form.cleaned_data.get("firts_name")
			last_name = form.cleaned_data.get("last_name")
			raw_password = form.cleaned_data.get("password1")
			user = authenticate(email=email,first_name=first_name,
						last_name=last_name,password=raw_password)
			print(user)
			msg = 'User created - please <a href="accounts/login">login</a>.'
			success = True
		else:
			email = form.cleaned_data.get("email")
			first_name = form.cleaned_data.get("firts_name")
			last_name = form.cleaned_data.get("last_name")
			raw_password = form.cleaned_data.get("password1")
			user = authenticate(email=email,first_name=first_name,
						last_name=last_name,password=raw_password)
			print(user)
			msg = 'Form is not valid'
	else:
		form = SignUpForm()

	return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})



def logout_view(request):
	logout(request)
	# messages.success(request, "Sad to see you leave! See you soon please!")
	return HttpResponseRedirect('%s'%(reverse("login")))

def profile_view(request):
	return render(request,'accounts/profile.html',{})