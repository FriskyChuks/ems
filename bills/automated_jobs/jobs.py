from django.conf import settings
import json
from bills.models import Bill
from apartments.models import *

def schedule_api():
    pass
    # occupant=Occupant.objects.all()
    # apartments=Apartment.objects.filter(status='taken')
    # for apartment in apartments:
    #     for c in apartment.occupant_set.all():
    #         bill_obj=Bill.objects.create(occupant_id=c.occupant.id,status='billed',
    #                     billed_for_id=apartment.id,amount_due=apartment.apartment_type.price,      
    #                 )
    # bill_obj.save()
    # print("Bills generated")
