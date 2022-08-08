from django.conf import settings
import json
from bills.models import Bill
from apartments.models import *

def schedule_api():
    pass
    # occupants=Occupant.objects.all()
    # for occupant in occupants:
    #     bill_obj=Bill.objects.create(occupant_id=occupant.occupant.id,status='billed',
    #                 billed_for_id=occupant.apartment.id,
    #                 amount_due=occupant.apartment.apartment_type.price)
    #     bill_obj.save()
    # print("Bills generated")
