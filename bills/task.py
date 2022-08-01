from celery import shared_task

from apartments.models import Apartment, Occupant

from .models import Bill

@shared_task(bind=True)
def create_bills_for_all(self):
    # occupant=Occupant.objects.all()
    # apartments=Apartment.objects.filter(occupant__in=occupant)
    # for apartment in apartments:
    #     for c in apartment.occupant_set.all():
    #         bill_obj=Bill.objects.create(user_id=c.occupant.id,status='billed',
    #                     billed_for_id=apartment.id,amount_due=10.00,      
    #                 )
    for i in range(100):
        bill_obj=Bill.objects.create(user_id=1,status='billed',
                        billed_for_id=1,amount_due=10.00,      
                     )
        bill_obj.save()
    print('Billed Successfully')
    return 'Billed Successfully!'