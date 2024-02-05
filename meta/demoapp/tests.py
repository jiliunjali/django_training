from django.test import TestCase
from .models import Reservation
from datetime import datetime
# Create your tests here.

class ReservationModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls): #cls is class object
        cls.reservation = Reservation.objects.create(
            name ="jake",
            contact="243124",
            count=34,
            notes="yuihbnm"
        )
        

    def test_fields(self):
        self.assertIsInstance(self.reservation.name,str)
        self.assertIsInstance(self.reservation.contact,str)
        self.assertIsInstance(self.reservation.count,int)
        self.assertIsInstance(self.reservation.notes,str)
    

    # def test_timestamps(self):
    #     self.assertIsInstance(self.reservation.time,datetime)