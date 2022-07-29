from email import message
from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from .forms import *
from .models import *

def home(request):
	return render(request,'home/index.html',{})


def create_apartment_view(request):
	types = ApartmentType.objects.all()
	streets = Street.objects.all()
	context={"types":types,"streets":streets}

	apartment_category=request.POST.get('apartment_category')
	apartment_type=request.POST.get('apartment_type')
	phase=request.POST.get('phase')
	street=request.POST.get('street')
	compound=request.POST.get('compound')
	flat_number=request.POST.get('flat_number')
	if request.method=='POST':
		obj=Apartment.objects.create(apartment_category=apartment_category,
						phase=phase,apartment_type_id=apartment_type,street_id=street,
						compound=compound,flat_number=flat_number,
						created_by_id=request.user.id)
		obj.save()
		messages.success(request,'Apartment created sucessfully!')
		return redirect('create_apartment')
	return render(request,'apartments/create_apartment.html',context)


def apartment_list_view(request):
	apartments=Apartment.objects.all()
	residential_apartments = Apartment.objects.filter(apartment_category='residential')
	business_apartments = Apartment.objects.filter(apartment_category='business')
	available = Apartment.objects.filter(status='free')
	taken = Apartment.objects.filter(status='taken')

	context={'apartments':apartments,"residential_apartments":residential_apartments,
		"business_apartments":business_apartments,"available":available,"taken":taken}
	return render(request,'apartments/apartment_list.html',context)


def add_occupant_view(request,id):
	apartment=Apartment.objects.get(id=id)
	email=request.POST.get('email')
	user=None
	if request.method=='POST':
		try:
			user=User.objects.get(email=email)
			obj=Occupant.objects.create(occupant_id=user.id,apartment_id=id,
										assigned_by_id=request.user.id)
			obj.save()
			Apartment.objects.filter(id=id).update(status='taken')
			messages.success(request,f"Apartment successfully assigned to {email}")
			return redirect('apartment_list')
		except ObjectDoesNotExist:
			messages.error(request,f"No user with the email '{email}'")
			return redirect("add_occupant",id=id)
	print(user)
	context={"apartment":apartment}
	return render(request,'apartments/add_occupant.html',context)