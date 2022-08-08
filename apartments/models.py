from django.db import models

from accounts.models import User

ApartmentCategory=(
    ('residential','Residential'),
    ('business','Business'),
)

ApartmentStatus=(
    ('free','Free'),
    ('taken','Taken'),
)
    
class ApartmentType(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(decimal_places=2, default='00.00', max_digits=20)
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Street(models.Model):
    title = models.CharField(max_length=225)
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Apartment(models.Model):
    apartment_category = models.CharField(max_length=15, choices=ApartmentCategory)
    apartment_type = models.ForeignKey(ApartmentType,on_delete=models.CASCADE)
    # price = models.DecimalField(decimal_places=2, default='00.00', max_digits=20)
    phase = models.IntegerField()
    street = models.ForeignKey(Street,on_delete=models.CASCADE)
    compound = models.CharField(max_length=100)
    flat_number = models.IntegerField()
    status = models.CharField(max_length=15, choices=ApartmentStatus,default='free')
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.apartment_type} || {self.apartment_category}"

class Occupant(models.Model):
    occupant = models.ForeignKey(User,on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment,on_delete=models.CASCADE)
    # assigned_by = models.ForeignKey(User,related_name='assigned_by', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.occupant.email} || {self.apartment}"