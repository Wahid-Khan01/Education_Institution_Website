# management/commands/populate_states.py

from django.core.management.base import BaseCommand
from .models import IndianStates

class Command(BaseCommand):
    help = 'Populate states data into the database'

    def handle(self, *args, **kwargs):
        states = [
            "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", 
            "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", 
            "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", 
            "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", 
            "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", 
            "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", 
            "Daman and Diu", "Delhi", "Lakshadweep", "Puducherry"
        ]
        
        for state_name in states:
            IndianStates.objects.create(name=state_name)
            
